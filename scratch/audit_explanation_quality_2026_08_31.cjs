const fs = require("node:fs");
const path = require("node:path");

const root = process.cwd();
const dataRoot = path.join(root, "public", "data", "exams");
const reportDir = path.join(root, "reports");

const labels = ["A", "B", "C", "D"];
const requiredLearningFields = [
  "key_point",
  "explanation",
  "flashcard_front",
  "flashcard_back",
  "flashcard_summary",
];
const requiredHeadings = ["【題幹解析】", "【選項詳解】", "【核心考點】"];
const optionHeading = "【選項詳解】";
const coreHeading = "【核心考點】";

const bannedTemplatePhrases = [
  "原始解析",
  "不是最佳答案",
  "並非最佳答案",
  "不是本題答案",
  "非本題答案",
  "與正確答案",
  "與標準答案",
  "選項內容",
  "作答時",
  "複習時不要只背答案",
  "最符合題幹",
  "符合題幹",
  "不符合題幹",
  "不能作為答案",
  "回到題幹",
  "對照本題",
  "關鍵判斷",
];

const templateFamilies = [
  {
    key: "local_core_template",
    patterns: [
      "本題選項的差異不在於核心考點是否存在",
      "本題選項都在處理同一個主題",
      "真正要抓的是",
      "若只用選項名稱判斷",
    ],
  },
  {
    key: "not_best_answer_template",
    patterns: [
      "不是最佳答案",
      "並非最佳答案",
      "不是本題答案",
      "非本題答案",
      "與正確答案",
      "與標準答案",
    ],
  },
];

function walk(dir) {
  const out = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) out.push(...walk(fullPath));
    if (entry.isFile() && entry.name.endsWith(".json")) out.push(fullPath);
  }
  return out.sort();
}

function rel(fullPath) {
  return path.relative(root, fullPath).replace(/\\/g, "/");
}

function readJson(fullPath) {
  return JSON.parse(fs.readFileSync(fullPath, "utf8").replace(/^\uFEFF/, ""));
}

function compactText(value) {
  return String(value || "").replace(/\s+/g, "");
}

function excerpt(value, limit = 120) {
  const text = String(value || "").replace(/\s+/g, " ").trim();
  return text.length <= limit ? text : `${text.slice(0, limit - 1)}...`;
}

function optionSection(explanation) {
  let section = String(explanation || "");
  const start = section.indexOf(optionHeading);
  if (start >= 0) section = section.slice(start + optionHeading.length);
  const end = section.indexOf(coreHeading);
  if (end >= 0) section = section.slice(0, end);
  return section;
}

const optionLinePattern = /(?:^|\n)\s*(?:[-*]\s*)?(?:[（(]?\s*)([A-D])\s*(?:[）)]|[.．、：:])\s*/g;

function optionBlocks(explanation) {
  const section = optionSection(explanation);
  const matches = [...section.matchAll(optionLinePattern)];
  const blocks = new Map();
  for (let index = 0; index < matches.length; index += 1) {
    const match = matches[index];
    const next = index + 1 < matches.length ? matches[index + 1].index : section.length;
    if (!blocks.has(match[1])) {
      blocks.set(match[1], section.slice(match.index + match[0].length, next).trim());
    }
  }
  return blocks;
}

function normalize(value) {
  return String(value || "")
    .normalize("NFKC")
    .toLowerCase()
    .replace(/^[\s\-*()（）.．、：:]+/g, "")
    .replace(/答案[:：]?/g, "")
    .replace(/[\s\r\n\t]+/g, "")
    .replace(/[，,。；;：:、.．\-_/\\()[\]（）「」『』【】]/g, "")
    .replace(/本題|選項|題幹|答案|正確|錯誤|最佳|標準|核心考點/g, "");
}

function ngrams(value, size = 3) {
  const text = normalize(value);
  if (!text) return [];
  if (text.length <= size) return [text];
  const grams = [];
  for (let index = 0; index <= text.length - size; index += 1) {
    grams.push(text.slice(index, index + size));
  }
  return grams;
}

function dice(left, right) {
  const leftGrams = ngrams(left);
  const rightGrams = ngrams(right);
  if (!leftGrams.length || !rightGrams.length) return 0;
  const counts = new Map();
  for (const gram of leftGrams) counts.set(gram, (counts.get(gram) || 0) + 1);
  let intersection = 0;
  for (const gram of rightGrams) {
    const count = counts.get(gram) || 0;
    if (count > 0) {
      intersection += 1;
      counts.set(gram, count - 1);
    }
  }
  return (2 * intersection) / (leftGrams.length + rightGrams.length);
}

function commonPrefix(left, right) {
  const a = normalize(left);
  const b = normalize(right);
  let index = 0;
  while (index < a.length && index < b.length && a[index] === b[index]) index += 1;
  return index;
}

function repeatedLongSegments(explanation) {
  const seen = new Map();
  for (const [label, block] of optionBlocks(explanation)) {
    for (const piece of block.split(/[。；;！!？?\n]/)) {
      const compact = compactText(piece);
      if (compact.length >= 36) {
        if (!seen.has(compact)) seen.set(compact, new Set());
        seen.get(compact).add(label);
      }
    }
  }
  return [...seen.entries()]
    .filter(([, optionLabels]) => optionLabels.size >= 3)
    .map(([segment, optionLabels]) => ({ segment, labels: [...optionLabels].sort() }));
}

function compressRanges(numbers) {
  const sorted = [...new Set(numbers)].sort((a, b) => a - b);
  const ranges = [];
  for (let index = 0; index < sorted.length; index += 1) {
    const start = sorted[index];
    let end = start;
    while (index + 1 < sorted.length && sorted[index + 1] === end + 1) {
      index += 1;
      end = sorted[index];
    }
    ranges.push(start === end ? String(start) : `${start}-${end}`);
  }
  return ranges.join(", ");
}

function pushIssue(fileSummary, code, question, detail = {}) {
  const number = Number(question.question_number);
  if (!fileSummary.issues[code]) fileSummary.issues[code] = [];
  fileSummary.issues[code].push(number);
  if (!fileSummary.samples[code]) fileSummary.samples[code] = [];
  if (fileSummary.samples[code].length < 5) {
    fileSummary.samples[code].push({
      question_number: number,
      question_id: question.id,
      question_text: excerpt(question.question_text),
      ...detail,
    });
  }
}

const files = walk(dataRoot);
const fileSummaries = [];
let totalQuestions = 0;
let completeLearningFields = 0;
let missingLearningFields = 0;

for (const file of files) {
  const dataset = readJson(file);
  const fileSummary = {
    path: rel(file),
    dataset_id: dataset.id,
    title: dataset.title,
    question_count: 0,
    issues: {},
    samples: {},
  };

  for (const question of dataset.questions || []) {
    totalQuestions += 1;
    fileSummary.question_count += 1;

    const explanation = String(question.explanation || "").trim();
    const fields = Object.fromEntries(
      requiredLearningFields.map((field) => [field, String(question[field] || "").trim()]),
    );
    const filled = requiredLearningFields.filter((field) => fields[field]);
    if (filled.length === requiredLearningFields.length) {
      completeLearningFields += 1;
    } else {
      missingLearningFields += 1;
      pushIssue(fileSummary, filled.length === 0 ? "missing_all_learning_fields" : "partial_learning_fields", question, {
        filled_fields: filled,
        missing_fields: requiredLearningFields.filter((field) => !fields[field]),
      });
    }

    if (!explanation) continue;

    const missingHeadings = requiredHeadings.filter((heading) => !explanation.includes(heading));
    if (missingHeadings.length) {
      pushIssue(fileSummary, "missing_required_headings", question, { missing_headings: missingHeadings });
    }

    const blocks = optionBlocks(explanation);
    const missingOptions = labels.filter((label) => !blocks.has(label));
    if (missingOptions.length) {
      pushIssue(fileSummary, "incomplete_option_details", question, { missing_options: missingOptions });
    }

    if (compactText(explanation).length < 180) {
      pushIssue(fileSummary, "short_explanation", question, {
        char_count_no_space: compactText(explanation).length,
      });
    }

    const repeated = repeatedLongSegments(explanation);
    if (repeated.length) {
      pushIssue(fileSummary, "repeated_option_segment", question, {
        labels: repeated[0].labels,
        repeated_segment: excerpt(repeated[0].segment),
      });
    }

    const optionText = optionSection(explanation);
    const phraseHits = bannedTemplatePhrases.filter((phrase) => optionText.includes(phrase));
    if (phraseHits.length) {
      pushIssue(fileSummary, "broad_or_banned_template_phrase", question, { phrase_hits: phraseHits });
    }

    if (blocks.size === 4) {
      const optionTexts = labels.map((label) => blocks.get(label) || "");
      const pairwise = [];
      const prefixes = [];
      for (let i = 0; i < optionTexts.length; i += 1) {
        for (let j = i + 1; j < optionTexts.length; j += 1) {
          pairwise.push(dice(optionTexts[i], optionTexts[j]));
          prefixes.push(commonPrefix(optionTexts[i], optionTexts[j]));
        }
      }
      const avg = pairwise.reduce((sum, value) => sum + value, 0) / pairwise.length;
      const min = Math.min(...pairwise);
      const maxPrefix = Math.max(...prefixes);
      const repeatedOpenings = new Map();
      for (const option of optionTexts) {
        const opening = normalize(option).slice(0, 10);
        if (opening.length >= 6) repeatedOpenings.set(opening, (repeatedOpenings.get(opening) || 0) + 1);
      }
      const repeatedOpening = [...repeatedOpenings.entries()].filter(([, count]) => count >= 3);
      const familyHits = templateFamilies
        .filter((family) => family.patterns.some((pattern) => optionText.includes(pattern)))
        .map((family) => family.key);
      const strongSimilarity =
        avg >= 0.42 ||
        min >= 0.34 ||
        maxPrefix >= 18 ||
        phraseHits.length >= 2 ||
        familyHits.length > 0;
      if (strongSimilarity) {
        pushIssue(fileSummary, "strong_option_similarity", question, {
          avg_similarity: Number(avg.toFixed(3)),
          min_similarity: Number(min.toFixed(3)),
          max_common_prefix_chars: maxPrefix,
          repeated_opening_count: repeatedOpening.length,
          template_families: familyHits.length ? familyHits : ["structural_similarity"],
          option_excerpts: Object.fromEntries(labels.map((label, index) => [label, excerpt(optionTexts[index], 80)])),
        });
      }
    }
  }

  const issueTotal = Object.values(fileSummary.issues).reduce((sum, numbers) => sum + numbers.length, 0);
  if (issueTotal > 0) {
    fileSummary.issue_counts = Object.fromEntries(
      Object.entries(fileSummary.issues).map(([code, numbers]) => [code, numbers.length]).sort((a, b) => a[0].localeCompare(b[0])),
    );
    fileSummary.unique_question_numbers = [...new Set(Object.values(fileSummary.issues).flat())].sort((a, b) => a - b);
    fileSummary.unique_issue_question_count = fileSummary.unique_question_numbers.length;
    fileSummary.question_ranges = compressRanges(fileSummary.unique_question_numbers);
    fileSummaries.push(fileSummary);
  }
}

const issueCounts = {};
for (const fileSummary of fileSummaries) {
  for (const [code, count] of Object.entries(fileSummary.issue_counts)) {
    issueCounts[code] = (issueCounts[code] || 0) + count;
  }
}

const prioritizedFiles = fileSummaries
  .map((fileSummary) => {
    const hard =
      (fileSummary.issue_counts.missing_all_learning_fields || 0) * 6 +
      (fileSummary.issue_counts.partial_learning_fields || 0) * 5 +
      (fileSummary.issue_counts.missing_required_headings || 0) * 5 +
      (fileSummary.issue_counts.incomplete_option_details || 0) * 5 +
      (fileSummary.issue_counts.repeated_option_segment || 0) * 4 +
      (fileSummary.issue_counts.broad_or_banned_template_phrase || 0) * 3 +
      (fileSummary.issue_counts.strong_option_similarity || 0) * 2 +
      (fileSummary.issue_counts.short_explanation || 0) * 2;
    return { ...fileSummary, priority_score: hard };
  })
  .sort((a, b) => b.priority_score - a.priority_score || b.unique_issue_question_count - a.unique_issue_question_count || a.path.localeCompare(b.path));

const report = {
  generated_at: new Date().toISOString(),
  scanned_files: files.length,
  total_questions: totalQuestions,
  complete_learning_fields: completeLearningFields,
  missing_or_partial_learning_fields: missingLearningFields,
  issue_counts: Object.fromEntries(Object.entries(issueCounts).sort((a, b) => a[0].localeCompare(b[0]))),
  file_count_with_any_issue: prioritizedFiles.length,
  files: prioritizedFiles,
};

fs.mkdirSync(reportDir, { recursive: true });
fs.writeFileSync(path.join(reportDir, "audit-2026-08-31-explanation-quality-full.json"), `${JSON.stringify(report, null, 2)}\n`, "utf8");

const lines = [
  "# 2026-08-31 Explanation Quality Full Audit",
  "",
  `- scanned_files: ${report.scanned_files}`,
  `- total_questions: ${report.total_questions}`,
  `- complete_learning_fields: ${report.complete_learning_fields}`,
  `- missing_or_partial_learning_fields: ${report.missing_or_partial_learning_fields}`,
  `- file_count_with_any_issue: ${report.file_count_with_any_issue}`,
  "",
  "## Issue Counts",
  "",
  ...Object.entries(report.issue_counts).map(([code, count]) => `- ${code}: ${count}`),
  "",
  "## Files",
  "",
  "| Priority | File | Unique Questions | Ranges | Issue Counts |",
  "|---:|---|---:|---|---|",
  ...report.files.map((fileSummary) => {
    const counts = Object.entries(fileSummary.issue_counts)
      .map(([code, count]) => `${code}=${count}`)
      .join("; ");
    return `| ${fileSummary.priority_score} | ${fileSummary.path} | ${fileSummary.unique_issue_question_count} | ${fileSummary.question_ranges} | ${counts} |`;
  }),
  "",
];
fs.writeFileSync(path.join(reportDir, "audit-2026-08-31-explanation-quality-full.md"), `${lines.join("\n")}\n`, "utf8");

console.log(
  JSON.stringify(
    {
      scanned_files: report.scanned_files,
      total_questions: report.total_questions,
      complete_learning_fields: report.complete_learning_fields,
      missing_or_partial_learning_fields: report.missing_or_partial_learning_fields,
      file_count_with_any_issue: report.file_count_with_any_issue,
      issue_counts: report.issue_counts,
      top_files: report.files.slice(0, 20).map((fileSummary) => ({
        path: fileSummary.path,
        priority_score: fileSummary.priority_score,
        unique_issue_question_count: fileSummary.unique_issue_question_count,
        question_ranges: fileSummary.question_ranges,
        issue_counts: fileSummary.issue_counts,
      })),
    },
    null,
    2,
  ),
);
