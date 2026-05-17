# SJTU PPT Template Skill

一个给 Codex 使用的上海交通大学风格 PPT 生成 skill。它的目标不是简单套背景，而是帮助 Codex 先理解材料，再按汇报场景选择合适的上交风格，生成可继续编辑的 PowerPoint。

> 个人公开项目，非上海交通大学官方发布。本仓库只包含工作流和提示规则，不包含官方校标、官方模板、私有文档或受版权保护的素材。请使用你自己有权限的校标与 PPT 模板。

## 它适合做什么

- 课程汇报、读书报告、综述展示
- 组会汇报、课题组进展、项目总结
- 本科/硕士/博士答辩初稿
- 学术讲座、学院/实验室介绍
- 学生活动、招生宣传、校园文化展示

这个 skill 会引导 Codex 做这些事：

- 从长文本、提纲、DOCX、PDF 笔记或已有 PPT 中提炼主线。
- 把“文章逻辑”改写成“演示逻辑”。
- 根据场景选择正式答辩、学术组会、课程展示、宣传路演等视觉风格。
- 使用你本地提供的授权校标和 PPT 模板。
- 生成可编辑的 `.pptx`，而不是整页截图。
- 在交付前渲染预览，检查中文换行、版式、logo、页脚和内容溢出。

## 一句话安装

如果你已经在使用 Codex，可以直接把下面这句话发给 Codex：

```text
请帮我从网上获取 https://github.com/ACTAshui/sjtu-ppt-template-skill 这个 skill，并安装到本地。之后当我需要做上海交通大学风格 PPT 时，请优先调用它：先理解我的材料，再根据课程汇报、学术组会、答辩、讲座或宣传展示等场景，选择合适的风格和模板，生成一份可编辑的 PPTX。
```

## 手动安装

如果你想自己安装：

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
  agents/
  assets/
  references/
  scripts/
```

4. 重新打开 Codex，或者开始一个新任务，让 Codex 能发现这个 skill。

## 准备你的本地素材

这个仓库不会内置学校官方素材，所以你需要在自己的任务工作区里放入有权限使用的文件。

可以让 Codex 先创建一个工作区：

```bash
python scripts/create_workspace.py ./my-sjtu-deck --profile academic-report
```

然后把文件放进去：

```text
my-sjtu-deck/
  source/              放 DOCX、PDF、Markdown、提纲或已有 PPT
  assets/logos/        放你有权限使用的校标、院系标识
  assets/templates/    放你有权限使用的 PPTX 模板
  output/              生成后的 PPTX 和预览图
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

也可以更明确一点：

```text
请使用 sjtu-ppt-template skill，做一份博士开题汇报风格的 PPT。希望整体偏深蓝金色、正式、学术，不要太花哨。请保留图表和文字可编辑。
```

## 推荐给 Codex 的信息

为了让效果更稳定，最好同时告诉 Codex：

- 这份 PPT 的用途：课程汇报、组会、答辩、讲座、宣传展示等。
- 听众是谁：老师、同学、评审专家、课题组、公众等。
- 期望页数：例如 6 页、10 页、15 页。
- 风格偏好：正式、清爽、学术、宣传感、校园文化感等。
- 是否必须使用某个模板或 logo。
- 是否需要图表、时间线、机制图、对比矩阵、总结页。

## 工作流简述

skill 会要求 Codex 按这个顺序处理：

1. 阅读材料，确认主题、用途、听众和页数。
2. 提炼每页一句话的 claim spine，也就是演示主线。
3. 为每页选择合适的表达方式：标题页、章节页、流程图、矩阵、时间线、图表页、总结页等。
4. 按场景选择上交视觉风格。
5. 使用本地授权模板和 logo 生成可编辑 PPT。
6. 渲染预览图，检查中文排版、内容溢出和整体一致性。
7. 修正问题后再交付最终 `.pptx`。

## 常见问题

### 这个 skill 里有上海交通大学官方 PPT 模板吗？

没有。本仓库只提供工作流和设计规则。官方校标、模板、院系标识、活动素材等请使用你自己有权限的本地文件。

### 生成的 PPT 是可编辑的吗？

目标是生成可编辑 `.pptx`：标题、正文、形状、表格、图表、页码等都应尽量保持为 PowerPoint 原生对象。除非用户明确要求，否则不要把整页做成一张图片。

### 我只有 Word 文档，可以用吗？

可以。把 Word 文档放进工作区的 `source/` 目录，然后告诉 Codex 使用这个 skill 制作 PPT。它会先把长文改写成适合演示的结构。

### 我没有模板怎么办？

也可以做。没有模板时，skill 会使用上交红、蓝、金等视觉系统作为默认方向。但如果你提供授权 PPT 模板，通常更容易贴近你想要的正式效果。

### 为什么要先渲染预览？

因为中文 PPT 很容易出现换行、遮挡、页脚错位、logo 模糊、图表太小等问题。这个 skill 要求 Codex 在交付前渲染检查，发现问题后修正源文件再导出。

## 仓库结构

```text
SKILL.md                         skill 入口说明
README.md                        给使用者看的说明
agents/openai.yaml               agent 配置示例
references/authoring-workflow.md 长文转 PPT 的流程
references/template-selection.md 模板和风格选择规则
references/style-system.md       上交风格视觉系统
references/quality-gates.md      交付前检查清单
scripts/create_workspace.py      创建本地任务工作区
assets/.gitkeep                  素材占位，不放官方或私有素材
```

## 免责声明

本项目为个人整理的 Codex skill，用于学习和效率工具分享。请遵守学校视觉识别规范、版权要求和你所在单位的材料使用规定。
