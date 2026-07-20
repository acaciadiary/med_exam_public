# Media Field Contract

Use this contract when adding image assets to exam question JSON.

## Question Field

Add an optional `media` array to a question object:

```json
{
  "media": [
    {
      "type": "question",
      "src": "data/exams/113-1/images/medicine-6/q014-figure-1.png",
      "alt": "113-1 醫學六第 14 題題幹圖片",
      "source_page": 3,
      "source_bbox": [72.0, 180.0, 520.0, 420.0],
      "review_status": "reviewed"
    }
  ]
}
```

## Fields

- `type`: `question` or `option`.
- `label`: required only when `type` is `option`; use `A`, `B`, `C`, or `D`.
- `src`: public path relative to the Vite public root, without a leading slash.
- `alt`: Traditional Chinese description for accessibility and broken-image fallback.
- `source_page`: 1-based PDF page number.
- `source_bbox`: PDF coordinate bbox `[x0, y0, x1, y1]`.
- `review_status`: `needs_review`, `reviewed`, or `rejected`.

## Storage

Put confirmed public assets here:

```text
public/data/exams/<year>/images/<subject>/
```

Use stable filenames:

```text
q014-figure-1.png
q014-option-a.png
q014-option-b.png
```

Do not put raw PDFs, extraction reports, or uncertain crops in `public/data`.
