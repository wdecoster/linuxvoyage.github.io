#!/usr/bin/env python3
"""Build docs/commands.html, an A-Z index of every command the course uses.

Without this a reader can only find grep if they remember it lives in Text-Fu.
The index is generated from the lessons rather than maintained by hand, so it
cannot drift: every "$ something" line in a <pre> block is a usage, and a
lesson whose title names the command is where it is taught.

    python3 tools/build_command_index.py
"""
import html
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EN = ROOT / "lessons" / "locales" / "en_english"
OUT = ROOT / "docs" / "commands.html"

# Placeholders and examples, not commands anyone can look up.
SKIP = {
    "mytool", "mycommand", "somecommand", "coolcommand", "yourfile.py",
    "analysis.py", "analysis.R", "package_name", "somepattern", "foobar",
    "chrome", "Miniconda3-latest-Linux-x86_64.sh", "pete", "username",
}
# Prefixes to step over to reach the real command.
PREFIX = {"sudo", "time", "nohup", "eval", "watch"}

PROMPT = re.compile(r'^\s*(?:\([\w.-]+\)\s*)?\$\s+(.*)$')
PRE = re.compile(r'<pre>(.*?)</pre>', re.S)


def lessons():
    for order in sorted(EN.glob("*/*.txt")):
        section = order.parent.name[3:].replace("-", " ").title()
        for line in order.read_text(encoding="utf-8").split():
            path = order.parent / line
            title = path.read_text(encoding="utf-8").split("\n", 1)[0].lstrip("# ").strip()
            yield section, title, path.stem[3:], path


def commands_in(text):
    for block in PRE.findall(text):
        for raw in html.unescape(block).splitlines():
            m = PROMPT.match(raw)
            if not m:
                continue
            words = m.group(1).split()
            while words and words[0] in PREFIX:
                words = words[1:]
            if not words:
                continue
            cmd = words[0]
            if (cmd in SKIP or cmd.startswith(("./", "/", "$", "#", "-", "&"))
                    or not re.fullmatch(r'[a-zA-Z][\w.+-]*', cmd)):
                continue
            yield cmd


def main():
    usage = defaultdict(set)      # command -> {(section, title, slug)}
    taught = {}                   # command -> (section, title, slug)
    for section, title, slug, path in lessons():
        text = path.read_text(encoding="utf-8")
        where = (section, title, slug)
        found = set(commands_in(text))
        for cmd in found:
            usage[cmd].add(where)
        # the lesson that names the command in its title is where it is taught
        words = set(re.findall(r'[a-zA-Z][\w.+-]*', f"{title} {slug}".lower()))
        for cmd in found:
            if cmd.lower() in words and cmd not in taught:
                taught[cmd] = where

    rows = []
    for cmd in sorted(usage, key=str.lower):
        places = sorted(usage[cmd], key=lambda w: (w[0], w[1]))
        home = taught.get(cmd)
        links = " ".join(
            f'<a class="{"taught" if p == home else ""}" href="lesson/{p[2]}.html">'
            f'{html.escape(p[1])}</a>' for p in places)
        rows.append(
            f'<tr data-cmd="{html.escape(cmd.lower())}">'
            f'<th><code>{html.escape(cmd)}</code></th>'
            f'<td>{links}</td></tr>')

    page = TEMPLATE.replace("{{rows}}", "\n".join(rows)).replace("{{count}}", str(len(rows)))
    OUT.write_text(page, encoding="utf-8")
    print(f"{len(rows)} commands indexed across {len(list(lessons()))} lessons -> {OUT}")
    return 0


TEMPLATE = """<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Commands | Linux for Bioinformatics</title>
  <link rel="stylesheet" media="all" href="static/assets/home/application-b0b91461d093aa2ed95d8a7467856e4dc16f55744d3c17a927c3598e5b26cd3f.css">
  <style>
    body { background-color: #F7F7F7; }
    .wrap { max-width: 900px; margin: 0 auto; padding: 110px 20px 60px; }
    h1 { margin: 0 0 6px; color: #2C3E50; }
    .lede { color: #777; margin-bottom: 24px; }
    #filter {
      width: 100%; padding: 12px 14px; font-size: 18px;
      border: 1px solid #CCC; border-radius: 3px; margin-bottom: 6px;
    }
    #count { color: #777; font-size: 13px; margin-bottom: 18px; }
    table { width: 100%; border-collapse: collapse; background: #fff; }
    th, td { padding: 9px 12px; border-bottom: 1px solid #EEE; text-align: left;
             vertical-align: top; }
    th { width: 170px; font-weight: normal; }
    code { font-size: 15px; color: #C7254E; background: #F9F2F4;
           padding: 2px 6px; border-radius: 3px; }
    td a { display: inline-block; margin: 0 12px 4px 0; color: #4183C4; }
    td a.taught { font-weight: bold; }
    td a.taught:after { content: " \\2605"; color: #16A085; }
    .none { color: #777; padding: 20px 0; display: none; }
  </style>
</head>

<body>
  <nav class="navbar navbar-custom navbar-fixed-top">
    <div class="container">
      <div class="navbar-header">
        <a id="logo" class="navbar-brand" href="index.html">Linux for Bioinformatics</a>
      </div>
      <p class="nav navbar-nav navbar-right">
        <a class="navbar-brand" href="about.html">About</a>
        <a class="navbar-brand" href="index.html">All sections</a>
      </p>
    </div>
  </nav>

  <div class="wrap">
    <h1>Commands</h1>
    <p class="lede">Every command used anywhere in the course, and the lessons it appears in.
      A star marks the lesson where it is actually taught.</p>

    <input id="filter" type="search" placeholder="Type a command, e.g. grep" autofocus
           autocomplete="off" spellcheck="false">
    <p id="count">{{count}} commands</p>

    <table>
      <tbody id="rows">
{{rows}}
      </tbody>
    </table>
    <p class="none" id="none">Nothing matches that.</p>
  </div>

  <script>
    (function () {
      var box = document.getElementById('filter');
      var rows = Array.prototype.slice.call(
        document.querySelectorAll('#rows tr'));
      var count = document.getElementById('count');
      var none = document.getElementById('none');

      function apply() {
        var q = box.value.trim().toLowerCase();
        var shown = 0;
        rows.forEach(function (row) {
          var hit = !q || row.getAttribute('data-cmd').indexOf(q) !== -1;
          row.style.display = hit ? '' : 'none';
          if (hit) shown++;
        });
        count.textContent = q ? shown + ' of ' + rows.length + ' commands'
                              : rows.length + ' commands';
        none.style.display = shown ? 'none' : 'block';
      }

      box.addEventListener('input', apply);
      // support linking straight to a command, e.g. commands.html#grep
      if (location.hash.length > 1) {
        box.value = decodeURIComponent(location.hash.slice(1));
        apply();
      }
    })();
  </script>
</body>

</html>
"""

if __name__ == "__main__":
    sys.exit(main())
