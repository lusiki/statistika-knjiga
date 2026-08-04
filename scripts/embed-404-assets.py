"""Embed local assets in the rendered 404 page.

Quarto intentionally roots resources in 404.html at the production site path.
That is correct for a deployed project site, but leaves the page unstyled when
the same build is inspected from a local document root. A self-contained 404
works in both places and at every missing-URL depth.
"""

from __future__ import annotations

import base64
import mimetypes
import os
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

sys.dont_write_bytecode = True

from book_inventory import load_inventory

MARKER = "<!-- local assets embedded for portable 404 -->"
URL_IN_CSS = re.compile(r"url\(\s*([\"']?)([^\"')]+)\1\s*\)")
MODULE_REF = re.compile(
    r"""(?P<prefix>\b(?:from\s*|import\s*)["'])(?P<url>\.[^"']+)(?P<suffix>["'])"""
)


def data_uri(payload: bytes, mime: str) -> str:
    encoded = base64.b64encode(payload).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def local_path(url: str, output_dir: Path, relative_to: Path | None = None) -> Path | None:
    parts = urlsplit(url)
    if parts.scheme or parts.netloc or url.startswith(("#", "data:")):
        return None

    raw_path = unquote(parts.path).replace("\\", "/")
    if relative_to is not None and not raw_path.startswith("/"):
        candidate = (relative_to / raw_path).resolve()
    else:
        trimmed = raw_path.lstrip("/")
        candidates = [trimmed]
        # The deployed site is a GitHub Pages project path. Strip that first
        # segment only when the direct output-relative candidate does not exist.
        if "/" in trimmed:
            candidates.append(trimmed.split("/", 1)[1])
        candidate = next(
            (
                (output_dir / item).resolve()
                for item in candidates
                if (output_dir / item).is_file()
            ),
            (output_dir / trimmed).resolve(),
        )

    try:
        candidate.relative_to(output_dir.resolve())
    except ValueError:
        return None
    return candidate if candidate.is_file() else None


def mime_for(path: Path) -> str:
    overrides = {
        ".js": "text/javascript",
        ".css": "text/css",
        ".woff": "font/woff",
        ".woff2": "font/woff2",
        ".svg": "image/svg+xml",
    }
    return overrides.get(path.suffix.lower()) or mimetypes.guess_type(path.name)[0] or (
        "application/octet-stream"
    )


def embed_css(path: Path, output_dir: Path) -> bytes:
    css = path.read_text(encoding="utf-8")

    def replace_url(match: re.Match[str]) -> str:
        value = match.group(2).strip()
        asset = local_path(value, output_dir, path.parent)
        if asset is None:
            return match.group(0)
        return f'url("{data_uri(asset.read_bytes(), mime_for(asset))}")'

    return URL_IN_CSS.sub(replace_url, css).encode("utf-8")


def embed_module(path: Path, output_dir: Path, seen: frozenset[Path] = frozenset()) -> bytes:
    resolved = path.resolve()
    if resolved in seen:
        return path.read_bytes()
    source = path.read_text(encoding="utf-8")
    nested_seen = seen | {resolved}

    def replace_module(match: re.Match[str]) -> str:
        module = local_path(match.group("url"), output_dir, path.parent)
        if module is None:
            return match.group(0)
        payload = embed_module(module, output_dir, nested_seen)
        uri = data_uri(payload, "text/javascript")
        return f'{match.group("prefix")}{uri}{match.group("suffix")}'

    return MODULE_REF.sub(replace_module, source).encode("utf-8")


def embed_html_assets(html: str, output_dir: Path) -> str:
    tag_pattern = re.compile(r"<(?P<tag>script|link)\b(?P<attrs>[^>]*)>", re.I)
    attr_pattern = re.compile(
        r"""(?P<name>src|href)\s*=\s*(?P<quote>["'])(?P<url>[^"']+)(?P=quote)""",
        re.I,
    )

    def replace_tag(match: re.Match[str]) -> str:
        tag = match.group("tag").lower()
        attrs = match.group("attrs")
        attr = attr_pattern.search(attrs)
        if attr is None:
            return match.group(0)
        if tag == "link" and attr.group("name").lower() != "href":
            return match.group(0)

        asset = local_path(attr.group("url"), output_dir)
        if asset is None:
            return match.group(0)
        suffix = asset.suffix.lower()
        if tag == "script" and suffix != ".js":
            return match.group(0)
        if tag == "link" and suffix != ".css":
            return match.group(0)

        if suffix == ".css":
            payload = embed_css(asset, output_dir)
        elif re.search(r"""\btype\s*=\s*["']module["']""", attrs, re.I):
            payload = embed_module(asset, output_dir)
        else:
            payload = asset.read_bytes()
        uri = data_uri(payload, mime_for(asset))
        start, end = attr.span("url")
        new_attrs = attrs[:start] + uri + attrs[end:]
        return f"<{match.group('tag')}{new_attrs}>"

    return tag_pattern.sub(replace_tag, html)


def main() -> None:
    project_dir = Path(os.environ.get("QUARTO_PROJECT_DIR", Path.cwd())).resolve()
    inventory = load_inventory(project_dir)
    output_env = os.environ.get("QUARTO_PROJECT_OUTPUT_DIR")
    output_dir = (
        Path(output_env).resolve()
        if output_env
        else (project_dir / "docs").resolve()
    )
    portable_pages = [item for item in inventory["pages"] if item.get("portable_assets")]
    if not portable_pages:
        print("Portable pages: nema konfiguriranih putova")
        return
    for item in portable_pages:
        page = output_dir / Path(item["output"])
        if not page.is_file():
            print(f"Portable page: preskočeno ({page} ne postoji)")
            continue

        html = page.read_text(encoding="utf-8")
        if MARKER in html:
            print(f"Portable page: lokalni resursi već su ugrađeni ({page})")
            continue

        embedded = embed_html_assets(html, output_dir)
        embedded = embedded.replace("<head>", f"<head>\n{MARKER}", 1)
        page.write_text(embedded, encoding="utf-8", newline="\n")
        print(f"Portable page: ugrađeni lokalni resursi u {page}")


if __name__ == "__main__":
    main()
