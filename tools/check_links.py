#!/usr/bin/env python3
"""Check that external links in the course still resolve.

Reads every lesson markdown file, the published pages and the README, pulls out
http(s) URLs, and requests each one. Placeholders that are meant to be examples
rather than real destinations are skipped, see IGNORE below.

Exit status is 1 if anything is broken, so CI fails. Sites that merely refuse
automated requests are reported as warnings and do not fail the run, because a
403 from a bot filter says nothing about whether the page is still there.

    python3 tools/check_links.py [--verbose]
"""
import argparse
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SEARCH = [
    ROOT / "lessons" / "locales" / "en_english",
    ROOT / "docs" / "index.html",
    ROOT / "README.md",
]
SUFFIXES = {".md", ".html"}

# Not real destinations: teaching placeholders, local addresses, and the dev
# server's own language links.
IGNORE = re.compile(
    r"^https?://("
    r"localhost|127\.|0\.0\.0\.0|"
    r"example\.(org|com)|"
    r"IP_ADDRESS|"
    r"\d+\.\d+\.\d+\.\d+|"
    r"download\.widgets|"
    r"remotehost\.com"
    r")",
    re.I,
)

URL_RE = re.compile(r'https?://[^\s"\'<>)\]}]+')
# markdown and prose leave these clinging to the end of a URL
TRAILING = '.,;:!*_`"\''

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")
TIMEOUT = 20


def collect():
    """Map each URL to the files it appears in."""
    found = {}
    files = []
    for target in SEARCH:
        if target.is_dir():
            files += [p for p in target.rglob("*") if p.suffix in SUFFIXES]
        elif target.exists():
            files.append(target)
    for path in sorted(files):
        text = path.read_text(encoding="utf-8", errors="replace")
        for raw in URL_RE.findall(text):
            url = raw.rstrip(TRAILING)
            if IGNORE.match(url):
                continue
            found.setdefault(url, set()).add(str(path.relative_to(ROOT)))
    return found


def fetch(url, method):
    req = urllib.request.Request(url, method=method, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,*/*",
    })
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return r.status


def classify(detail):
    """Only fail on evidence a link is actually gone.

    A 404 means the page is not there, and a DNS failure means the host is not
    there. Everything else - bot filters, rate limits, server errors, TLS
    complaints, timeouts, and the runner having no route to a host - says
    something about the network or the far end's mood, not about whether the
    link still points at anything. Those are reported and eyeballed rather
    than failing the build, because a checker that cries wolf gets ignored.
    """
    if detail.startswith("HTTP "):
        code = int(detail.split()[1])
        return "broken" if 400 <= code < 500 and code not in (403, 405, 408, 429) else "warn"
    if "Name or service not known" in detail or "nodename nor servname" in detail:
        return "broken"
    return "warn"


def check(url):
    """Return (state, detail) where state is ok, warn or broken."""
    last = ""
    for _attempt in range(2):
        for method in ("HEAD", "GET"):
            try:
                return "ok", str(fetch(url, method))
            except urllib.error.HTTPError as e:
                last = f"HTTP {e.code}"
                if classify(last) == "broken":
                    return "broken", last
            except urllib.error.URLError as e:
                last = f"{type(e.reason).__name__}: {e.reason}"
            except Exception as e:  # noqa: BLE001 - report anything else as-is
                last = f"{type(e).__name__}: {e}"
    return classify(last), last


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--verbose", action="store_true", help="list every URL checked")
    args = ap.parse_args()

    urls = collect()
    print(f"checking {len(urls)} external links\n")

    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(lambda u: (u, *check(u)), sorted(urls)))

    broken = [(u, d) for u, s, d in results if s == "broken"]
    warned = [(u, d) for u, s, d in results if s == "warn"]

    if args.verbose:
        for url, state, detail in results:
            print(f"  {state:6} {detail:24} {url}")
        print()

    for label, group in (("WARNING (refused automated request)", warned),
                         ("BROKEN", broken)):
        if group:
            print(f"{label}:")
            for url, detail in group:
                print(f"  {url}")
                print(f"      {detail}")
                for f in sorted(urls[url]):
                    print(f"      in {f}")
            print()

    ok = len(results) - len(broken) - len(warned)
    print(f"{ok} ok, {len(warned)} warned, {len(broken)} broken")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
