from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

EXPECTED_OPTION_LABELS = ("A", "B", "C", "D")
REQUIRED_HEADINGS = ("【題幹解析】", "【選項詳解】", "【核心考點】")
VALID_REVIEW_STATUSES = {"empty", "ai_generated", "reviewed"}

BANNED_TEMPLATE_PHRASES = (
    "非本題答案",
    "不是本題標準答案",
    "回到題幹線索",
    "請用題幹線索連回",
    "題目中選項 A 所代表的鑑別或處置",
    "不能最精準回答本題",
    "最符合題幹",
    "核心記憶點",
    "定義、機轉、典型表現或處置原則",
)

OPTION_LINE_PATTERN = re.compile(
    r"(?m)^\s*(?:[-*•]\s*)?(?:[（(【\[]?\s*)([A-D])\s*(?:[）)】\]]|[.．、:：])"
)


def expand_paths(patterns: list[str]) -> list[Path]:
    paths: list[Path] = []
    for pattern in patterns:
        matches = sorted(Path().glob(pattern))
        paths.extend(matches or [Path(pattern)])
    return paths


def normalize_path(path: Path) -> str:
    return str(path).replace("\\", "/")


def load_dataset(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def count_chars(text: str) -> int:
    return len(re.sub(r"\s+", "", text))


def option_section(explanation: str) -> str:
    if "【選項詳解】" not in explanation:
        return explanation
    section = explanation.split("【選項詳解】", 1)[1]
    if "【核心考點】" in section:
        section = section.split("【核心考點】", 1)[0]
    return section


def detected_option_labels(explanation: str) -> set[str]:
    section = option_section(explanation)
    return {match.group(1) for match in OPTION_LINE_PATTERN.finditer(section)}


def text_excerpt(text: str, limit: int = 220) -> str:
    compact = re.sub(r"\s+", " ", text).strip()
    if len(compact) <= limit:
        return compact
    return compact[: limit - 1] + "…"


def question_ref(path: Path, dataset: dict[str, Any], question: dict[str, Any]) -> dict[str, Any]:
    return {
        "path": normalize_path(path),
        "dataset_id": dataset.get("id"),
        "question_id": question.get("id"),
        "question_number": question.get("question_number"),
    }


def audit_file(path: Path, min_explanation_chars: int, max_samples_per_file: int) -> dict[str, Any]:
    dataset = load_dataset(path)
    questions = dataset.get("questions", [])

    issue_counts: Counter[str] = Counter()
    phrase_counts: Counter[str] = Counter()
    review_status_counts: Counter[str] = Counter()
    incomplete_option_samples: list[dict[str, Any]] = []
    missing_heading_samples: list[dict[str, Any]] = []
    short_explanation_samples: list[dict[str, Any]] = []

    for question in questions:
        explanation = str(question.get("explanation", "") or "").strip()
        status = str(question.get("review_status", "empty") or "empty").strip()
        review_status_counts[status] += 1

        if status not in VALID_REVIEW_STATUSES:
            issue_counts["invalid_review_status"] += 1

        missing_headings = [heading for heading in REQUIRED_HEADINGS if heading not in explanation]
        if missing_headings:
            issue_counts["missing_required_headings"] += 1
            if len(missing_heading_samples) < max_samples_per_file:
                sample = question_ref(path, dataset, question)
                sample["missing_headings"] = missing_headings
                sample["excerpt"] = text_excerpt(explanation)
                missing_heading_samples.append(sample)

        labels = detected_option_labels(explanation)
        missing_options = [label for label in EXPECTED_OPTION_LABELS if label not in labels]
        if missing_options:
            issue_counts["incomplete_option_details"] += 1
            if len(incomplete_option_samples) < max_samples_per_file:
                sample = question_ref(path, dataset, question)
                sample["detected_options"] = sorted(labels)
                sample["missing_options"] = missing_options
                sample["excerpt"] = text_excerpt(option_section(explanation))
                incomplete_option_samples.append(sample)

        if explanation and count_chars(explanation) < min_explanation_chars:
            issue_counts["short_explanation"] += 1
            if len(short_explanation_samples) < max_samples_per_file:
                sample = question_ref(path, dataset, question)
                sample["char_count_no_space"] = count_chars(explanation)
                sample["excerpt"] = text_excerpt(explanation)
                short_explanation_samples.append(sample)
        elif not explanation:
            issue_counts["empty_explanation"] += 1

        for phrase in BANNED_TEMPLATE_PHRASES:
            hits = explanation.count(phrase)
            if hits:
                phrase_counts[phrase] += hits
                issue_counts["banned_template_phrase"] += hits

    risk_score = (
        issue_counts["missing_required_headings"] * 4
        + issue_counts["incomplete_option_details"] * 4
        + issue_counts["empty_explanation"] * 4
        + issue_counts["short_explanation"] * 2
        + issue_counts["invalid_review_status"] * 2
        + issue_counts["banned_template_phrase"]
    )

    return {
        "path": normalize_path(path),
        "dataset_id": dataset.get("id"),
        "title": dataset.get("title"),
        "question_count": len(questions),
        "risk_score": risk_score,
        "issue_counts": dict(sorted(issue_counts.items())),
        "review_status_counts": dict(sorted(review_status_counts.items())),
        "phrase_counts": dict(sorted(phrase_counts.items())),
        "samples": {
            "missing_headings": missing_heading_samples,
            "incomplete_options": incomplete_option_samples,
            "short_explanations": short_explanation_samples,
        },
    }


def merge_counters(reports: list[dict[str, Any]], key: str) -> dict[str, int]:
    total: Counter[str] = Counter()
    for report in reports:
        total.update(report.get(key, {}))
    return dict(sorted(total.items()))


def summarize(reports: list[dict[str, Any]], top_limit: int) -> dict[str, Any]:
    issue_counts = merge_counters(reports, "issue_counts")
    phrase_counts = merge_counters(reports, "phrase_counts")
    review_status_counts = merge_counters(reports, "review_status_counts")
    total_questions = sum(report["question_count"] for report in reports)
    risky_reports = [report for report in reports if report["risk_score"] > 0]

    return {
        "dataset_count": len(reports),
        "question_count": total_questions,
        "risky_file_count": len(risky_reports),
        "issue_counts": issue_counts,
        "phrase_counts": phrase_counts,
        "review_status_counts": review_status_counts,
        "reviewed_rate": (
            round(review_status_counts.get("reviewed", 0) / total_questions, 4) if total_questions else 0
        ),
        "top_risky_files": [
            {
                "path": report["path"],
                "dataset_id": report["dataset_id"],
                "question_count": report["question_count"],
                "risk_score": report["risk_score"],
                "issue_counts": report["issue_counts"],
                "review_status_counts": report["review_status_counts"],
                "phrase_counts": report["phrase_counts"],
            }
            for report in sorted(reports, key=lambda item: (-item["risk_score"], item["path"]))[:top_limit]
            if report["risk_score"] > 0
        ],
    }


def collect_samples(reports: list[dict[str, Any]], sample_key: str, limit: int) -> list[dict[str, Any]]:
    samples: list[dict[str, Any]] = []
    for report in sorted(reports, key=lambda item: (-item["risk_score"], item["path"])):
        samples.extend(report["samples"].get(sample_key, []))
        if len(samples) >= limit:
            return samples[:limit]
    return samples


def build_report(args: argparse.Namespace) -> dict[str, Any]:
    paths = expand_paths(args.paths)
    file_reports = [audit_file(path, args.min_explanation_chars, args.max_samples_per_file) for path in paths]
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "scope": {
            "paths": [normalize_path(path) for path in paths],
            "required_headings": list(REQUIRED_HEADINGS),
            "expected_option_labels": list(EXPECTED_OPTION_LABELS),
            "min_explanation_chars_no_space": args.min_explanation_chars,
            "banned_template_phrases": list(BANNED_TEMPLATE_PHRASES),
        },
        "summary": summarize(file_reports, args.top),
        "incomplete_option_samples": collect_samples(file_reports, "incomplete_options", args.samples),
        "missing_heading_samples": collect_samples(file_reports, "missing_headings", args.samples),
        "short_explanation_samples": collect_samples(file_reports, "short_explanations", args.samples),
        "files": file_reports,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit exam explanation trust signals before promotion.")
    parser.add_argument("paths", nargs="+", help="Dataset JSON paths or glob patterns")
    parser.add_argument("--out", default="reports/prepromo-content-trust.json")
    parser.add_argument("--top", type=int, default=15, help="Number of risky files to include in the summary")
    parser.add_argument("--samples", type=int, default=40, help="Maximum cross-site samples per sample bucket")
    parser.add_argument("--max-samples-per-file", type=int, default=3)
    parser.add_argument(
        "--min-explanation-chars",
        type=int,
        default=180,
        help="Minimum explanation length after whitespace removal",
    )
    args = parser.parse_args()

    report = build_report(args)
    output = json.dumps(report, ensure_ascii=False, indent=2)
    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output + "\n", encoding="utf-8")
    print(json.dumps(report["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
