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
        "notes": [
            "Place authorized logos and PPT templates in assets/.",
            "Keep private source files inside the task workspace, not inside the skill folder.",
        ],
    }
    (workspace / "sjtu_ppt_task.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps({"workspace": str(workspace), **manifest}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

