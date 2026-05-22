# Editable Diagram Workflow

Use this workflow when a deck needs flowcharts, structure diagrams, mechanism chains, research roadmaps, policy paths, organization charts, or complex system diagrams.

## Core Rule

Prefer editable PowerPoint objects over static screenshots:

- Native shapes for nodes.
- Connectors or lines for relationships.
- Text boxes for labels.
- Tables for grid-like structures.
- Native SmartArt only when it remains easy to edit.
- Externally generated SVG/PNG only for diagrams that are too complex for native editing; preserve the source plan and generation code.

## Plan Before Drawing

Create `planning/diagram-plan.md` before drawing important diagrams.

Record:

- Slide number and diagram purpose.
- One-sentence claim the diagram supports.
- Diagram type: linear flow, branching decision, swimlane, hierarchy, matrix, loop, architecture, evidence chain.
- Nodes, node groups, and hierarchy.
- Connector direction and meaning.
- Color semantics.
- Which parts must remain editable.

## Simple Flowchart Pattern

Use for 3-7 steps.

- One row or one column.
- Consistent node size.
- Clear left-to-right or top-to-bottom direction.
- One short label per node.
- Optional small numbered badges.
- No connector crossings.

Best for: process summaries, presentation agendas, application workflows, experimental pipelines.

## Complex Structure Pattern

Use for multi-layer systems.

- Group related nodes into bands or lanes.
- Use hierarchy before using many colors.
- Keep connector styles meaningful: solid for primary flow, dashed for optional/feedback paths.
- Limit one slide to one main logic.
- Move secondary detail to appendix or speaker notes.
- Use labels on connectors only when the relationship is not obvious.

Best for: research frameworks, governance structures, mechanisms, system architecture, admissions-roadshow storylines.

## Readability Rules

- Use 12 pt as the practical lower bound for labels in normal 16:9 slides; larger for lecture halls.
- Keep node labels to one line when possible; two lines maximum for dense diagrams.
- Leave at least 8-12 px visual spacing between nodes and connectors.
- Use neutral fills with SJTU red or blue accents; avoid filling every node with saturated color.
- Route connectors around labels and images.
- Put the diagram title as a claim, not as "Flowchart" or "Structure".

## Editability Checks

Before delivery:

- Click-test a sample node and confirm its text can be edited.
- Confirm connectors move logically with nodes when grouped or manually adjusted.
- Confirm diagram labels are not embedded in a bitmap unless intentionally exported.
- If an exported diagram is used, keep source files in `figures/` and mention regeneration steps.

## Required Stress Test

When the task depends on generated diagrams, build and inspect:

- One simple 3-5 node flow.
- One complex multi-group structure.

Render both and check whether labels, connectors, grouping, and contrast remain clear at slide size.
