---
name: project-low-friction-workflow
description: Use when working in D:\Antigravity\med_exam_public and the user asks for project changes, validation, troubleshooting, GitHub Desktop handoff, or continuity from prior habits. Preserves the user's Traditional Chinese, step-by-step, low-traffic workflow and this project's preferred verification paths.
---

# Project Low Friction Workflow

This skill keeps work in `D:\Antigravity\med_exam_public` efficient, explainable, and consistent with the user's habits.

## Always-On Habits

- Reply in Traditional Chinese.
- When the user must do anything manually, give numbered step-by-step instructions.
- Keep updates practical: say what is being checked, what was learned, and the next action.
- If memory or conversation history is incomplete, say so plainly. Do not invent past project conversations.
- Preserve user changes. Do not revert unrelated edits.

## Project Context

This is a Vite + React + TypeScript medical exam project with JSON exam data under `public/data/exams`.

Useful commands from `package.json`:

```powershell
npm run typecheck
npm run test
npm run build
npm run validate:data
npm run validate:explanations
npm run dev:local
```

Choose the smallest verification set that matches the change:

- Frontend behavior or UI: `npm run typecheck`, targeted `npm run test` when available, then `npm run build`.
- Exam JSON/data shape: `npm run validate:data`.
- Explanation quality or imported explanations: `npm run validate:explanations`.
- Broad shared behavior: combine `npm run typecheck`, `npm run test`, and `npm run build`.

## Local Web Verification

The built-in browser may block `localhost` or `127.0.0.1` in this project.

When validating local web behavior:

1. Prefer build, tests, server response checks, and data-loading checks first.
2. If a browser check is useful, try it once.
3. If blocked, do not repeatedly retry the same local URL.
4. Switch to command-line checks such as local server logs, HTTP response checks, loaded asset/data checks, frontend tests, and build output.

## GitHub Desktop Meaning

When the user says `推送到Github`, interpret it as a GitHub Desktop handoff, not CLI push permission.

Final reminder should be step-by-step:

1. 打開 GitHub Desktop。
2. 檢查左側 changed files 和每個 diff。
3. 在 Summary 輸入 commit 訊息。
4. 按 `Commit`。
5. 按 `Push origin`。

Only run CLI GitHub push/PR actions when the user explicitly asks for CLI or automation.

## Troubleshooting Pattern

When something fails:

1. Capture the exact symptom or error.
2. Decide whether it is likely environment-related, dependency-related, data-related, or code-related.
3. Use the lowest-cost check that can confirm the cause.
4. If a command fails because a tool is missing, report the missing tool and continue with available checks.
5. If sandbox/network permissions block a needed command, request escalation only for that command.
6. Summarize the workaround so future turns do not repeat the same failed path.

Known current baseline:

- Durable memory may only contain collaboration preferences and no complete rollout summaries.
- PowerShell may not have `git` on PATH. If `git` is unavailable, avoid relying on CLI git status; inspect files directly and give GitHub Desktop instructions when needed.

## Medical Exam Explanation Work

When the task is about writing, rewriting, importing, or auditing Traditional Chinese medical exam explanations, also use `medical-exam-explainer`.

Core safety rules:

- Only change explanation-related fields unless the user clearly asks for broader edits.
- Do not change question text, option text, answer keys, IDs, ordering, routes, or layout during explanation-only work.
- Validate JSON and explanation quality after edits.
- Flag suspected official-answer problems for manual review instead of silently changing answers.

## Finish Format

For completed work, keep the final response concise and include:

- What changed.
- What was verified and the result.
- What could not be verified, if anything.
- Any manual next steps, written step by step when needed.

