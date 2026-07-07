import { describe, expect, it } from "vitest";
import {
  buildSearchForExam,
  buildSearchForPage,
  readExamRouteTarget,
  readPageFromSearch,
} from "../../src/app/routes";

describe("app route search params", () => {
  it("reads shared exam and question links as the exam page", () => {
    const search = "?page=exam&exam=115-1_medicine-6&question=q17";

    expect(readPageFromSearch(search)).toBe("exam");
    expect(readExamRouteTarget(search)).toEqual({
      examId: "115-1_medicine-6",
      questionId: "q17",
    });
  });

  it("keeps stable exam and question params when building a question link", () => {
    expect(
      buildSearchForExam(
        { examId: "115-1_medicine-6", questionId: "q17" },
        "?page=home",
      ),
    ).toBe("?page=exam&exam=115-1_medicine-6&question=q17");
  });

  it("removes stale exam params when navigating away from the exam page", () => {
    expect(
      buildSearchForPage(
        "mistakes",
        "?page=exam&exam=115-1_medicine-6&question=q17",
      ),
    ).toBe("?page=mistakes");
  });
});
