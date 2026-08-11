# About these directories

Only **`en_english`** is part of this course. It is the only one the build
reads, the only one the dev server in `src/` can serve, and the only one the
published site under `docs/` is generated from.

Everything else here is inherited from upstream and is **not maintained**.

## The other languages

They came with the fork and are translations of the *original* Linux Journey,
not of this version. Since this fork reordered the course, rewrote a good deal
of it and removed some lessons, they no longer correspond to anything on the
site. Most were never close to finished either:

| locale | lessons | | locale | lessons |
| --- | --- | --- | --- | --- |
| et_estonian | 186 | | es_spanish | 16 |
| fa-persian | 186 | | it_italian | 11 |
| ru_russian | 36 | | ja_japanese | 11 |
| de_german | 31 | | sk_slovak | 9 |
| fr_french | 30 | | he_hebrew | 7 |
| | | | el_greek | 6 |
| | | | kr_korean, tr_turkish | 4 each |

For comparison, `en_english` has 197.

## Why they are still here

Two reasons, both about provenance rather than translation.

They are the only record of the **original English wording** before this fork
edited it. That is not hypothetical: the fork began by finding that the English
grep lesson had been overwritten with the env lesson, and the correct text was
recovered from `fa-persian/text-fu/grep-command.md`, which had never been
translated, with `ru_russian` used to confirm it matched section for section.
The fix sent back upstream rests on those files.

They are also other people's work, contributed under
[CC BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/). Keeping them
costs a couple of megabytes and nothing else.

## If you want them gone

Nothing depends on them, so this is safe, and git remembers them anyway:

```bash
git rm -r lessons/locales/{de_german,el_greek,es_spanish,et_estonian,fa-persian}
git rm -r lessons/locales/{fr_french,he_hebrew,it_italian,ja_japanese,kr_korean}
git rm -r lessons/locales/{ru_russian,sk_slovak,tr_turkish}
```

## original-order-reference

Screenshots of the upstream lesson ordering, moved out of the section
directories when the course was resequenced. They document the order this fork
departed from. Not used by anything.
