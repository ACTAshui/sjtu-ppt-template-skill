# SJTU PPT Template Skill English Guide

A Codex skill for creating and safely revising Shanghai Jiao Tong University style editable PowerPoint decks. It helps Codex understand the material first, choose an appropriate SJTU-style presentation direction, and produce an editable `.pptx`.

> Personal project, not an official Shanghai Jiao Tong University release. This repository now includes user-provided SJTU logo PNGs, PPTX templates, and an optional font package for direct use. Read [ASSET_NOTICE.md](ASSET_NOTICE.md) before public, official, commercial, or redistributed use.

## What It Is For

- Course presentations, reading reports, review talks
- Lab meetings, project progress reports, research summaries
- Undergraduate, master's, or doctoral defense drafts
- Academic lectures, school or lab introductions
- Student activities, admissions, campus culture
- Presentation decks with data analysis, charts, scientific figures, or figure polishing

The skill guides Codex to:

- Extract the main narrative from DOCX, notes, PDF notes, outlines, existing PPT files, or long Chinese drafts.
- Convert article logic into presentation logic.
- Choose an appropriate style for defenses, seminars, course presentations, or promotional decks.
- Use bundled logos and PPT templates, or replace them with your own authorized materials.
- Generate editable `.pptx` files instead of full-slide screenshots.
- Create a new timestamped revision file for every update, so user-edited decks are not overwritten.
- Read user-inserted or user-replaced images and record image habits for later revisions.
- Generate per-slide speaker notes/scripts and insert them into the PPT speaker notes area.
- After the user corrects a slide's notes or visible content in the first review round, lock that slide so later revisions do not automatically change it.
- Apply Nature-like scientific visualization rules when handling CSV, Excel, experimental data, or statistical tables.
- Render previews and check Chinese wrapping, layout, logos, footers, chart readability, and overflow before delivery.

## One-Line Install Prompt

Copy this into Codex:

```text
Please fetch and install this skill from https://github.com/ACTAshui/sjtu-ppt-template-skill. When I need a Shanghai Jiao Tong University style presentation, use it to understand my materials, choose an appropriate style, preserve my edits during revisions, and generate an editable PPTX.
```

## Manual Installation

1. Download this repository, or download the zip file from Releases.
2. Place the whole `sjtu-ppt-template` folder in your Codex skills directory:

```text
C:\Users\your-name\.codex\skills\sjtu-ppt-template
```

3. Confirm the folder contains:

```text
sjtu-ppt-template/
  SKILL.md
  README.md
  README.zh-CN.md
  README.en.md
  agents/
  assets/
  references/
  scripts/
```

4. Restart Codex or start a new task so Codex can discover the skill.

## Prepare Local Materials

This repository includes user-provided logo, template, and font assets. The workspace creator copies them by default. You can also add your own authorized files.

Ask Codex to create a workspace:

```bash
python scripts/create_workspace.py ./my-sjtu-deck --profile academic-report
```

Then place files like this:

```text
my-sjtu-deck/
  source/              DOCX, PDF, Markdown, outlines, or existing PPT files
  data/raw/            original CSV, Excel, experimental data, or statistical tables
  data/processed/      cleaned data
  assets/logos/        authorized SJTU logos or department marks
  assets/templates/    authorized PPTX templates
  assets/fonts/        optional font packages
  assets/images/       images to insert or replace
  figures/             chart code, chart data, PNG/PDF/SVG outputs
  planning/            revision logs, image habits, and chart plans
  planning/speaker-notes.md
  planning/speaker-note-locks.json
  output/previews/     rendered slide previews
  output/versions/     new versioned PPTX files
```

## How To Ask Codex To Use It

After installation, you can say:

```text
Use the sjtu-ppt-template skill to turn this Word document into an SJTU-style course presentation. Make it 8-10 slides, clean and formal, and output an editable PPTX.
```

Or:

```text
Use the sjtu-ppt-template skill to create a lab meeting deck from my review notes. First extract the claim spine, then choose a suitable SJTU-style template. Do not copy paragraphs slide by slide.
```

For data and charts:

```text
Use the sjtu-ppt-template skill to process this Excel dataset and make the key results into academic presentation charts. I want a clean, restrained, Nature-like style with clear labels and PPT-ready outputs.
```

For speaker notes:

```text
Use the sjtu-ppt-template skill to generate speaker notes for every slide and insert them into the PPT speaker notes area. If I correct a slide's notes or visible content, lock that slide and do not automatically change it in later revisions.
```

## Helpful Details To Provide

Tell Codex:

- Purpose: course presentation, lab meeting, defense, lecture, promotional deck, etc.
- Audience: teachers, students, reviewers, lab members, public audience, etc.
- Expected slide count.
- Style preference: formal, clean, academic, promotional, campus storytelling, etc.
- Whether a specific template or logo must be used.
- Whether charts, timelines, mechanism diagrams, comparison matrices, or summary pages are needed.
- Data source type: CSV, Excel, experimental table, questionnaire result, statistical summary, etc.
- What each chart should emphasize: trend, difference, correlation, group comparison, mechanism, evidence chain, etc.

## Workflow

1. Read the material and identify topic, purpose, audience, and slide count.
2. Write a one-sentence claim spine for the deck.
3. Choose slide roles: cover, divider, flow, matrix, timeline, chart page, summary, etc.
4. If data is present, clean and understand the data before choosing chart types.
5. Select an SJTU-style visual direction.
6. Generate or align per-slide speaker notes and insert them into the PPT speaker notes area.
7. Use local authorized templates and logos to generate an editable PPT.
8. For revisions, copy the latest user-edited deck first and save a new timestamped version.
9. Render previews and inspect Chinese layout, overflow, chart readability, and visual consistency.
10. Fix issues before delivering the final `.pptx`.

## Speaker Notes

The skill can generate natural per-slide speaker notes from the slide claim, visible content, charts, images, and source materials, then insert them into the PowerPoint speaker notes area. Notes are not placed on visible slides unless requested.

If the user provides a script, the skill aligns it slide by slide and preserves the user's voice. If AI wants to substantially rewrite user-provided notes, it asks for confirmation first.

Revision behavior:

- Notes for changed, unlocked slides are updated automatically.
- If the user corrects a slide's notes or visible content in the first review round, that slide is recorded in `planning/speaker-note-locks.json`.
- Later revisions do not automatically change locked slide notes or visible content.
- Locked slides are changed again only after an explicit unlock/edit request.

## Non-Destructive Revisions

If you manually edit a PPT and ask Codex to continue revising it, this skill tells Codex to read your latest edited file, create a new revision, and avoid overwriting the original.

Recommended filename pattern:

```text
original-name__YYYYMMDD-HHMMSS__rNN.pptx
```

Example:

```text
AI-youth-SJTU-demo__20260518-143022__r03.pptx
```

This makes it easy to return to older versions.

## Image Habit Tracking

When you insert, replace, crop, or move images, later revisions preserve those choices when possible. The skill records preferences in:

```text
planning/image-preferences.md
planning/image-inventory.json
planning/revision-log.md
```

Codex can then learn whether you prefer wide documentary photos, side-panel figures, full-bleed images, short labels, no captions, or other recurring image habits.

## Data Visualization Enhancement

When the material includes data tables, CSV, Excel, statistical results, or experimental figures, the skill uses [references/data-visualization.md](references/data-visualization.md):

- Keep charts reproducible by preserving raw data, cleaned data, plotting code, and outputs.
- Use native PowerPoint charts for simple charts that should remain editable.
- Use Python/Matplotlib for more scientific or complex charts, exporting PNG plus PDF/SVG where appropriate.
- Apply restrained Nature-like visual rules: minimal decoration, consistent typography, color-blind-safe palettes, direct labels, clean axes, and clear source notes.
- Make every chart serve a slide-level claim instead of adding charts only for decoration.

## Bundled Assets

This repository includes:

- `assets/logos/sjtu/`: SJTU logo PNG variants.
- `assets/templates/sjtu-civilization-office/`: user-provided SJTU PPT templates.
- `assets/fonts/`: optional font package.

The workspace creator copies bundled assets by default. To create an empty workspace for your own assets:

```bash
python scripts/create_workspace.py ./my-sjtu-deck --no-bundled-assets
```

See [references/bundled-assets.md](references/bundled-assets.md) for the asset inventory and [ASSET_NOTICE.md](ASSET_NOTICE.md) for usage notes.

## FAQ

### Does this skill include official SJTU PPT templates?

It now includes user-provided SJTU logo and PPT template files for convenience. This is not an official release and does not grant trademark or copyright permission. Confirm authorization before official, public, commercial, or redistributed use.

### Are generated PPT files editable?

The goal is an editable `.pptx`: titles, body text, shapes, tables, charts, page numbers, and simple diagrams should remain native PowerPoint objects whenever possible. Complex scientific figures may be inserted as high-quality PNG/SVG/PDF outputs, with source data and code preserved for regeneration.

### Can I start from a Word document?

Yes. Put the Word document in `source/` and ask Codex to use this skill. It will convert long prose into a presentation structure.

### Can I use Excel or CSV data?

Yes. Put data in `data/raw/`. Codex can clean it, choose chart types, generate PPT-ready visualizations, and keep reproducible figure assets.

### What if I do not have a template?

The skill can still create a deck using default SJTU red, blue, and gold visual directions. Authorized local PPT templates usually improve fit and consistency.

### Why render previews?

Chinese PPTs often suffer from wrapping, overlap, footer collisions, blurry logos, and tiny chart labels. This skill requires preview rendering and inspection before final delivery.

## Repository Structure

```text
SKILL.md                              skill entry
README.md                             language entry
README.zh-CN.md                       Chinese guide
README.en.md                          English guide
agents/openai.yaml                    agent metadata
references/authoring-workflow.md      source-to-slide workflow
references/template-selection.md      template and style selection
references/style-system.md            SJTU-style visual system
references/data-visualization.md      data processing and Nature-like chart workflow
references/quality-gates.md           final checks
references/revision-safety.md         non-destructive revisions and image habit tracking
references/bundled-assets.md          bundled logo, PPT template, and font inventory
references/speaker-notes.md           speaker note generation, insertion, sync, and locks
scripts/create_workspace.py           local workspace creator
scripts/plot_style.py                 PPT scientific chart style helper
assets/logos/                         bundled logo PNGs
assets/templates/                     bundled PPTX templates
assets/fonts/                         optional font package
ASSET_NOTICE.md                       bundled asset usage notes
```

## Disclaimer

This is a personal Codex skill for learning and productivity. Follow applicable SJTU visual identity rules, copyright requirements, and your institution's material usage policies.
