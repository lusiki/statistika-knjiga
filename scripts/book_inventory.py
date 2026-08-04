"""Load, validate, and project the sanctioned book/page inventory."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath
from typing import Any, Iterable


INVENTORY_PATH = Path("config/book-inventory.json")
MARKERS = {
    "navbar": (
        "  # BEGIN GENERATED: book-inventory navbar",
        "  # END GENERATED: book-inventory navbar",
    ),
    "footer": (
        "    # BEGIN GENERATED: book-inventory footer",
        "    # END GENERATED: book-inventory footer",
    ),
    "sidebar_tools": (
        "    # BEGIN GENERATED: book-inventory sidebar-tools",
        "    # END GENERATED: book-inventory sidebar-tools",
    ),
    "book_structure": (
        "  # BEGIN GENERATED: book-inventory structure",
        "  # END GENERATED: book-inventory structure",
    ),
    "runtime_routes": (
        "  // BEGIN GENERATED: book-inventory runtime-routes",
        "  // END GENERATED: book-inventory runtime-routes",
    ),
}


class InventoryError(ValueError):
    """Raised when a sanctioned inventory or one of its projections drifts."""


def _string(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise InventoryError(f"{field} must be a non-empty string")
    return value.strip()


def _list(value: Any, field: str) -> list[Any]:
    if not isinstance(value, list):
        raise InventoryError(f"{field} must be an array")
    return value


def _relative_path(value: Any, field: str, suffix: str | None = None) -> str:
    path = _string(value, field).replace("\\", "/")
    pure = PurePosixPath(path)
    if pure.is_absolute() or ".." in pure.parts or path.startswith("./"):
        raise InventoryError(f"{field} must be a normalized project-relative path")
    if suffix and pure.suffix != suffix:
        raise InventoryError(f"{field} must end in {suffix}")
    return path


def page_map(inventory: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {page["id"]: page for page in inventory["pages"]}


def asset_map(inventory: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {asset["id"]: asset for asset in inventory["public_assets"]}


def chapter_page_ids(inventory: dict[str, Any]) -> list[str]:
    ids: list[str] = []
    for index, entry in enumerate(inventory["book"]["chapters"]):
        if not isinstance(entry, dict):
            raise InventoryError(f"book.chapters[{index}] must be an object")
        if "page" in entry:
            ids.append(_string(entry["page"], f"book.chapters[{index}].page"))
        elif "part" in entry:
            _string(entry["part"], f"book.chapters[{index}].part")
            ids.extend(
                _string(value, f"book.chapters[{index}].pages")
                for value in _list(entry.get("pages"), f"book.chapters[{index}].pages")
            )
        else:
            raise InventoryError(f"book.chapters[{index}] needs page or part")
    return ids


def chapter_pages(inventory: dict[str, Any], include_landing: bool = True) -> list[dict[str, Any]]:
    pages = page_map(inventory)
    selected = [pages[page_id] for page_id in chapter_page_ids(inventory)]
    return selected if include_landing else [page for page in selected if page["kind"] != "landing"]


def appendix_pages(inventory: dict[str, Any]) -> list[dict[str, Any]]:
    pages = page_map(inventory)
    return [pages[page_id] for page_id in inventory["book"]["appendices"]]


def solution_pages(inventory: dict[str, Any]) -> list[dict[str, Any]]:
    pages = page_map(inventory)
    return [pages[page_id] for page_id in inventory["solution_routes"]]


def all_page_sources(inventory: dict[str, Any]) -> list[str]:
    return [page["source"] for page in inventory["pages"]]


def public_routes(inventory: dict[str, Any], include_root_alias: bool = False) -> list[tuple[str, str]]:
    routes = [(f"/{page['output']}", page["audit_label"]) for page in inventory["pages"]]
    if include_root_alias:
        routes = [
            (alias["path"], alias["audit_label"])
            for alias in inventory["public_aliases"]
        ] + routes
    return routes


def _validate_unique(values: Iterable[str], label: str) -> None:
    items = list(values)
    duplicates = sorted({value for value in items if items.count(value) > 1})
    if duplicates:
        raise InventoryError(f"duplicate {label}: {duplicates}")


def _nav_entries(inventory: dict[str, Any]) -> Iterable[dict[str, Any]]:
    for entry in inventory["navigation"]["navbar"]:
        yield entry
        for child in entry.get("menu", []):
            yield child
    yield from inventory["navigation"]["footer"]


def validate_inventory(inventory: dict[str, Any], root: Path) -> None:
    if not isinstance(inventory, dict):
        raise InventoryError("inventory root must be an object")
    if inventory.get("schema_version") != 1:
        raise InventoryError("schema_version must be 1")
    if inventory.get("inventory") != "sanctioned-book-pages-and-routes":
        raise InventoryError("inventory identity is not sanctioned-book-pages-and-routes")

    pages = _list(inventory.get("pages"), "pages")
    allowed_kinds = {"landing", "preface", "chapter", "references", "appendix", "standalone", "solution"}
    for index, page in enumerate(pages):
        if not isinstance(page, dict):
            raise InventoryError(f"pages[{index}] must be an object")
        page["id"] = _string(page.get("id"), f"pages[{index}].id")
        page["source"] = _relative_path(page.get("source"), f"pages[{index}].source", ".qmd")
        page["output"] = _relative_path(page.get("output"), f"pages[{index}].output", ".html")
        page["audit_label"] = _string(page.get("audit_label"), f"pages[{index}].audit_label")
        page["kind"] = _string(page.get("kind"), f"pages[{index}].kind")
        if page["kind"] not in allowed_kinds:
            raise InventoryError(f"pages[{index}].kind is unsupported: {page['kind']}")
        expected_output = str(PurePosixPath(page["source"]).with_suffix(".html"))
        if page["output"] != expected_output:
            raise InventoryError(
                f"{page['id']} output must derive from its source: {expected_output}"
            )
        if not isinstance(page.get("standalone"), bool):
            raise InventoryError(f"{page['id']} standalone must be boolean")
        _string(page.get("render_via"), f"{page['id']}.render_via")
        if not (root / Path(page["source"])).is_file():
            raise InventoryError(f"sanctioned page source is missing: {page['source']}")

    _validate_unique((page["id"] for page in pages), "page id")
    _validate_unique((page["source"] for page in pages), "page source")
    _validate_unique((page["output"] for page in pages), "page output")
    _validate_unique((page["audit_label"] for page in pages), "audit label")
    pages_by_id = page_map(inventory)

    book = inventory.get("book")
    if not isinstance(book, dict):
        raise InventoryError("book must be an object")
    chapter_ids = chapter_page_ids(inventory)
    appendix_ids = [
        _string(value, "book.appendices")
        for value in _list(book.get("appendices"), "book.appendices")
    ]
    book["appendices"] = appendix_ids
    references_id = _string(book.get("references"), "book.references")
    standalone_ids = [
        _string(value, "standalone_pages")
        for value in _list(inventory.get("standalone_pages"), "standalone_pages")
    ]
    solution_ids = [
        _string(value, "solution_routes")
        for value in _list(inventory.get("solution_routes"), "solution_routes")
    ]
    inventory["standalone_pages"] = standalone_ids
    inventory["solution_routes"] = solution_ids
    role_ids = chapter_ids + [references_id] + appendix_ids + standalone_ids + solution_ids
    unknown_roles = sorted(set(role_ids) - pages_by_id.keys())
    if unknown_roles:
        raise InventoryError(f"inventory roles reference unknown pages: {unknown_roles}")
    _validate_unique(role_ids, "page role assignment")
    if set(role_ids) != set(pages_by_id):
        missing = sorted(set(pages_by_id) - set(role_ids))
        raise InventoryError(f"every sanctioned page must be assigned exactly once; missing={missing}")

    if pages_by_id[chapter_ids[0]]["kind"] != "landing" or pages_by_id[chapter_ids[1]]["kind"] != "preface":
        raise InventoryError("book order must begin with landing and preface")
    numbered = [pages_by_id[page_id].get("chapter_number") for page_id in chapter_ids]
    numbered = [number for number in numbered if number is not None]
    if numbered != list(range(1, 19)):
        raise InventoryError(f"numbered chapters must preserve the 1-18 sequence: {numbered}")
    if pages_by_id[references_id]["kind"] != "references":
        raise InventoryError("book.references must identify the references page")

    appendix_letters = []
    for page_id in appendix_ids:
        page = pages_by_id[page_id]
        if page["kind"] != "appendix":
            raise InventoryError(f"book.appendices contains non-appendix page: {page_id}")
        appendix_letters.append(_string(page.get("appendix_letter"), f"{page_id}.appendix_letter"))
    expected_letters = [chr(ord("A") + index) for index in range(len(appendix_letters))]
    if appendix_letters != expected_letters:
        raise InventoryError(
            f"appendices must be contiguous and ordered from A: {appendix_letters}"
        )
    for page_id in solution_ids:
        if pages_by_id[page_id]["kind"] != "solution":
            raise InventoryError(f"solution_routes contains non-solution page: {page_id}")

    aliases = _list(inventory.get("public_aliases"), "public_aliases")
    for index, alias in enumerate(aliases):
        if not isinstance(alias, dict):
            raise InventoryError(f"public_aliases[{index}] must be an object")
        route = _string(alias.get("path"), f"public_aliases[{index}].path")
        if not route.startswith("/") or ".." in PurePosixPath(route).parts:
            raise InventoryError(f"public_aliases[{index}].path must be a root-relative route")
        alias["path"] = route
        page_id = _string(alias.get("page"), f"public_aliases[{index}].page")
        if page_id not in pages_by_id:
            raise InventoryError(f"public alias references unknown page: {page_id}")
        alias["page"] = page_id
        alias["audit_label"] = _string(
            alias.get("audit_label"), f"public_aliases[{index}].audit_label"
        )
    _validate_unique((alias["path"] for alias in aliases), "public alias path")
    _validate_unique((alias["audit_label"] for alias in aliases), "public alias audit label")

    assets = _list(inventory.get("public_assets"), "public_assets")
    for index, asset in enumerate(assets):
        if not isinstance(asset, dict):
            raise InventoryError(f"public_assets[{index}] must be an object")
        asset["id"] = _string(asset.get("id"), f"public_assets[{index}].id")
        asset["output"] = _relative_path(asset.get("output"), f"public_assets[{index}].output")
        asset["producer"] = _relative_path(asset.get("producer"), f"public_assets[{index}].producer")
        if not (root / Path(asset["producer"])).is_file():
            raise InventoryError(f"public asset producer is missing: {asset['producer']}")
    _validate_unique((asset["id"] for asset in assets), "public asset id")
    _validate_unique((asset["output"] for asset in assets), "public asset output")
    assets_by_id = asset_map(inventory)

    navigation = inventory.get("navigation")
    if not isinstance(navigation, dict):
        raise InventoryError("navigation must be an object")
    for field in ("navbar", "footer", "sidebar_tools"):
        _list(navigation.get(field), f"navigation.{field}")
    for index, entry in enumerate(_nav_entries(inventory)):
        if not isinstance(entry, dict):
            raise InventoryError(f"navigation entry {index} must be an object")
        _string(entry.get("text"), f"navigation entry {index}.text")
        if "page" in entry:
            page_id = _string(entry["page"], f"navigation entry {index}.page")
            if page_id not in pages_by_id:
                raise InventoryError(f"navigation references unknown page: {page_id}")
            if entry.get("href", "output") not in ("source", "output"):
                raise InventoryError(f"navigation entry {index}.href must be source or output")
        elif "menu" not in entry:
            raise InventoryError(f"navigation entry {index} needs page or menu")
    for index, entry in enumerate(navigation["navbar"]):
        if "menu" in entry:
            _string(entry.get("runtime_id"), f"navigation.navbar[{index}].runtime_id")
    for index, tool in enumerate(navigation["sidebar_tools"]):
        if not isinstance(tool, dict):
            raise InventoryError(f"sidebar_tools[{index}] must be an object")
        _string(tool.get("icon"), f"sidebar_tools[{index}].icon")
        _string(tool.get("text"), f"sidebar_tools[{index}].text")
        asset_id = _string(tool.get("asset"), f"sidebar_tools[{index}].asset")
        if asset_id not in assets_by_id:
            raise InventoryError(f"sidebar tool references unknown asset: {asset_id}")

    footer_page_ids = [entry["page"] for entry in navigation["footer"]]
    rendered_via_footer = [page["id"] for page in pages if page["render_via"] == "footer"]
    if footer_page_ids != rendered_via_footer:
        raise InventoryError(
            "footer render inventory must match navigation.footer order: "
            f"footer={footer_page_ids} pages={rendered_via_footer}"
        )
    expected_book_ids = chapter_ids + [references_id] + appendix_ids
    rendered_via_book = [page["id"] for page in pages if page["render_via"] == "book"]
    if rendered_via_book != expected_book_ids:
        raise InventoryError(
            "book render inventory must match chapters, references, and appendices: "
            f"book={rendered_via_book} expected={expected_book_ids}"
        )

    disk_sources = {
        path.relative_to(root).as_posix()
        for directory in (root, root / "chapters", root / "dodaci")
        for path in (
            directory.glob("*.qmd") if directory.is_dir() else []
        )
    }
    sanctioned_sources = set(all_page_sources(inventory))
    if disk_sources != sanctioned_sources:
        missing = sorted(sanctioned_sources - disk_sources)
        extra = sorted(disk_sources - sanctioned_sources)
        raise InventoryError(f"QMD source inventory drift: missing={missing} extra={extra}")


def load_inventory(root: Path) -> dict[str, Any]:
    path = root / INVENTORY_PATH
    try:
        inventory = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise InventoryError(f"canonical inventory is missing: {INVENTORY_PATH}") from error
    except json.JSONDecodeError as error:
        raise InventoryError(f"canonical inventory is invalid JSON: {error}") from error
    validate_inventory(inventory, root)
    return inventory


def inventory_sha256(root: Path) -> str:
    inventory = json.loads((root / INVENTORY_PATH).read_text(encoding="utf-8"))
    canonical = json.dumps(
        inventory,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def _yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def _href(entry: dict[str, Any], pages: dict[str, dict[str, Any]]) -> str:
    page = pages[entry["page"]]
    return page[entry.get("href", "output")]


def _js_assignment(name: str, value: Any) -> str:
    encoded = json.dumps(value, ensure_ascii=False, indent=2).replace("\n", "\n  ")
    return f"  var {name} = {encoded};"


def generated_sections(inventory: dict[str, Any]) -> dict[str, str]:
    pages = page_map(inventory)
    assets = asset_map(inventory)

    navbar = ["  navbar:", "    pinned: true", "    left:"]
    for entry in inventory["navigation"]["navbar"]:
        navbar.append(f"      - text: {_yaml_quote(entry['text'])}")
        if "menu" in entry:
            navbar.append("        menu:")
            for child in entry["menu"]:
                navbar.extend(
                    [
                        f"          - text: {_yaml_quote(child['text'])}",
                        f"            href: {_href(child, pages)}",
                    ]
                )
        else:
            navbar.append(f"        href: {_href(entry, pages)}")
    navbar.append("    right: []")

    footer = ["    right:"]
    for entry in inventory["navigation"]["footer"]:
        footer.extend(
            [
                f"      - text: {_yaml_quote(entry['text'])}",
                f"        href: {_href(entry, pages)}",
            ]
        )

    sidebar_tools = ["    tools:"]
    for entry in inventory["navigation"]["sidebar_tools"]:
        sidebar_tools.extend(
            [
                f"      - icon: {entry['icon']}",
                f"        href: {assets[entry['asset']]['output']}",
                f"        text: {_yaml_quote(entry['text'])}",
            ]
        )

    structure = ["  chapters:"]
    for entry in inventory["book"]["chapters"]:
        if "page" in entry:
            structure.append(f"    - {pages[entry['page']]['source']}")
        else:
            structure.append(f"    - part: {_yaml_quote(entry['part'])}")
            structure.append("      chapters:")
            structure.extend(
                f"        - {pages[page_id]['source']}" for page_id in entry["pages"]
            )
    structure.extend(
        [
            "",
            f"  references: {pages[inventory['book']['references']]['source']}",
            "",
            "  appendices:",
        ]
    )
    structure.extend(
        f"    - {pages[page_id]['source']}" for page_id in inventory["book"]["appendices"]
    )
    standalone_routes = [
        f"/{page['output']}" for page in inventory["pages"] if page["standalone"]
    ]
    runtime_groups = [
        {
            "id": entry["runtime_id"],
            "routes": [f"/{pages[child['page']]['output']}" for child in entry["menu"]],
        }
        for entry in inventory["navigation"]["navbar"]
        if "menu" in entry
    ]
    runtime_page_routes = {
        page["id"]: f"/{page['output']}" for page in inventory["pages"]
    }
    runtime_chapters = [
        {
            "route": f"/{page['output']}",
            "ai": f"/ai/{PurePosixPath(page['source']).stem}.md",
        }
        for page in chapter_pages(inventory, include_landing=False)
    ]
    runtime_routes = [
        _js_assignment("SAMOSTALNE", standalone_routes),
        _js_assignment("NAVBAR_SKUPINE", runtime_groups),
        _js_assignment("PUTOVI_STRANICA", runtime_page_routes),
        _js_assignment("AI_PUTOVI_POGLAVLJA", runtime_chapters),
    ]
    return {
        "navbar": "\n".join(navbar),
        "footer": "\n".join(footer),
        "sidebar_tools": "\n".join(sidebar_tools),
        "book_structure": "\n".join(structure),
        "runtime_routes": "\n".join(runtime_routes),
    }


def _replace_section(text: str, name: str, body: str) -> tuple[str, bool]:
    start_marker, end_marker = MARKERS[name]
    lines = text.splitlines()
    try:
        start = lines.index(start_marker)
        end = lines.index(end_marker)
    except ValueError as error:
        raise InventoryError(f"_quarto.yml is missing generated markers for {name}") from error
    if end <= start:
        raise InventoryError(f"_quarto.yml has reversed generated markers for {name}")
    replacement = body.splitlines()
    changed = lines[start + 1 : end] != replacement
    updated = lines[: start + 1] + replacement + lines[end:]
    return "\n".join(updated) + "\n", changed


def _sync_file(path: Path, sections: dict[str, str], write: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    changed = False
    for name, body in sections.items():
        text, section_changed = _replace_section(text, name, body)
        changed = changed or section_changed
    if changed and write:
        path.write_text(text, encoding="utf-8", newline="\n")
    return changed


def sync_projections(root: Path, inventory: dict[str, Any], write: bool = False) -> bool:
    sections = generated_sections(inventory)
    quarto_changed = _sync_file(
        root / "_quarto.yml",
        {name: sections[name] for name in ("navbar", "footer", "sidebar_tools", "book_structure")},
        write,
    )
    runtime_changed = _sync_file(
        root / "styles/book-include.html",
        {"runtime_routes": sections["runtime_routes"]},
        write,
    )
    return quarto_changed or runtime_changed
