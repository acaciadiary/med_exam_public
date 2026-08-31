const fs = require("node:fs");
const path = require("node:path");

const root = process.cwd();
const base = path.join(root, "public", "data", "exams");
const labels = ["A", "B", "C", "D"];
const optionHeading = "\u3010\u9078\u9805\u8a73\u89e3\u3011";
const coreHeading = "\u3010\u6838\u5fc3\u8003\u9ede\u3011";

const broadPhrases = [
  "\u6700\u7b26\u5408\u984c\u5e79",
  "\u7b26\u5408\u984c\u5e79",
  "\u4e0d\u7b26\u5408\u984c\u5e79",
  "\u4e0d\u662f\u6700\u4f73\u7b54\u6848",
  "\u4e26\u975e\u6700\u4f73\u7b54\u6848",
  "\u4e0d\u80fd\u4f5c\u70ba\u7b54\u6848",
  "\u4e0d\u662f\u672c\u984c\u7b54\u6848",
  "\u975e\u672c\u984c\u7b54\u6848",
  "\u8207\u6b63\u78ba\u7b54\u6848",
  "\u8207\u6a19\u6e96\u7b54\u6848",
  "\u56de\u5230\u984c\u5e79",
  "\u5c0d\u7167\u672c\u984c",
  "\u95dc\u9375\u5224\u65b7",
  "\u9078\u9805\u5167\u5bb9",
  "\u4f5c\u7b54\u6642",
  "\u8907\u7fd2\u6642\u4e0d\u8981\u53ea\u80cc\u7b54\u6848",
];

const templateFamilies = [
  {
    key: "local_core_template",
    label: "local-medical-explainer core-template wording",
    patterns: [
      "此選項與題幹線索或核心考點不完全相符",
      "此選項符合題幹線索與官方答案",
      "本題可用的判斷核心是",
      "作答時需回到題幹關鍵字",
    ],
  },
  {
    key: "best_answer_template",
    label: "not-best-answer core-template wording",
    patterns: [
      "不是最佳答案，與本題核心考點不完全相符",
      "正確，符合本題核心考點",
      "題幹重點可整理為",
    ],
  },
  {
    key: "all_credit_repetition",
    label: "all-credit repeated option wording",
    patterns: [
      "全給分",
      "official correct_answers",
      "官方 correct_answers",
      "因選項缺漏而全給分",
    ],
  },
];

function walk(dir) {
  let out = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, entry.name);
    if (entry.isDirectory()) out = out.concat(walk(p));
    else if (entry.isFile() && entry.name.endsWith(".json")) out.push(p);
  }
  return out.sort();
}

function rel(p) {
  return path.relative(root, p).replace(/\\/g, "/");
}

function optionSection(explanation) {
  let text = String(explanation || "");
  const start = text.indexOf(optionHeading);
  if (start >= 0) text = text.slice(start + optionHeading.length);
  const end = text.indexOf(coreHeading);
  if (end >= 0) text = text.slice(0, end);
  return text;
}

const optRe = /(?:^|\n)\s*(?:[-*•]\s*)?(?:[（(【\[]?\s*)([A-D])\s*(?:[）)】\]]|[.．、:：])\s*/g;

function optionBlocks(explanation) {
  const section = optionSection(explanation);
  const matches = [...section.matchAll(optRe)];
  const blocks = new Map();
  for (let i = 0; i < matches.length; i += 1) {
    const match = matches[i];
    const next = i + 1 < matches.length ? matches[i + 1].index : section.length;
    const raw = section.slice(match.index + match[0].length, next).trim();
    if (!blocks.has(match[1])) blocks.set(match[1], raw);
  }
  return blocks;
}

function normalize(s) {
  return String(s || "")
    .normalize("NFKC")
    .toLowerCase()
    .replace(/^[\s。．、:：,，;；]*(正確答案|正確|錯誤|非本題答案|答案|對|錯)[\s。．、:：,，;；]*/g, "")
    .replace(/選項內容[:：]?/g, "")
    .replace(/「|」|『|』|\(|\)|（|）|\[|\]|【|】/g, "")
    .replace(/[\s\r\n\t]+/g, "")
    .replace(/[，。．、:：;；!！?？,.\-_/\\]/g, "")
    .replace(/此選項|本選項|該選項/g, "")
    .replace(/本題|題幹|線索|標準答案|正解|答案|正確|錯誤/g, "");
}

function ngrams(s, n = 3) {
  const text = normalize(s);
  if (!text) return [];
  if (text.length <= n) return [text];
  const grams = [];
  for (let i = 0; i <= text.length - n; i += 1) grams.push(text.slice(i, i + n));
  return grams;
}

function dice(a, b) {
  const aGrams = ngrams(a);
  const bGrams = ngrams(b);
  if (!aGrams.length || !bGrams.length) return 0;
  const counts = new Map();
  for (const gram of aGrams) counts.set(gram, (counts.get(gram) || 0) + 1);
  let intersection = 0;
  for (const gram of bGrams) {
    const count = counts.get(gram) || 0;
    if (count > 0) {
      intersection += 1;
      counts.set(gram, count - 1);
    }
  }
  return (2 * intersection) / (aGrams.length + bGrams.length);
}

function commonPrefix(a, b) {
  const left = normalize(a);
  const right = normalize(b);
  let index = 0;
  while (index < left.length && index < right.length && left[index] === right[index]) index += 1;
  return index;
}

function excerpt(text, limit = 130) {
  const compact = String(text || "").replace(/\s+/g, " ").trim();
  return compact.length <= limit ? compact : `${compact.slice(0, limit - 1)}...`;
}

function opening(block) {
  return normalize(block).slice(0, 18);
}

function classify(optionText, question, avg, maxLength) {
  const families = [];
  for (const family of templateFamilies) {
    if (family.patterns.some((pattern) => optionText.includes(pattern))) {
      families.push(family.key);
    }
  }
  if (question.correct_answer === "#" && !families.includes("all_credit_repetition")) {
    families.push("all_credit_repetition");
  }
  if (maxLength > 0 && maxLength < 48 && avg >= 0.65) {
    families.push("very_short_option_detail");
  }
  if (!families.length) families.push("structural_similarity");
  return families;
}

const files = walk(base);
let totalQuestions = 0;
let complete = 0;
let empty = 0;
let incomplete = 0;
const candidates = [];
const byFile = new Map();

for (const file of files) {
  const dataset = JSON.parse(fs.readFileSync(file, "utf8").replace(/^\uFEFF/, ""));
  for (const question of dataset.questions || []) {
    totalQuestions += 1;
    const explanation = String(question.explanation || "").trim();
    if (!explanation) {
      empty += 1;
      continue;
    }

    const blocks = optionBlocks(explanation);
    const presentLabels = labels.filter((label) => blocks.has(label));
    if (presentLabels.length < 4) {
      incomplete += 1;
      continue;
    }
    complete += 1;

    const optionTexts = labels.map((label) => blocks.get(label) || "");
    const pairwise = [];
    for (let i = 0; i < optionTexts.length; i += 1) {
      for (let j = i + 1; j < optionTexts.length; j += 1) {
        pairwise.push(dice(optionTexts[i], optionTexts[j]));
      }
    }
    const avg = pairwise.reduce((sum, value) => sum + value, 0) / pairwise.length;
    const min = Math.min(...pairwise);
    const max = Math.max(...pairwise);
    const optionLengths = optionTexts.map((text) => normalize(text).length);
    const minLength = Math.min(...optionLengths);
    const maxLength = Math.max(...optionLengths);
    const lengthSpread = maxLength ? (maxLength - minLength) / maxLength : 0;
    const prefixes = [];
    for (let i = 0; i < optionTexts.length; i += 1) {
      for (let j = i + 1; j < optionTexts.length; j += 1) {
        prefixes.push(commonPrefix(optionTexts[i], optionTexts[j]));
      }
    }
    const maxPrefix = Math.max(...prefixes);

    const openingCounts = new Map();
    for (const block of optionTexts) {
      const text = opening(block).slice(0, 10);
      openingCounts.set(text, (openingCounts.get(text) || 0) + 1);
    }
    const repeatedOpening = [...openingCounts.entries()]
      .filter(([text, count]) => text.length >= 6 && count >= 3)
      .map(([text, count]) => ({ opening: text, count }));

    const optionText = optionSection(explanation);
    const phraseHits = broadPhrases.filter((phrase) => optionText.includes(phrase));
    const families = classify(optionText, question, avg, maxLength);
    const score = avg * 75 + min * 45 + maxPrefix * 0.9 + (repeatedOpening.length ? 12 : 0) + phraseHits.length * 8 - lengthSpread * 10;
    const flagged =
      avg >= 0.36 ||
      min >= 0.28 ||
      maxPrefix >= 12 ||
      repeatedOpening.length > 0 ||
      phraseHits.length >= 2;

    if (!flagged) continue;

    const item = {
      ref: `${dataset.id || path.basename(file, ".json")} Q${String(question.question_number).padStart(3, "0")}`,
      path: rel(file),
      dataset_id: dataset.id,
      title: dataset.title,
      question_id: question.id,
      question_number: question.question_number,
      correct_answer: question.correct_answer,
      score: Number(score.toFixed(1)),
      avg_similarity: Number(avg.toFixed(3)),
      min_similarity: Number(min.toFixed(3)),
      max_similarity: Number(max.toFixed(3)),
      max_common_prefix_chars: maxPrefix,
      repeated_opening: repeatedOpening,
      broad_phrase_hits: phraseHits,
      template_families: families,
      option_lengths: Object.fromEntries(labels.map((label, index) => [label, optionLengths[index]])),
      question_text: excerpt(question.question_text, 180),
      options: question.options || {},
      option_excerpts: Object.fromEntries(labels.map((label, index) => [label, excerpt(optionTexts[index])])),
      review_status: question.review_status || "empty",
      explanation_model: question.explanation_model || "",
    };
    candidates.push(item);
    const key = rel(file);
    byFile.set(key, (byFile.get(key) || 0) + 1);
  }
}

candidates.sort((a, b) => b.score - a.score || b.avg_similarity - a.avg_similarity || a.path.localeCompare(b.path));

const strong = candidates.filter(
  (item) =>
    item.avg_similarity >= 0.42 ||
    item.min_similarity >= 0.34 ||
    item.max_common_prefix_chars >= 18 ||
    item.repeated_opening.length > 0 ||
    item.broad_phrase_hits.length >= 2,
);

function countBy(items, callback) {
  const counts = new Map();
  for (const item of items) {
    const keys = callback(item);
    for (const key of Array.isArray(keys) ? keys : [keys]) {
      counts.set(key, (counts.get(key) || 0) + 1);
    }
  }
  return [...counts.entries()]
    .sort((a, b) => b[1] - a[1] || String(a[0]).localeCompare(String(b[0])))
    .map(([key, count]) => ({ key, count }));
}

const report = {
  scanned_files: files.length,
  total_questions: totalQuestions,
  complete_option_explanations: complete,
  empty_explanations: empty,
  incomplete_option_explanations: incomplete,
  candidate_count: candidates.length,
  strong_candidate_count: strong.length,
  template_family_counts: countBy(candidates, (item) => item.template_families),
  model_counts: countBy(candidates, (item) => item.explanation_model || "(empty)"),
  strong_template_family_counts: countBy(strong, (item) => item.template_families),
  top_files_by_candidate_count: [...byFile.entries()]
    .sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))
    .slice(0, 20)
    .map(([filePath, count]) => ({ path: filePath, count })),
  top_candidates: candidates.slice(0, 80),
};

fs.mkdirSync(path.join(root, "reports"), { recursive: true });
fs.writeFileSync(path.join(root, "reports", "option-similarity-audit.json"), `${JSON.stringify(report, null, 2)}\n`, "utf8");
console.log(JSON.stringify({
  scanned_files: report.scanned_files,
  total_questions: report.total_questions,
  complete_option_explanations: report.complete_option_explanations,
  empty_explanations: report.empty_explanations,
  incomplete_option_explanations: report.incomplete_option_explanations,
  candidate_count: report.candidate_count,
  strong_candidate_count: report.strong_candidate_count,
  template_family_counts: report.template_family_counts,
  model_counts: report.model_counts.slice(0, 12),
  strong_template_family_counts: report.strong_template_family_counts,
  top_files_by_candidate_count: report.top_files_by_candidate_count.slice(0, 10),
  top_candidates: report.top_candidates.slice(0, 25),
}, null, 2));
