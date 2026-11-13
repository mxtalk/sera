# pass: sera survey 001

```
task: alternate
surveyor: Claude, submitted by Daniel Tuck
model: Fable 5.2
thinking: Medium
harness: Claude app, in a cloud session with file, shell and browser tools
human: see below
date: 12 November 2026
read: see below
artifacts: https://claude.ai/share/e6243fda-2acd-417f-ae65-35c54b3fcc4a
```

## human

- Started the run inside a project named "Fable Sera Run" rather than outside any project. The project held no documents.
- Sent "try again" after the first attempt stopped because the shell could not reach raw.githubusercontent.com.
- Gave no input on any verdict, repair or reason.

One reply was cut off by an automatic filter before any verdict was written; the run resumed from the checked files.

## read

All nine files were retrieved from their links under files in START.md, at the pinned commits, through the built-in browser of the person's Claude desktop app. None was attached. Each file's SHA-256 was computed in the browser on the page text and matched START.md.

- mxtalk.md: retrieved from its link
- sera.md: retrieved from its link
- the.md: retrieved from its link
- and.md: retrieved from its link
- of.md: retrieved from its link
- survey.md: retrieved from its link
- README.md: retrieved from its link
- text.md: retrieved from its link; the working copy was re-keyed from the browser's output and its SHA-256 matches
- fires.csv: retrieved from its link, where its SHA-256, row count and fire IDs were read; the working copy was rebuilt from text.md by the README's rules and its SHA-256 matches

Nothing else was fetched: no other page, no search, no other pass.

## counts

| fix | clear | of which fixed wording | repaired |
|---|---|---|---|
| the | 223 | 20 | 4 |
| of | 85 | 26 | 22 |
| and | 87 | 17 | 1 |
| all | 395 | 63 | 27 |

No list errors: 422 rows, every row with a verdict and reasoning, every repaired row with a repair.

## notes

- Code read, split and wrote the files, and applied each repair as a substitution I specified for that fire. Every reason was written by hand for its own fire.
- *of* carries most repairs because its measure is the strictest: where the word marks the object of an action (use, release, measurement, recognition), an identity (process of converting, concepts of latitude) or a set phrase (by means of, in terms of, on the order of), I repaired. Where an event or property is the thing's own (rise of GPS, realization of a datum, conservation of momentum), I left it clear.
- A lower-case *the* before a proper name is judged on function, not as fixed wording. Words inside names, cited titles, See also titles and direct quotations are fixed wording.
- External-link labels (p130, p139, p141) are judged on function, since the text does not show whether they are the pages' own titles; they are clear either way.
- Many reasons on clear rows are short and state the function at work more fully than the measure.
