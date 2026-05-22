# Web Content Acquisition

Use this workflow when the user asks for online text, images, institutional information, news, examples, maps, or public reference material for an SJTU-style deck.

## Source Selection

Prefer sources in this order:

1. Official SJTU, school, department, lab, event, or government pages.
2. Primary documents, PDFs, notices, datasets, or press releases.
3. User-approved public pages.
4. Secondary media only when the user asks for broader context.

Avoid private, login-only, paywalled, unclear-license, or personal material unless the user provides authorization.

## Collection Records

Keep web material inside the task workspace:

```text
assets/web/pages/       saved HTML or PDF/source snapshots
assets/web/images/      downloaded candidate images
assets/web/sources.json machine-readable source manifest
planning/web-sources.md human-readable source notes
```

For every source record:

- Original URL.
- Access date/time.
- Page title.
- Short extracted snippets.
- Image URLs and local filenames.
- Usage decision: used, reference only, rejected, or needs permission.
- Any copyright/license concern.

## Text Use

- Extract facts, terms, names, dates, and official wording.
- Rewrite slide text into concise presentation language.
- Do not paste long web paragraphs into slides.
- Keep exact quotations short and attributed.
- If a fact may be time-sensitive, verify it against current sources before final delivery.

## Image Use

- Download only candidate images into `assets/web/images/`.
- Keep source URL and alt/caption metadata.
- Do not insert images into public decks when copyright or authorization is unclear.
- Prefer user-provided, official, or clearly authorized images for final decks.
- Crop and place images only after checking that text, logos, and labels remain unobstructed in rendered previews.

## Suggested Helper

Use `scripts/web_collect.py` to fetch public pages, extract headings/paragraph snippets, list image candidates, and optionally download images with provenance records.

Example:

```bash
python scripts/web_collect.py ./my-sjtu-deck https://example.edu/page --download-images --max-images 8
```

Review the generated `planning/web-sources.md` before inserting material into slides.
