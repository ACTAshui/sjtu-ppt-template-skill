#!/usr/bin/env python3
"""Collect public web text and image candidates for an SJTU PPT workspace."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import mimetypes
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path


DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (compatible; sjtu-ppt-template-skill/0.1; "
    "+https://github.com/ACTAshui/sjtu-ppt-template-skill)"
)


def slugify(value: str, fallback: str = "page") -> str:
    value = urllib.parse.urlparse(value).netloc + urllib.parse.urlparse(value).path
    value = re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-._")
    return value[:80] or fallback


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self._tag_stack: list[str] = []
        self._buffer: list[str] = []
        self._current: str | None = None
        self.headings: list[dict[str, str]] = []
        self.paragraphs: list[str] = []
        self.images: list[dict[str, str]] = []
        self.links: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {k.lower(): v or "" for k, v in attrs}
        tag = tag.lower()
        self._tag_stack.append(tag)
        if tag in {"title", "h1", "h2", "h3", "p", "li", "a"}:
            self._current = tag
            self._buffer = []
        if tag == "img":
            src = attrs_dict.get("src", "")
            if src and not src.startswith("data:"):
                self.images.append(
                    {
                        "src": src,
                        "alt": normalize_text(attrs_dict.get("alt", "")),
                        "title": normalize_text(attrs_dict.get("title", "")),
                    }
                )

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if self._current == tag:
            text = normalize_text("".join(self._buffer))
            if text:
                if tag == "title" and not self.title:
                    self.title = text
                elif tag in {"h1", "h2", "h3"}:
                    self.headings.append({"level": tag, "text": text})
                elif tag in {"p", "li"}:
                    self.paragraphs.append(text)
                elif tag == "a":
                    self.links.append({"text": text})
            self._current = None
            self._buffer = []
        if self._tag_stack:
            self._tag_stack.pop()

    def handle_data(self, data: str) -> None:
        if self._current:
            self._buffer.append(data)


def fetch(url: str, user_agent: str, timeout: int = 30) -> tuple[bytes, str]:
    request = urllib.request.Request(url, headers={"User-Agent": user_agent})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        content_type = response.headers.get("Content-Type", "")
        return response.read(), content_type


def decode_html(body: bytes, content_type: str) -> str:
    charset_match = re.search(r"charset=([\w.-]+)", content_type, flags=re.I)
    encodings = [charset_match.group(1)] if charset_match else []
    encodings += ["utf-8", "gb18030", "latin-1"]
    for encoding in encodings:
        try:
            return body.decode(encoding)
        except UnicodeDecodeError:
            continue
    return body.decode("utf-8", errors="replace")


def choose_extension(url: str, content_type: str, default: str = ".bin") -> str:
    path_ext = Path(urllib.parse.urlparse(url).path).suffix
    if path_ext and len(path_ext) <= 8:
        return path_ext
    guessed = mimetypes.guess_extension(content_type.split(";")[0].strip())
    return guessed or default


def download_image(url: str, dest_dir: Path, user_agent: str, index: int) -> dict[str, str]:
    body, content_type = fetch(url, user_agent)
    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:10]
    ext = choose_extension(url, content_type, ".img")
    filename = f"web-image-{index:02d}-{digest}{ext}"
    target = dest_dir / filename
    target.write_bytes(body)
    return {
        "url": url,
        "local_path": str(target),
        "content_type": content_type,
        "bytes": str(len(body)),
    }


def load_manifest(path: Path) -> dict:
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {"sources": []}


def append_markdown(path: Path, record: dict) -> None:
    lines = [
        "",
        f"## {record.get('title') or record['url']}",
        "",
        f"- URL: {record['url']}",
        f"- Accessed: {record['accessed_at']}",
        f"- Saved page: `{record['saved_page']}`",
        f"- Usage decision: review before slide insertion",
        "",
        "### Headings",
        "",
    ]
    for heading in record.get("headings", [])[:12]:
        lines.append(f"- {heading['level']}: {heading['text']}")
    lines += ["", "### Text Snippets", ""]
    for paragraph in record.get("paragraphs", [])[:20]:
        lines.append(f"- {paragraph}")
    lines += ["", "### Image Candidates", ""]
    for image in record.get("images", [])[:20]:
        local = image.get("local_path", "")
        local_part = f" -> `{local}`" if local else ""
        alt = f" | alt: {image.get('alt')}" if image.get("alt") else ""
        lines.append(f"- {image['url']}{local_part}{alt}")
    path.write_text(path.read_text(encoding="utf-8") + "\n".join(lines) + "\n", encoding="utf-8")


def collect_url(args: argparse.Namespace, workspace: Path, url: str, index: int) -> dict:
    web_dir = workspace / "assets" / "web"
    page_dir = web_dir / "pages"
    image_dir = web_dir / "images"
    page_dir.mkdir(parents=True, exist_ok=True)
    image_dir.mkdir(parents=True, exist_ok=True)

    body, content_type = fetch(url, args.user_agent, args.timeout)
    text = decode_html(body, content_type)
    parser = PageParser()
    parser.feed(text)

    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    slug = slugify(url, f"source-{index:02d}")
    page_name = f"{timestamp}-{index:02d}-{slug}.html"
    page_path = page_dir / page_name
    page_path.write_text(text, encoding="utf-8", errors="replace")

    images = []
    for img in parser.images:
        absolute = urllib.parse.urljoin(url, img["src"])
        item = {"url": absolute, "alt": img.get("alt", ""), "title": img.get("title", "")}
        if args.download_images and len(images) < args.max_images:
            try:
                item.update(download_image(absolute, image_dir, args.user_agent, len(images) + 1))
            except (urllib.error.URLError, TimeoutError, OSError) as exc:
                item["download_error"] = str(exc)
        images.append(item)
        if len(images) >= args.max_images and not args.list_all_images:
            break

    return {
        "url": url,
        "accessed_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
        "content_type": content_type,
        "title": parser.title,
        "saved_page": str(page_path),
        "headings": parser.headings[: args.max_text],
        "paragraphs": parser.paragraphs[: args.max_text],
        "images": images,
        "usage_note": "Review copyright, source authority, and deck use case before inserting into slides.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", type=Path, help="Task workspace created by create_workspace.py")
    parser.add_argument("urls", nargs="+", help="Public page URLs to collect")
    parser.add_argument("--download-images", action="store_true", help="Download image candidates")
    parser.add_argument("--list-all-images", action="store_true", help="Keep all image URLs in the manifest")
    parser.add_argument("--max-images", type=int, default=12)
    parser.add_argument("--max-text", type=int, default=80)
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument("--user-agent", default=DEFAULT_USER_AGENT)
    args = parser.parse_args()

    workspace = args.workspace.resolve()
    (workspace / "planning").mkdir(parents=True, exist_ok=True)
    (workspace / "assets" / "web").mkdir(parents=True, exist_ok=True)
    markdown_path = workspace / "planning" / "web-sources.md"
    manifest_path = workspace / "assets" / "web" / "sources.json"
    if not markdown_path.exists():
        markdown_path.write_text("# Web Sources\n\n", encoding="utf-8")

    manifest = load_manifest(manifest_path)
    for index, url in enumerate(args.urls, start=1):
        try:
            record = collect_url(args, workspace, url, index)
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            print(json.dumps({"url": url, "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
            continue
        manifest.setdefault("sources", []).append(record)
        append_markdown(markdown_path, record)
        print(json.dumps({"url": url, "title": record.get("title"), "images": len(record["images"])}, ensure_ascii=False))

    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
