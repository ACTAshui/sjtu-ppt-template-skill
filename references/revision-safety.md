# Revision Safety

Use this reference whenever revising, continuing, polishing, or updating an existing deck.

## Non-Destructive Rule

Never overwrite:

- original source documents
- user-provided PPTX files
- previously delivered PPTX files
- PPTX files that the user may have manually edited

Before any edit, choose the newest user-approved or user-edited PPTX as the base, copy it to a new output path, and modify only that copy.

## Versioned Filename Pattern

Use the computer's current local date and time. Scan existing output files to pick the next revision number.

Recommended pattern:

```text
<deck-stem>__YYYYMMDD-HHMMSS__rNN.pptx
```

Example:

```text
青年与生成式AI_SJTU演示样稿__20260518-143022__r03.pptx
```

Rules:

- Preserve the original deck stem when possible.
- Use `r01`, `r02`, `r03` as the revision sequence.
- If multiple revisions happen in the same minute or second, increment `rNN`; do not reuse a filename.
- Save previews with the same stem, for example `<version-stem>__preview-01.png`.
- Put revision outputs in `output/versions/` when using the standard workspace.

## Revision Workflow

1. Identify the base file:
   - If the user provides a modified PPTX, use that file as base.
   - Otherwise use the newest delivered revision in `output/versions/`.
   - If there is ambiguity, ask which file should be treated as current.
2. Read the base file before editing:
   - slide count
   - slide order
   - changed text
   - user-added images
   - deleted pages
   - changed colors, fonts, or layout habits
3. Create the new versioned PPTX path before making changes.
4. Copy the base deck to that path.
5. Apply the user's new request only to the copied version.
6. Render the copied version and inspect it.
7. Append a short entry to `planning/revision-log.md`.

## User-Edited Content

When the user has edited the deck, treat those edits as intentional unless there is clear evidence otherwise.

- Preserve rewritten titles and notes.
- Preserve manual layout changes unless they conflict with the new request.
- Preserve deleted slides; do not recreate them just because they existed in an older version.
- Preserve added slides and integrate the new request around them.
- If the user asks for a broad redesign, still start from the latest user-edited deck and save a new version.

## Image Habit Tracking

When the user inserts, replaces, crops, or repositions images, inspect those choices and record them in `planning/image-preferences.md`.

Track:

- image source type: screenshot, campus photo, diagram, chart, generated image, scanned figure
- placement: full-bleed, side panel, small icon, background, figure card, comparison pair
- crop habit: square, wide banner, circle, rounded rectangle, uncropped
- caption habit: no caption, short label, numbered figure, explanatory caption
- visual tone: formal, documentary, clean academic, promotional, campus culture
- repeated preference: logo position, photo opacity, border style, shadow, image-to-text ratio

Also maintain `planning/image-inventory.json` when practical. Track each important image's slide number, role, source path, caption or nearby label, crop style, approximate placement, and whether it was user-added.

When revising later:

- Read `planning/image-preferences.md` before replacing or adding images.
- Read `planning/image-inventory.json` before moving, deleting, or relinking existing images.
- Keep user-inserted images in place unless the user explicitly requests replacement.
- If a new slide needs an image, prefer the user's observed image style before generating or searching for a different style.
- If image paths have moved, relink to the user's latest supplied image rather than falling back to an older asset.

## Revision Log Entry

Append entries like:

```text
## 2026-05-18 14:30 r03

- Base file: output/versions/demo__20260518-132005__r02.pptx
- New file: output/versions/demo__20260518-143022__r03.pptx
- User request: replace section 2 images and tighten conclusion.
- Preserved: user-added campus photo on slide 4; manual title edits on slides 6-7.
- Image habit update: user prefers wide documentary photos with short labels.
```
