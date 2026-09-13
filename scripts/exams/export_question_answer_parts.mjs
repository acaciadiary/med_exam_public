import fs from "node:fs";
import path from "node:path";
import process from "node:process";

const ROOT = process.cwd();
const MANIFEST_PATH = path.join(ROOT, "public", "data", "manifest.json");
const OUTPUT_DIR = path.join(
  ROOT,
  "public",
  "data",
  "question-answer-fulltext",
);
const PART_COUNT = 5;
const OMITTED_QUESTION_FIELDS = new Set([
  "explanation",
  "explanation_model",
  "explanation_generated_at",
]);

function readJson(filePath) {
  const raw = fs.readFileSync(filePath, "utf8").replace(/^\uFEFF/, "");
  return JSON.parse(raw);
}

function compareExamItems(a, b) {
  const [aYear, aAttempt] = a.year.split("-").map(Number);
  const [bYear, bAttempt] = b.year.split("-").map(Number);
  if (aYear !== bYear) return aYear - bYear;
  if (aAttempt !== bAttempt) return aAttempt - bAttempt;

  const aSubject = Number(a.subject.replace("medicine-", ""));
  const bSubject = Number(b.subject.replace("medicine-", ""));
  return aSubject - bSubject;
}

function withoutOmittedFields(question) {
  return Object.fromEntries(
    Object.entries(question).filter(([key]) => !OMITTED_QUESTION_FIELDS.has(key)),
  );
}

function getCorrectAnswerText(question) {
  const answers = Array.isArray(question.correct_answers)
    ? question.correct_answers
    : question.correct_answer
      ? [question.correct_answer]
      : [];

  return answers
    .map((key) => ({
      key,
      text: question.options?.[key] ?? null,
    }))
    .filter((item) => item.text !== null);
}

function chunkEvenly(items, partCount) {
  const partSize = Math.ceil(items.length / partCount);
  return Array.from({ length: partCount }, (_, index) =>
    items.slice(index * partSize, (index + 1) * partSize),
  );
}

function buildExportQuestions(manifest) {
  const exams = [...manifest.exams].sort(compareExamItems);
  const questions = [];

  for (const exam of exams) {
    const sourcePath = path.join(ROOT, "public", exam.path);
    const dataset = readJson(sourcePath);

    for (const question of dataset.questions) {
      const correctAnswerText = getCorrectAnswerText(question);

      questions.push({
        global_index: questions.length + 1,
        source_exam: {
          id: dataset.id,
          year: dataset.year,
          title: dataset.title,
          subject: dataset.subject,
          source: dataset.source,
          updated_at: dataset.updated_at,
          path: path.relative(ROOT, sourcePath).replaceAll(path.sep, "/"),
        },
        ...withoutOmittedFields(question),
        correct_answer_text:
          correctAnswerText.length === 1 ? correctAnswerText[0].text : null,
        correct_answer_texts: correctAnswerText,
      });
    }
  }

  return questions;
}

function writeExports(questions) {
  fs.mkdirSync(OUTPUT_DIR, { recursive: true });

  for (const fileName of fs.readdirSync(OUTPUT_DIR)) {
    if (/^question-answer-fulltext-part-\d{2}\.json$/.test(fileName)) {
      fs.unlinkSync(path.join(OUTPUT_DIR, fileName));
    }
  }

  const chunks = chunkEvenly(questions, PART_COUNT);
  const exportedAt = new Date().toISOString();
  const files = [];

  chunks.forEach((chunk, index) => {
    const part = index + 1;
    const fileName = `question-answer-fulltext-part-${String(part).padStart(
      2,
      "0",
    )}.json`;
    const filePath = path.join(OUTPUT_DIR, fileName);
    const payload = {
      export_type: "question_answer_fulltext",
      exported_at: exportedAt,
      part,
      part_count: PART_COUNT,
      total_questions: questions.length,
      question_count: chunk.length,
      global_index_start: chunk[0]?.global_index ?? null,
      global_index_end: chunk.at(-1)?.global_index ?? null,
      questions: chunk,
    };

    fs.writeFileSync(filePath, `${JSON.stringify(payload, null, 2)}\n`, "utf8");
    files.push({ filePath, count: chunk.length });
  });

  return files;
}

function verifyExports(files, expectedQuestionCount) {
  let total = 0;
  const ids = new Set();

  for (const { filePath } of files) {
    const payload = readJson(filePath);
    total += payload.questions.length;

    for (const question of payload.questions) {
      ids.add(question.id);

      for (const forbiddenField of OMITTED_QUESTION_FIELDS) {
        if (Object.hasOwn(question, forbiddenField)) {
          throw new Error(`${filePath} contains omitted field: ${forbiddenField}`);
        }
      }

      if (!Array.isArray(question.correct_answer_texts)) {
        throw new Error(`${filePath} has invalid correct_answer_texts`);
      }
    }
  }

  if (total !== expectedQuestionCount) {
    throw new Error(`Expected ${expectedQuestionCount} questions, got ${total}`);
  }

  if (ids.size !== expectedQuestionCount) {
    throw new Error(`Expected ${expectedQuestionCount} unique ids, got ${ids.size}`);
  }
}

const manifest = readJson(MANIFEST_PATH);
const questions = buildExportQuestions(manifest);
const files = writeExports(questions);
verifyExports(files, questions.length);

console.log(`Exported ${questions.length} questions into ${files.length} files.`);
for (const { filePath, count } of files) {
  console.log(`${path.relative(ROOT, filePath)}: ${count}`);
}
