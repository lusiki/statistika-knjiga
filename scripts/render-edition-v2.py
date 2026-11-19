"""Build the separate prose revision without touching the first-version sources.

Usage: python scripts/render-edition-v2.py [--prepare-only] [--stage PATH]
The engine and data come from the pinned commit in editions/v2/edition.json.
Only the edition overlays are substituted. The approved PDF wrapper runs in
an isolated temporary checkout, never in the original project directory.
"""
from pathlib import Path
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import tarfile
import uuid

ROOT = Path(__file__).resolve().parents[1]
EDITION = ROOT / "editions/v2"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def assert_baseline(manifest):
    expected = dict(manifest["sources"])
    expected.update({"data/" + k: v for k, v in manifest["unchanged_data"].items()})
    expected[manifest["baseline_pdf"]["path"]] = manifest["baseline_pdf"]["sha256"]
    for name, sha in expected.items():
        raw = (ROOT / name).read_bytes()
        exact = hashlib.sha256(raw).hexdigest() == sha
        # Git may check text out with LF or CRLF. Binary/data hashes stay exact.
        text_sha = manifest.get("source_content_sha256", {}).get(name)
        same_text = text_sha and hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest() == text_sha
        if not exact and not same_text:
            raise RuntimeError(f"First-version file changed: {name}")


def prepare(manifest, existing=None):
    scratch = (ROOT / "tmp").resolve()
    scratch.mkdir(exist_ok=True)
    if existing:
        stage = Path(existing).resolve()
        if not stage.is_relative_to(scratch) or not (stage / ".edition-v2-build").is_file():
            raise ValueError("Stage must be a marked edition-v2 build below project tmp/")
        if (stage / ".edition-v2-build").read_text(encoding="utf-8") != manifest["baseline_commit"]:
            raise ValueError("Stage belongs to a different first-version commit")
    else:
        # Inherit the workspace ACL. Python's Windows mkdtemp creates a private
        # ACL that prevents the desktop account running TeX from reading it.
        stage = (scratch / ("edition-v2-" + uuid.uuid4().hex)).resolve()
        stage.mkdir()
        proc = subprocess.Popen(
            ["git", "archive", "--format=tar", manifest["baseline_commit"]],
            cwd=ROOT, stdout=subprocess.PIPE,
        )
        omitted = {"docs", "docs-kolegij", "pdf", "word", "_freeze", "node_modules", ".git"}
        with tarfile.open(fileobj=proc.stdout, mode="r|") as archive:
            for member in archive:
                relative = Path(member.name)
                if relative.parts[0] in omitted or not member.isfile():
                    continue
                target = (stage / relative).resolve()
                if not target.is_relative_to(stage):
                    raise ValueError("Unsafe archive member")
                target.parent.mkdir(parents=True, exist_ok=True)
                with archive.extractfile(member) as source, target.open("wb") as dest:
                    shutil.copyfileobj(source, dest)
        if proc.wait():
            raise RuntimeError("Could not export pinned first-version source")
        (stage / ".edition-v2-build").write_text(manifest["baseline_commit"], encoding="utf-8")
    for folder in ("chapters", "dodaci", "scripts", "tex", "assessment"):
        if (EDITION / folder).exists():
            shutil.copytree(EDITION / folder, stage / folder, dirs_exist_ok=True)
    shutil.copy2(EDITION / "references.bib", stage / "references.bib")
    subprocess.run(
        ["python", str(stage / "scripts/build-solution-routes.py")],
        cwd=stage, check=True,
    )
    return stage


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prepare-only", action="store_true")
    parser.add_argument("--stage", type=Path)
    args = parser.parse_args()
    manifest = json.loads((EDITION / "edition.json").read_text(encoding="utf-8"))
    assert_baseline(manifest)
    stage = prepare(manifest, args.stage)
    print(f"EDITION_STAGE={stage}", flush=True)
    if args.prepare_only:
        return
    env = os.environ.copy()
    # Use installed dependencies, not an empty scratch-local renv library.
    env["RENV_CONFIG_AUTOLOADER_ENABLED"] = "FALSE"
    if os.name == "nt":
        # POSIX C.UTF-8 is not a valid Windows R locale. Let recent Windows R
        # select its native UTF-8 locale; do not change the user's environment.
        for name in list(env):
            if name == "LANG" or name.startswith("LC_"):
                env.pop(name)
    subprocess.run(
        ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File",
         str(stage / "scripts/render-book-pdf.ps1")],
        cwd=stage, env=env, check=True,
    )
    fresh = stage / "pdf/Statistika.pdf"
    if not fresh.is_file() or not fresh.read_bytes().startswith(b"%PDF-"):
        raise RuntimeError("The approved wrapper did not produce a PDF")
    assert_baseline(manifest)
    output = ROOT / "pdf/Statistika-v2.pdf"
    shutil.copy2(fresh, output)
    print(f"EDITION_PDF={output}\nSHA256={digest(output)}", flush=True)


if __name__ == "__main__":
    main()
