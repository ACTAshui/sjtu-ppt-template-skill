---
name: sjtu-ppt-template
description: Create Shanghai Jiao Tong University style editable PowerPoint decks from DOCX, notes, outlines, reports, papers, datasets, course materials, project summaries, or draft slides. Use when the user asks for 上海交通大学, 上海交大, 上交, SJTU, school-branded PPT, academic report slides, seminar decks, thesis defense slides, group meeting slides, course presentation decks, template selection, data visualization, scientific charts, Nature-like plotting, or converting Chinese research writing into a polished editable SJTU-style presentation.
---

# SJTU PPT Template

Create editable Shanghai Jiao Tong University style presentation decks for students, teachers, labs, courses, seminars, defenses, and academic reports.

This skill includes user-provided logo PNGs, PPTX templates, and an optional font package under `assets/` for direct use. It is not an official SJTU release; users must follow the asset notice and replace bundled assets with their own authorized files when needed.

## Quick Start

1. Create a task workspace:
   ```bash
   python scripts/create_workspace.py ./my-sjtu-deck --profile academic-report
   ```
2. Place user-provided assets in the workspace:
   - `source/`: DOCX, Markdown, PDF notes, outline, or existing PPT.
   - `assets/logos/`: bundled SJTU logo PNGs are copied here by default; add authorized department marks if needed.
   - `assets/templates/`: bundled PPTX templates are copied here by default; add authorized custom templates if needed.
   - `assets/fonts/`: bundled optional font package is copied here by default when present.
3. Read the source and identify the user's real intent:
   - academic report
   - thesis defense
   - course presentation
   - student activity
   - lab/project progress
   - policy/admin briefing
4. Select a style using [references/template-selection.md](references/template-selection.md).
5. Build native editable slides: text boxes, shapes, tables, charts, diagrams, and images.
6. If the task includes data, CSV, Excel, statistical tables, or chart polish, use [references/data-visualization.md](references/data-visualization.md).
7. For revisions, follow [references/revision-safety.md](references/revision-safety.md): never overwrite a source or user-edited PPTX; create a new timestamped version first.
8. Render previews, check layout, and iterate before delivery.

## What This Skill Should Demonstrate

- Understand the user's source material rather than mechanically copying paragraphs.
- Convert dense Chinese writing into a slide claim spine.
- Choose a suitable SJTU-style visual direction for the audience and occasion.
- Produce editable PPTX content, not a stack of full-slide screenshots.
- Reuse user-provided templates and logos responsibly.
- Preserve user-edited decks by creating a new dated revision file for every update.
- Learn from user-inserted images and keep image choices consistent across later revisions.
- Turn user-provided data into clean, reproducible, PPT-ready, Nature-like scientific charts when needed.
- Keep a consistent formal SJTU visual system across cover, section, content, chart, matrix, and closing pages.

## Template Choice

Read [references/template-selection.md](references/template-selection.md) before choosing a style.
Read [references/bundled-assets.md](references/bundled-assets.md) to see which logos, templates, and fonts are bundled.

Default recommendations:

- `simple-blue`: clean academic reports, weekly group meetings, course presentations.
- `sjtu-red`: formal school events, anniversary, party-building, institutional communication.
- `deep-blue-gold`: thesis defense, research results, major project report, formal review.
- `campus-poetic`: student activities, admissions, culture, campus storytelling.
- `minimal-white`: text-heavy academic material that needs clarity first.

When the user provides multiple PPT templates, inspect slide size, master layouts, theme colors, title zones, footer patterns, and logo placement. Choose the template that best matches the user's audience and message, not the prettiest template in isolation.

## Source-To-Slide Workflow

Read [references/authoring-workflow.md](references/authoring-workflow.md) for details.

1. Extract title, audience, purpose, and source sections.
2. Write a claim spine: one sentence per slide.
3. Map each claim to a proof object: chart, table, mechanism, timeline, matrix, quote, or visual comparison.
4. Rebuild content as presentation language:
   - shorten long paragraphs
   - turn lists into grouped arguments
   - turn tables into maps or matrices
   - turn mechanisms into flows
   - turn conclusions into closing takeaways
5. Apply the selected SJTU style system.
6. If revising an existing deck, copy the latest user-edited deck to a new versioned file before making changes.
7. Render and inspect every slide.

## Data Visualization And Scientific Charts

Read [references/data-visualization.md](references/data-visualization.md) when the user provides CSV, Excel, statistics, experimental tables, chart screenshots, or asks for charts, data processing, figure polishing, 科研绘图, 图表美化, or Nature-like visuals.

Core rules:

- Every chart must support a slide-level claim.
- Keep data and plotting code in the task workspace when charts are generated outside PPT.
- Use native PowerPoint charts for simple editable charts.
- Use Python/Matplotlib for polished scientific figures, multi-panel charts, error bars, distributions, heatmaps, or dense annotations.
- Export PPT-ready PNG plus PDF/SVG when useful, then insert without distorting aspect ratio.
- Use restrained SJTU/Nature-like styling: clean axes, readable labels, color-blind-safe accents, direct annotations, and minimal decoration.

## Revision Safety And Image Continuity

Read [references/revision-safety.md](references/revision-safety.md) whenever the user asks to update, revise, polish, continue, replace images, add pages, change text, or modify an existing PPT.

Core rules:

- Do not edit or overwrite the user's source files, previously delivered PPTX, or manually modified PPTX.
- Before changing a deck, create a new output file named with local date/time plus an incrementing revision number.
- Treat the newest user-provided or user-edited deck as the base for the next revision.
- Inspect user-added or replaced images before revising; preserve them unless the user asks otherwise.
- Maintain a local revision log and image preference notes in the task workspace so future revisions can follow the user's habits.

## Design Rules

Read [references/style-system.md](references/style-system.md).

Core defaults:

- 16:9 unless the user asks otherwise.
- Use an SJTU blue/red/gold system when no template theme is available.
- Use exact user-provided logo files; never ask image generation to redraw official marks.
- Prefer bundled logo/template assets when the user has not provided a different authorized file.
- Keep titles as conclusions, not generic topic labels.
- Prefer calm academic layouts for teachers, defenses, and research groups.
- Use more image-led rhythm only for campus culture or student-facing decks.
- Keep charts visually restrained and aligned with the selected template; use SJTU red for emphasis rather than filling every chart element.

## Quality Gates

Read [references/quality-gates.md](references/quality-gates.md).

Before final delivery:

- Confirm final PPTX exists and is non-empty.
- Confirm the final PPTX is a new revision file, not an overwritten source or prior delivery.
- Confirm expected slide count.
- Confirm important text is editable.
- Render all slides and inspect Chinese wrapping, logo sharpness, footer alignment, text overflow, and chart readability.
- For generated charts, confirm data/code/output files are saved and the rendered chart remains readable in slide previews.
- Fix the source deck and rerender if visual defects appear.

## Resources

- [references/authoring-workflow.md](references/authoring-workflow.md): source-to-slide process.
- [references/template-selection.md](references/template-selection.md): style selection rules.
- [references/style-system.md](references/style-system.md): SJTU-style layout, color, and typography defaults.
- [references/data-visualization.md](references/data-visualization.md): data processing, reproducible figures, and Nature-like PPT chart rules.
- [references/quality-gates.md](references/quality-gates.md): final verification checklist.
- [references/revision-safety.md](references/revision-safety.md): non-destructive revision naming, user-edit preservation, and image habit tracking.
- [references/bundled-assets.md](references/bundled-assets.md): bundled logo, PPT template, and font inventory.
- `scripts/create_workspace.py`: creates a clean local workspace for source files and user-provided assets.
- `scripts/plot_style.py`: reusable Matplotlib styling helper for SJTU/Nature-like PPT charts.
- `assets/`: bundled logos, templates, and fonts. See [ASSET_NOTICE.md](ASSET_NOTICE.md) before use or redistribution.
