# Data Visualization For SJTU PPT

Use this reference when a deck includes CSV, Excel, statistical tables, experimental data, survey results, chart screenshots, manuscript figures, or requests such as "make the chart better", "Nature style", "科研绘图", "数据处理", "图表美化", or "更适合学术汇报".

## Core Standard

Every chart should support one slide claim. Make it readable in a projected PPT, visually restrained, and reproducible from stored data and code when possible.

Use a Nature-like scientific style as a direction, not as a journal claim:

- clean axes and thin rules
- no decorative gradients, shadows, or 3D effects
- restrained color-blind-safe palette
- direct labels when they reduce legend searching
- consistent typography and capitalization
- short source notes when data are synthesized or user-provided
- enough contrast for projection

## Native PPT vs Generated Figure

Use native PowerPoint charts when:

- the chart is simple: bar, line, scatter, pie/donut only if truly appropriate
- the user may need to edit values or labels inside PowerPoint
- the deck is business/admin/course-facing rather than manuscript-like

Use Python/Matplotlib outputs when:

- the chart needs publication-style polish
- there are multiple panels, error bars, confidence intervals, distributions, heatmaps, or dense annotations
- the source data should be reproducible
- the chart needs PNG plus PDF/SVG export

For generated figures, keep the data and code in the task workspace and insert the exported chart into PPT. If the user needs editability, also provide a simplified native PPT chart or a data table appendix.

## Workspace Pattern

For each important chart, create or maintain:

```text
figures/
  fig01_short_name/
    code/
    data/
    outputs/
    sources/
    README.md
```

Store:

- `code/`: one script that regenerates the chart.
- `data/`: CSV/JSON used directly by the script.
- `outputs/`: PNG for PPT, PDF/SVG for vector preservation when useful.
- `sources/`: a short note distinguishing user-provided data, cleaned data, reproduced metrics, and author-synthesized frameworks.
- `README.md`: chart purpose, command, output files, and source type.

## Figure Planning

Before drawing:

1. Identify the slide claim the chart must support.
2. Identify the data source and whether values are raw, cleaned, computed, or illustrative.
3. Choose the simplest chart type that answers the claim.
4. Decide whether the final PPT needs native editability or reproducible figure quality.
5. Decide whether labels should be in Chinese, English, or bilingual.

## Chart Type Guidance

- Trend over time: line chart or slope chart.
- Group comparison: bar chart with direct labels; use dot/interval plots for scientific comparisons.
- Distribution: box, violin, histogram, or ridgeline only when the audience can read it quickly.
- Relationship: scatter with modest fit line and annotation; avoid overplotting.
- Part-to-whole: stacked bar or small multiples; avoid pie charts unless categories are few and obvious.
- Process/mechanism: editable PPT flow or vector diagram, not a decorative infographic.
- Literature map or taxonomy: matrix, alluvial-like flow, or grouped table.
- Before/after or method comparison: paired dots, dumbbell chart, or two-column matrix.

## PPT Readability Rules

- Titles should state conclusions, not chart types.
- Axis labels must be readable at slide size.
- Avoid more than 5-7 visual groups on one slide.
- Prefer direct labels over legends when space allows.
- Use annotations to explain the one thing the audience should notice.
- Keep gridlines light and minimal.
- Avoid tiny footnotes; move details to speaker notes or appendix.
- For Chinese slides, use Microsoft YaHei, DengXian, Source Han Sans SC, Noto Sans CJK SC, or HarmonyOS Sans SC.

## Palette

Use the SJTU palette first, then extend with color-blind-safe accents:

- SJTU blue: `#004098`
- SJTU red: `#C8161E`
- SJTU gold: `#BD9F68`
- Ink: `#172033`
- Muted gray: `#6B778A`
- Safe teal: `#2A9D8F`
- Safe orange: `#E69F00`
- Safe purple: `#7B61A8`

Do not make every chart red/blue only. Use SJTU red as emphasis, not as the default fill for all categories.

## Matplotlib Preference

Prefer Matplotlib for reproducible charts. If `SciencePlots` is installed, this style is acceptable:

```python
import scienceplots
plt.style.use(["science", "nature", "no-latex"])
```

If it is not installed, use the bundled `scripts/plot_style.py` helper or equivalent `rcParams`: embedded fonts, thin axes, high DPI, clean background, restrained colors, and no unnecessary frames.

Minimum outputs for PPT:

- `chart-name.png`: transparent or white background, 200-300 dpi for slides.
- `chart-name.pdf` or `chart-name.svg`: vector copy when useful.
- data file and script that regenerate the chart.

## Inserting Charts Into PPT

- Use native PPT charts for simple editable values.
- Use PNG for reliable cross-platform display.
- Keep SVG/PDF next to the deck for future edits or publication reuse.
- Do not stretch charts; preserve aspect ratio.
- Put charts in a layout with enough label room.
- If the chart is dense, give it a full slide rather than squeezing it into a small card.
- Add source notes only when they help trust or interpretation.

## QA Checklist

Before delivery:

- The chart supports the slide claim.
- The data source is recorded.
- Outputs can be regenerated from code/data when generated externally.
- Text and labels are readable in rendered slide previews.
- Colors are distinguishable in grayscale or for common color-vision deficiencies.
- Important chart text is either editable in PPT or reproducible from code.
- The chart style matches the selected SJTU deck style.
