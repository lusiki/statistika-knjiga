#!/usr/bin/env python3
"""Run an R script without assuming that Rscript is on PATH.

Usage:
    python run_rscript.py --check
    python run_rscript.py path/to/script.R [script arguments ...]

The launcher is intentionally dependency-free.  It honours an explicit
RSCRIPT/BW_RSCRIPT setting, then checks PATH, R_HOME, the usual Windows R
registry/install locations, and the standard macOS/Linux locations.  If no
Rscript binary is directly discoverable but Quarto is available, it delegates
to ``quarto run``; Quarto has its own cross-platform R discovery.
"""

from __future__ import annotations

import glob
import os
from pathlib import Path
import shutil
import subprocess
import sys
from typing import Iterable


def _existing(paths: Iterable[str | os.PathLike[str]]) -> list[Path]:
    found: list[Path] = []
    seen: set[str] = set()
    for raw in paths:
        if not raw:
            continue
        path = Path(raw).expanduser()
        try:
            resolved = path.resolve(strict=True)
        except (OSError, RuntimeError):
            continue
        key = os.path.normcase(str(resolved))
        if resolved.is_file() and key not in seen:
            seen.add(key)
            found.append(resolved)
    return found


def _windows_registry_candidates() -> list[str]:
    if os.name != "nt":
        return []
    try:
        import winreg  # type: ignore[attr-defined]
    except ImportError:
        return []

    candidates: list[str] = []
    views = [0]
    for attr in ("KEY_WOW64_64KEY", "KEY_WOW64_32KEY"):
        value = getattr(winreg, attr, None)
        if value is not None:
            views.append(value)

    for hive in (winreg.HKEY_CURRENT_USER, winreg.HKEY_LOCAL_MACHINE):
        for view in views:
            try:
                with winreg.OpenKey(
                    hive, r"SOFTWARE\R-core\R", 0, winreg.KEY_READ | view
                ) as key:
                    install_path, _ = winreg.QueryValueEx(key, "InstallPath")
            except OSError:
                continue
            candidates.extend(
                [
                    str(Path(install_path) / "bin" / "Rscript.exe"),
                    str(Path(install_path) / "bin" / "x64" / "Rscript.exe"),
                ]
            )
    return candidates


def _version_key(path: str) -> tuple[int, ...]:
    """Sort R-4.6.0-like paths numerically, newest first."""
    name = Path(path).parent.parent.name
    digits: list[int] = []
    current = ""
    for char in name:
        if char.isdigit():
            current += char
        elif current:
            digits.append(int(current))
            current = ""
    if current:
        digits.append(int(current))
    return tuple(digits)


def find_runner() -> tuple[str, list[str]]:
    """Return (kind, command prefix), where kind is rscript or quarto."""
    explicit = [os.environ.get("BW_RSCRIPT", ""), os.environ.get("RSCRIPT", "")]
    on_path = [shutil.which("Rscript") or "", shutil.which("Rscript.exe") or ""]

    r_home = os.environ.get("R_HOME", "")
    home_candidates: list[str] = []
    if r_home:
        home_candidates.extend(
            [
                str(Path(r_home) / "bin" / ("Rscript.exe" if os.name == "nt" else "Rscript")),
                str(Path(r_home) / "bin" / "x64" / "Rscript.exe"),
            ]
        )

    platform_candidates: list[str] = []
    if os.name == "nt":
        platform_candidates.extend(_windows_registry_candidates())
        roots = {
            os.environ.get("ProgramFiles", r"C:\Program Files"),
            os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)"),
            os.environ.get("LOCALAPPDATA", ""),
        }
        installs: list[str] = []
        for root in roots:
            if not root:
                continue
            installs.extend(glob.glob(str(Path(root) / "R" / "R-*" / "bin" / "Rscript.exe")))
            installs.extend(
                glob.glob(str(Path(root) / "R" / "R-*" / "bin" / "x64" / "Rscript.exe"))
            )
        platform_candidates.extend(sorted(installs, key=_version_key, reverse=True))
    else:
        platform_candidates.extend(
            [
                "/Library/Frameworks/R.framework/Resources/bin/Rscript",
                "/opt/homebrew/bin/Rscript",
                "/usr/local/bin/Rscript",
                "/usr/bin/Rscript",
            ]
        )

    found = _existing([*explicit, *on_path, *home_candidates, *platform_candidates])
    if found:
        return "rscript", [str(found[0])]

    quarto = shutil.which("quarto")
    if quarto:
        return "quarto", [quarto, "run"]

    raise FileNotFoundError(
        "Could not find Rscript or Quarto. Install R, put Rscript on PATH, "
        "set BW_RSCRIPT/R_HOME, or install Quarto."
    )


def main(argv: list[str]) -> int:
    check = argv == ["--check"]
    if not argv or (argv[0].startswith("-") and not check):
        print(__doc__.strip(), file=sys.stderr)
        return 2

    try:
        kind, prefix = find_runner()
    except FileNotFoundError as exc:
        print(f"bookwright R launcher: {exc}", file=sys.stderr)
        return 127

    if check:
        if kind == "rscript":
            result = subprocess.run([*prefix, "--version"], check=False)
        else:
            result = subprocess.run([*prefix, "--help"], check=False)
        print(f"bookwright R launcher: {kind} -> {prefix[0]}")
        return result.returncode

    script = Path(argv[0]).expanduser()
    if not script.is_file():
        print(f"bookwright R launcher: script not found: {script}", file=sys.stderr)
        return 2

    command = [*prefix, str(script), *argv[1:]]
    try:
        return subprocess.run(command, check=False).returncode
    except OSError as exc:
        print(f"bookwright R launcher: failed to start {prefix[0]}: {exc}", file=sys.stderr)
        return 126


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
