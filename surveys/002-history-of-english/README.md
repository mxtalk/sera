# survey 002

"History of English", English Wikipedia, as a desktop reader receives it, from the title through "Grammatical changes".

23 November 2026 · Daniel Tuck

## source

- **Article**: [History of English, revision 1385199942](https://en.wikipedia.org/w/index.php?title=History_of_English&oldid=1385199942), last edited 09:01, 12 November 2026 (UTC).
- **Page**: saved from Chrome (desktop site) as MHTML, 06:06 UTC, 23 November 2026.
- **Wikitext**: the revision's wikitext, saved via `action=raw`. source.txt is that file, byte for byte. A pass doesn't use it.

## licence

The text is by Wikipedia's contributors, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); their names are in the [page history](https://en.wikipedia.org/w/index.php?title=History_of_English&action=history). source.txt copies it; text.md and fires.csv adapt it, as set out below. All three are under the same licence.

## text

text.md holds the article, as a desktop reader receives it, in page order, from the title to the end of "Grammatical changes". Each piece sits on its own line, numbered from p1.

Left out:

- The "Examples" section (Beowulf, The Voyages of Ohthere and Wulfstan, Ayenbite of Inwyt, The Canterbury Tales, Paradise Lost, Oliver Twist) and everything after it: See also, Notes, References, Further reading, External links. The small "Examples" table under "Phonological changes" stays.
- As in survey 001: hatnotes ("Main article: …", "See also: …", the redirect note), the English language sidebar, the timeline graphic, the short description, categories, language links, edit links, maintenance messages (the IPA notice and the "needs to be updated", "does not cite any sources" and "needs more citations" banners), and site menus and notices.

Kept as readers see them: footnote markers such as [3], [citation needed] tags, and superscript note numbers in tables (as in "whom, who1").

Changed:

- Non-breaking spaces are plain spaces, and repeated white space is one space. Line breaks inside a caption or a cell are spaces.
- Bold and italics are dropped; captions are in *italics*.
- Markdown marks show each piece's form: `# p1` title, `## p7`, `### p19` and `#### p89` headings, `p8 *…*` captions (image captions and table captions), `| p53 … |` table rows (cells joined by " | ", a separator line after each table's first row).

## fire list

fires.csv has a row for each *the*, *and* and *of* in text.md, as a whole word: 660 fires, *the* 352, *of* 168, *and* 140.

Not fires:

- **Words mentioned rather than used.** Where the text names a word instead of using it, the word isn't a fire. There are four:
  - p18: "did not have the definite article *the*" (the fifth *the* in p18)
  - p36: "Definite article þe appears around 1200, later spelled as *the*" (the fifth *the* in p36)
  - p39: "For some time þe (modern "*the*") was written as ye." (the eighth *the* in p39)
  - p103: "Usually replaced by *of* what" (the first *of* in p103)
- **Old and Middle English words.** Only modern English *the*, *and* and *of* are fires. Forms such as þe, se, seo and the letters þ and ð are not.

Fire IDs count fires only, so a mentioned word takes no ID: in p18 the mentioned *the* has none, and the next fire, "The Old English period…", is p18.the5.

If the list misses a fire or includes a word that isn't one, flag it as a list error, as survey.md says.

**original** is the sentence holding the fire. These pieces stand whole: the title, headings, table rows and table captions.

Elsewhere, a sentence ends at . ! ? or …, after any closing quote, bracket or footnote marker, where a space and then a capital letter follow, with or without an opening quote or bracket. The split skips these abbreviations: U.S., e.g., i.e., etc., vs., ca., No., Dr., Mr., Mrs., St., Inc., pp., p., ed.

## pins

This survey runs on mxtalk.md and sera.md at mxtalk/mxtalk `c716391c151c8302d6d69fd4fc3f943dc3b07691`, the fixes at mxtalk/sera `2f82021688b4593d7ef4989d1f3849cda014f2e8`, and survey.md at mxtalk/sera `5a201616bc4105ce1e5dce814aac0baae9cf0de1`, as survey 001 does.

## checksums

SHA-256:

- text.md `969060ad5cadbb1bd31f7c93f88d126f20566a5835fe69e520faa65f4a23e113`
- fires.csv `d0eebc9e079ab4fed3da7c4d248bc95a9a2ec7eae8510e6e7e587ff4f36e0d3f`
- source.txt `f4b6ab48c4dc073b9b7407d03aeb302d700d12fcbfb2fa6350034b7dacccbc80`
