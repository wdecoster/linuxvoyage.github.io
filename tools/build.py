#!/usr/bin/env python3
"""Rebuild every generated file in the site from the lesson markdown.

Everything under docs/, and the .html sibling of each lesson, is generated.
Edit the markdown under lessons/locales/en_english/ and run this; do not edit
the HTML by hand, it will be overwritten.

    python3 tools/build.py            rebuild everything
    python3 tools/build.py --check    fail if anything is out of date, change nothing

What it produces:
    lessons/locales/en_english/*/NN-*.html   one per lesson, via src/convert.py's converter
    docs/lesson/<slug>.html                  the published lesson pages
    docs/index.html                          the course grid, from tools/sections.py
    docs/commands.html                       the command index
    lessons/locales/en_english/index.html    the same grid for the dev server in src/
    lessons/locales/en_english/home_page.md

Lesson order within a section comes from that section's *-order.txt file.
Section grouping and card text come from tools/sections.py.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EN = ROOT / "lessons" / "locales" / "en_english"
DOCS = ROOT / "docs"

sys.path.insert(0, str(Path(__file__).resolve().parent))

# py-gfm 0.1.4 emits an inline (?i) that Python 3.11+ rejects unless it is at
# the very start of the pattern. Strip it and pass the flag instead, so the
# repo's original converter runs unmodified. The patch has to stay in place for
# the whole run: the offending pattern is compiled when a converter is built,
# not when the module is imported.
_orig_compile = re.compile


def _patched_compile(pattern, flags=0):
    if isinstance(pattern, str) and "(?i)" in pattern:
        pattern = pattern.replace("(?i)", "")
        flags |= re.I
    return _orig_compile(pattern, flags)


re.compile = _patched_compile

from markdownserver.markdown_converter import MarkdownConverter  # noqa: E402
from bs4 import BeautifulSoup       # noqa: E402
from jinja2 import Template         # noqa: E402
from sections import TIERS          # noqa: E402

INNER, OUTER = " " * 28, " " * 24


# --------------------------------------------------------------------------- #
# markdown -> the per-lesson html, exactly as src/convert.py does it
# --------------------------------------------------------------------------- #

def convert(md_path: Path, out_path: Path):
    MarkdownConverter().convert(str(md_path), str(out_path))
    meta = '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />'
    data = out_path.read_text(encoding="UTF-8")
    i = data.index("</head>")
    data = data[:i] + meta + data[i:]
    data = (data.replace("<h2>Lesson Content</h2>", "")
                .replace("h2", "h3").replace("h1", "h3"))
    out_path.write_text(data, encoding="UTF-8")


# --------------------------------------------------------------------------- #
# the three panels of a lesson page, split as src/main.py splits them
# --------------------------------------------------------------------------- #

def hide_answer(quiz: str) -> str:
    """Put the answer behind a disclosure widget so there is a moment to think.
    Lessons whose answer is empty are left alone."""
    m = re.search(r'<h3>Quiz Answers?</h3>', quiz)
    if not m:
        return quiz
    question, answer = quiz[:m.start()], quiz[m.end():]
    trailing = ""
    if answer.rstrip().endswith("</div>"):
        cut = answer.rstrip()[: -len("</div>")]
        trailing, answer = answer[len(cut):], cut
    if not re.sub(r'<[^>]+>|\s', '', answer):
        return quiz
    return (f'{question}<details class="quiz-answer">\n'
            f'<summary>Show answer</summary>\n{answer.strip()}\n</details>{trailing}')


def split_lesson(generated: Path):
    bs = BeautifulSoup(generated.read_text(encoding="UTF-8"), "html.parser")
    page = str(bs.find("div", {"class": "markdown-body"}))
    exe_i = page.index("<h3>Exercise</h3>")
    try:
        quiz_i = page.index("<h3>Quiz Question</h3>")
    except ValueError:
        quiz_i = page.index("<h3>Quiz Questions</h3>")
    return (page[len('<div class="markdown-body">'):exe_i],
            page[exe_i:quiz_i],
            hide_answer(page[quiz_i:]))


def lesson_template():
    raw = (ROOT / "templates" / "lesson.html").read_text(encoding="utf-8")
    return Template(
        raw.replace('src="/static/', 'src="../static/')
           .replace('href="/static/', 'href="../static/')
           .replace('href="/"', 'href="../index.html"')
           .replace('href="/commands.html"', 'href="../commands.html"')
           .replace('href="/about.html"', 'href="../about.html"')
           .replace('href="/lesson/{{result}}"', 'href="{{result}}.html"'),
        keep_trailing_newline=True)


# --------------------------------------------------------------------------- #
# the home page grid
# --------------------------------------------------------------------------- #

CARD = """    <div class="col-sm-6 col-md-3">
      <div class="thumbnail thumbnail-border fade">
        <a href="lesson/{page}.html">
          <img alt="{title}" class="img-circle" src="static/assets/home/{image}">
          <div class="caption">
            <h3>{title}</h3>
            <p>{blurb}</p>
          </div>
        </a>
      </div>
    </div>
"""


def icon(name):
    home = DOCS / "static" / "assets" / "home"
    hits = [p for p in sorted(home.glob(f"{name}-*.png"))
            if re.fullmatch(rf"{re.escape(name)}-[0-9a-f]{{64}}\.png", p.name)]
    assert len(hits) == 1, f"no unique icon for {name!r}: {hits}"
    return hits[0].name


def build_home():
    html = (DOCS / "index.html").read_text(encoding="utf-8")
    start = html.index('<div class="container content">')
    end = html.index("</div><!-- end of wrap -->")

    grid = ['<div class="container content">\n']
    for tier, sections in TIERS:
        grid.append('  <div class="row">\n\n')
        grid.append(f'    <h2 class="text-center buffer-bottom">{tier}</h2>\n\n')
        for title, page, image, blurb in sections:
            grid.append(CARD.format(page=page, title=title, image=icon(image), blurb=blurb))
        grid.append('  </div>\n\n')
    grid.append('</div>\n\n  ')

    (DOCS / "index.html").write_text(html[:start] + "".join(grid) + html[end:],
                                     encoding="utf-8")

    # the dev server in src/ serves its own copy, with absolute paths
    src = (DOCS / "index.html").read_text(encoding="utf-8")
    src = src.replace('href="lesson/', 'href="/lesson/').replace('src="static/', 'src="/static/')
    src = re.sub(r'href="/lesson/([^"]+)\.html"', r'href="/lesson/\1"', src)
    (EN / "index.html").write_text(src, encoding="utf-8")

    md = ["# Home Page\n"]
    for tier, sections in TIERS:
        md.append(f"\n## {tier}\n")
        for title, _page, _image, blurb in sections:
            md.append(f"\n* {title} - {blurb}\n")
    (EN / "home_page.md").write_text("".join(md), encoding="utf-8")


# --------------------------------------------------------------------------- #

def sections_on_disk():
    for d in sorted(p for p in EN.iterdir() if p.is_dir()):
        orders = list(d.glob("*.txt"))
        assert len(orders) == 1, f"{d} needs exactly one order file, found {orders}"
        menu = [l.strip() for l in orders[0].read_text(encoding="utf-8").split() if l.strip()]
        yield d, d.name[3:], menu


def build_lessons():
    tpl = lesson_template()
    built = set()
    for d, category, menu in sections_on_disk():
        slugs = [m[3:-3] for m in menu]
        for name in menu:
            md = d / name
            assert md.exists(), f"{d.name}/{name} is listed in the order file but missing"
            gen = md.with_suffix(".html")
            convert(md, gen)
            slug = md.stem[3:]
            content, exercise, quiz = split_lesson(gen)
            page = tpl.render(page=slug, category=category, menu=slugs,
                              content=content, exercise=exercise, quiz=quiz)
            (DOCS / "lesson" / f"{slug}.html").write_text(page, encoding="utf-8")
            built.add(f"{slug}.html")
    stale = {p.name for p in (DOCS / "lesson").glob("*.html")} - built
    for name in sorted(stale):
        (DOCS / "lesson" / name).unlink()
        print(f"  removed stale page {name}")
    return len(built)


def git_dirty():
    out = subprocess.run(["git", "-C", str(ROOT), "status", "--porcelain"],
                         capture_output=True, text=True, check=True).stdout
    return [l[3:] for l in out.splitlines()]


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true",
                    help="fail if the generated files are out of date")
    args = ap.parse_args()

    before = set(git_dirty()) if args.check else set()

    n = build_lessons()
    build_home()
    subprocess.run([sys.executable, str(ROOT / "tools" / "build_command_index.py")],
                   check=True)
    print(f"built {n} lessons")

    if args.check:
        changed = sorted(set(git_dirty()) - before)
        if changed:
            print("\nGenerated files are out of date. Run: python3 tools/build.py")
            for f in changed:
                print(f"  {f}")
            return 1
        print("generated files are up to date")
    return 0


if __name__ == "__main__":
    sys.exit(main())
