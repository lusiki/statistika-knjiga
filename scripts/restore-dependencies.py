#!/usr/bin/env python3
"""Restore the exact R and Playwright dependencies declared by this checkout."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> "NoReturn":
    print(f"dependency restore: {message}", file=sys.stderr)
    raise SystemExit(2)


def read_text(path: Path, label: str) -> str:
    if not path.is_file():
        fail(f"missing committed {label}: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8").strip()


def run(command: list[str], env: dict[str, str]) -> None:
    print("+", " ".join(command), flush=True)
    result = subprocess.run(command, cwd=ROOT, env=env, check=False)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--fixture",
        choices=("missing-browser-lock",),
        help="Deliberately fail closed without changing canonical lockfiles.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    required = {
        "R lockfile": ROOT / "renv.lock",
        "renv bootstrap": ROOT / "renv" / "activate.R",
        "browser manifest": ROOT / "package.json",
        "browser lockfile": ROOT / "package-lock.json",
        "Node version pin": ROOT / ".node-version",
    }
    if args.fixture == "missing-browser-lock":
        required["browser lockfile"] = ROOT / "fixtures" / "missing-package-lock.json"

    for label, path in required.items():
        if not path.is_file():
            fail(f"missing committed {label}: {path.relative_to(ROOT)}")

    package = json.loads(read_text(required["browser manifest"], "browser manifest"))
    package_lock = json.loads(read_text(required["browser lockfile"], "browser lockfile"))
    node_pin = read_text(required["Node version pin"], "Node version pin")
    expected_npm = str(package.get("packageManager", "")).removeprefix("npm@")
    expected_playwright = str(package.get("devDependencies", {}).get("playwright", ""))
    locked_root = package_lock.get("packages", {}).get("", {})
    locked_playwright = package_lock.get("packages", {}).get(
        "node_modules/playwright", {}
    )

    if package_lock.get("lockfileVersion") != 3:
        fail("package-lock.json must use lockfileVersion 3")
    if locked_root.get("devDependencies", {}).get("playwright") != expected_playwright:
        fail("package.json and package-lock.json disagree on Playwright")
    if locked_playwright.get("version") != expected_playwright:
        fail("Playwright is not pinned to one exact locked version")
    if not locked_playwright.get("integrity"):
        fail("Playwright lock record lacks registry integrity")
    if not node_pin or not expected_npm:
        fail("Node and npm must both have exact version pins")

    node = shutil.which("node")
    npm = shutil.which("npm.cmd" if os.name == "nt" else "npm")
    if not node or not npm:
        fail("node and npm must be available before dependency restoration")

    running_node = subprocess.check_output([node, "--version"], text=True).strip()
    running_npm = subprocess.check_output([npm, "--version"], text=True).strip()
    if running_node.removeprefix("v") != node_pin:
        fail(f"Node version mismatch: expected {node_pin}, found {running_node}")
    if running_npm != expected_npm:
        fail(f"npm version mismatch: expected {expected_npm}, found {running_npm}")

    env = os.environ.copy()
    env.setdefault("RENV_CONFIG_AUTO_SNAPSHOT", "FALSE")
    # The R stage performs a stricter lock/source reconciliation after restore;
    # suppress renv's duplicate startup warning before that stage can run.
    env.setdefault("RENV_CONFIG_SYNCHRONIZED_CHECK", "FALSE")

    run(
        [
            sys.executable,
            str(ROOT / "bookwright_plugin" / "bookwright" / "scripts" / "run_rscript.py"),
            str(ROOT / "scripts" / "init-renv.R"),
            "--restore",
        ],
        env,
    )
    run(
        [npm, "ci", "--ignore-scripts", "--no-audit", "--fund=false"],
        env,
    )
    run(
        [
            node,
            str(ROOT / "node_modules" / "playwright" / "cli.js"),
            "install",
            "chromium",
        ],
        env,
    )

    verify = (
        "const fs=require('fs');"
        "const p=require('playwright');"
        "const v=require('playwright/package.json').version;"
        f"if(v!=={json.dumps(expected_playwright)})throw new Error('version '+v);"
        "const exe=p.chromium.executablePath();"
        "if(!fs.existsSync(exe))throw new Error('missing browser '+exe);"
        "console.log('BROWSER_RESTORE_OK version='+v+' executable='+exe);"
    )
    run([node, "-e", verify], env)
    print(
        "DEPENDENCY_RESTORE_OK "
        f"r_lock=renv.lock playwright={expected_playwright} "
        f"node={node_pin} npm={expected_npm}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
