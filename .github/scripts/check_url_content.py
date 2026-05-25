#!/usr/bin/env python3
"""Flag URLs in scripts that look like file downloads but return HTML.

Writes a markdown report to stdout, to $GITHUB_STEP_SUMMARY (the run's
Summary tab), and to ./url-content-report.md (for the scheduled issue).
Exits 1 if any problems are found.
"""
import os
import re
import sys
import urllib.request
from pathlib import Path

SCAN_EXT = {".sh", ".bash", ".py", ".ijm", ".groovy", ".R", ".r",
            ".yml", ".yaml", ".js", ".ts"}

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
    # Only the headers are read, so large files aren't downloaded.
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.headers.get("Content-Type", "")

def scan(root: Path):
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
                        seen[url] = f"ERROR: {e}"   # blocked/unreachable — not flagged
                if "text/html" in seen[url].lower():
                    problems.append((path.relative_to(root), ln, url, seen[url]))
    return problems

def report_md(problems) -> str:
    out = ["## File-URL content check", ""]
    if not problems:
        out.append("✓ No file-like URLs returned HTML.")
        return "\n".join(out) + "\n"
    out.append(f"⚠️ **{len(problems)} URL(s) look like file downloads but return HTML** "
               "(often a `blob/` link that should point at raw content):")
    out.append("")
    out.append("| File | Line | URL | Content-Type |")
    out.append("|------|------|-----|--------------|")
    for f, ln, url, ctype in problems:
        out.append(f"| `{f}` | {ln} | {url} | `{ctype}` |")
    return "\n".join(out) + "\n"

def main(root: str = ".") -> int:
    problems = scan(Path(root).resolve())
    md = report_md(problems)

    print(md)                                          # build log

    summary = os.environ.get("GITHUB_STEP_SUMMARY")    # run's Summary tab
    if summary:
        with open(summary, "a", encoding="utf-8") as fh:
            fh.write(md + "\n")

    Path("url-content-report.md").write_text(md, encoding="utf-8")  # for the issue

    return 1 if problems else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
