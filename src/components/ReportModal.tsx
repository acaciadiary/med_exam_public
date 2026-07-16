import { useState } from "react";
import { AlertCircle, CheckCircle2, Loader2, Send, X } from "lucide-react";
import { motion, AnimatePresence } from "motion/react";
import { GOOGLE_FORM_CONFIG, isReportDevMode } from "../lib/reportConfig";
import type { ExamQuestion } from "../types/exam";

type ReportModalProps = {
  isOpen: boolean;
  onClose: () => void;
  question: ExamQuestion;
};

// 解析考卷與題號為好讀的中文格式
function getFormattedExamName(question: ExamQuestion) {
  const parts = question.id.split("_")[0].split("-");
  let examName = question.id.split("_")[0];

  if (parts.length >= 3) {
    const year = parts[0];
    const term = parts[1];
    const subjectCode = parts[2];

    const subjectLabels: Record<string, string> = {
      m1: "醫學一",
      m2: "醫學二",
      m3: "醫學三",
      m4: "醫學四",
      m5: "醫學五",
      m6: "醫學六",
    };
    const subject = subjectLabels[subjectCode] || subjectCode;
    examName = `${year}年第${term}次 ${subject}`;
  }

  return `${examName} 第 ${question.question_number} 題`;
}

export function ReportModal({ isOpen, onClose, question }: ReportModalProps) {
  const [type, setType] = useState("答案疑義");
  const [description, setDescription] = useState("");
  const [email, setEmail] = useState("");
  
  // 狀態管理：'idle' | 'submitting' | 'success' | 'error'
  const [status, setStatus] = useState<"idle" | "submitting" | "success" | "error">("idle");
  const [errorMessage, setErrorMessage] = useState("");

  if (!isOpen) return null;

  const examInfo = getFormattedExamName(question);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!description.trim()) return;

    setStatus("submitting");
    setErrorMessage("");

    // 模擬測試模式
    if (isReportDevMode()) {
      setTimeout(() => {
        console.log("【模擬送出問題回報】", {
          googleFormId: GOOGLE_FORM_CONFIG.GOOGLE_FORM_ID,
          payload: {
            [GOOGLE_FORM_CONFIG.FORM_ENTRY_IDS.type]: type,
            [GOOGLE_FORM_CONFIG.FORM_ENTRY_IDS.examInfo]: examInfo,
            [GOOGLE_FORM_CONFIG.FORM_ENTRY_IDS.description]: description,
            [GOOGLE_FORM_CONFIG.FORM_ENTRY_IDS.email]: email,
          }
        });
        setStatus("success");
      }, 1000);
      return;
    }

    // 正式發送模式
    try {
      const url = `https://docs.google.com/forms/d/e/${GOOGLE_FORM_CONFIG.GOOGLE_FORM_ID}/formResponse`;
      const formData = new URLSearchParams();
      formData.append(GOOGLE_FORM_CONFIG.FORM_ENTRY_IDS.type, type);
      formData.append(GOOGLE_FORM_CONFIG.FORM_ENTRY_IDS.examInfo, examInfo);
      formData.append(GOOGLE_FORM_CONFIG.FORM_ENTRY_IDS.description, description);
      formData.append(GOOGLE_FORM_CONFIG.FORM_ENTRY_IDS.email, email);

      // Google Form 需要 no-cors 模式，CORS 標頭不影響寫入
      await fetch(url, {
        method: "POST",
        mode: "no-cors",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: formData.toString(),
      });

      // 由於 no-cors 模式下無法讀取實際 response，只要 fetch 沒有丟出錯誤 (網路斷線等)，就視為成功
      setStatus("success");
    } catch (err) {
      console.error("Failed to submit feedback", err);
      setStatus("error");
      setErrorMessage("送出失敗，請檢查網路連線或稍後再試。");
    }
  };

  const handleReset = () => {
    setType("答案疑義");
    setDescription("");
    setEmail("");
    setStatus("idle");
    onClose();
  };

  return (
    <AnimatePresence>
      <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
        {/* 背景遮罩 */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          onClick={status === "submitting" ? undefined : handleReset}
          className="absolute inset-0 bg-[#3f342d]/40 backdrop-blur-sm"
        />

        {/* 視窗主體 */}
        <motion.div
          initial={{ opacity: 0, scale: 0.96, y: 18 }}
          animate={{ opacity: 1, scale: 1, y: 0 }}
          exit={{ opacity: 0, scale: 0.96, y: 18 }}
          transition={{ type: "spring", duration: 0.35 }}
          className="relative z-10 w-full max-w-lg overflow-hidden rounded-[1.8rem] border border-[#efd9d0] bg-[#fff8f4] p-6 shadow-[0_24px_70px_rgba(118,91,78,0.28)] dark:border-[#4d3d35] dark:bg-[#2b2430]"
        >
          {/* 信紙風背景 (如果專案中有此樣式則會生效) */}
          <div className="pointer-events-none absolute inset-0 z-0 journal-paper opacity-30" />

          <div className="relative z-10">
            {/* 關閉按鈕 */}
            {status !== "submitting" && (
              <button
                type="button"
                onClick={handleReset}
                className="absolute -right-1 -top-1 flex h-8 w-8 items-center justify-center rounded-full border border-[#efd9d0] bg-white/80 text-[#6f5b50] transition hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b] dark:border-white/10 dark:bg-[#3b3240] dark:text-[#dccbd3] dark:hover:bg-[#472431]"
                aria-label="關閉"
              >
                <X size={16} />
              </button>
            )}

            {status === "success" ? (
              /* 成功畫面 */
              <div className="flex flex-col items-center py-6 text-center">
                <motion.div
                  initial={{ scale: 0.5, opacity: 0 }}
                  animate={{ scale: 1, opacity: 1 }}
                  transition={{ type: "spring", stiffness: 200, damping: 15 }}
                  className="mb-4 text-[#4c806e] dark:text-[#b8efd9]"
                >
                  <CheckCircle2 size={54} />
                </motion.div>
                <h3 className="text-xl font-bold text-[#3f342d] dark:text-[#f8edf3]">感謝您的回報！</h3>
                <p className="mt-2 text-sm leading-6 text-[#8b7666] dark:text-[#cbb8c2]">
                  問題已成功送出。我們會盡快核對題目資訊，<br />
                  努力讓 Ariel's Med 的內容更加完善。
                </p>
                {isReportDevMode() && (
                  <div className="mt-4 w-full rounded-xl bg-amber-50 dark:bg-amber-950/20 p-3 text-left border border-amber-200/60 dark:border-amber-900/30">
                    <p className="text-xs font-semibold text-amber-800 dark:text-amber-300">⚠️ 測試模式提示</p>
                    <p className="mt-1 text-[11px] text-amber-700 dark:text-amber-400/90 leading-5">
                      目前由於未替換 Google 表單 ID，系統處於模擬測試狀態。您可以在瀏覽器的開發者工具 (F12) 控制台中查看送出的完整資料。
                    </p>
                  </div>
                )}
                <button
                  type="button"
                  onClick={handleReset}
                  className="mt-6 flex h-10 w-32 items-center justify-center rounded-xl bg-[#b8e2d4] text-sm font-bold text-[#355249] transition hover:bg-[#a5d9c7] active:scale-[0.98]"
                >
                  關閉視窗
                </button>
              </div>
            ) : (
              /* 表單填寫畫面 */
              <form onSubmit={handleSubmit} className="space-y-4">
                <div className="text-center">
                  <h3 className="text-xl font-bold text-[#3f342d] dark:text-[#f8edf3]">回報題目問題</h3>
                  <p className="mt-1 text-xs text-[#8b7666] dark:text-[#cbb8c2]">
                    如果您發現題目答案、解析有誤或排版問題，歡迎直接回報！
                  </p>
                </div>

                {/* 考卷與題號（唯讀） */}
                <div>
                  <label className="block text-xs font-bold text-[#6f5b50] dark:text-[#cbb8c2] mb-1.5">
                    考卷與題號
                  </label>
                  <input
                    type="text"
                    readOnly
                    value={examInfo}
                    className="w-full h-10 px-3.5 rounded-xl border border-[#efd9d0] bg-[#f8eae3]/40 text-sm text-[#6f5b50] font-semibold outline-none dark:border-white/10 dark:bg-white/5 dark:text-[#eadbe3]"
                  />
                </div>

                {/* 回報類型 */}
                <div>
                  <label className="block text-xs font-bold text-[#6f5b50] dark:text-[#cbb8c2] mb-1.5">
                    問題類型
                  </label>
                  <select
                    value={type}
                    onChange={(e) => setType(e.target.value)}
                    className="w-full h-10 px-3 rounded-xl border border-[#efd9d0] bg-white text-sm text-[#4b3b35] outline-none transition focus:border-[#f1aac8] focus:ring-2 focus:ring-[#ffd9e8]/55 dark:border-white/10 dark:bg-[#2b2430] dark:text-[#f8edf3] dark:focus:border-[#f3a6c4]"
                  >
                    <option value="答案疑義">答案疑義 (答案可能有誤或多個正解)</option>
                    <option value="解析有誤">解析有誤 (AI 產生的詳解有明顯錯誤)</option>
                    <option value="排版或圖片有誤">排版或圖片有誤 (文字缺漏、圖片無法顯示)</option>
                    <option value="其他">其他</option>
                  </select>
                </div>

                {/* 詳細描述 */}
                <div>
                  <label className="block text-xs font-bold text-[#6f5b50] dark:text-[#cbb8c2] mb-1.5">
                    錯誤詳細描述 <span className="text-rose-500">*</span>
                  </label>
                  <textarea
                    required
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                    rows={4}
                    placeholder="請描述您發現的錯誤，例如：選項 B 應改為...，因教科書中記載..."
                    className="w-full p-3 rounded-xl border border-[#efd9d0] bg-white text-sm text-[#4b3b35] outline-none transition placeholder:text-[#aa8a7d]/70 focus:border-[#f1aac8] focus:ring-2 focus:ring-[#ffd9e8]/55 dark:border-white/10 dark:bg-[#2b2430] dark:text-[#f8edf3] dark:placeholder:text-[#aa8a7d]/40 dark:focus:border-[#f3a6c4]"
                  />
                </div>

                {/* 聯絡信箱（選填） */}
                <div>
                  <label className="block text-xs font-bold text-[#6f5b50] dark:text-[#cbb8c2] mb-1.5">
                    您的聯絡信箱 (選填)
                  </label>
                  <input
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="如需後續說明或修正結果回覆，可填寫您的信箱"
                    className="w-full h-10 px-3.5 rounded-xl border border-[#efd9d0] bg-white text-sm text-[#4b3b35] outline-none transition placeholder:text-[#aa8a7d]/70 focus:border-[#f1aac8] focus:ring-2 focus:ring-[#ffd9e8]/55 dark:border-white/10 dark:bg-[#2b2430] dark:text-[#f8edf3] dark:placeholder:text-[#aa8a7d]/40 dark:focus:border-[#f3a6c4]"
                  />
                </div>

                {/* 錯誤提示 */}
                {status === "error" && (
                  <div className="flex items-center gap-2 rounded-xl bg-rose-50 dark:bg-rose-950/20 p-3 border border-rose-100 dark:border-rose-950/50">
                    <AlertCircle className="text-rose-500 shrink-0" size={16} />
                    <span className="text-xs font-medium text-rose-600 dark:text-rose-400">{errorMessage}</span>
                  </div>
                )}

                {/* 操作按鈕 */}
                <div className="flex gap-3 pt-2">
                  <button
                    type="button"
                    disabled={status === "submitting"}
                    onClick={handleReset}
                    className="flex-1 h-10 rounded-xl border border-[#efd9d0] bg-white text-sm font-semibold text-[#6f5b50] transition hover:bg-[#fff0f6] disabled:opacity-50 dark:border-white/10 dark:bg-[#3b3240] dark:text-[#dccbd3] dark:hover:bg-[#472431]"
                  >
                    取消
                  </button>
                  <button
                    type="submit"
                    disabled={status === "submitting" || !description.trim()}
                    className="flex-1 h-10 flex items-center justify-center gap-1.5 rounded-xl bg-[#b8e2d4] text-sm font-bold text-[#355249] shadow-[0_8px_20px_rgba(184,226,212,0.3)] transition hover:bg-[#a5d9c7] active:scale-[0.98] disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:bg-[#b8e2d4] disabled:active:scale-100"
                  >
                    {status === "submitting" ? (
                      <>
                        <Loader2 className="animate-spin" size={16} />
                        送出中...
                      </>
                    ) : (
                      <>
                        <Send size={14} />
                        送出回報
                      </>
                    )}
                  </button>
                </div>
              </form>
            )}
          </div>
        </motion.div>
      </div>
    </AnimatePresence>
  );
}
