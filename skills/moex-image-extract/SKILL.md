---
name: moex-image-extract
description: Use when adding, auditing, or repairing image-based Taiwan MOEX exam questions in med_exam_public. Covers scanning existing MOEX question PDFs for embedded images, rendered figures, tables, pathology/radiology/ECG images, and A-D image options; mapping image candidates to the correct question JSON record; producing reviewable reports; and adding independent media fields without mixing images into question_text or option text.
---

# Moex Image Extract

## Overview

Use this skill to safely find image questions in official MOEX PDFs and connect extracted PNG assets to the correct question in `public/data/exams`. Keep the image workflow separate from normal text parsing: text fields remain stable, and images live in a dedicated media layer.

## Core Rules

- Answer in Traditional Chinese.
- Prefer official PDFs already downloaded under `downloads/moex/<year>/<subject>/questions.pdf`.
- Never edit official answer keys, question numbers, question text, or option text just because a picture is missing.
- Do not commit raw PDFs, OCR dumps, `downloads/`, `reports/`, or scratch extraction logs.
- Store web-visible extracted assets under `public/data/exams/<year>/images/<subject>/`.
- Store uncertainty in `manual_review_notes` or extraction reports. Do not silently guess when a figure cannot be confidently mapped to one question.
- Use a separate `media` field. Do not insert Markdown images, HTML, or path strings into `question_text`.

## Target Data Shape

Add media only after the frontend/types are ready, or place the proposed additions in a review report first.

Preferred question-level shape:

```json
"media": [
  {
    "type": "question",
    "src": "data/exams/113-1/images/medicine-6/q014-figure-1.png",
    "alt": "113-1 醫學六第 14 題題幹圖片",
    "source_page": 3,
    "source_bbox": [72.0, 180.0, 520.0, 420.0],
    "review_status": "needs_review"
  },
  {
    "type": "option",
    "label": "A",
    "src": "data/exams/113-1/images/medicine-6/q014-option-a.png",
    "alt": "113-1 醫學六第 14 題選項 A 圖片",
    "source_page": 3,
    "source_bbox": [82.0, 445.0, 210.0, 560.0],
    "review_status": "needs_review"
  }
]
```

Use `type: "question"` for a figure that belongs to the stem. Use `type: "option"` plus `label` for A-D image choices.

## Workflow

### 1. Confirm Inputs

Identify the exact pair:

```text
PDF:  downloads/moex/<year>/<subject>/questions.pdf
JSON: public/data/exams/<year>/<subject>.json
```

Before extraction, read the JSON question numbers and inspect whether there are existing placeholders such as `圖示 A（圖片選項，請對照官方題本）`, `image_options_missing_asset`, or `missing image`.

### 2. Build A Page-To-Question Map

Use PyMuPDF (`fitz`) first. Extract each page as structured blocks:

```python
page.get_text("dict", sort=True)["blocks"]
```

Collect text blocks containing question-number starts such as `14.` or `14、`. Record:

```text
question_number, page_index, text_bbox_top, text_bbox_bottom
```

The mapping rule is:

- An image after a question start and before the next question start belongs to that question.
- If a figure appears above the first detected question on a page, compare with the previous page's last question and mark `needs_review`.
- If multiple image blocks appear in the same question region and align with A-D labels, classify them as option candidates.
- If the next question boundary is unclear, do not merge. Put the candidate in the report.

### 3. Detect Image Candidates

Run two detection passes:

1. Embedded image pass:
   - Use `page.get_text("dict")` blocks with `type == 1`.
   - Keep each block's bbox, width, height, extension, and byte size.
   - Ignore tiny icons or bullets using minimum thresholds such as width/height >= 40 px and area >= 1600 px.

2. Rendered crop pass:
   - Some MOEX diagrams are vector drawings or mixed text/image content, not extractable as standalone images.
   - Render the PDF page at 2x or 3x zoom.
   - Crop the region between a question start and the next question start when the region contains dense non-text drawings, image blocks, or placeholder text in the existing JSON.
   - Prefer a slightly generous crop over a tight crop, but avoid including the next question.

### 4. Name And Save Assets

Save candidates with stable names:

```text
public/data/exams/<year>/images/<subject>/q014-figure-1.png
public/data/exams/<year>/images/<subject>/q014-option-a.png
public/data/exams/<year>/images/<subject>/q014-option-b.png
```

Use lowercase subject ids and three-digit question numbers. If a candidate is uncertain, still save it under `scratch/` or report it without adding it to `public/data` until reviewed.

### 5. Produce A Review Report First

Before editing the dataset JSON, create a report under `reports/` or `scratch/` with:

```json
{
  "year": "113-1",
  "subject": "medicine-6",
  "pdf": "downloads/moex/113-1/medicine-6/questions.pdf",
  "candidates": [
    {
      "question_number": 14,
      "classification": "option",
      "confidence": "medium",
      "page": 3,
      "bbox": [82.0, 445.0, 210.0, 560.0],
      "suggested_src": "data/exams/113-1/images/medicine-6/q014-option-a.png",
      "reason": "candidate appears after Q14 start and before Q15 start; existing JSON has image option placeholders"
    }
  ]
}
```

Use confidence levels:

- `high`: clear question boundary, clear A-D labels or single figure, no overlap with next question.
- `medium`: likely mapping, but labels or crop boundary need visual confirmation.
- `low`: page layout is ambiguous; do not merge without manual review.

### 6. Merge Only Confirmed Media

Merge into JSON only when candidates are `high` confidence or explicitly reviewed. Preserve all existing fields. If a question already has image placeholders, keep the placeholder option text unless the user asks for broader data cleanup.

If the question is image-dependent and still lacks a confirmed image, add or preserve `manual_review_notes` rather than changing the answer.

### 7. Validate

After any JSON/schema/frontend changes, run the smallest relevant checks:

```powershell
node scripts/exams/run_python.mjs scripts/exams/validate_dataset.py "public/data/exams/**/*.json" --out reports/dataset-quality.json
npm run typecheck
npm run test
npm run build
```

For asset checks, verify:

- Every `media[].src` exists under `public/`.
- Image filenames are unique and stable.
- No `downloads/` or `reports/` files are staged as deliverable data.
- A sample built page can load the JSON and media paths. If localhost browser access is blocked, use build output and HTTP/data-loading checks.

## Practical Heuristics

- For A-D image options, compare candidate image centers with nearby A/B/C/D text labels. If labels are missing, use visual report thumbnails and require review.
- For radiology/pathology/ECG images, classify as `type: "question"` unless the official PDF clearly labels separate answer choices.
- For tables that are rendered as text, do not convert them into images unless the table structure is lost in text extraction.
- For vector-only diagrams, crop from the rendered page instead of relying on embedded image extraction.
- For page-spanning questions, allow media from the next page only if the next page has no new question start before the figure.

## References

Read `references/media-field-contract.md` when adding or reviewing dataset schema fields for image assets.
