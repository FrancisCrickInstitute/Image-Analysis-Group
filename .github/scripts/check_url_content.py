#!/usr/bin/env python3
"""Flag URLs in scripts that look like file downloads but return HTML.

The heuristic: if a URL's path ends in a data-file extension (.yml, .csv,
.sh, ...) but the server responds with text/html, the script is probably
downloading a web page instead of the file it wants.
"""
import re
import sys
import urllib.request
from pathlib import Path

# File types to scan for URLs
SCAN_EXT = {".sh", ".bash", ".py", ".ijm", ".groovy", ".R", ".r",
            ".yml", ".yaml", ".js", ".ts"}

# A URL pointing at one of these => we expect raw bytes, not a web page
DATA_EXT = {".yml", ".yaml", ".csv", ".tsv", ".json", ".sh", ".py",
            ".txt", ".cfg", ".ini", ".toml", ".r", ".ijm", ".groovy",
            ".zip", ".tar", ".gz", ".whl", ".h5", ".pkl", ".xml"}

URL_RE = re.compile(r'https?://[^\s"\'`)>\]]+')

def expected_raw(url: str) -> bool:
    path = url.split("?")[0].split("#")[0]
    return Path(path).suffix.lower() in DATA_EXT

def content_type(url: str) -> str:
    req = urllib.request.Request(
        url, method="GET", headers={"User-Agent": "url-content-check"})
    # We read only the headers, never the body, so large files aren't downloaded.
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.headers.get("Content-Type", "")

def main(root: str = ".") -> int:
    root = Path(root).resolve()
    problems, seen = [], {}

    for path in root.rglob("*"):
        if not path.is_file() or path.suffix not in SCAN_EXT:
            continue
        if any(p in {".git", "node_modules", ".venv"} for p in path.parts):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")

        for ln, line in enumerate(text.splitlines(), 1):
            for url in URL_RE.findall(line):
                url = url.rstrip(".,;")
                if not expected_raw(url):
                    continue
                if url not in seen:
                    try:
                        seen[url] = content_type(url)
                    except Exception as e:
                        seen[url] = f"ERROR: {e}"   # unreachable/blocked — not flagged
                if "text/html" in seen[url].lower():
                    problems.append((path.relative_to(root), ln, url, seen[url]))

    if not problems:
        print("✓ No file-like URLs returned HTML")
        return 0

    print(f"✗ {len(problems)} URL(s) look like file downloads but return HTML:\n")
    for f, ln, url, ctype in problems:
        print(f"  {f}:{ln}\n      {url}\n      Content-Type: {ctype}\n")
    return 1

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
