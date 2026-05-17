# Quality Gates

Run these checks before delivery.

## Package Checks

- Final `.pptx` exists and is non-empty.
- Final `.pptx` is a newly named revision file when the task was an update.
- No source file, user-provided PPTX, or previous delivery was overwritten.
- Slide count matches the planned outline.
- No empty media files.
- Important slide text is editable.
- User-provided logos and templates are not embedded in any public skill package unless authorized.
- `planning/revision-log.md` is updated when revising an existing deck.
- `planning/image-preferences.md` is updated when user-inserted or user-replaced images are observed.
- `planning/image-inventory.json` is updated when important deck images are inserted, replaced, moved, or removed.
- Generated chart outputs have accompanying data/code/source notes when external plotting is used.

## Render Checks

Render every slide and inspect:

- Chinese text wrapping
- title and body hierarchy
- logo sharpness
- footer alignment
- page numbers
- chart labels
- table readability
- data figure readability at projected slide size
- overlapping objects
- placeholder text

## Presentation Checks

- The deck has a clear beginning, middle, and ending.
- Each slide has a role.
- The chosen template style matches the user's context.
- The deck looks like a coherent SJTU-style deck, not a generic template with a school name pasted on top.
- User edits and user-added images from the base deck are preserved unless explicitly changed by request.
- Each data chart has a clear claim and avoids decorative chart effects.
