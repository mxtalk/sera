# alternate pass

How to make a pass for sera survey 002 outside Taskmarket.

23 November 2026 · Daniel Tuck

## for the person running it

1. Open a fresh chat, outside any project, with memory off and web access and code tools on. Choose the highest thinking setting available.
2. Attach this file.
3. In your first message, give your name or handle, today's date and the time, the app, and the model's exact name, version and thinking setting, as the app shows them. Then ask it to follow start.md.
4. Download the two files it hands back. Check the .md, and put the chat's share link in `artifacts:`.
5. Open a pull request on [mxtalk/sera](https://github.com/mxtalk/sera) adding both files to `surveys/002-history-of-english/passes/`.

Opening the pull request hands in the pass and licenses it under CC BY-SA 4.0, so sera can publish it. The chat behind the share link becomes public too.

## for the surveyor

You are making one pass of sera survey 002. Follow survey.md exactly. This file stands in for the Taskmarket task that survey.md mentions, and changes three things:

- **files** — Fetch the nine files from their links under files, at the pinned commits, and check each against its SHA-256. Fetch nothing else: no other page, no search, no other pass, nothing remembered from other chats. If a file won't come through whole, or its hash doesn't match, stop and ask for it to be attached. If you can only reach the repos with git, clone each one without checking it out (`git clone --no-checkout`), read each file with `git show <commit>:<path>`, and don't list or open anything else. The one exception is [sera-check.py](https://raw.githubusercontent.com/mxtalk/sera/main/sera-check.py): survey.md lets you run it on your pass before handing in, so you may fetch it from the main branch (with git, `git show origin/main:sera-check.py`). Say in `read:` if you ran it.
- **names** — Name your files `pass-<name>-<model>-<date>-<time>.csv` and `pass-<name>-<model>-<date>-<time>.md`, from the name, model, date and time you were given, in lowercase with hyphens for spaces, the date as YYYYMMDD and the time as HHMM (for example `pass-ada-lovelace-astra-6-20261117-0830.csv`).
- **hand-in** — No reward, no deadline. Hand both files back in this chat.

Write each reason for its own fire, in your own words. Code may read, split and write the files, but not the reasons. Stock or templated reasons aren't accepted.

Read the whole text before giving verdicts. Then work down the fire list, in batches if you need to, keeping sera's three columns exactly as given.

In the .md:

- `task:` is `alternate`.
- `surveyor:` is the model, submitted by the person.
- `model:` and `thinking:` are the model and setting actually used, exactly as the person gave them.
- `read:` lists the files you read and how each reached you: retrieved from its link, read with git, or attached.
- `human:` says what the person did beyond starting the run.
- `artifacts:` is a line for the chat's share link.

## files

| file | SHA-256 |
|---|---|
| [mxtalk.md](https://raw.githubusercontent.com/mxtalk/mxtalk/c716391c151c8302d6d69fd4fc3f943dc3b07691/mxtalk.md) | `233b018d4fd7247516be183042d01eda0a6000597aa7a19436e72ae018c943f0` |
| [sera.md](https://raw.githubusercontent.com/mxtalk/mxtalk/c716391c151c8302d6d69fd4fc3f943dc3b07691/sera.md) | `dbff6c7069630c27d30f624cb91539c91473d67d838a84a23ee3d35fa92bfcf5` |
| [the.md](https://raw.githubusercontent.com/mxtalk/sera/2f82021688b4593d7ef4989d1f3849cda014f2e8/fixes/the.md) | `343ef803f7e12ee7d3df59a2b400d0467da8f389b7503fa452f7ef19bca32b67` |
| [and.md](https://raw.githubusercontent.com/mxtalk/sera/2f82021688b4593d7ef4989d1f3849cda014f2e8/fixes/and.md) | `eca0560abee3854e9af4917fa4822f6185f76d22b84d0437fdcd145fb214856f` |
| [of.md](https://raw.githubusercontent.com/mxtalk/sera/2f82021688b4593d7ef4989d1f3849cda014f2e8/fixes/of.md) | `799779213ca68c9657a95c7ce322c93981094b1ddd22612e8e857e88d8d3eb7f` |
| [survey.md](https://raw.githubusercontent.com/mxtalk/sera/5a201616bc4105ce1e5dce814aac0baae9cf0de1/survey.md) | `99f00385a706c927f02285959f3d43fdf028e8740e309e40ca550933ba4fe0dd` |
| [README.md](https://raw.githubusercontent.com/mxtalk/sera/4a775e9a651f44b2fe5de703f180750364082d5d/surveys/002-history-of-english/README.md) | `4b5fc89725c606592dce7ffbae837e35028ab57298a4cf15d3c6a9d2f5518396` |
| [text.md](https://raw.githubusercontent.com/mxtalk/sera/4a775e9a651f44b2fe5de703f180750364082d5d/surveys/002-history-of-english/text.md) | `969060ad5cadbb1bd31f7c93f88d126f20566a5835fe69e520faa65f4a23e113` |
| [fires.csv](https://raw.githubusercontent.com/mxtalk/sera/4a775e9a651f44b2fe5de703f180750364082d5d/surveys/002-history-of-english/fires.csv) | `d0eebc9e079ab4fed3da7c4d248bc95a9a2ec7eae8510e6e7e587ff4f36e0d3f` |
