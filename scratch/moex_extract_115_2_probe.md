# moex-extract 115-2 醫師國考探路紀錄

日期：2026-07-20
工作目標：照 `moex-extract` skill 嘗試找出 115-2 醫師國考官方檔案並下載，記錄流程與 skill 優化點。

## 結論

- 現有 skill 流程「優先用 preset 下載」的方向正確，但目前專案只有 `physician-115-first`，沒有 `physician-115-second`。
- `download_moex.py --year 115 --keyword 醫師` 可以執行並連到考選部，但沒有下載到任何檔案。
- 失敗原因不是官方檔案不存在，而是探索邏輯只篩選 `href` 含 `.pdf` 的連結；考選部實際檔案連結是 `wHandExamQandA_File.ashx?...&t=Q/S/M`。
- 115-2 醫師六科官方檔案可以正確下載，但需要兩個不同 `exam_code`：
  - 醫學（一）（二）：`code=115090`，`c=301`，`s=0101/0102`
  - 醫學（三）到（六）：`code=115070`，`c=302`，`s=0101/0102/0103/0104`
- 官方頁面這次未列出醫師科目的「更正答案」，所以目前應先設 `has_correction=False`，日後若官方補上再更新。

## 實際操作紀錄

1. 讀取使用者提供的 skill 路徑：
   - `C:\Users\User\.codex\skills\moex-extract\moex-extract\SKILL.md`
   - 結果：不存在。
   - 改讀實際安裝位置：
   - `C:\Users\User\.codex\skills\moex-extract\SKILL.md`

2. 依 skill 指示檢查專案：
   - `git status --short`：乾淨，沒有既有變更。
   - `package.json`：已有 `download:moex:115-1`、`build:moex:115-1`，preset 是 `physician-115-first`。
   - `scripts/exams/moex_sources.py`：只有 `PHYSICIAN_115_FIRST`，沒有 `PHYSICIAN_115_SECOND`。
   - `public/data/exams`：目前最新資料夾是 `115-1`。
   - `.gitignore`：`downloads/` 已忽略，適合放測試下載 PDF。

3. 驗證 Python 啟動方式：
   - 系統 `python`、`py` 都不可用。
   - 專案包裝器可用：`node scripts/exams/run_python.mjs ...`
   - `node scripts/exams/run_python.mjs -m py_compile scripts/exams/moex_sources.py` 通過。

4. 依 skill 的探索下載方式測試：
   - 指令：`node scripts/exams/run_python.mjs scripts/exams/download_moex.py --year 115 --keyword 醫師 --out-dir downloads/moex-skill-probe-discovery`
   - 第一次因沙盒禁止網路連線失敗。
   - 取得網路權限後重跑成功結束，但只建立空資料夾，未下載 PDF。
   - 判斷：探索邏輯未支援 `.ashx` 類型官方檔案連結。

5. 使用官方考選部頁面人工核對：
   - 第二階段頁：`https://wwwq.moex.gov.tw/exam/wFrmExamQandASearch.aspx?e=115070&y=2026`
   - 第一階段所在年度總頁：`https://wwwq.moex.gov.tw/exam/wFrmExamQandASearch.aspx?e=115180&y=2026`
   - 舊 115-1 頁：`https://wwwq.moex.gov.tw/exam/wFrmExamQandASearch.aspx?e=115020&y=2026`

6. 直接下載已核對的 115-2 醫師六科 PDF：
   - 下載位置：`downloads/moex-skill-probe-direct/115-2`
   - 共 12 個 PDF：6 份試題、6 份答案。
   - 下載檔案大小都合理，沒有 0 byte 或錯誤頁。

7. 抽讀 PDF 第一頁驗證：
   - 需要設定 `PYTHONPATH=D:\Antigravity\med_exam_public\.python-packages`，否則 `fitz` 找不到。
   - 醫學（一）：醫師(一)，第一階段，試題 19 頁，答案 1 頁。
   - 醫學（二）：醫師(一)，第一階段，試題 19 頁，答案 1 頁。
   - 醫學（三）：醫師(二)，第二階段，試題 17 頁，答案 1 頁。
   - 醫學（四）：醫師(二)，第二階段，試題 18 頁，答案 1 頁。
   - 醫學（五）：醫師(二)，第二階段，試題 20 頁，答案 1 頁。
   - 醫學（六）：醫師(二)，第二階段，試題 19 頁，答案 1 頁。

## 115-2 醫師建議 preset 來源

| subject | year | exam_code | category_code | subject_code | correction |
| --- | --- | --- | --- | --- | --- |
| medicine-1 | 115-2 | 115090 | 301 | 0101 | no |
| medicine-2 | 115-2 | 115090 | 301 | 0102 | no |
| medicine-3 | 115-2 | 115070 | 302 | 0101 | no |
| medicine-4 | 115-2 | 115070 | 302 | 0102 | no |
| medicine-5 | 115-2 | 115070 | 302 | 0103 | no |
| medicine-6 | 115-2 | 115070 | 302 | 0104 | no |

## 需要優化 skill 的地方

1. 路徑說明要避免假設 nested skill path
   - 使用者提供的 `...\moex-extract\moex-extract\SKILL.md` 不存在。
   - 實際是 `...\moex-extract\SKILL.md`。

2. Windows Python 指令要優先使用專案包裝器
   - 本機沒有 `python` / `py`。
   - 建議 skill 指令改成：
   - `node scripts/exams/run_python.mjs scripts/exams/download_moex.py ...`

3. PDF 解析驗證要補 `PYTHONPATH`
   - 本專案 PDF 套件在 `.python-packages`。
   - 建議抽讀或解析前提醒設定：
   - `$env:PYTHONPATH='D:\Antigravity\med_exam_public\.python-packages'`

4. 探索下載邏輯要支援 `.ashx`
   - 現有 `discover_pdf_links` 只找 `.pdf`。
   - 考選部實際檔案連結格式：
   - `wHandExamQandA_File.ashx?c=<category>&code=<exam_code>&q=1&s=<subject>&t=<Q|S|M>`

5. 115-2 醫師要允許一個 preset 混用兩個 exam_code
   - 醫學（一）（二）在 `115090`。
   - 醫學（三）到（六）在 `115070`。
   - 不能只用單一 `exam_code` 推整個年度。

6. correction 不要從舊年度慣性複製
   - 115-2 官方目前沒有列「更正答案」。
   - preset 應先不加 `has_correction=True`。

7. 官方頁搜尋頁可能需要分兩種策略
   - 精準 preset：最穩，適合正式建置。
   - 官方頁解析：應解析所有 `<a>` 的 `href`，不要只靠 `.pdf`，並保留頁面上下文來判斷考試名稱、類科與科目。

## 本次下載檔案

- `downloads/moex-skill-probe-direct/115-2/medicine-1/questions.pdf`
- `downloads/moex-skill-probe-direct/115-2/medicine-1/answers.pdf`
- `downloads/moex-skill-probe-direct/115-2/medicine-2/questions.pdf`
- `downloads/moex-skill-probe-direct/115-2/medicine-2/answers.pdf`
- `downloads/moex-skill-probe-direct/115-2/medicine-3/questions.pdf`
- `downloads/moex-skill-probe-direct/115-2/medicine-3/answers.pdf`
- `downloads/moex-skill-probe-direct/115-2/medicine-4/questions.pdf`
- `downloads/moex-skill-probe-direct/115-2/medicine-4/answers.pdf`
- `downloads/moex-skill-probe-direct/115-2/medicine-5/questions.pdf`
- `downloads/moex-skill-probe-direct/115-2/medicine-5/answers.pdf`
- `downloads/moex-skill-probe-direct/115-2/medicine-6/questions.pdf`
- `downloads/moex-skill-probe-direct/115-2/medicine-6/answers.pdf`
