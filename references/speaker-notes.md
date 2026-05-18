# Speaker Notes And Presentation Script

Use this reference when the user asks for 演讲稿, 讲稿, speaker notes, presentation script, 备注, or when a deck is meant for live presentation.

## Goal

Generate a concise, natural speaker script for every slide and insert it into the PPTX speaker notes area. Notes should help the presenter speak, not duplicate all visible slide text.

## Inputs

Use these sources in priority order:

1. User-provided speaker script or draft notes.
2. User-corrected speaker notes from the latest PPTX.
3. Current slide title, visible text, charts, images, and speaker intent.
4. Source documents and claim spine.

If the user provides a full script, align it to slides and lightly edit for flow only when needed. Do not replace the user's voice with a generic AI style.

## Note Style

- Match the deck language: Chinese, English, or bilingual.
- Keep one slide's notes short enough to speak naturally, usually 80-180 Chinese characters or 60-120 English words unless the user asks for a full script.
- Use spoken language, not paper prose.
- Include transitions only when they help flow.
- Explain charts by naming the one pattern the audience should notice.
- Avoid reading every bullet aloud.
- Avoid adding unsupported claims that are not on the slide or in source materials.

## Insertion Rule

Insert generated notes into the PPTX speaker notes area for each slide whenever the authoring or editing tool supports notes. Do not place the script as visible slide text unless the user asks for a teleprompter or handout page.

If the current toolchain cannot write PPT speaker notes, produce `planning/speaker-notes.md`, explain the limitation, and use a notes-capable workflow before final delivery when possible.

## Synchronization Rule

When a deck is revised:

1. Identify changed slides.
2. Update speaker notes for changed, unlocked slides.
3. Keep notes for unchanged slides unless the user asks for a full script rewrite.
4. Do not update notes or visible content on locked slides.
5. Record updates in `planning/revision-log.md`.

## User-Provided Script

When the user provides a script:

- Split it into slide-level notes.
- Preserve user phrasing where it is clear and accurate.
- If a slide's visible content conflicts with the script, propose a small alignment change.
- Ask before substantially rewriting user-provided wording.

## AI Self-Correction

AI may propose improvements when notes are too long, unsupported, repetitive, or mismatched with the slide. Before applying a substantial rewrite to user-provided or user-corrected notes, show the proposed change and ask whether to update.

Small mechanical fixes can be applied automatically:

- punctuation
- obvious typo correction
- slide number references
- trimming duplicate visible text

## Locking After User Correction

If the user corrects a slide's notes or visible content during the first review round, lock that slide.

Locked means:

- do not update that slide's speaker notes automatically
- do not update that slide's visible slide content automatically
- preserve the user's corrected wording and layout
- only modify it again when the user explicitly asks to unlock or edit that slide

Store locks in `planning/speaker-note-locks.json`:

```json
{
  "slides": {
    "3": {
      "notes_locked": true,
      "content_locked": true,
      "reason": "User corrected slide 3 in first review round",
      "locked_at": "2026-05-18 14:30",
      "unlock_rule": "Only change after explicit user request"
    }
  }
}
```

When a user says "后续不要再改这一页", "这一页备注就这样", "保留我改的", or similar, lock that slide even if it is not the first review round.

## Review Workflow

For first-round notes:

1. Generate or align notes.
2. Insert notes into PPTX.
3. Provide a short review summary listing slides where AI made substantive script decisions.
4. Ask the user whether any notes should be corrected.

After user corrections:

1. Update only the corrected slides.
2. Lock corrected slide notes and visible content.
3. In later revisions, skip locked slides unless explicitly unlocked.

## Planning Files

Maintain:

```text
planning/speaker-notes.md
planning/speaker-note-locks.json
planning/revision-log.md
```

`speaker-notes.md` can mirror the inserted notes for easier review:

```text
## Slide 1 - Title

Speaker notes:
...

Status: unlocked
```
