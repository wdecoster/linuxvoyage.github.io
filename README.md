This repository is one of the ways to go through the English Version of [Linux Journey](https://linuxjourney.com) Course - https://linuxvoyage.github.io/

---

## About this fork

Served at **https://wdecoster.github.io/linuxvoyage.github.io/**

This is a fork of [linuxvoyage/linuxvoyage.github.io](https://github.com/linuxvoyage/linuxvoyage.github.io), reworked as the Linux component of an **introductory Master's level bioinformatics course**.

The students it is written for have little or no command line experience, and they **ssh into a shared server** rather than installing Linux on their own machine. That single fact is what most of the changes follow from: they cannot choose a distribution, they have no `sudo`, their jobs need to outlive an ssh session, and their first real task is usually to get data onto the machine and run a tool over it. The upstream course assumes the opposite on every one of those points.

Text and examples lean towards the kind of files these students will actually handle, and the exercises use small tabular sample data rather than lists of animals.

### What is different

**Corrections**, all also offered upstream:

* the grep lesson served the env lesson's content ([PR #1](https://github.com/linuxvoyage/linuxvoyage.github.io/pull/1))
* broken markup, a blank quiz answer, and five misleading statements ([PR #2](https://github.com/linuxvoyage/linuxvoyage.github.io/pull/2))

**Resequenced.** The course now opens with connecting to a server instead of ten pages on choosing a distribution. Text editing moved into the beginner section, tab completion moved to lesson two, `grep` moved to the front of Text Manipulation, and the distribution tour, init systems and networking became background reading.

**New lessons**, none of which existed upstream:

| section | lessons |
| --- | --- |
| Connecting | ssh, ssh keys, VS Code over ssh |
| Command Line | filenames and quoting, nano |
| Scripting | shell variables, your first script, loops over files, exit codes and chaining |
| Jobs and Processes | interrupting commands, background jobs, screen sessions |
| Your Environment | PATH and export, installing your own tools |

**Removed.** Two vim lessons that were empty `# Title` placeholders upstream.

**Examples.** The core text-processing lessons (`sort`, `uniq`, `cut`) now work on a sample table rather than lists of animals, and the `sort -n` example no longer sorts words numerically.

### Editing a lesson

Lessons are markdown under `lessons/locales/en_english/<section>/`. **Everything else is generated** — the `.html` beside each lesson, every page under `docs/`, the home page grid, and the command index. Never edit those by hand; they get overwritten.

To change a lesson, edit its `.md` and push. A GitHub Action rebuilds and commits the generated files for you, so the published site and the command index cannot drift from the lessons. On a pull request it checks instead of committing, and fails if the generated files are stale.

To rebuild locally, which is worth doing to preview:

```bash
pip install markdown-server==0.1.4 beautifulsoup4==4.11.1 jinja2
python3 tools/build.py            # rebuild everything
python3 tools/build.py --check    # just report whether anything is out of date
```

Other things you may want to change:

| what | where |
| --- | --- |
| lesson order within a section | that section's `*-order.txt` |
| which sections exist | add a directory with an order file, then add it to `tools/sections.py` |
| section grouping, card text, card icons | `tools/sections.py` |
| lesson page layout | `templates/lesson.html` |
| home page outside the grid, About page | `docs/index.html`, `docs/about.html` (edited by hand, preserved by the build) |

Two other Actions run on their own: `check-links.yml` verifies every external link weekly, and opens an issue if one dies.

### Based on

* [Linux Journey](https://github.com/cindyq/linuxjourney/) is a site dedicated to making learning Linux fun and easy.

* [LunaGNUisance/linuxjourney](https://github.com/LunaGNUisance/linuxjourney) for ordering the content.

* [web.archive.org](https://web.archive.org/web/20220706072307/https://linuxjourney.com/) for copying the original site's styles

* [itamarg365/linuxjourney](https://github.com/itamarg365/linuxjourney) for helping to serve locally.

### Usage - Serve the MD lessons with python3 app

#### From your machine:
```bash
pip install -r requirements.txt
cd src
uvicorn main:app
```
#### From a typical container:
To serve from container, you might need to specify host address and port as
 1. running uvicorn will try to host at 127.0.0.1 which did not work while testing out of container
 2. you might have port 80 occupied for some other project.
```bash
uvicorn main:app --host 0.0.0.0 --port 9090
```
And...
![](./images/site.png "Website")

#### Other minor issues:
If you find any lesson/page missing in a lesson, feel free to checkout the 
live version / 2023 version of Linux Journey 
[here](https://linuxvoyage.github.io/liveLJ/). Note: Quiz Q/A and 
translations will not work as expected.

### Brief History

Though Linux Journey was created to document the journey of the [original author](https://github.com/cindyq) and their contributors to learn Linux, everyone's journey is a little different. So, One fine day, the linuxjourney.com website went down and open source community was concerned. Hence, someone volunteered to help us serve it locally and then put it together as static site. After over 2 months, it seems the domain owner/author of the site, resurrected it up again.  So, Now We can further improve the knowledge of the greater Linux community through contribution and collaboration, again. Feel free to refer to below issues and may be make a contribution or PR. Good day!

#### Related GitHub Issues:
* [213](https://github.com/cindyq/linuxjourney/issues/213#issuecomment-1420893647)
* [216](https://github.com/cindyq/linuxjourney/issues/216)


### License
The text content of this repo (Linux Journey) has been made free to modify and distribute. For full license terms see: [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/). This license does not include the images, site design and source code which is subject to All Rights Reserved.
