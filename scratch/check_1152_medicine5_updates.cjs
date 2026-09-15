const fs = require("fs");
const path = require("path");

const sourcePath = "public/data/exams/115-2/medicine-5.json";
const source = JSON.parse(fs.readFileSync(sourcePath, "utf8"));
const sourceById = new Map(source.questions.map((q) => [q.id, q]));
const updateDir = "scratch/rewrite_updates/115-2_medicine-5";

const allowedTop = new Set(["source_file", "dataset_id", "range", "updates"]);
const allowedUpdate = new Set([
  "question_id",
  "question_number",
  "explanation",
  "key_point",
  "flashcard_front",
  "flashcard_back",
  "flashcard_summary",
  "review_status",
  "explanation_model",
  "explanation_generated_at",
  "manual_review_notes",
]);

const banned = [
  "非本題答案",
  "不是本題標準答案",
  "回到題幹線索",
  "請用題幹線索連回",
  "題目中選項 A 所代表的鑑別或處置",
  "不能最精準回答本題",
  "最符合題幹",
  "核心記憶點",
  "定義、機轉、典型表現或處置原則",
  "標準答案所接受的判斷",
  "雖然與題目主題相關",
  "與標準答案的關鍵判斷不一致",
  "對照本題核心解析",
  "此選項不是最佳答案",
  "與正確答案的關鍵判斷點不一致",
  "原始解析重點指出",
];

function sentenceList(text) {
  return text
    .split(/[。；;]/)
    .map((item) => item.trim().replace(/\s+/g, " "))
    .filter((item) => item.length >= 18);
}

const errors = [];
let updateCount = 0;
const seenQuestions = new Set();

for (const name of fs.readdirSync(updateDir).filter((file) => file.endsWith(".json")).sort()) {
  const filePath = path.join(updateDir, name);
  const payload = JSON.parse(fs.readFileSync(filePath, "utf8"));

  for (const key of Object.keys(payload)) {
    if (!allowedTop.has(key)) errors.push(`${name}: unexpected top field ${key}`);
  }
  if (payload.source_file !== sourcePath) errors.push(`${name}: source_file mismatch`);
  if (payload.dataset_id !== "115-2_medicine-5") errors.push(`${name}: dataset_id mismatch`);

  for (const item of payload.updates) {
    updateCount += 1;
    for (const key of Object.keys(item)) {
      if (!allowedUpdate.has(key)) errors.push(`${name} Q${item.question_number}: unexpected update field ${key}`);
    }
    const sourceQuestion = sourceById.get(item.question_id);
    if (!sourceQuestion) {
      errors.push(`${name} Q${item.question_number}: source question_id not found`);
      continue;
    }
    if (sourceQuestion.question_number !== item.question_number) {
      errors.push(`${name} Q${item.question_number}: question number mismatch`);
    }
    if (item.question_number < payload.range.start || item.question_number > payload.range.end) {
      errors.push(`${name} Q${item.question_number}: update outside batch range`);
    }
    if (seenQuestions.has(item.question_number)) {
      errors.push(`${name} Q${item.question_number}: duplicate update`);
    }
    seenQuestions.add(item.question_number);

    for (const heading of ["【題幹解析】", "【選項詳解】", "【核心考點】"]) {
      if (!item.explanation.includes(heading)) errors.push(`${name} Q${item.question_number}: missing ${heading}`);
    }
    for (const label of ["- A.", "- B.", "- C.", "- D."]) {
      if (!item.explanation.includes(label)) errors.push(`${name} Q${item.question_number}: missing ${label}`);
    }
    for (const phrase of banned) {
      if (
        item.explanation.includes(phrase) ||
        item.key_point.includes(phrase) ||
        item.flashcard_summary.includes(phrase)
      ) {
        errors.push(`${name} Q${item.question_number}: banned phrase ${phrase}`);
      }
    }

    const optionBlock = (item.explanation.split("【選項詳解】")[1] || "").split("【核心考點】")[0] || "";
    const optionParts = optionBlock.split(/\n- [ABCD]\. /).slice(1);
    const repeatedSentences = new Map();
    for (const optionPart of optionParts) {
      for (const sentence of sentenceList(optionPart)) {
        repeatedSentences.set(sentence, (repeatedSentences.get(sentence) || 0) + 1);
      }
    }
    for (const [sentence, count] of repeatedSentences) {
      if (count >= 3) {
        errors.push(`${name} Q${item.question_number}: repeated option sentence x${count}: ${sentence}`);
      }
    }
  }
}

if (updateCount !== 80) errors.push(`Expected 80 updates, found ${updateCount}`);
for (let i = 1; i <= 80; i += 1) {
  if (!seenQuestions.has(i)) errors.push(`Missing question ${i}`);
}

const result = {
  files: fs.readdirSync(updateDir).filter((file) => file.endsWith(".json")).length,
  updates: updateCount,
  errors,
};
console.log(JSON.stringify(result, null, 2));
if (errors.length > 0) process.exit(1);
