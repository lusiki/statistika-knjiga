#!/usr/bin/env python3
"""Keep R subprocesses on the locked renv library when they run outside the checkout.

renv activates through the checkout's `.Rprofile`, which R loads only when the
process starts in the checkout root. Checks that build a fixture tree in a
temporary directory and run R there therefore lose the renv library: `.libPaths()`
falls back to the user or system library, and a script fails on a missing package
even though `renv.lock` pins it correctly.

That failure mode is invisible on a developer machine, where the package usually
exists in the user library, and it is doubly damaging in a negative fixture, which
would pass on the missing-package error instead of the defect it injected.

Resolving `.libPaths()` once in the checkout root and exporting it as `R_LIBS`
keeps every such subprocess on exactly the locked library.
"""

from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
LAUNCHER = ROOT / "bookwright_plugin/bookwright/scripts/run_rscript.py"

_CACHED_LIBS: str | None = None


def project_r_libs(root: Path = ROOT) -> str:
    """Return the checkout's `.libPaths()` joined by the platform separator."""
    global _CACHED_LIBS
    if _CACHED_LIBS is not None:
        return _CACHED_LIBS
    with tempfile.TemporaryDirectory(prefix="statistika-rlibs-") as directory:
        work = Path(directory)
        target = work / "libpaths.txt"
        probe = work / "libpaths.R"
        probe.write_text(
            "writeLines(paste(.libPaths(), collapse = .Platform$path.sep), "
            f"{_r_string(target)})\n",
            encoding="utf-8",
        )
        subprocess.run(
            [sys.executable, str(LAUNCHER), str(probe)],
            cwd=root,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=True,
        )
        _CACHED_LIBS = target.read_text(encoding="utf-8").strip()
    return _CACHED_LIBS


def r_subprocess_env(root: Path = ROOT) -> dict[str, str]:
    """Environment for an R subprocess that cannot start in the checkout root."""
    env = dict(os.environ)
    libs = project_r_libs(root)
    if libs:
        env["R_LIBS"] = libs
    return env


def _r_string(path: Path) -> str:
    escaped = str(path).replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


if __name__ == "__main__":
    print(project_r_libs())
