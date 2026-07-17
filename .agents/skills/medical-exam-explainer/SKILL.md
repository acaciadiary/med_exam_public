---
name: medical-exam-explainer
description: Use when creating, rewriting, auditing, or batch-updating high-quality Traditional Chinese explanations for Taiwan medical exam question JSON files in this project. Trigger when the user asks to 製作詳解、重寫詳解、修正低品質詳解、把某幾年或某 18 張考卷詳解重寫、處理某一年考卷、分 6 張考卷處理、只替換 explanation/詳解欄位、不改網頁架構、或完成後提醒用 GitHub Desktop Commit and Push origin.
---

# Medical Exam Explainer

Use this skill to produce high-quality Traditional Chinese explanations for medical exam questions in `public/data/exams/<YEAR>/<SUBJECT>.json`.

The core rule is simple: **only replace explanation-related content. Do not change the question bank structure or frontend.**

## Scope

Allowed changes:

- Rewrite `explanation` / `詳解` / `解析` fields.
- Update closely related learning fields only when they already exist and are clearly derived from the explanation, such as `key_point`, `flashcard_summary`, `flashcard_front`, `flashcard_back`, `review_status`, `explanation_model`, and `explanation_generated_at`.
- Add a gentle note inside the explanation when the official answer appears questionable.
- During parallel micro-batch work, writer subagents should create 10-question update JSON files under `scratch/rewrite_updates/` instead of editing the source exam JSON directly. The main thread merges approved updates.

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

Default to processing exam papers sequentially, one paper at a time, unless the user explicitly asks to trade quality for speed. Do not assign an entire 80-100 question paper to one long-running subagent.

### Micro-Batch Subagent Workflow

For quality-critical rewrites, use short-lived micro-batch workers:

- Work on one paper at a time.
- Split the paper into 10-question ranges:
  - 100-question paper: `1-10`, `11-20`, ..., `91-100`.
  - 80-question paper: `1-10`, `11-20`, ..., `71-80`.
- Run at most 5 subagents in parallel per wave.
- Give each subagent exactly one 10-question range from exactly one source JSON file.
- Writer subagents must not edit `public/data/exams/...` directly.
- Each writer writes a standalone update file:
  - Path pattern: `scratch/rewrite_updates/<YEAR>_<SUBJECT>/q<START>-q<END>.json`
  - Example: `scratch/rewrite_updates/109-1_medicine-3/q001-q010.json`
- After the wave finishes, collect update files, validate update JSON, run the anti-AI style gate, and close those subagents.
- Do not send a 10-question update file to review if it still contains banned filler phrases, repeated option paragraphs, or generic "not the best answer" wording.
- The main thread merges approved update files into the source exam JSON after review.
- Then launch the next wave of 5 fresh subagents.
- Finish all ranges for the current paper before starting the next paper.
- After every completed 100 questions, launch one fresh review subagent to audit those 100 rewritten questions before continuing to the next 100-question block when practical.

Why this matters:

- 80-100 questions in one agent causes context fatigue and template drift.
- Fresh 10-question workers are less likely to copy the same paragraph into every option.
- Update files prevent parallel workers from overwriting each other inside the same large JSON file.
- Sequential paper processing makes conflicts easier to detect and keeps diffs reviewable.
- 5 parallel workers is usually enough speed without sacrificing quality.
- A separate 100-question review subagent catches drift early, so the user does not need to manually recheck the whole project at the end.

If subagents are unavailable, process the same 10-question ranges sequentially in the main thread and report that fallback.

### Review Gates

Use a lightweight gate after every 10-question update file and a full review gate after each completed 100 questions.

10-question anti-AI gate:

- Run this before a micro-batch can be marked ready for review.
- The update file must have zero banned template phrases.
- No sentence or paragraph longer than one short clause should be reused across three or more options in the same question.
- Each option A-D must mention that option's own medical content, not only compare it to the standard answer.
- Wrong options must name the concrete wrong claim, mechanism, anatomy, diagnostic criterion, contraindication, or management step.
- If a 10-question file fails this gate, repair only the failed questions and rerun the gate before review.

100-question review gate:

- For a 100-question paper, run the review subagent after the whole paper is rewritten.
- For an 80-question paper, combine with the next paper's first 20 rewritten questions when convenient, or run an 80-question review gate if it is the end of the current work chunk.
- The review subagent must be independent from the writers and must not rewrite by default.
- Review subagents should review the update JSON files against the source exam JSON before those updates are merged.
- The review subagent audits only quality and scope:
  - Check that all assigned questions have the required three headings.
  - Check that each option A-D has a concrete reason.
  - Check that wrong options explain the specific false statement, not generic "not best answer" language.
  - Check that banned filler phrases are absent.
  - Check that no long sentence or source paragraph is reused across three or more option explanations.
  - Check that options do not share a rigid template opening such as "對照本題核心解析" or "雖然與題目主題相關". Each option should begin from the option's own content when possible.
  - For negative stems such as "不是" or "較不可能", check that the labels make the logic clear: the keyed option is the exception, while the other options are true/possible statements.
  - Check that `key_point`, `flashcard_summary`, and `flashcard_back` are useful and not vague.
  - Check that learning fields do not carry a stale department/template label unrelated to the question content.
  - Check that no question text, options, answer keys, IDs, ordering, or frontend files changed.
  - Flag suspected medical or official-answer issues for manual review.
- If the reviewer finds serious issues, pause the next writing wave and repair the failed 10-question range with a fresh worker.
- Only continue once the review subagent reports pass or lists a bounded repair queue.
- Merge only update files that pass review or have completed bounded repair.

The review gate is meant to reduce final manual inspection. It does not replace final validation, but it prevents discovering repeated low-quality output only at the end.

Progress reporting:

- Report progress after each wave, not only after each paper.
- Include current paper, completed range count, completed question count, latest review-gate result, remaining question count, and suspected issues.
- Keep reports concise and understandable for a non-technical user.

## Explanation Quality Bar

Every explanation must teach the actual exam logic, not merely restate the answer.

Gold-standard explanations must look like the manually repaired pregnancy/internal-medicine example:

- The stem analysis identifies the tested decision, not just "answer is C".
- Each option gets its own concrete medical reason.
- Wrong options explain the specific false claim, contraindication, wrong mechanism, wrong anatomy, wrong treatment, or wrong diagnostic criterion.
- Correct options explain why the official answer is medically valid.
- The core point is a reusable rule the student can apply next time.
- Do not copy the same paragraph into A, B, C, and D.
- Do not write "original explanation says..." or "existing analysis says..." inside the final explanation.

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

For negative questions such as "何者錯誤", "何者不適當", "何者不是", "何者較不可能", explicitly remind that the selected option is the wrong/inappropriate statement, exception, or non-typical item. Do not label the other options as simply "wrong" without explaining that they are true/possible and therefore not selected.

## Gold Standard Rewrite Pattern

When rewriting low-quality explanations, use this process for each question:

1. Identify the exam task:
   - Is the stem asking diagnosis, mechanism, anatomy, drug choice, contraindication, guideline-like management, epidemiology, or "which is false"?
   - If the stem is negative, state that the selected answer is the exception or false statement.
2. Extract the official answer without changing it.
3. For each option A-D, write the specific reason:
   - Use the option's own medical content.
   - Explain exactly why it is correct or wrong.
   - Avoid generic comparisons such as "not the best answer".
4. Write a compact core rule:
   - One to three sentences.
   - Include the high-yield contrast, contraindication, diagnostic criterion, mechanism, or clinical trap.
5. Update learning fields if present:
   - `key_point`: one precise rule.
   - `flashcard_front`: keywords only, if it already exists.
   - `flashcard_back`: direct answer rule, not vague encouragement.
   - `flashcard_summary`: compact `topic -> rule` summary.
   - `review_status`: use `ai_generated` unless the user explicitly asks to mark as reviewed or the item was manually reviewed.
   - `explanation_model`: use a clear tag such as `codex-high-quality-rewrite`.
   - `explanation_generated_at`: update with the current timestamp.

## Update JSON Contract

Writer subagents must output update JSON, not patch the source exam file.

Use this shape:

```json
{
  "source_file": "public/data/exams/109-1/medicine-3.json",
  "dataset_id": "109-1_medicine-3",
  "range": { "start": 1, "end": 10 },
  "updates": [
    {
      "question_id": "109-1_medicine-3_001",
      "question_number": 1,
      "explanation": "【題幹解析】...",
      "key_point": "...",
      "flashcard_front": "...",
      "flashcard_back": "...",
      "flashcard_summary": "...",
      "review_status": "ai_generated",
      "explanation_model": "codex-high-quality-rewrite",
      "explanation_generated_at": "2026-07-07T20:55:00+08:00",
      "manual_review_notes": []
    }
  ]
}
```

Rules:

- Include exactly the assigned question range unless a question is intentionally skipped with a `manual_review_notes` reason.
- Do not include question text, options, correct answers, answer status, IDs for other questions, or frontend fields.
- Preserve `question_id` and `question_number` exactly from the source.
- `manual_review_notes` must be an array of short strings. Use an empty array if no issue.
- The main thread is responsible for applying update files to the source JSON.

### Good Option Explanation Shape

For a pregnancy internal-medicine question, the final answer should be this specific:

```text
- A. 錯誤。子癲前症的典型診斷重點確實包括妊娠 20 週後新發高血壓與蛋白尿或器官受損，但「絕對禁用 aspirin」錯。對高風險孕婦，低劑量 aspirin 常用於預防子癲前症，重點是低劑量與適當適應症，而不是一律禁用。
- B. 錯誤。ARB 與 ACE inhibitor 會影響胎兒腎臟發育，可造成羊水過少、胎兒腎衰竭等風險，因此懷孕期間禁用；孕期高血壓常用 labetalol、nifedipine 或 methyldopa。
- C. 正確。二尖瓣狹窄會阻礙左心房血液進入左心室；懷孕時血容量與心輸出量上升，會讓左心房壓更高，進一步造成肺鬱血、肺水腫與心衰竭。
- D. 錯誤。妊娠糖尿病先以飲食、運動與血糖監測處理；若仍無法達標，傳統上以胰島素為最可靠且常用的藥物選擇。DPP-IV inhibitor 不是妊娠糖尿病第一線建議藥物。
```

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
- `標準答案所接受的判斷`
- `雖然與題目主題相關`
- `與標準答案的關鍵判斷不一致`
- `對照本題核心解析`

These phrases are considered low-quality when used as filler. Replace them with concrete mechanisms, clinical clues, diagnostic criteria, anatomy, pathology, pharmacology, treatment principles, or exam-relevant contrasts.

Also eliminate these low-value rewrite habits:

- Repeating the same source paragraph after every option.
- Repeating the same long sentence or core paragraph in three or more A-D option explanations, even if each option has a different opening phrase.
- Saying only `此選項不是最佳答案`.
- Saying only `與正確答案的關鍵判斷點不一致`.
- Saying only `與標準答案的關鍵判斷不一致`.
- Saying `作答時應回到題幹線索與標準答案比對`.
- Writing a core point like `熟悉疾病機轉、臨床表現、診斷檢查與治療原則`.
- Using department labels such as `心臟內科的基本判斷能力` as the main explanation.
- Treating all wrong options as generic distractors instead of explaining each option's actual false statement.

## Anti-AI Style Gate

This project should read like a careful senior student or teacher explaining the exam logic, not like a templated answer generator.

Hard fail patterns:

- Starting many options with the same scaffolding phrase, such as "對照本題核心解析", "雖然與題目主題相關", or "與標準答案的關鍵判斷不一致".
- Explaining wrong options only by saying they are not the official answer.
- Copying the same disease overview, stem summary, or treatment paragraph into A, B, C, and D.
- Writing a core point that could fit almost any question, such as "熟悉定義、機轉、臨床表現與治療原則".
- Making the explanation sound like it is grading options from outside the question instead of teaching why each option is medically right or wrong.

Preferred human explanation style:

- Start each option from the option's own claim: "C 錯在把外淋巴與內淋巴的鈉鉀組成反過來", "B 錯在 ACE inhibitor/ARB 懷孕禁用", "D 對，因為 metformin 會抑制肝臟糖質新生".
- Use short exam-facing contrasts: "不是一律禁用 aspirin，而是高風險孕婦可用低劑量 aspirin 預防子癲前症".
- For infectious disease, surgery, anatomy, pathology, pharmacology, and guideline-like questions, name the exact clue, structure, mechanism, drug class, threshold, or contraindication.
- Keep the tone professional and compact. Avoid sounding chatty, but also avoid boilerplate.
- If the same sentence would still make sense after replacing the disease name with another disease, it is probably too generic and should be rewritten.

Content trust interpretation:

- `validate:explanations` passing means the format is complete; it does not prove the explanation is natural or high quality.
- A paper is not ready to call "clean" until its file-scoped `content:trust` report has `banned_template_phrase = 0` and `repeated_option_segment = 0`, or the remaining flags are explicitly reviewed and accepted with a reason.
- If whole-site `content:trust` is noisy, use file-scoped trust for the active paper and track unrelated risky files as backlog.

## Medical Accuracy Rules

- Use current standard medical knowledge for stable concepts.
- For high-risk, uncertain, recent guideline-dependent, or answer-disputed content, verify with reliable sources before finalizing.
- Prefer authoritative references such as official guidelines, professional societies, standard textbooks, or government/academic medical resources.
- If verification is not possible, write a cautious explanation and add a manual-review issue.
- Do not invent facts to make an option sound wrong.
- Distinguish "less likely" from "impossible"; medical options are often distractors, not absolute falsehoods.
- For current guideline-sensitive topics such as pregnancy medication safety, diabetes treatment, hypertension guidelines, anticoagulation, cancer screening, infectious disease treatment, or emergency algorithms, verify with reliable sources when possible before rewriting.
- If a question reflects older official-answer logic, preserve the official answer but add a concise manual-review note only when the modern standard appears to conflict.

## Style

- Write in Traditional Chinese.
- Use English medical terms in parentheses when useful, especially for exam keywords.
- Keep wording concise but educational.
- Aim for medical students and national exam candidates.
- Avoid overly casual tone inside explanations.
- Avoid long textbook paragraphs unless the question truly requires it.

## Subagent Prompt Template

Use this prompt for each 10-question micro-batch subagent:

```text
你負責處理 <YEAR> 的 <SUBJECT> 這一張考卷中的第 <START>-<END> 題。這是短任務；你只需要處理這 10 題，完成後停止。

請讀取 <FILE_PATH> 中第 <START>-<END> 題，但不要直接修改 <FILE_PATH>。請把第 <START>-<END> 題的重寫結果輸出成 update JSON 檔：<UPDATE_FILE_PATH>。

update JSON 只能包含 source_file、dataset_id、range、updates，以及每題的 question_id、question_number、explanation、key_point、flashcard_front、flashcard_back、flashcard_summary、review_status、explanation_model、explanation_generated_at、manual_review_notes。不要輸出題目、選項、答案、題號以外的原始結構，也不要修改任何網頁架構。

每一題詳解必須包含：
【題幹解析】
【選項詳解】
【核心考點】

請逐一說明 A、B、C、D 為何正確或錯誤，避免模板廢話。禁止使用「題目中選項 A 所代表的鑑別或處置」「不能最精準回答本題」「請用題幹線索連回」這類空泛句。

品質要求要比「有三段標題」更高：不能重複貼同一段原始解析到每個選項；不能只寫「不是最佳答案」；每個選項都要有自己的醫學理由。例如藥物題要指出禁忌或第一線選擇，解剖題要指出神經/血管/構造，病理題要指出機轉或診斷標準。

每題完成前自查：
1. A-D 是否都有自己的具體醫學理由？
2. 是否刪掉「回到題幹線索」「不是最佳答案」「原始解析重點指出」等模板句？
3. 【核心考點】是否是可複用的考試規則，而不是科別空話？
4. 是否沒有在三個以上選項重複同一段疾病總論或題幹摘要？
5. 每個錯誤選項是否都明確指出該選項自己的錯點？
6. 是否只輸出了 update JSON，沒有直接改原始考卷檔？

若發現官方答案疑似錯誤，不要更改答案，請在詳解中以「補充提醒」指出需要人工複核，並在回報中列出題號。

完成後請回報：
1. 已完成題號範圍與題數
2. 疑似需人工複核題號
3. update JSON 檔案路徑
4. 是否已清除禁用模板句
5. 是否沒有重複選項段落
6. 是否通過 JSON 格式檢查
```

## Review Subagent Prompt Template

Use this prompt for each 100-question review gate:

```text
你是回頭檢查用的品質審查員，不是本批詳解撰寫者。

請審查 <UPDATE_FILES> 中剛重寫完成的 update JSON，並對照來源考卷 <SOURCE_FILES>。不要主動重寫整批內容；你的任務是找出可以合併的 update 檔、需要返工的題號與原因。

審查標準：
1. 每題是否都有【題幹解析】【選項詳解】【核心考點】。
2. A-D 是否都有各自的具體醫學理由，而不是共用同一段話。
3. 是否出現禁用模板句：非本題答案、不是本題標準答案、回到題幹線索、請用題幹線索連回、不能最精準回答本題、最符合題幹、核心記憶點、定義、機轉、典型表現或處置原則、標準答案所接受的判斷、雖然與題目主題相關、與標準答案的關鍵判斷不一致、對照本題核心解析。
4. 是否還有「此選項不是最佳答案」「與正確答案的關鍵判斷點不一致」「原始解析重點指出」這類低品質句。
5. 是否有同一長句或同一核心段落出現在三個以上選項；有的話列為返工。
6. 若題幹是否定問法，例如「不是」「錯誤」「較不可能」，是否清楚說明正答是例外，而其他選項是真正可能或正確的敘述。
7. key_point、flashcard_summary、flashcard_back 是否具體可用，且沒有殘留錯誤科別或舊模板標籤。
8. 是否有疑似醫學內容錯誤或官方答案疑義。
9. update JSON 是否只包含允許欄位，沒有夾帶題目、選項、答案、JSON 結構或前端修改。
10. 若這批題解讀起來像用固定模板套出的答案，請直接列為返工，即使格式驗證會通過。

請輸出：
1. 審查範圍與題數
2. 通過題數
3. 可合併 update 檔清單
4. 需要返工題號清單，每題用一句話說明問題
5. 疑似需人工複核題號
6. 是否建議暫停下一波寫作
```

## Validation

After updating explanations:

1. Check JSON parse validity for every source exam JSON and every update JSON.
2. Validate every update JSON before merge:
   - source file exists.
   - dataset id matches.
   - question ids and question numbers match the source.
   - updates stay inside the assigned range.
   - only allowed update fields are present.
3. Search update files for banned filler phrases and repeated option paragraphs before review.
4. Run the 10-question anti-AI style gate before a micro-batch can be approved.
5. Run the 100-question review gate against update files before merging when applicable.
6. Merge only approved update files into source exam JSON.
7. After merge, compare diffs and confirm only explanation-related fields changed.
8. For micro-batches, confirm the merged diff only touches approved question ranges.
9. Spot-check at least one rewritten question per 10-question range before launching the next wave.
10. Run available project validation/build commands when reasonable.
11. Run a file-scoped `content:trust` audit for the active paper after merge, especially before saying a paper is clean.
12. Treat `repeated_option_segment`, `banned_template_phrase`, stale learning fields, and unclear negative-stem labels as repair items, even when `validate:explanations` passes.
13. Do not call an active paper clean unless file-scoped `content:trust` has zero risky findings, or the remaining findings are explicitly listed and accepted as false positives.
14. If local browser access to `localhost` or `127.0.0.1` is blocked, do not retry repeatedly. Use server response checks, data loading checks, tests, and build verification.

Suggested checks when relevant:

```powershell
python .agents/skills/medical-exam-explainer/scripts/check_diff.py
python .agents/skills/medical-exam-explainer/scripts/check_progress.py
node scripts/exams/run_python.mjs scripts/exams/audit_content_trust.py public/data/exams/<YEAR>/<SUBJECT>.json --out reports/<YEAR>_<SUBJECT>-content-trust.json
npm run build
```

Only run commands that fit the current repository state. If a command is unavailable, explain that clearly.

## Final Report

Final response to the user must include:

- Which year was processed.
- Which 6 papers were completed or skipped.
- Whether the micro-batch workflow was used, including batch size and max parallel workers.
- How many 10-question update JSON files were produced and merged.
- How many 100-question review gates were run and whether any repair queue remains.
- Whether the 10-question anti-AI style gates passed, especially banned phrase and repeated option checks.
- Any suspected answer/content issues requiring manual review.
- What validation was run and whether it passed.
- Confirmation that no website structure was changed.
- If the user requested "推送到Github", remind them step by step:
  1. Open GitHub Desktop.
  2. Review the changed files.
  3. Enter a commit message.
  4. Click Commit.
  5. Click Push origin.
