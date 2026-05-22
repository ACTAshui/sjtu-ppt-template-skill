# Quality Gates

Run these checks before delivery.

## Package Checks

- Final `.pptx` exists and is non-empty.
- Final `.pptx` is a newly named revision file when the task was an update.
- No source file, user-provided PPTX, or previous delivery was overwritten.
- Slide count matches the planned outline.
- If revising an existing deck, confirm whether the task is conservative revision or explicit redesign.
- If in conservative revision mode, confirm user-approved content and working layouts were not rewritten or replaced.
- No empty media files.
- Important slide text is editable.
- User-provided logos and templates are not embedded in any public skill package unless authorized.
- `planning/revision-log.md` is updated when revising an existing deck.
- `planning/image-preferences.md` is updated when user-inserted or user-replaced images are observed.
- `planning/image-inventory.json` is updated when important deck images are inserted, replaced, moved, or removed.
- Generated chart outputs have accompanying data/code/source notes when external plotting is used.
- `planning/diagram-plan.md` is updated when generated flowcharts or structure diagrams are used.
- `planning/visual-qa.md` is updated after rendered preview review.
- `planning/web-sources.md` and `assets/web/sources.json` are updated when web text or images are collected.
- `planning/speaker-note-locks.json` is checked before updating notes or visible content on revised decks.
- If the user reports open failures, the final handoff file is validated with a local presentation engine using [office-compatibility.md](office-compatibility.md).

## Render Checks

Render every slide and inspect:

- Chinese text wrapping
- title and body hierarchy
- logo sharpness
- footer alignment
- page numbers
- duplicated page numbers or duplicated footer elements
- chart labels
- table readability
- data figure readability at projected slide size
- text and images not blocking each other
- color contrast and readability over image backgrounds
- diagram node labels, connector routing, and editability expectations
- speaker notes presence for expected presentation slides
- overlapping objects
- placeholder text
- local Office openability when requested or when a previous output failed to open

## Presentation Checks

- The deck has a clear beginning, middle, and ending.
- Each slide has a role.
- The chosen template style matches the user's context.
- The deck looks like a coherent SJTU-style deck, not a generic template with a school name pasted on top.
- User edits and user-added images from the base deck are preserved unless explicitly changed by request.
- Existing strong pages are preserved in conservative revision mode; optimization must not silently replace good content.
- Each data chart has a clear claim and avoids decorative chart effects.
- User-corrected speaker notes and visible content on locked slides are preserved.
- Flowcharts and structure diagrams are clear enough to explain verbally without tracing a confusing path.
- Web-collected facts and image candidates have source/provenance notes and are suitable for the intended use.
