#!/usr/bin/env python3
"""Create a clean local workspace for an SJTU-style presentation task."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


PROFILES = [
    "academic-report",
    "thesis-defense",
    "course-presentation",
    "group-meeting",
    "student-activity",
    "admin-briefing",
]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", type=Path)
    parser.add_argument("--profile", choices=PROFILES, default="academic-report")
    parser.add_argument("--language", choices=["zh", "en", "bilingual"], default="zh")
    parser.add_argument("--slides", type=int, default=9)
    args = parser.parse_args()

    workspace = args.workspace.resolve()
    dirs = [
        "source",
        "assets/logos",
        "assets/templates",
        "assets/images",
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
        "logo_dir": "assets/logos",
        "template_dir": "assets/templates",
        "private_output_dir": "output/private",
        "preview_output_dir": "output/previews",
        "version_output_dir": "output/versions",
        "revision_log": "planning/revision-log.md",
        "image_preferences": "planning/image-preferences.md",
        "image_inventory": "planning/image-inventory.json",
        "notes": [
            "Place authorized logos and PPT templates in assets/.",
            "Keep private source files inside the task workspace, not inside the skill folder.",
            "Never overwrite user-provided or previously delivered PPTX files; write revisions to output/versions/.",
        ],
    }
    (workspace / "sjtu_ppt_task.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
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
    print(json.dumps({"workspace": str(workspace), **manifest}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
