# Visual QA

Use this checklist after every substantial deck generation or revision. The goal is to catch layout defects by looking at rendered slides, not only by inspecting the PPTX object tree.

## Required Outputs

For every delivery, create or update:

- `output/previews/`: one rendered image per slide.
- `output/previews/contact-sheet.png` or `.jpg`: all slides in one overview image.
- `planning/visual-qa.md`: a short record of defects found, fixes made, and remaining risks.

## Visual Review Loop

1. Render the current PPTX to slide images.
2. Review the contact sheet first to catch global rhythm, color, and spacing problems.
3. Open full-size previews for slides with dense text, images, charts, tables, or diagrams.
4. Fix the source PPTX, script, or JSX source.
5. Rerender and repeat until the deck passes the checks below.

Do not mark the deck complete after finding a visible defect unless the defect has been fixed or explicitly accepted by the user.

## Layout Checks

Check every rendered slide for:

- Text boxes overlapping photos, logos, charts, or other text.
- Images covering titles, labels, footers, page numbers, or captions.
- Text cropped by shape boundaries or slide edges.
- Long Chinese lines breaking awkwardly or becoming too small.
- Title, subtitle, and body hierarchy collapsing into the same visual weight.
- Footer/logo/page-number alignment drifting across slides.
- Decorative elements competing with the main claim.

## Color And Contrast Checks

Check whether key text remains readable over fills, images, and template backgrounds.

Minimum practical rules:

- Use dark text on light backgrounds or white text on intentionally darkened image areas.
- If text sits over a photo, add a solid or semi-transparent overlay behind the text.
- Avoid SJTU red on dark blue or dark red backgrounds unless the text is large and contrast-tested.
- Use gold as accent, not as dense body text.
- Keep chart/category colors distinct enough in grayscale and projection conditions.

When in doubt, simplify the palette. Academic decks should be readable before they are decorative.

## Automated Geometry Checks

When the authoring tool exposes PPT shapes:

- Extract bounding boxes for text, images, charts, and logos.
- Flag text-image overlaps above a small threshold.
- Flag text boxes outside slide bounds.
- Flag very small text in dense diagrams or charts.
- Flag locked/manual user content before changing it.

Automated checks are advisory. A rendered visual pass is still required because background images, grouped shapes, and transparency can fool geometry-only checks.

## QA Record Template

```markdown
# Visual QA

- Deck:
- Rendered at:
- Slide count:
- Preview folder:
- Contact sheet:

## Issues Found

| Slide | Issue | Fix |
| --- | --- | --- |
|  |  |  |

## Final Pass

- Text/image overlap:
- Text overflow:
- Contrast/readability:
- Diagram clarity:
- Chart/table readability:
- User-locked content preserved:
```
