#!/usr/bin/env python3
"""Create a clean local workspace for an SJTU-style presentation task."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
BUNDLED_ASSETS = SKILL_DIR / "assets"

PROFILES = [
    "academic-report",
    "thesis-defense",
    "course-presentation",
    "group-meeting",
    "student-activity",
    "admin-briefing",
]


def copy_tree_contents(src: Path, dst: Path) -> list[str]:
    copied: list[str] = []
    if not src.exists():
        return copied
    dst.mkdir(parents=True, exist_ok=True)
    for item in src.rglob("*"):
        if item.is_dir():
            continue
        rel = item.relative_to(src)
        if item.name == ".gitkeep":
            continue
        target = dst / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            continue
        shutil.copy2(item, target)
        copied.append(str(target.relative_to(dst)))
    return copied


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", type=Path)
    parser.add_argument("--profile", choices=PROFILES, default="academic-report")
    parser.add_argument("--language", choices=["zh", "en", "bilingual"], default="zh")
    parser.add_argument("--slides", type=int, default=9)
    parser.add_argument(
        "--no-bundled-assets",
        action="store_true",
        help="Do not copy bundled logos, templates, or fonts into the workspace.",
    )
    args = parser.parse_args()

    workspace = args.workspace.resolve()
    dirs = [
        "source",
        "data/raw",
        "data/processed",
        "assets/logos",
        "assets/templates",
        "assets/fonts",
        "assets/images",
        "figures",
        "figures/_shared",
        "planning",
        "output/private",
        "output/previews",
        "output/versions",
    ]
    for folder in dirs:
        (workspace / folder).mkdir(parents=True, exist_ok=True)

    manifest = {
        "profile": args.profile,
        "language": args.language,
        "planned_slides": args.slides,
        "source_dir": "source",
        "raw_data_dir": "data/raw",
        "processed_data_dir": "data/processed",
        "logo_dir": "assets/logos",
        "template_dir": "assets/templates",
        "font_dir": "assets/fonts",
        "figure_dir": "figures",
        "private_output_dir": "output/private",
        "preview_output_dir": "output/previews",
        "version_output_dir": "output/versions",
        "revision_log": "planning/revision-log.md",
        "image_preferences": "planning/image-preferences.md",
        "image_inventory": "planning/image-inventory.json",
        "figure_plan": "planning/figure-plan.md",
        "bundled_assets_dir": "assets",
        "bundled_assets_copied": not args.no_bundled_assets,
        "notes": [
            "Bundled logos, templates, and fonts are copied into assets/ by default when present.",
            "Place additional authorized logos and PPT templates in assets/.",
            "Place raw CSV, Excel, or statistical data in data/raw/.",
            "Keep private source files inside the task workspace, not inside the skill folder.",
            "Never overwrite user-provided or previously delivered PPTX files; write revisions to output/versions/.",
            "For generated charts, keep plotting code, data, source notes, and outputs under figures/.",
        ],
    }
    revision_log = workspace / "planning" / "revision-log.md"
    if not revision_log.exists():
        revision_log.write_text(
            "# Revision Log\n\nRecord every PPTX update here. Each revision should name the base file, new file, user request, preserved user edits, and image habit updates.\n",
            encoding="utf-8",
        )
    image_preferences = workspace / "planning" / "image-preferences.md"
    if not image_preferences.exists():
        image_preferences.write_text(
            "# Image Preferences\n\nRecord user image habits here: source type, crop style, placement, caption style, tone, and repeated preferences.\n",
            encoding="utf-8",
        )
    image_inventory = workspace / "planning" / "image-inventory.json"
    if not image_inventory.exists():
        image_inventory.write_text(
            json.dumps({"images": []}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    figure_plan = workspace / "planning" / "figure-plan.md"
    if not figure_plan.exists():
        figure_plan.write_text(
            "# Figure Plan\n\nRecord chart claims, data sources, chart types, output paths, and whether each chart is native PPT or externally generated.\n",
            encoding="utf-8",
        )
    shared_readme = workspace / "figures" / "_shared" / "README.md"
    if not shared_readme.exists():
        shared_readme.write_text(
            "# Figure Workflow\n\nCreate one folder per important chart with code/, data/, outputs/, sources/, and README.md. Keep generated charts reproducible.\n",
            encoding="utf-8",
        )
    copied_assets: dict[str, list[str]] = {"logos": [], "templates": [], "fonts": []}
    if not args.no_bundled_assets:
        copied_assets["logos"] = copy_tree_contents(BUNDLED_ASSETS / "logos", workspace / "assets" / "logos")
        copied_assets["templates"] = copy_tree_contents(
            BUNDLED_ASSETS / "templates", workspace / "assets" / "templates"
        )
        copied_assets["fonts"] = copy_tree_contents(BUNDLED_ASSETS / "fonts", workspace / "assets" / "fonts")
        manifest["copied_bundled_assets"] = copied_assets
    (workspace / "sjtu_ppt_task.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps({"workspace": str(workspace), **manifest}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
