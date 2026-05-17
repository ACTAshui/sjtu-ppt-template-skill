# Bundled Assets

This skill includes user-provided local assets under `assets/` so users can create SJTU-style decks without separately collecting logos or templates.

## Logos

Folder: `assets/logos/sjtu/`

- `校标-中文横版.png`
- `校标-中文竖版.png`
- `校标-标志中英文上下组合.png`
- `校标-标志中英文横版.png`
- `校标-标志中英文竖版.png`
- `校标-标志英文横版.png`
- `校标-校徽.png`
- `校标-英文横版 (2).png`
- `校标-英文横版.png`
- `校标-英文竖版.png`

## PPT Templates

Folder: `assets/templates/sjtu-civilization-office/`

- `1.百廿红-李一.pptx`
- `2.简单蓝-沈小丹/简单蓝（16：9）-沈小丹.pptx`
- `2.简单蓝-沈小丹/简单蓝（4：3）-沈小丹.pptx`
- `3.天空之境-潘冬远、张娉.pptx`
- `4.深海金芒-许歆瑶.pptx`
- `5.浩瀚星河-迮佳.pptx`
- `6.鎏金岁月-陈玥彤.pptx`
- `7.诗意校园-徐臻/1.诗意校园-2023酒红醉人（极速版）.pptx`
- `7.诗意校园-徐臻/2.诗意校园-2022蓝绿青春（徐臻）.pptx`
- `7.诗意校园-徐臻/3.诗意校园-2023赤霞银珠（极速版）.pptx`
- `7.诗意校园-徐臻/4.诗意校园-2023暗夜奔驰（极速版）.pptx`

## Fonts

Folder: `assets/fonts/`

- `HarmonyOS_Sans_SC.zip`

## How The Skill Uses Them

When `scripts/create_workspace.py` is run, bundled logos, templates, and fonts are copied into the new task workspace by default. Existing files in the workspace are not overwritten.

Use `--no-bundled-assets` when you want an empty workspace and will provide your own assets.
