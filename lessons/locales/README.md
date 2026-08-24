# About this directory

Only **`en_english`** is here. It is the only thing the build reads, the only
thing the dev server in `src/` can serve, and the only source the published
site under `docs/` is generated from.

## The other languages

Thirteen non-English directories used to sit here, inherited from upstream and
never maintained: 560 files and about 2.5 MB. Nothing read them. The build, the
dev server and both workflows have always been `en_english` only, and the
language switcher on the home page was inside an HTML comment pointing at
`localhost:9090`, so it never worked on the published site.

They were also translations of the *original* Linux Journey rather than of this
course. Since this fork reordered the lessons, rewrote a good deal of the text
and removed some lessons entirely, they no longer corresponded to anything you
can see on the site. Most were nowhere near finished: 4 lessons for Korean and
Turkish, 6 for Greek, 16 for Spanish, against 197 in English. The two
near-complete ones, Estonian and Persian at 186 each, describe the course as it
was before this fork touched it.

They have been removed. Nothing in this repository depended on them.

## If you need them back

They mattered once, for provenance rather than for translation. This fork began
by finding that the English `grep` lesson had been overwritten with the `env`
lesson, and the correct text was recovered from
`fa-persian/text-fu/grep-command.md`, which had never been translated, with
`ru_russian` used to confirm it matched section for section. The fix offered
back upstream rests on those files.

So if you ever need the original English wording of a lesson before this fork
edited it, it is still reachable in two places:

* this repository's history, before the commit that removed the directories
* [linuxvoyage/linuxvoyage.github.io](https://github.com/linuxvoyage/linuxvoyage.github.io),
  which still carries all of them

```bash
# list what was there
git log --diff-filter=D --name-only -1 -- lessons/locales

# bring one file back to look at it
git show <commit>^:lessons/locales/fa-persian/text-fu/grep-command.md
```

They are other people's work, contributed under
[CC BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/), and removing
them from the working tree does not remove them from the record.

## original-order-reference

Screenshots of the upstream lesson ordering, moved out of the section
directories when the course was resequenced. They document the order this fork
departed from. Not used by anything.
