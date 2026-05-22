# SJTU PPT Template Skill 中文说明

一个给 Codex 使用的上海交通大学风格 PPT 生成与修订 skill。它的目标不是简单套背景，而是帮助 Codex 先理解材料，再按汇报场景选择合适的上交风格，生成可继续编辑、可复查、可继续迭代的 PowerPoint。现在它还包含可编辑流程图/结构图、网页图文采集、可视化复查和科研图表优化流程。

> 个人公开项目，非上海交通大学官方发布。本仓库现在包含你提供的校标 PNG、PPTX 模板和可选字体包，方便安装后直接使用。使用或再分发前请阅读 [ASSET_NOTICE.md](ASSET_NOTICE.md)，并确认符合原始素材来源、版权、商标和学校视觉规范。

## 它适合做什么

- 课程汇报、读书报告、综述展示
- 组会汇报、课题组进展、项目总结
- 本科/硕士/博士答辩初稿
- 学术讲座、学院/实验室介绍
- 学生活动、招生宣传、校园文化展示
- 带数据分析、图表、科研图片优化的汇报材料
- 需要流程图、结构图、机制图、路线图的演示材料
- 需要从公开网页整理文字、图片候选和来源记录的演示材料

这个 skill 会引导 Codex 做这些事：

- 从长文本、提纲、DOCX、PDF 笔记或已有 PPT 中提炼主线。
- 把“文章逻辑”改写成“演示逻辑”。
- 根据场景选择正式答辩、学术组会、课程展示、宣传路演等视觉风格。
- 使用仓库内置的校标和 PPT 模板，也可以替换成你自己的授权素材。
- 生成可编辑的 `.pptx`，而不是整页截图。
- 每次修订都新建一个带日期、时间和序号的文件，避免覆盖你已经改好的版本。
- 读取你手动插入或替换的图片，并记录你的图片使用习惯，后续修订尽量保持一致。
- 自动生成每页演讲者备注/讲稿，并插入 PPT 的备注区；修订后自动同步未锁定页面的讲稿。
- 如果你第一轮修正过某页备注或内容，后续默认锁定该页，不再自动改动该页备注和可见内容。
- 处理 CSV、Excel、实验数据或统计表时，使用更接近 Nature 风格的科研图表规则，让图表更清晰、克制、适合学术汇报。
- 生成简单流程图和复杂结构图时，优先使用 PowerPoint 原生形状、连接线和文本框，方便继续编辑。
- 需要网络资料时，把网页文字、图片候选、URL、访问时间和使用判断记录到工作区，而不是无来源地堆素材。
- 在交付前渲染预览，检查中文换行、版式、logo、页脚、文字和图片遮挡、颜色对比、流程图清晰度、图表可读性和内容溢出。
- 当用户反馈 PPT 打不开，或明确要求兼容性检查时，用本机可用的 PowerPoint/WPS/LibreOffice 引擎验证能否打开。

## 一句话安装

如果你已经在使用 Codex，可以直接把下面这句话发给 Codex：

```text
请帮我从网上获取 https://github.com/ACTAshui/sjtu-ppt-template-skill 这个 skill，并安装到本地。之后当我需要做上海交通大学风格 PPT 时，请优先调用它：先理解我的材料，再根据课程汇报、学术组会、答辩、讲座或宣传展示等场景，选择合适的风格和模板，保留我已经修改好的内容，并生成一份可编辑的 PPTX。
```

## 手动安装

1. 下载本仓库，或者下载 Release 里的 zip 包。
2. 把整个 `sjtu-ppt-template` 文件夹放到你的 Codex skills 目录：

```text
C:\Users\你的用户名\.codex\skills\sjtu-ppt-template
```

3. 确认目录里有这些文件：

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

4. 重新打开 Codex，或者开始一个新任务，让 Codex 能发现这个 skill。

## 准备你的本地素材

这个仓库已经内置你提供的校标、模板和字体包。创建工作区时，脚本会默认复制这些资源；你也可以继续放入自己的授权文件。

可以让 Codex 先创建一个工作区：

```bash
python scripts/create_workspace.py ./my-sjtu-deck --profile academic-report
```

然后把文件放进去：

```text
my-sjtu-deck/
  source/              放 DOCX、PDF、Markdown、提纲或已有 PPT
  data/raw/            放原始 CSV、Excel、实验数据、统计表
  data/processed/      放清洗后的数据
  assets/logos/        放你有权限使用的校标、院系标识
  assets/templates/    放你有权限使用的 PPTX 模板
  assets/fonts/        放可选字体包
  assets/images/       放你想插入或替换的图片
  assets/web/pages/    保存公开网页来源页面
  assets/web/images/   保存网页图片候选
  figures/             放图表代码、数据、PNG/PDF/SVG 输出
  planning/            记录修订日志、图片习惯、图表计划、网页来源和可视化复查
  planning/diagram-plan.md
  planning/visual-qa.md
  planning/web-sources.md
  planning/speaker-notes.md
  planning/speaker-note-locks.json
  output/previews/     渲染预览图
  output/versions/     每次修订自动新建的新版本
```

## 怎么让 Codex 调用它

安装好后，你可以这样说：

```text
请使用 sjtu-ppt-template skill，把这个 Word 文档做成一份上海交通大学风格的课程汇报 PPT。要求 8-10 页，风格清爽正式，最终输出可编辑 PPTX。
```

或者：

```text
请使用 sjtu-ppt-template skill，根据我的综述材料做一份组会汇报 PPT。请先提炼主线，再选择合适的上交风格模板，不要逐段复制原文。
```

如果有数据或图表，可以这样说：

```text
请使用 sjtu-ppt-template skill 处理这个 Excel 数据，并把关键结果做成更适合学术汇报的图表。图表风格希望接近 Nature：干净、克制、标注清楚、适合放进 PPT。
```

如果需要演讲稿，可以这样说：

```text
请使用 sjtu-ppt-template skill 为这份 PPT 生成每一页的演讲者备注，并自动插入 PPT 备注区。后续如果我改过某页备注或内容，请锁定该页，不要再自动改它。
```

如果需要流程图或结构图，可以这样说：

```text
请使用 sjtu-ppt-template skill，把这段机制整理成可编辑的 PPT 流程图。请同时做一个简单总览图和一个复杂结构图，并渲染预览检查文字、连接线、图片和颜色不要互相遮挡。
```

如果需要从网上整理图文，可以这样说：

```text
请使用 sjtu-ppt-template skill，从官方网页整理这次招生宣讲需要的公开文字和图片候选，记录 URL、访问时间和图片来源，然后把网页内容改写成适合 PPT 的表达。
```

## 推荐给 Codex 的信息

为了让效果更稳定，最好同时告诉 Codex：

- 这份 PPT 的用途：课程汇报、组会、答辩、讲座、宣传展示等。
- 听众是谁：老师、同学、评审专家、课题组、公众等。
- 期望页数：例如 6 页、10 页、15 页。
- 风格偏好：正式、清爽、学术、宣传感、校园文化感等。
- 是否必须使用某个模板或 logo。
- 是否需要图表、时间线、机制图、对比矩阵、总结页。
- 是否需要联网整理资料，以及优先使用或禁止使用哪些网站。
- 数据来源是什么：CSV、Excel、实验表格、问卷结果、统计摘要等。
- 图表需要强调什么：趋势、差异、相关性、分组比较、流程机制、证据链等。

## 工作流简述

skill 会要求 Codex 按这个顺序处理：

1. 阅读材料，确认主题、用途、听众和页数。
2. 提炼每页一句话的 claim spine，也就是演示主线。
3. 为每页选择合适的表达方式：标题页、章节页、流程图、矩阵、时间线、图表页、总结页等。
4. 如果需要网页资料，先采集公开来源并记录 URL、访问时间、文字片段和图片候选。
5. 如果有数据，先清洗和理解数据，再决定适合的图表类型。
6. 如果需要流程图或结构图，先规划节点、层级、连接线和是否可编辑，再开始绘制。
7. 按场景选择上交视觉风格。
8. 生成或对齐每页演讲者备注，并插入 PPT 备注区。
9. 使用本地授权模板和 logo 生成可编辑 PPT。
10. 如果是修改已有 PPT，先复制最新版用户文件，再生成新的日期时间序号版本。
11. 渲染预览图，检查中文排版、文字/图片遮挡、颜色对比、流程图清晰度、图表可读性和整体一致性。
12. 修正问题后再交付最终 `.pptx`。

## 演讲者备注/讲稿

skill 会根据每页标题、可见内容、图表、图片和原始材料，为每一页生成适合口头表达的演讲者备注，并插入 PPT 的 speaker notes 区域。它不会默认把讲稿放到可见页面上。

如果你提供了自己的讲稿，skill 会优先按你的稿件逐页对齐，而不是直接替换成 AI 风格。若 AI 认为某页讲稿需要大幅改写，会先给出建议并询问是否修改。

修订逻辑：

- PPT 内容变化后，未锁定页面的备注会自动同步更新。
- 用户第一轮修正过某页备注或页面内容后，该页会写入 `planning/speaker-note-locks.json`。
- 后续修订默认不再改动锁定页的备注和可见内容。
- 只有用户明确要求“解锁/继续改这一页”时，才会再次修改锁定页。

## 修订时不会覆盖原文件

如果你已经手动改过 PPT，再让 Codex 继续修改时，这个 skill 会要求它先读取你改过的最新文件，然后新建一个修订版，不直接在原文件上覆盖。

推荐文件名格式：

```text
原文件名__YYYYMMDD-HHMMSS__rNN.pptx
```

例如：

```text
青年与生成式AI_SJTU演示样稿__20260518-143022__r03.pptx
```

这样你随时可以回到旧版本，不会因为一次自动修改把已经调好的内容破坏掉。

## 会记录你的图片习惯

当你自己插入、替换、裁剪或移动图片后，后续修订会优先保留这些改动，并把你的偏好记录到工作区：

```text
planning/image-preferences.md
planning/image-inventory.json
planning/revision-log.md
```

它会观察你更喜欢哪类图片、常用什么裁剪比例、图片放左边还是做背景、是否加短标签或说明，也会记录重要图片在第几页、承担什么作用、是否是你手动添加。下一次继续改 PPT 时，Codex 会先读这些记录，再决定怎么维护图片。

## 数据图表增强

当材料里有数据表、CSV、Excel、统计结果或实验图时，skill 会参考 [references/data-visualization.md](references/data-visualization.md)：

- 优先做可复现图表：保留原始数据、清洗数据、绘图代码和输出文件。
- 简单图表优先使用 PPT 原生图表，方便后续编辑。
- 更复杂或更学术的图表使用 Python/Matplotlib 生成 PNG + PDF/SVG，再插入 PPT。
- 采用克制、清晰、适合学术汇报的 Nature-like 视觉规则：少装饰、字体一致、色盲友好、标签直接、线条干净。
- 每个图表都要服务于某一页的核心结论，而不是为了好看而堆图。

## 可编辑流程图与可视化复查

当材料需要流程图、结构图、机制图、路线图时，skill 会参考 [references/diagram-workflow.md](references/diagram-workflow.md)：简单流程优先使用 PowerPoint 原生形状和连接线，复杂结构图也要保留节点、层级和连接逻辑记录，方便后续修改。

交付前会参考 [references/visual-qa.md](references/visual-qa.md)：渲染每页预览图和总览图，检查文字和图片是否遮挡、颜色是否压住信息、标签是否可读、流程图连接线是否清楚。发现问题后修改源 PPT 并重新渲染，不只停留在口头说明。

## 网页图文采集

需要公开网页资料时，skill 会参考 [references/web-content-acquisition.md](references/web-content-acquisition.md)，并可使用：

```bash
python scripts/web_collect.py ./my-sjtu-deck https://example.edu/page --download-images --max-images 8
```

采集结果会放在 `assets/web/`，来源说明会记录到 `planning/web-sources.md`。公开发布或正式使用前，需要检查来源权威性、版权和图片使用权限。

## Office 兼容性检查

当 PPT 打不开或需要本地检查时，skill 会参考 [references/office-compatibility.md](references/office-compatibility.md)，并可运行：

```powershell
powershell -ExecutionPolicy Bypass -File scripts/office_bridge.ps1 -InputPptx "C:\path\deck.pptx" -OutputPptx "C:\path\deck_saved.pptx" -Engine auto -Visible
```

脚本会优先尝试 Microsoft PowerPoint 桌面版，其次 WPS 演示，并记录实际打开成功的引擎。

## 内置素材

本仓库包含：

- `assets/logos/sjtu/`：上海交通大学校标 PNG 变体。
- `assets/templates/sjtu-civilization-office/`：你提供的上海交大 PPT 模板。
- `assets/fonts/`：可选字体包。

创建工作区时默认复制内置素材。若只想使用自己的素材，可以让 Codex 运行：

```bash
python scripts/create_workspace.py ./my-sjtu-deck --no-bundled-assets
```

素材清单见 [references/bundled-assets.md](references/bundled-assets.md)。授权说明见 [ASSET_NOTICE.md](ASSET_NOTICE.md)。

## 常见问题

### 这个 skill 里有上海交通大学官方 PPT 模板吗？

本仓库现在包含你提供的校标和 PPT 模板，方便直接使用。但它不是官方发布，也不代表自动获得官方商标或版权授权。正式公开、官方传播或商业使用前，请确认你有权限使用这些素材。

### 生成的 PPT 是可编辑的吗？

目标是生成可编辑 `.pptx`：标题、正文、形状、表格、图表、页码等都应尽量保持为 PowerPoint 原生对象。复杂科研图可以作为高清 PNG/SVG/PDF 插入，同时保留数据和代码，方便下次重画。

### 我只有 Word 文档，可以用吗？

可以。把 Word 文档放进工作区的 `source/` 目录，然后告诉 Codex 使用这个 skill 制作 PPT。它会先把长文改写成适合演示的结构。

### 我有 Excel 或 CSV，可以用吗？

可以。把数据放进 `data/raw/`，让 Codex 使用这个 skill 读取、清洗、选择图表类型，并生成适合 PPT 的图表页。

### 我没有模板怎么办？

也可以做。没有模板时，skill 会使用上交红、蓝、金等视觉系统作为默认方向。但如果你提供授权 PPT 模板，通常更容易贴近你想要的正式效果。

### 为什么要先渲染预览？

因为中文 PPT 很容易出现换行、遮挡、页脚错位、logo 模糊、图表太小等问题。这个 skill 要求 Codex 在交付前渲染检查，发现问题后修正源文件再导出。

## 仓库结构

```text
SKILL.md                              skill 入口说明
README.md                             中英文入口
README.zh-CN.md                       中文完整说明
README.en.md                          English guide
agents/openai.yaml                    agent 配置示例
references/authoring-workflow.md      长文转 PPT 的流程
references/template-selection.md      模板和风格选择规则
references/style-system.md            上交风格视觉系统
references/data-visualization.md      数据处理与 Nature-like 科研图表流程
references/diagram-workflow.md        可编辑流程图和结构图流程
references/visual-qa.md               渲染预览、遮挡、对比度和清晰度检查
references/web-content-acquisition.md 公开网页图文采集和来源记录
references/office-compatibility.md    本地 PowerPoint/WPS/LibreOffice 打开检查
references/quality-gates.md           交付前检查清单
references/revision-safety.md         非覆盖式修订、版本命名和图片习惯记录
references/bundled-assets.md          内置校标、模板和字体清单
references/speaker-notes.md           演讲者备注生成、插入、同步与锁定规则
scripts/create_workspace.py           创建本地任务工作区
scripts/plot_style.py                 PPT 科研图表样式助手
scripts/web_collect.py                公开网页图文采集助手
scripts/office_bridge.ps1             本地 Office/WPS PPTX 检查和另存助手
assets/logos/                         内置校标 PNG
assets/templates/                     内置 PPTX 模板
assets/fonts/                         可选字体包
ASSET_NOTICE.md                       内置素材使用提醒
```

## 免责声明

本项目为个人整理的 Codex skill，用于学习和效率工具分享。请遵守学校视觉识别规范、版权要求和你所在单位的材料使用规定。
