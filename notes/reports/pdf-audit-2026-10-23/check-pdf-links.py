"""Check actual PDF link annotations, avoiding the legacy text URL regex."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
import fitz
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[3]
REPORT = Path(__file__).resolve().parent
PDF = ROOT / "pdf/Statistika.pdf"
doc = fitz.open(PDF)
links = {}
for number, page in enumerate(doc, 1):
    for annotation in page.get_links():
        uri = annotation.get("uri", "")
        if urlparse(uri).scheme in {"https", "http"}:
            links.setdefault(uri, set()).add(number)

def check(item):
    uri, pages = item
    result = subprocess.run([
        "curl.exe", "--location", "--silent", "--show-error",
        "--connect-timeout", "8", "--max-time", "25",
        "--output", "NUL", "--write-out", "%{http_code}\n%{url_effective}", uri
    ], capture_output=True, text=True, encoding="utf-8", errors="replace")
    values = result.stdout.splitlines()
    return {"uri": uri, "physical_pages": sorted(pages),
            "http_status": values[0] if values else "000",
            "final_uri": values[1] if len(values) > 1 else "",
            "curl_exit": result.returncode, "error": result.stderr.strip()}

with ThreadPoolExecutor(max_workers=10) as pool:
    checked = list(pool.map(check, links.items()))
payload = {"checked_at": datetime.now(timezone.utc).isoformat(),
           "pdf_sha256": hashlib.sha256(PDF.read_bytes()).hexdigest(),
           "scope": "HTTP GET of actual link annotations; does not validate fragment targets or prove source claims.",
           "results": checked}
(REPORT / "pdf-links.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(f"Checked {len(checked)} distinct link annotations")
for row in checked:
    if not row["http_status"].startswith("2"):
        print(row["http_status"], row["uri"], row["error"])
