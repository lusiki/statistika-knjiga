#!/usr/bin/env python3
"""Prove canonical inventory sync and missing/extra/reordered drift failures."""

from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "scripts/check-book-inventory.py"


def run(root: Path, *arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(CHECKER), "--root", str(root), *arguments],
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def print_output(label: str, result: subprocess.CompletedProcess[str]) -> None:
    print(f"===== {label} =====")
    encoding = sys.stdout.encoding or "utf-8"
    print(result.stdout.encode(encoding, errors="replace").decode(encoding), end="")


def copy_fixture(destination: Path) -> dict[str, object]:
    (destination / "config").mkdir(parents=True)
    (destination / "scripts").mkdir(parents=True)
    (destination / "styles").mkdir(parents=True)
    (destination / ".github/workflows").mkdir(parents=True)
    shutil.copy2(ROOT / "config/book-inventory.json", destination / "config/book-inventory.json")
    shutil.copy2(ROOT / "_quarto.yml", destination / "_quarto.yml")
    shutil.copy2(
        ROOT / "styles/book-include.html",
        destination / "styles/book-include.html",
    )
    for profile in ROOT.glob("_quarto-*.yml"):
        shutil.copy2(profile, destination / profile.name)
    for name in (
        "audit-rendered-html.js",
        "check-pdf-release-path.ps1",
        "check-rendered-html.py",
        "embed-404-assets.py",
        "render-book-docx.ps1",
        "render-book-pdf.ps1",
    ):
        shutil.copy2(ROOT / "scripts" / name, destination / "scripts" / name)
    shutil.copy2(
        ROOT / ".github/workflows/publish.yml",
        destination / ".github/workflows/publish.yml",
    )
    inventory = json.loads((destination / "config/book-inventory.json").read_text(encoding="utf-8"))
    for page in inventory["pages"]:
        source = destination / Path(page["source"])
        source.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / Path(page["source"]), source)
    return inventory


def write_inventory(root: Path, inventory: dict[str, object]) -> None:
    (root / "config/book-inventory.json").write_text(
        json.dumps(inventory, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def require_failure(name: str, root: Path, expected: str) -> None:
    result = run(root)
    print_output(f"EXPECTED FAILURE: {name}", result)
    if result.returncode == 0:
        raise RuntimeError(f"{name} unexpectedly passed")
    if expected.casefold() not in result.stdout.casefold():
        raise RuntimeError(f"{name} failed for the wrong reason; expected {expected!r}")
    print(f"EXPECTED_FAILURE fixture={name} exit={result.returncode}")


def main() -> int:
    try:
        with tempfile.TemporaryDirectory(prefix="statistika-book-inventory-") as directory:
            base = Path(directory).resolve()
            temp_root = Path(tempfile.gettempdir()).resolve()
            if temp_root not in base.parents:
                raise RuntimeError(f"unsafe fixture root: {base}")

            sync_root = base / "sync-positive"
            sync_root.mkdir()
            inventory = copy_fixture(sync_root)
            inventory["pages"].append(
                {
                    "id": "fixture-route",
                    "source": "fixture-route.qmd",
                    "output": "fixture-route.html",
                    "kind": "standalone",
                    "audit_label": "fixture-route",
                    "standalone": True,
                    "render_via": "footer",
                }
            )
            inventory["standalone_pages"].append("fixture-route")
            inventory["navigation"]["footer"].append(
                {"text": "Fixture route", "page": "fixture-route", "href": "source"}
            )
            (sync_root / "fixture-route.qmd").write_text(
                "---\ntitle: Fixture route\n---\n",
                encoding="utf-8",
                newline="\n",
            )
            write_inventory(sync_root, inventory)
            synced = run(sync_root, "--write")
            print_output("POSITIVE: source-driven route sync", synced)
            if synced.returncode != 0:
                raise RuntimeError("source-driven route sync failed")
            checked = run(sync_root)
            print_output("POSITIVE: synced route check", checked)
            if checked.returncode != 0:
                raise RuntimeError("synced route did not pass the canonical checker")
            print("BOOK_INVENTORY_SYNC_FIXTURE_OK added=fixture-route publish=false")

            missing_root = base / "missing"
            missing_root.mkdir()
            inventory = copy_fixture(missing_root)
            inventory["book"]["appendices"].remove("app-f")
            write_inventory(missing_root, inventory)
            require_failure("missing-route", missing_root, "assigned exactly once")

            extra_root = base / "extra"
            extra_root.mkdir()
            inventory = copy_fixture(extra_root)
            inventory["pages"].append(
                {
                    "id": "extra-route",
                    "source": "extra-route.qmd",
                    "output": "extra-route.html",
                    "kind": "standalone",
                    "audit_label": "extra-route",
                    "standalone": True,
                    "render_via": "footer",
                }
            )
            inventory["standalone_pages"].append("extra-route")
            inventory["navigation"]["footer"].append(
                {"text": "Extra route", "page": "extra-route", "href": "source"}
            )
            (extra_root / "extra-route.qmd").write_text(
                "---\ntitle: Extra route\n---\n",
                encoding="utf-8",
                newline="\n",
            )
            write_inventory(extra_root, inventory)
            require_failure("extra-route", extra_root, "generated book inventory drift")

            reordered_root = base / "reordered"
            reordered_root.mkdir()
            inventory = copy_fixture(reordered_root)
            inventory["book"]["appendices"][0:2] = list(
                reversed(inventory["book"]["appendices"][0:2])
            )
            write_inventory(reordered_root, inventory)
            require_failure("reordered-route", reordered_root, "appendices must be contiguous")

        print("BOOK_INVENTORY_NEGATIVE_FIXTURES_OK fixtures=3 publish=false")
        return 0
    except (OSError, RuntimeError, KeyError, TypeError, json.JSONDecodeError) as error:
        print(f"book inventory fixture proof: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
