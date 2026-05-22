---
name: sjtu-ppt-template
description: Create Shanghai Jiao Tong University style editable PowerPoint decks from DOCX, notes, outlines, reports, papers, datasets, course materials, project summaries, web sources, or draft slides. Use when the user asks for 上海交通大学, 上海交大, 上交, SJTU, school-branded PPT, academic report slides, seminar decks, thesis defense slides, group meeting slides, course presentation decks, template selection, speaker notes, 演讲稿, 备注, data visualization, scientific charts, Nature-like plotting, editable flowcharts, structure diagrams, visual QA, web text/image acquisition, or converting Chinese research writing into a polished editable SJTU-style presentation.
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
   - `assets/web/`: collected web text, source pages, and downloaded images with provenance notes when web material is needed.
3. Read the source and identify the user's real intent:
   - academic report
   - thesis defense
   - course presentation
   - student activity
   - lab/project progress
   - policy/admin briefing
4. Select a style using [references/template-selection.md](references/template-selection.md).
5. Build native editable slides: text boxes, shapes, tables, charts, diagrams, and images.
6. If the deck needs flowcharts, roadmaps, mechanism diagrams, or complex structures, use [references/diagram-workflow.md](references/diagram-workflow.md) and keep diagrams editable whenever practical.
7. If the task includes data, CSV, Excel, statistical tables, or chart polish, use [references/data-visualization.md](references/data-visualization.md).
8. If web text or images are needed, use [references/web-content-acquisition.md](references/web-content-acquisition.md) and keep source/provenance records.
9. Generate and insert speaker notes when requested or when the deck is for live presentation; use [references/speaker-notes.md](references/speaker-notes.md).
10. For revisions, follow [references/revision-safety.md](references/revision-safety.md): never overwrite a source or user-edited PPTX; create a new timestamped version first.
11. Render previews, run visual QA using [references/visual-qa.md](references/visual-qa.md), and iterate before delivery.
12. When local Office compatibility matters, validate the deck with [references/office-compatibility.md](references/office-compatibility.md) and `scripts/office_bridge.ps1`.

## What This Skill Should Demonstrate

- Understand the user's source material rather than mechanically copying paragraphs.
- Convert dense Chinese writing into a slide claim spine.
- Choose a suitable SJTU-style visual direction for the audience and occasion.
- Produce editable PPTX content, not a stack of full-slide screenshots.
- Reuse user-provided templates and logos responsibly.
- Preserve user-edited decks by creating a new dated revision file for every update.
- For existing decks, default to conservative revision mode: preserve good content and fix only verifiable or explicitly requested issues unless the user asks for redesign.
- Generate per-slide speaker notes, insert them into PPT speaker notes, and keep them synchronized unless a user-corrected slide is locked.
- Learn from user-inserted images and keep image choices consistent across later revisions.
- Turn user-provided data into clean, reproducible, PPT-ready, Nature-like scientific charts when needed.
- Collect useful public web text/images with source records when the user asks for online material.
- Draw simple and complex flowcharts as editable PowerPoint shapes rather than static screenshots when feasible.
- Visually review rendered slides for text-image overlap, blocked colors, unclear diagrams, poor contrast, and unreadable labels.
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
   - For flowcharts or structural diagrams, plan the node hierarchy and connector logic before drawing.
   - For web-supported content, collect sources first and log URLs, capture dates, snippets, and image provenance.
4. Rebuild content as presentation language:
   - shorten long paragraphs
   - turn lists into grouped arguments
   - turn tables into maps or matrices
   - turn mechanisms into flows
   - turn conclusions into closing takeaways
5. Apply the selected SJTU style system.
6. If revising an existing deck, copy the latest user-edited deck to a new versioned file before making changes.
7. Render and inspect every slide.

## Editable Diagrams And Visual QA

Read [references/diagram-workflow.md](references/diagram-workflow.md) when the deck needs process diagrams, flowcharts, organization diagrams, mechanism diagrams, roadmap structures, or simple/complex architecture diagrams.

Read [references/visual-qa.md](references/visual-qa.md) before final delivery and after substantial revisions.

Core rules:

- Build diagrams from native PowerPoint shapes, text boxes, lines, connectors, groups, tables, or charts whenever practical.
- Keep simple flows editable; for complex flows, keep an editable source plan even if a polished exported figure is inserted.
- Render slide previews and inspect every page for object overlap, text overflow, low contrast, blocked images, inconsistent color pairing, and unreadable labels.
- If visual defects appear, fix the source deck and rerender. Do not only describe the issue.
- Test diagram quality with at least one simple flow and one complex structure when the deck depends on auto-generated diagrams.

## Web Text And Image Acquisition

Read [references/web-content-acquisition.md](references/web-content-acquisition.md) when the user asks to collect public text, images, news, institutional introductions, project materials, or other online references for a deck.

Core rules:

- Prefer official, primary, or user-approved sources.
- Save source URL, access time, extracted snippets, image URLs, and usage notes in the task workspace.
- Do not silently insert copyrighted, private, login-only, or unclear-license images into public-facing decks.
- Use web material as evidence and visual reference; rewrite slide text into presentation language instead of pasting long webpages.
- Keep downloaded images under `assets/web/images/` and source page records under `assets/web/pages/`.

## Speaker Notes And Presentation Script

Read [references/speaker-notes.md](references/speaker-notes.md) when the user asks for 演讲稿, 讲稿, speaker notes, speaker script, 备注, presentation notes, or when a deck is intended for live presenting.

Core rules:

- Generate concise per-slide speaker notes that match each slide claim and audience.
- Insert notes into the PPTX speaker notes area, not visible slide text, whenever the authoring/editing tool supports notes.
- If the user provides a script, align it slide-by-slide instead of replacing it wholesale.
- When the deck changes, update notes for changed slides automatically unless that slide is locked.
- After the user corrects a slide's notes or content in the first review round, mark that slide locked; future revisions must not change that slide's notes or content unless the user explicitly unlocks it.
- If AI wants to substantially rewrite user-provided notes, present the proposed change and ask for confirmation before applying it.

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
- Do not silently replace a working page, screenshot, diagram, or layout in the name of optimization; keep good content unless the user asks for a redesign.
- If a revision damages good content, restore from the latest user-provided base before making any further changes.
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
- Check text-image overlap, blocked visual layers, color contrast, and whether key labels remain readable on rendered previews.
- Confirm generated flowcharts and structure diagrams are clear, logically routed, and editable where feasible.
- Confirm web-collected material has source notes and is suitable for the deck's use case.
- Confirm the deck opens in an available local Office engine when the user reports open failures or asks for Office validation.
- For generated charts, confirm data/code/output files are saved and the rendered chart remains readable in slide previews.
- Confirm speaker notes exist for expected slides and that user-locked notes/content were not changed.
- Fix the source deck and rerender if visual defects appear.

## Resources

- [references/authoring-workflow.md](references/authoring-workflow.md): source-to-slide process.
- [references/template-selection.md](references/template-selection.md): style selection rules.
- [references/style-system.md](references/style-system.md): SJTU-style layout, color, and typography defaults.
- [references/data-visualization.md](references/data-visualization.md): data processing, reproducible figures, and Nature-like PPT chart rules.
- [references/diagram-workflow.md](references/diagram-workflow.md): editable flowchart and structure diagram rules.
- [references/visual-qa.md](references/visual-qa.md): rendered-preview review, overlap checks, contrast checks, and iteration loop.
- [references/web-content-acquisition.md](references/web-content-acquisition.md): public web text/image collection, provenance, and usage checks.
- [references/office-compatibility.md](references/office-compatibility.md): PowerPoint/WPS/LibreOffice validation and repair workflow.
- [references/quality-gates.md](references/quality-gates.md): final verification checklist.
- [references/revision-safety.md](references/revision-safety.md): non-destructive revision naming, user-edit preservation, and image habit tracking.
- [references/bundled-assets.md](references/bundled-assets.md): bundled logo, PPT template, and font inventory.
- [references/speaker-notes.md](references/speaker-notes.md): speaker script generation, PPT notes insertion, note synchronization, and user-correction locks.
- `scripts/create_workspace.py`: creates a clean local workspace for source files and user-provided assets.
- `scripts/plot_style.py`: reusable Matplotlib styling helper for SJTU/Nature-like PPT charts.
- `scripts/web_collect.py`: collects public web text/image candidates into a task workspace with source records.
- `scripts/office_bridge.ps1`: validates and resaves PPTX files through available local presentation engines.
- `assets/`: bundled logos, templates, and fonts. See [ASSET_NOTICE.md](ASSET_NOTICE.md) before use or redistribution.
