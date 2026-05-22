# Authoring Workflow

Use this workflow to convert user materials into an editable SJTU-style presentation.

## 1. Understand The Task

Identify:

- audience: teacher, student, committee, lab, course, public event, school office
- format: report, defense, seminar, group meeting, lecture, activity recap
- language: Chinese, English, or bilingual
- desired length
- must-use logos or templates
- whether the final PPTX must remain fully editable

## 2. Extract The Source Structure

For DOCX or long Chinese drafts:

- extract headings
- identify tables and lists
- preserve essential numbers and citations
- find the central thesis
- mark material that belongs in appendix rather than main slides

Do not copy long paragraphs verbatim into slides.

## 3. Build A Claim Spine

Write one claim per slide. Each claim should say what the audience should believe after seeing the slide.

Common deck structures:

- academic review: topic -> literature map -> reality base -> mechanism -> risk/problem -> governance/solution -> future agenda
- thesis defense: question -> method -> data -> results -> contribution -> limitations -> conclusion
- group meeting: goal -> progress -> experiment -> issue -> next step
- course presentation: concept -> case -> analysis -> reflection -> takeaway
- activity report: theme -> highlights -> timeline -> participation -> outcomes -> closing

## 4. Choose Proof Objects

Use the proof object that best fits the claim:

- table for classification
- matrix for risk, comparison, or governance mapping
- mechanism chain for formation processes
- timeline for development stages
- chart for trend or proportion
- quote/case panel for qualitative material
- visual montage for campus or event storytelling

If the proof object depends on CSV, Excel, experimental data, statistics, or existing chart screenshots, read [data-visualization.md](data-visualization.md) before drawing or inserting charts.

If the proof object is a process, mechanism, architecture, governance path, or structure diagram, read [diagram-workflow.md](diagram-workflow.md) before drawing. Plan nodes and connectors before placing shapes.

If the proof object depends on public online information or images, read [web-content-acquisition.md](web-content-acquisition.md) before collecting material. Keep source records and permission notes.

## 5. Build Editable Slides

Prefer native PowerPoint objects:

- text boxes
- shapes
- editable tables
- native charts or editable chart-like primitives
- image layers for photos, logos, and complex figures

Avoid full-slide screenshots except for temporary references or explicitly image-based deliverables.

For diagrams, use native editable shapes/connectors whenever feasible. For web-supported images, keep source records and verify that placement does not block text or logos.

## 6. Visual QA Before Delivery

Render the PPTX to slide images and inspect the deck using [visual-qa.md](visual-qa.md).

Check:

- text and image overlap
- blocked labels, footers, logos, and titles
- low color contrast
- text overflow and awkward Chinese wrapping
- chart/table readability
- diagram connector clarity and label readability
- user-locked content preservation

## 7. Revise Without Overwriting

When the task is an update to an existing deck, do not regenerate from scratch unless the user asks for a full rebuild. Read the latest user-edited deck, preserve their manual changes, then create a new versioned file before applying the new request.

Use [revision-safety.md](revision-safety.md) for naming, revision logs, and image habit tracking.
