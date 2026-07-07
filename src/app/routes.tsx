export type AppPage =
  | "home"
  | "exam"
  | "progress"
  | "mistakes"
  | "favorites"
  | "notes"
  | "diseases";

const pageParam = "page";
const examParam = "exam";
const questionParam = "question";

export type ExamRouteTarget = {
  examId: string;
  questionId?: string;
};

export function readPageFromSearch(search: string): AppPage {
  const params = new URLSearchParams(search);
  const page = params.get(pageParam);

  if (
    page === "home" ||
    page === "exam" ||
    page === "progress" ||
    page === "mistakes" ||
    page === "favorites" ||
    page === "notes" ||
    page === "diseases"
  ) {
    return page;
  }

  if (params.get(examParam)) {
    return "exam";
  }

  return "home";
}

export function buildSearchForPage(page: AppPage, currentSearch: string) {
  const params = new URLSearchParams(currentSearch);

  if (page === "home") {
    params.delete(pageParam);
  } else {
    params.set(pageParam, page);
  }

  if (page !== "exam") {
    params.delete(examParam);
    params.delete(questionParam);
  }

  const nextSearch = params.toString();
  return nextSearch ? `?${nextSearch}` : "";
}

export function readExamRouteTarget(search: string): ExamRouteTarget | null {
  const params = new URLSearchParams(search);
  const examId = params.get(examParam)?.trim();
  if (!examId) return null;

  const questionId = params.get(questionParam)?.trim();
  return questionId ? { examId, questionId } : { examId };
}

export function buildSearchForExam(target: ExamRouteTarget, currentSearch: string) {
  const params = new URLSearchParams(currentSearch);

  params.set(pageParam, "exam");
  params.set(examParam, target.examId);

  if (target.questionId) {
    params.set(questionParam, target.questionId);
  } else {
    params.delete(questionParam);
  }

  return `?${params.toString()}`;
}
