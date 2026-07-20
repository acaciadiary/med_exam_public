# 115-2 前台可見性與位置整理紀錄

日期：2026-07-20

## 目標

- 讓 115-2 在前台更容易被看見。
- 以不改網頁架構為原則，不新增路由、不新增 manifest 欄位、不改資料載入模式。
- 把操作過程整理成可回寫 `moex-extract` skill 的經驗。

## 檢查路徑

1. 檢查 `src/lib/loadExamData.ts`
   - 前台資料入口是 `public/data/manifest.json`。
   - 考卷資料由 manifest 的 `path` 載入。
   - 結論：新增 115-2 後，不需要新增頁面或硬編資料路徑。

2. 檢查 `src/lib/examMetadata.ts`
   - 年份排序使用 numeric sort。
   - 科目與階段由 `medicine-1` 至 `medicine-6` 推導。
   - 結論：115-2、116、117 後續年份可沿用同一套排序與階段推導。

3. 檢查 `src/components/AppShell.tsx`
   - 頂部考卷選單已經有年度、階段、科目三段選擇。
   - 調整方式：在既有年度按鈕旁，對排序後第一個年度加上「最新」標記。
   - 架構影響：無新增狀態、無新增資料欄位、無新增元件樹層級。

4. 檢查 `src/features/progress/StudyOverviewPage.tsx`
   - 我的進度頁已依年份分區，並依階段 tab 顯示。
   - 調整方式：在排序後第一個年度的年份標題旁加上「最新考卷」標記。
   - 架構影響：只使用既有 `years` 排序結果。

5. 檢查 `tests/frontend/study-overview-stage-tabs.test.tsx`
   - 新增測試：用 `114-1` 與 `115-2` 測試資料確認最新年份標記會自動出現。
   - 測試沒有寫死未來年份，只確認排序後最新年份被標示。

## 實作結果

- `src/components/AppShell.tsx`
  - 年度選單中，最新年份顯示「最新」小標籤。

- `src/features/progress/StudyOverviewPage.tsx`
  - 我的進度年份區塊中，最新年份顯示「最新考卷」小標籤。

- `tests/frontend/study-overview-stage-tabs.test.tsx`
  - 新增最新年份標記測試。

## 驗證結果

- 前台單檔測試：
  - `npm run test -- --run tests/frontend/study-overview-stage-tabs.test.tsx`
  - 結果：4 passed。

- TypeScript 型別檢查：
  - `npm run typecheck`
  - 結果：通過。

- 完整前台測試：
  - `npm run test`
  - 結果：8 files passed，23 tests passed。

- 建置：
  - `npm run build`
  - 結果：通過。

- manifest 前台入口檢查：
  - 前 6 筆 exam id：
    - `115-2_medicine-6`
    - `115-2_medicine-5`
    - `115-2_medicine-4`
    - `115-2_medicine-3`
    - `115-2_medicine-2`
    - `115-2_medicine-1`

## Skill 優化重點

- 新年度匯入後，先確認前台是否已經由 manifest 自動可見，不要直接新增路由或硬編年份。
- 優先檢查：
  - `public/data/manifest.json`
  - `src/lib/loadExamData.ts`
  - `src/lib/examMetadata.ts`
  - `src/components/AppShell.tsx`
  - `src/features/progress/StudyOverviewPage.tsx`
- 若要提升可見性，優先在既有選單、年份區塊、進度區塊加小標籤或排序提示。
- 未來 116、117 要沿用排序結果，不要寫死 115-2。
- 本專案 localhost 可能被擋，優先用 manifest 資料檢查、前台測試、typecheck、build 驗證。

## Skill 已回寫

- 已更新 `C:\Users\User\.codex\skills\moex-extract\SKILL.md`。
- 新增段落：`Frontend visibility after importing a new exam`。
- 重點：新考卷匯入後，先檢查 manifest 與既有前台入口；若要提高可見性，優先使用既有選單與進度區塊的小標記，並用排序結果支援未來年份。
