import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it, vi } from "vitest";
import { DiseaseComparePage } from "../../src/features/exam/DiseaseComparePage";

vi.mock("../../src/lib/loadExamData", () => ({
  loadDiseaseComparisons: vi.fn().mockResolvedValue({
    comparison_groups: [
      {
        id: "serotonin_vs_nms",
        title: "血清素症候群 vs NMS",
        category: "精神科 / 藥物副作用",
        exam_importance: "高頻",
        exam_focus_tips: "clonus 先想血清素症候群；鉛管僵硬先想 NMS。",
        common_traps: "兩者都可能發燒與意識改變。",
        highlight_keywords: ["clonus", "鉛管僵硬"],
        stage: "二階",
        diseases: [
          {
            name: "血清素症候群",
            aliases: ["Serotonin syndrome"],
            features: { 神經肌肉: "Hyperreflexia 與 clonus" },
          },
          {
            name: "抗精神病藥惡性症候群",
            aliases: ["NMS"],
            features: { 神經肌肉: "Lead-pipe rigidity" },
          },
        ],
        related_questions: [],
        must_know_numbers: [],
      },
    ],
  }),
  loadInstantKillFacts: vi.fn().mockResolvedValue({
    facts: [
      {
        id: "115-1_medicine-1_001",
        year: "115",
        subject: "醫學一",
        category: "內科",
        reason: "常考數值",
        highlight_value: "10",
        unit: "mEq/L",
        question_text: "血鈉矯正速度",
        explanation: "避免矯正過快。",
        flashcard_front: "高鈉血症",
        flashcard_back: "慢慢矯正",
        options: { A: "A", B: "B", C: "C", D: "D" },
      },
    ],
  }),
  loadMedicalGlossary: vi.fn().mockResolvedValue({
    terms: [
      {
        id: "pulsus_paradoxus",
        name: "奇脈",
        aliases: ["Pulsus paradoxus"],
        category: "心臟科",
        explanation: "吸氣時收縮壓下降。",
        exam_focus: "心包填塞線索。",
        related_questions: [],
        stage: "二階",
        frequency: 10,
      },
    ],
  }),
  loadEponyms: vi.fn().mockResolvedValue({
    eponyms: [
      {
        id: "kawasaki",
        name: "Kawasaki disease",
        aliases: ["川崎症"],
        category: "小兒科",
        origin_type: "人名",
        description: "黏膜皮膚淋巴結症候群。",
        clinical_signs: "發燒、草莓舌。",
        exam_focus: "冠狀動脈瘤。",
        related_questions: [],
        stage: "二階",
        frequency: 8,
      },
    ],
  }),
  loadClinicalGuidelines: vi.fn().mockResolvedValue({
    guidelines: [
      {
        id: "anaphylaxis",
        title: "過敏性休克",
        aliases: ["Anaphylaxis"],
        category: "急診",
        scenario: "低血壓、喘鳴、蕁麻疹。",
        first_line_action: "**Epinephrine IM**",
        dosage_info: "大腿外側肌肉注射。",
        common_traps: "不要先給抗組織胺。",
        related_questions: [],
        stage: "二階",
        frequency: 12,
      },
    ],
  }),
}));

describe("DiseaseComparePage tabs", () => {
  it("opens every must-know tab without blank content", async () => {
    const user = userEvent.setup();

    render(
      <DiseaseComparePage
        stickyNotes={[]}
        onAddNote={vi.fn()}
        onRemoveNote={vi.fn()}
        theme="light"
      />,
    );

    expect(await screen.findByText("疾病鑑別與對照專區")).toBeInTheDocument();

    await user.click(screen.getByRole("button", { name: "國考數字秒殺" }));
    expect(await screen.findByText("高鈉血症")).toBeInTheDocument();

    await user.click(screen.getByRole("button", { name: "臨床名詞百科" }));
    expect((await screen.findAllByText("奇脈")).length).toBeGreaterThan(0);

    await user.click(screen.getByRole("button", { name: "人名地名考點" }));
    expect((await screen.findAllByText("Kawasaki disease")).length).toBeGreaterThan(0);

    await user.click(screen.getByRole("button", { name: "二階首選指引" }));
    expect((await screen.findAllByText("過敏性休克")).length).toBeGreaterThan(0);

    await user.click(screen.getByRole("button", { name: "關鍵字秒殺" }));
    await waitFor(() => {
      expect(screen.getByText(/目前牌組/)).toBeInTheDocument();
    });
  });
});
