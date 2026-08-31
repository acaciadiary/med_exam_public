const fs = require("node:fs");

const file = "public/data/exams/111-1/medicine-6.json";
const labels = ["A", "B", "C", "D"];
const dataset = JSON.parse(fs.readFileSync(file, "utf8").replace(/^\uFEFF/, ""));

function normalize(text) {
  return String(text || "")
    .normalize("NFKC")
    .toLowerCase()
    .replace(/^[-*\s]*[a-d][.：:]\s*/i, "")
    .replace(/[^\p{L}\p{N}]+/gu, "");
}

function grams(text) {
  const normalized = normalize(text);
  if (!normalized) return [];
  if (normalized.length <= 3) return [normalized];
  return Array.from({ length: normalized.length - 2 }, (_, index) => normalized.slice(index, index + 3));
}

function dice(left, right) {
  const leftGrams = grams(left);
  const rightGrams = grams(right);
  if (!leftGrams.length || !rightGrams.length) return 0;
  const counts = new Map();
  for (const gram of leftGrams) counts.set(gram, (counts.get(gram) || 0) + 1);
  let hits = 0;
  for (const gram of rightGrams) {
    const count = counts.get(gram) || 0;
    if (count > 0) {
      hits += 1;
      counts.set(gram, count - 1);
    }
  }
  return (2 * hits) / (leftGrams.length + rightGrams.length);
}

function optionLines(explanation) {
  const section = String(explanation || "").split("【選項詳解】")[1]?.split("【核心考點】")[0] || "";
  const out = {};
  for (const line of section.split(/\n/).map((item) => item.trim()).filter(Boolean)) {
    const match = line.match(/^[-*\s]*([A-D])[.：:]\s*(.*)$/);
    if (match) out[match[1]] = match[2];
  }
  return out;
}

const flags = [];
for (const question of dataset.questions || []) {
  const options = optionLines(question.explanation);
  if (labels.some((label) => !options[label])) {
    flags.push({ question_number: question.question_number, issue: "missing option line" });
    continue;
  }
  const texts = labels.map((label) => options[label]);
  const pairwise = [];
  for (let i = 0; i < texts.length; i += 1) {
    for (let j = i + 1; j < texts.length; j += 1) pairwise.push(dice(texts[i], texts[j]));
  }
  const avg = pairwise.reduce((sum, value) => sum + value, 0) / pairwise.length;
  const max = Math.max(...pairwise);
  const openings = texts.map((text) => normalize(text).slice(0, 24));
  const repeated = openings.filter((value, index, all) => value && all.indexOf(value) !== index);
  if (avg >= 0.78 || max >= 0.94 || repeated.length) {
    flags.push({
      question_number: question.question_number,
      avg_similarity: Number(avg.toFixed(3)),
      max_similarity: Number(max.toFixed(3)),
      repeated_openings: [...new Set(repeated)],
    });
  }
}

console.log(JSON.stringify({
  file,
  question_count: dataset.questions.length,
  option_similarity_flags: flags.length,
  flags,
}, null, 2));
