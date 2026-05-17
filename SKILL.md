---
name: sjtu-ppt-template
description: Create Shanghai Jiao Tong University style editable PowerPoint decks from DOCX, notes, outlines, reports, papers, course materials, project summaries, or draft slides. Use when the user asks for 上海交通大学, 上海交大, 上交, SJTU, school-branded PPT, academic report slides, seminar decks, thesis defense slides, group meeting slides, course presentation decks, template selection, or converting Chinese research writing into a polished editable SJTU-style presentation.
---

# SJTU PPT Template

Create editable Shanghai Jiao Tong University style presentation decks for students, teachers, labs, courses, seminars, defenses, and academic reports.

This public skill contains workflow and design guidance only. It does not bundle official SJTU logos, school templates, private documents, or copyrighted assets. Users provide authorized logos and template decks in their local task workspace.

## Quick Start

1. Create a task workspace:
   ```bash
   python scripts/create_workspace.py ./my-sjtu-deck --profile academic-report
   ```
2. Place user-provided assets in the workspace:
   - `source/`: DOCX, Markdown, PDF notes, outline, or existing PPT.
   - `assets/logos/`: authorized SJTU logos or department marks.
   - `assets/templates/`: authorized PPTX templates.
3. Read the source and identify the user's real intent:
   - academic report
   - thesis defense
   - course presentation
   - student activity
   - lab/project progress
   - policy/admin briefing
4. Select a style using [references/template-selection.md](references/template-selection.md).
5. Build native editable slides: text boxes, shapes, tables, charts, diagrams, and images.
6. For revisions, follow [references/revision-safety.md](references/revision-safety.md): never overwrite a source or user-edited PPTX; create a new timestamped version first.
7. Render previews, check layout, and iterate before delivery.

## What This Skill Should Demonstrate

- Understand the user's source material rather than mechanically copying paragraphs.
- Convert dense Chinese writing into a slide claim spine.
- Choose a suitable SJTU-style visual direction for the audience and occasion.
- Produce editable PPTX content, not a stack of full-slide screenshots.
- Reuse user-provided templates and logos responsibly.
- Preserve user-edited decks by creating a new dated revision file for every update.
- Learn from user-inserted images and keep image choices consistent across later revisions.
- Keep a consistent formal SJTU visual system across cover, section, content, chart, matrix, and closing pages.

## Template Choice

Read [references/template-selection.md](references/template-selection.md) before choosing a style.

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
- Keep titles as conclusions, not generic topic labels.
- Prefer calm academic layouts for teachers, defenses, and research groups.
- Use more image-led rhythm only for campus culture or student-facing decks.

## Quality Gates

Read [references/quality-gates.md](references/quality-gates.md).

Before final delivery:

- Confirm final PPTX exists and is non-empty.
- Confirm the final PPTX is a new revision file, not an overwritten source or prior delivery.
- Confirm expected slide count.
- Confirm important text is editable.
- Render all slides and inspect Chinese wrapping, logo sharpness, footer alignment, text overflow, and chart readability.
- Fix the source deck and rerender if visual defects appear.

## Resources

- [references/authoring-workflow.md](references/authoring-workflow.md): source-to-slide process.
- [references/template-selection.md](references/template-selection.md): style selection rules.
- [references/style-system.md](references/style-system.md): SJTU-style layout, color, and typography defaults.
- [references/quality-gates.md](references/quality-gates.md): final verification checklist.
- [references/revision-safety.md](references/revision-safety.md): non-destructive revision naming, user-edit preservation, and image habit tracking.
- `scripts/create_workspace.py`: creates a clean local workspace for source files and user-provided assets.
- `assets/.gitkeep`: placeholder only; do not commit official logos, private documents, or copyrighted templates unless authorized.
