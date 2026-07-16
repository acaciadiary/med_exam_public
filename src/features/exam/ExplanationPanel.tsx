import { AlertTriangle, BadgeCheck, Lightbulb, Mail, Sparkles } from "lucide-react";
import { useEffect, useMemo, useState } from "react";
import { randomEncouragement } from "../../lib/encouragements";
import { loadDiseaseComparisons } from "../../lib/loadExamData";
import { DiseaseComparison } from "./DiseaseComparison";
import { ReportModal } from "../../components/ReportModal";
import type { ExamQuestion } from "../../types/exam";
import type { DiseaseComparisonGroup } from "../../types/disease";
import type { AppTheme } from "../../components/ThemeToggle";

const ACRONYM_CONTEXTS: Record<string, string[]> = {
  mg: ["肌無力", "重症", "achr", "眼瞼", "複視", "胸腺", "thymoma", "tensilon", "edrophonium", "mestinon", "去髓鞘", "gbs", "myasthenia", "gravis"],
  gbs: ["去髓鞘", "脫髓鞘", "無力", "腱反射", "guillain", "barre", "巴雷", "神經", "重症肌無力", "achr", "csf", "蛋白細胞", "升天性", "肢體", "paralysis"],
  uc: ["結腸", "大腸", "發炎", "腸道", "血便", "crohn", "克隆", "黏膜", "ibd", "colitis", "ulcerative"],
  ra: ["關節", "風濕", "晨僵", "rheumatoid", "滑膜", "rf", "ccp", "天鵝頸", "boutonniere", "arthritis"],
  oa: ["關節", "退化", "骨刺", "軟骨", "heberden", "bouchard", "osteoarthritis"],
  edh: ["血腫", "硬腦膜", "顱骨", "腦", "橋靜脈", "腦膜動脈", "新月", "凸透鏡", "清明期", "lucid", "hematoma", "epidural"],
  sdh: ["血腫", "硬腦膜", "顱骨", "腦", "橋靜脈", "腦膜動脈", "新月", "凸透鏡", "清明期", "lucid", "hematoma", "subdural"],
  cppd: ["焦磷酸", "假性痛風", "pseudogout", "關節", "軟骨", "calcium", "pyrophosphate"]
};

function isAliasMatch(combinedTextOriginal: string, alias: string): boolean {
  // Check if alias is a short acronym (English letters and numbers, length <= 4)
  const isAcronym = /^[A-Za-z0-9]{1,4}$/.test(alias);

  if (isAcronym) {
    // 1. Case-sensitive whole-word match
    const regex = new RegExp(`\\b${alias}\\b`);
    if (!regex.test(combinedTextOriginal)) {
      return false;
    }

    // 2. Context verification for acronyms
    const normAlias = alias.toLowerCase();
    const contextWords = ACRONYM_CONTEXTS[normAlias];
    if (contextWords) {
      const lowerText = combinedTextOriginal.toLowerCase();
      return contextWords.some((word) => lowerText.includes(word));
    }

    return true;
  }

  // Specific check to avoid matching molecular "cloning" (克隆) as Crohn's disease
  if (alias === "克隆") {
    const regex = /克隆(氏|氏症|氏病)/;
    return regex.test(combinedTextOriginal);
  }

  // Otherwise, case-insensitive substring match
  const normText = combinedTextOriginal.toLowerCase();
  const normAlias = alias.toLowerCase();
  return normText.includes(normAlias);
}

type ExplanationPanelProps = {
  question: ExamQuestion;
  theme: AppTheme;
};

function formatExplanationText(value: string) {
  return value
    .replace(/\s+(?=【(?:題幹解析|選項詳解|核心考點)】)/g, "\n\n")
    .replace(/\s+-\s+([A-D])\.\s*/g, "\n- $1. ")
    .replace(/\n{3,}/g, "\n\n")
    .trim();
}

const LOW_QUALITY_PATTERNS = [
  "非本題答案",
  "不是本題標準答案",
  "回到題幹線索",
  "請用題幹線索連回",
  "不能最精準回答本題",
  "最符合題幹",
  "核心記憶點",
  "定義、機轉、典型表現或處置原則",
  /題目中選項\s*[A-D]\s*所代表的鑑別或處置/,
];

function hasLowQualityTemplate(explanation: string) {
  return LOW_QUALITY_PATTERNS.some((pattern) =>
    typeof pattern === "string" ? explanation.includes(pattern) : pattern.test(explanation),
  );
}

function hasIncompleteOptionDetails(explanation: string) {
  if (!explanation.trim()) return true;

  return (["A", "B", "C", "D"] as const).some((option) => {
    const optionPattern = new RegExp(`(?:^|\\n)\\s*(?:[-•]\\s*)?${option}[.．、]`, "i");
    return !optionPattern.test(explanation);
  });
}

function inferExamId(question: ExamQuestion) {
  return question.id.match(/^(.+)_\d{3}$/)?.[1] || "未知考卷";
}

export function ExplanationPanel({ question, theme }: ExplanationPanelProps) {
  const [comparisons, setComparisons] = useState<DiseaseComparisonGroup[]>([]);
  const [isReportOpen, setIsReportOpen] = useState(false);

  useEffect(() => {
    loadDiseaseComparisons()
      .then((data) => {
        setComparisons(data.comparison_groups);
      })
      .catch((err) => {
        console.error("Failed to load disease comparisons", err);
      });
  }, []);

  const matchedGroups = useMemo(() => {
    if (!comparisons.length) return [];

    const matched: DiseaseComparisonGroup[] = [];
    const combinedTextOriginal = `${question.question_text} ${Object.values(question.options).join(" ")} ${
      question.explanation || ""
    }`;

    for (const group of comparisons) {
      // 1. Direct match by question ID
      const isDirectMatch = group.related_questions?.some(
        (rq) => rq.question_id === question.id
      );

      if (isDirectMatch) {
        matched.push(group);
        continue;
      }

      // 2. Keyword-based matching
      const hasMatch = group.diseases.some((disease) =>
        disease.aliases.some((alias) => {
          return isAliasMatch(combinedTextOriginal, alias);
        })
      );

      if (hasMatch) {
        matched.push(group);
      }
    }

    return matched;
  }, [comparisons, question]);


  const explanation =
    formatExplanationText(question.explanation || "") ||
    "這題尚未匯入詳解。之後可透過 Gemini 手動批次流程產生，並保留人工複查狀態。";
  const keyPoint = question.key_point || "考點提示尚未建立。";
  const summary =
    question.flashcard_summary ||
    "閃卡摘要尚未建立：之後會整理成「關鍵字 -> 選什麼」的一句話。";
  const status = question.review_status || (question.explanation ? "ai_generated" : "empty");
  const encouragement = useMemo(() => randomEncouragement(), [question.id]);
  const needsOptimization =
    hasLowQualityTemplate(explanation) || hasIncompleteOptionDetails(explanation);
  const statusMeta =
    status === "reviewed"
      ? {
          icon: <BadgeCheck size={14} />,
          text: "已審核",
          title: "內容已人工審核",
          className:
            "border-[#d8eadf] bg-white/70 text-[#4c806e] dark:border-[#3f6d5e] dark:bg-[#223d35] dark:text-[#b8efd9]",
        }
      : status === "ai_generated"
        ? {
            icon: <Sparkles size={14} />,
            text: "AI 初稿，建議複核",
            title: encouragement,
            className:
              "border-[#d8eadf] bg-white/70 text-[#4c806e] dark:border-[#3f6d5e] dark:bg-[#223d35] dark:text-[#b8efd9]",
          }
        : {
            icon: <AlertTriangle size={14} />,
            text: "待補詳解",
            title: "這題尚未匯入詳解",
            className:
              "border-[#f2d7a9] bg-[#fff8df] text-[#87693d] dark:border-[#725d32] dark:bg-[#40341f] dark:text-[#f1d58b]",
          };
  return (
    <>
      <div className="mt-6 box-border w-full min-w-0 max-w-full overflow-hidden rounded-[1.1rem] border border-[#d8eadf] bg-[#effaf5]/82 p-4 shadow-sm dark:border-[#3f6d5e] dark:bg-[#182f2a]/90 sm:p-5">
        <div className="flex min-w-0 flex-wrap items-center justify-between gap-3">
          <div className="flex items-center gap-2 text-sm font-semibold text-[#4c806e] dark:text-[#b8efd9]">
            <Lightbulb size={17} />
            詳解與考點提示
          </div>
          <div className="flex flex-wrap items-center gap-2">
            <span
              className={`inline-flex items-center gap-1.5 rounded-full border px-3 py-1 text-xs font-semibold ${statusMeta.className}`}
              title={statusMeta.title}
            >
              {statusMeta.icon}
              {statusMeta.text}
            </span>
            {needsOptimization && (
              <span
                className="inline-flex items-center gap-1.5 rounded-full border border-[#f2d7a9] bg-[#fff8df] px-3 py-1 text-xs font-semibold text-[#87693d] dark:border-[#725d32] dark:bg-[#40341f] dark:text-[#f1d58b]"
                title="此題詳解可能含模板句或選項詳解不完整"
              >
                <AlertTriangle size={14} />
                待優化
              </span>
            )}
            <button
              type="button"
              onClick={() => setIsReportOpen(true)}
              className="inline-flex items-center gap-1.5 rounded-full border border-[#efd9d0] bg-white/70 px-3 py-1 text-xs font-semibold text-[#6f5b50] transition hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b] dark:border-white/10 dark:bg-[#2b2430]/72 dark:text-[#dccbd3] dark:hover:bg-[#472431]"
              aria-label={`回報第 ${question.question_number} 題`}
              title="回報答案疑義、詳解錯誤或排版問題"
            >
              <Mail size={14} />
              回報此題
            </button>
          </div>
        </div>
        <div className="mobile-safe-text mt-4 rounded-[0.9rem] border border-[#d8eadf] bg-white/64 px-4 py-3 text-sm font-semibold leading-6 text-[#4c806e] dark:border-[#3f6d5e] dark:bg-[#11241f] dark:text-[#b8efd9]">
          {keyPoint}
        </div>
        <p className="mobile-safe-text explanation-text mt-3 text-sm leading-7 text-[#604b43] dark:text-[#eadbe3]">{explanation}</p>
        <div className="mobile-safe-text mt-4 rounded-[0.9rem] border border-[#f2d7a9] bg-[#fff8df] px-4 py-3 text-sm font-semibold text-[#7a6040] dark:border-[#725d32] dark:bg-[#40341f] dark:text-[#f1d58b]">
          {summary}
        </div>
      </div>

      {/* Disease Comparisons */}
      {matchedGroups.map((group) => (
        <DiseaseComparison
          key={group.id}
          group={group}
          currentQuestionId={question.id}
          theme={theme}
        />
      ))}

      <ReportModal
        isOpen={isReportOpen}
        onClose={() => setIsReportOpen(false)}
        question={question}
      />
    </>
  );
}
