---
name: medical-exam-explainer
description: Use when creating, rewriting, auditing, or batch-updating Traditional Chinese explanations for Taiwan medical exam question JSON files in this project. Trigger when the user asks to 製作詳解、重寫詳解、修正低品質詳解、處理某一年考卷、分 6 張考卷處理、只替換 explanation/詳解欄位、不改網頁架構、或完成後提醒用 GitHub Desktop Commit and Push origin.
---

# Medical Exam Explainer

Use this skill to produce high-quality Traditional Chinese explanations for medical exam questions in `public/data/exams/<YEAR>/<SUBJECT>.json`.

The core rule is simple: **only replace explanation-related content. Do not change the question bank structure or frontend.**

## Scope

Allowed changes:

- Rewrite `explanation` / `詳解` / `解析` fields.
- Update closely related learning fields only when they already exist and are clearly derived from the explanation, such as `key_point`, `flashcard_summary`, `flashcard_front`, `flashcard_back`, `review_status`, `explanation_model`, and `explanation_generated_at`.
- Add a gentle note inside the explanation when the official answer appears questionable.

Forbidden changes:

- Do not modify question text.
- Do not modify option text.
- Do not modify `correct_answer`, `correct_answers`, `answer_status`, or official correction fields.
- Do not add, delete, reorder, or renumber questions.
- Do not rename JSON fields.
- Do not modify frontend components, routes, styles, data loading logic, or website layout.
- Do not silently fix suspected answer errors. Flag them for manual review instead.

## Year Workflow

When the user provides one year, process that year as 6 exam papers:

- `medicine-1`
- `medicine-2`
- `medicine-3`
- `medicine-4`
- `medicine-5`
- `medicine-6`

Prefer using 6 parallel subagents when available, with one subagent per paper. Each subagent must only edit its assigned file. If subagents are unavailable, process the 6 files sequentially and report that fallback.

Progress reporting:

- Report progress every 120 seconds during long runs.
- Include completed paper count, completed question count, remaining question count, and suspected issues.
- Keep reports concise and understandable for a non-technical user.

## Explanation Quality Bar

Every explanation must teach the actual exam logic, not merely restate the answer.

Required structure:

```text
【題幹解析】
用 1 到 3 句說明本題在問什麼、關鍵線索是什麼、為什麼標準答案成立。

【選項詳解】
- A. 說明此選項為何正確或錯誤。必須包含具體醫學理由。
- B. 說明此選項為何正確或錯誤。必須包含具體醫學理由。
- C. 說明此選項為何正確或錯誤。必須包含具體醫學理由。
- D. 說明此選項為何正確或錯誤。必須包含具體醫學理由。

【核心考點】
用 1 到 3 句整理下次作答應記住的規則、鑑別點或臨床判斷。
```

For multi-answer or official correction questions, clearly state the accepted answer set and why each accepted choice is valid.

For negative questions such as "何者錯誤", "何者不適當", "何者較不可能", explicitly remind that the selected option is the wrong/inappropriate statement.

## Bad Explanation Patterns To Eliminate

Never write these template-like phrases unless immediately followed by specific medical reasoning:

- `非本題答案`
- `不是本題標準答案`
- `回到題幹線索`
- `請用題幹線索連回`
- `題目中選項 A 所代表的鑑別或處置`
- `不能最精準回答本題`
- `最符合題幹`
- `核心記憶點`
- `定義、機轉、典型表現或處置原則`

These phrases are considered low-quality when used as filler. Replace them with concrete mechanisms, clinical clues, diagnostic criteria, anatomy, pathology, pharmacology, treatment principles, or exam-relevant contrasts.

## Medical Accuracy Rules

- Use current standard medical knowledge for stable concepts.
- For high-risk, uncertain, recent guideline-dependent, or answer-disputed content, verify with reliable sources before finalizing.
- Prefer authoritative references such as official guidelines, professional societies, standard textbooks, or government/academic medical resources.
- If verification is not possible, write a cautious explanation and add a manual-review issue.
- Do not invent facts to make an option sound wrong.
- Distinguish "less likely" from "impossible"; medical options are often distractors, not absolute falsehoods.

## Style

- Write in Traditional Chinese.
- Use English medical terms in parentheses when useful, especially for exam keywords.
- Keep wording concise but educational.
- Aim for medical students and national exam candidates.
- Avoid overly casual tone inside explanations.
- Avoid long textbook paragraphs unless the question truly requires it.

## Subagent Prompt Template

Use this prompt for each paper-specific subagent:

```text
你負責處理 <YEAR> 的 <SUBJECT> 這一張考卷。

請只替換本檔案中的 explanation/詳解/解析相關內容，不要改題目、選項、答案、題號、欄位名稱、JSON 結構或任何網頁架構。

每一題詳解必須包含：
【題幹解析】
【選項詳解】
【核心考點】

請逐一說明 A、B、C、D 為何正確或錯誤，避免模板廢話。禁止使用「題目中選項 A 所代表的鑑別或處置」「不能最精準回答本題」「請用題幹線索連回」這類空泛句。

若發現官方答案疑似錯誤，不要更改答案，請在詳解中以「補充提醒」指出需要人工複核，並在回報中列出題號。

完成後請回報：
1. 已完成題數
2. 疑似需人工複核題號
3. 是否只修改詳解相關欄位
4. 是否通過 JSON 格式檢查
```

## Validation

After updating explanations:

1. Check JSON parse validity for every edited file.
2. Compare diffs and confirm only explanation-related fields changed.
3. Search edited files for banned filler phrases.
4. Run available project validation/build commands when reasonable.
5. If local browser access to `localhost` or `127.0.0.1` is blocked, do not retry repeatedly. Use server response checks, data loading checks, tests, and build verification.

Suggested checks when relevant:

```powershell
python .agents/skills/medical-exam-explainer/scripts/check_diff.py
python .agents/skills/medical-exam-explainer/scripts/check_progress.py
npm run build
```

Only run commands that fit the current repository state. If a command is unavailable, explain that clearly.

## Final Report

Final response to the user must include:

- Which year was processed.
- Which 6 papers were completed or skipped.
- Any suspected answer/content issues requiring manual review.
- What validation was run and whether it passed.
- Confirmation that no website structure was changed.
- If the user requested "推送到Github", remind them step by step:
  1. Open GitHub Desktop.
  2. Review the changed files.
  3. Enter a commit message.
  4. Click Commit.
  5. Click Push origin.

