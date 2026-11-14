# alternate pass

How to make a pass for sera survey 001 outside Taskmarket.

12 November 2026 · Daniel Tuck

## for the person running it

1. Open a fresh chat, outside any project, with memory off and web access and code tools on. Choose the highest thinking setting available.
2. Attach this file.
3. In your first message, give your name or handle, today's date, the app, and the model's exact name, version and thinking setting, as the app shows them. Then ask it to follow start.md.
4. Download the two files it hands back. Check the .md, and put the chat's share link in `artifacts:`.
5. Open a pull request on [mxtalk/sera](https://github.com/mxtalk/sera) adding both files to `surveys/001-geodetic-datum/passes/`.

Opening the pull request hands in the pass and licenses it under CC BY-SA 4.0, so sera can publish it. The chat behind the share link becomes public too.

## for the surveyor

You are making one pass of sera survey 001. Follow survey.md exactly. This file stands in for the Taskmarket task that survey.md mentions, and changes three things:

- **files** — Fetch the nine files from their links under files, at the pinned commits, and check each against its SHA-256. Fetch nothing else: no other page, no search, no other pass, nothing remembered from other chats. If a file won't come through whole, or its hash doesn't match, stop and ask for it to be attached. If you can only reach the repos with git, clone each one without checking it out (`git clone --no-checkout`), read each file with `git show <commit>:<path>`, and don't list or open anything else.
- **names** — Name your files `pass-<name>-<model>.csv` and `pass-<name>-<model>.md`, from the name and model you were given, in lowercase with hyphens for spaces.
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
| [survey.md](https://raw.githubusercontent.com/mxtalk/sera/ef44818ddbfcadea5694a68c70c426623256b2fa/survey.md) | `a41d8bced209b5f3b321e79d6cbf244814d0e733add59f8cce92e89df063ab32` |
| [README.md](https://raw.githubusercontent.com/mxtalk/sera/f73eb54c793fefda4803c8757953909667811ab4/surveys/001-geodetic-datum/README.md) | `803950847df60753204398678fa142fcfe5d614d0bf65887e497b119db90792e` |
| [text.md](https://raw.githubusercontent.com/mxtalk/sera/84ea19647e302c615881f960ad16f11a99f85bc4/surveys/001-geodetic-datum/text.md) | `00cf2c57df03cae42fdb02b83f93342f380df57af08513ec669ae4cb8be79f2a` |
| [fires.csv](https://raw.githubusercontent.com/mxtalk/sera/84ea19647e302c615881f960ad16f11a99f85bc4/surveys/001-geodetic-datum/fires.csv) | `7599dc49952ca7651ffb9d5c3fbe99722857ea8a10ffc8b607551616f21d4de4` |
