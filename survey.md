# survey

How to make a pass for sera.

13 November 2026 · Daniel Tuck

## pass

A pass is one surveyor's run through a survey, giving every fire a verdict. Terms are as sera.md defines them, or as this file does.

Surveys run as tasks on [Taskmarket](https://taskmarket.dev). Each task links its survey and sets the reward, deadline and hand-in. A pass can also be made outside Taskmarket, where the survey's folder has a start.md that says how.

A model makes its pass at the highest thinking setting available to it.

## read

Besides this file and the survey's README, text and fire list, and its start.md for a pass made outside Taskmarket, read these files, at these commits, and nothing else in either repo:

- [mxtalk.md](https://raw.githubusercontent.com/mxtalk/mxtalk/c716391c151c8302d6d69fd4fc3f943dc3b07691/mxtalk.md): the datum
- [sera.md](https://raw.githubusercontent.com/mxtalk/mxtalk/c716391c151c8302d6d69fd4fc3f943dc3b07691/sera.md): the framework and its terms
- [*the*](https://raw.githubusercontent.com/mxtalk/sera/2f82021688b4593d7ef4989d1f3849cda014f2e8/fixes/the.md), [*and*](https://raw.githubusercontent.com/mxtalk/sera/2f82021688b4593d7ef4989d1f3849cda014f2e8/fixes/and.md) and [*of*](https://raw.githubusercontent.com/mxtalk/sera/2f82021688b4593d7ef4989d1f3849cda014f2e8/fixes/of.md): the fixes

Apply the fixes exactly as written. Nothing else in either repo is part of a fix.

You may run [sera-check.py](sera-check.py) on your pass before handing in. It checks this file's rules, not your verdicts.

Consider mxtalk.md whilst making your pass.

## survey folder

Each survey has a folder in this repo. A pass uses three files from it:

- **README.md** — The source, and how the text and fire list were made from it.
- **text.md** — The text, numbered piece by piece from p1. Each title, heading, paragraph, caption, table row and list item is a piece.
- **fires.csv** — The fire list.

Read the whole text before giving verdicts.

## fire list

**fire** — One *the*, *and* or *of* in the text.

The fire list has a row for each fire, and is also your pass: fill it in and hand it back. sera fills the first three columns; you fill the other four. Leave sera's rows and cells as they are.

- **fire** — The fire's ID: piece, word, count. p3.the1 is the first *the* in p3.
- **fix** — The fix that applies: *the*, *and* or *of*.
- **original** — The sentence holding the fire, as it stands, with the fire in [brackets]. Some pieces stand whole; the survey's README says which.
- **verdict** — `clear` or `repaired`.
- **repair** — For a repaired fire: the repaired original, without the fire's brackets.
- **reasoning** — Your reasoning, in your own words, up to 50 words. Required on every row.
- **list_error** — `yes` where sera's row is wrong.

## verdicts

**clear** — The use does what the function says, and the measure calls for nothing more.

**repaired** — The use doesn't do what the function says, or the measure calls for a change.

**fixed wording** — A proper name, a cited or linked work's title, or a direct quotation. A fire inside fixed wording is clear by rule: changing it would break the reference or misquote the source. Put `fixed wording` in reasoning. No repair changes fixed wording.

Change only what the fix calls for at this fire. If that changes another fire, give its ID in reasoning. A repair may run to more than one sentence if it needs to.

In reasoning: for a clear fire, show the function at work on it and the measure considered; for a repaired fire, say why; for fixed wording, `fixed wording` is enough.

## list errors

Where a row is wrong, or the list misses a fire, put `yes` in list_error on that row, or the nearest one, and state the error in reasoning. A wrong row may leave verdict blank; a flag on a correct row doesn't excuse its verdict.

## hand in

Hand in two files:

- `pass-<wallet>.csv` — The fire list, filled in, as UTF-8 CSV.
- `pass-<wallet>.md` — The details below.

`<wallet>` is the wallet you submit from. A pass made outside Taskmarket is named as its start.md says.

```
task:
surveyor: name or wallet; for a model's pass that a person hands in, the model, then who submitted it
model: name and version, if any
thinking: the setting used, or that it can't be set
harness: what the model ran in, if any
human: what any person did beyond starting the run
date:
read: the files you read
artifacts: links to the record of the run, if any
```

A pass is complete when every row has a verdict or a list error, every repaired row has a repair, and every row has reasoning.

Handing in a pass licenses it under CC BY-SA 4.0, so sera can publish it.
