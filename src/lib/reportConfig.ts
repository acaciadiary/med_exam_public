/**
 * Google 表單問題回報系統設定檔
 * 
 * 考生填寫完回報表單後，資料會直接 POST 到此 Google Form 中。
 * 
 * 如何設定您的 Google 表單：
 * 1. 建立一個 Google 表單，包含以下欄位：
 *    - 回報類型 (建議用下拉選單或選擇題)
 *    - 考卷資訊與題號 (簡答)
 *    - 詳細描述 (段落)
 *    - 聯絡信箱 (簡答)
 * 2. 取得您的表單 ID (在表單編輯網址中，例如 https://docs.google.com/forms/d/e/【您的表單ID】/viewform)
 *    將其填入下方 GOOGLE_FORM_ID 中。
 * 3. 取得預先填入的連結來獲得各欄位的 entry ID，並填入下方 FORM_ENTRY_IDS 中。
 * 
 * 詳細教學將會在實作結束後呈現在您的畫面上！
 */

export const GOOGLE_FORM_CONFIG = {
  // TODO: 當您建立好表單後，請把下面的 "YOUR_GOOGLE_FORM_ID" 替換成您的 Google 表單 ID
  GOOGLE_FORM_ID: "YOUR_GOOGLE_FORM_ID",

  // 對應 Google 表單各個問題欄位的 Entry ID
  // TODO: 當您取得 entry ID 後，請將下面的數值替換掉
  FORM_ENTRY_IDS: {
    type: "entry.1000001",         // 回報類型 (答案疑義、解析有誤等)
    examInfo: "entry.1000002",     // 考卷資訊與題號 (如：111年第1次醫學一 第15題)
    description: "entry.1000003",  // 詳細描述
    email: "entry.1000004",        // 聯絡信箱
  }
};

/**
 * 判斷目前是否處於測試/模擬模式
 * 如果表單 ID 尚未被替換 (仍為預設值)，則自動進入模擬模式，不會發送真實 API 請求。
 */
export const isReportDevMode = (): boolean => {
  return GOOGLE_FORM_CONFIG.GOOGLE_FORM_ID === "YOUR_GOOGLE_FORM_ID";
};
