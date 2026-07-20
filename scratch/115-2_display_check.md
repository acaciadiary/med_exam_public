# 115-2 題目文字與前台顯示檢查

日期：2026-07-20

## 檢查範圍

- `public/data/exams/115-2/medicine-1.json`
- `public/data/exams/115-2/medicine-2.json`
- `public/data/exams/115-2/medicine-3.json`
- `public/data/exams/115-2/medicine-4.json`
- `public/data/exams/115-2/medicine-5.json`
- `public/data/exams/115-2/medicine-6.json`

## 結論

115-2 可以先上線作為「題目 + 目前官方解答」版本。

- 六份考卷 JSON 均可解析。
- 題號連續，總題數 520 題。
- 每題都有 A-D 選項。
- 每題都有目前官方答案。
- 沒有偵測到替代字元亂碼或明顯題目吞題。
- 前台 manifest 已收錄 115-2 六科，資料路徑存在。
- 前台測試、型別檢查與正式建置通過。

## 題數與答案驗證

來源：`node scripts/exams/run_python.mjs scripts/exams/validate_dataset.py "public/data/exams/115-2/*.json" --out reports/dataset-quality-115-2-display-check.json`

- `medicine-1.json`：100 題，issue 0
- `medicine-2.json`：100 題，issue 0
- `medicine-3.json`：80 題，issue 0
- `medicine-4.json`：80 題，issue 0
- `medicine-5.json`：80 題，issue 0
- `medicine-6.json`：80 題，issue 0

總計：520 題，total_issues 0。

## 文字掃描

已掃描：

- 缺題或題號不連續
- 缺 A-D 選項
- 空白選項
- 疑似替代字元亂碼
- 題幹過短
- 題幹過長
- 選項過長
- 選項疑似吞到下一題

結果：

- 缺題：0
- 缺 A-D 選項：0
- 題幹過短：0
- 題幹過長：0
- 選項過長：0
- 疑似替代字元亂碼：0

掃描曾標到少數小數點選項，例如 `1.6`、`2.0`、`0.737`、`1.5~10 公分`，人工判讀為正常數值選項，不是吞題。

## 已知限制

`medicine-5.json` 第 11 題為圖形選項題：

- 題目：高解析度食道壓力測試圖形判讀。
- A-D 選項在 JSON 中為：
  - `圖形選項 A，請參照官方試題 PDF`
  - `圖形選項 B，請參照官方試題 PDF`
  - `圖形選項 C，請參照官方試題 PDF`
  - `圖形選項 D，請參照官方試題 PDF`
- 已保留官方答案 A。
- 已保留 `manual_review_notes`，提醒需參照官方 PDF。

這不是資料壞掉，而是 PDF 圖形無法完整轉成純文字。

## 前台資料入口

`public/data/manifest.json` 已收錄 115-2 六科，順序如下：

- `115-2_medicine-6`
- `115-2_medicine-5`
- `115-2_medicine-4`
- `115-2_medicine-3`
- `115-2_medicine-2`
- `115-2_medicine-1`

六個 `path` 均存在於 `public/data/exams/115-2/`。

## 本機 PDF 檢查

`downloads/moex/115-2` 中每科都有：

- `questions.pdf`
- `answers.pdf`

六科 PDF 檔案大小均非 0，未見假 HTML 檔。

## 前台驗證

- `npm run test`：8 files passed，23 tests passed。
- `npm run typecheck`：通過。
- `npm run build`：通過。

## 未完成項目

- 本輪沒有開 localhost 瀏覽器截圖，因本專案既有規則是 localhost 可能被擋時，優先使用資料檢查、前台測試與建置驗證。
- Python parser 測試本輪未能執行，原因是目前可用的 bundled Python runtime 缺少 `pytest` 模組；這是環境問題，不是 115-2 資料驗證失敗。

## 上線建議

建議可以先上線。

上線文案或前台狀態應維持：

- `尚未申覆完成`
- 詳解暫無或待補
- 圖形題需參照官方 PDF

申覆完成後，再用安全答案更新流程，只更新答案相關欄位，再決定是否開始撰寫詳解。
