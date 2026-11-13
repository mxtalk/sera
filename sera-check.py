"""sera pass checker: checks a pass against survey.md's mechanical rules.
Usage: python3 -I sera-check.py fires.csv pass.csv [pass.md]
Errors break a rule survey.md states. Warnings need a human look (templates, odd repairs).
Judgment (are the reasons right?) stays with spot-checks. Thresholds are a first guess; tune them."""
import csv, collections, difflib, re, sys

TAO = {"the", "and", "of"}
FIRE = re.compile(r"\[(the|and|of)\]", re.I)
IDS = re.compile(r"\bp\d+\.(?:the|and|of)\d+\b")
HEADER = ["fire", "fix", "original", "verdict", "repair", "reasoning", "list_error"]
MD_FIELDS = ["task", "surveyor", "model", "thinking", "harness", "human", "date", "read"]
TEMPLATE_WARN = 0.30   # share of non-fixed-wording rows covered by the five commonest reason templates

def toks(s): return re.findall(r"[A-Za-z0-9'’]+|[^\sA-Za-z0-9'’]", s)
def words(s): return len(s.split())
def template(s):
    s = re.sub(r"“[^”]*”", "“…”", s); s = re.sub(r'"[^"]*"', '"…"', s); s = re.sub(r"'[^']*'", "'…'", s)
    return IDS.sub("pID", s).strip().lower()
def split_fire(orig):
    m = list(FIRE.finditer(orig))
    if len(m) != 1: return None, None
    t = toks(orig[:m[0].start()] + "" + orig[m[0].end():]); i = t.index(""); t[i] = m[0].group(1)
    return t, i

def main(fires_path, pass_path, md_path=None):
    err, warn = [], []
    src = list(csv.reader(open(fires_path, encoding="utf-8-sig", newline="")))
    dst = list(csv.reader(open(pass_path, encoding="utf-8-sig", newline="")))
    if [h.strip() for h in dst[0]] != HEADER: err.append(f"header is {dst[0]}")
    if len(dst) != len(src): err.append(f"{len(dst)-1} rows, fire list has {len(src)-1}")
    where = collections.defaultdict(dict)          # (piece, plain sentence) -> {token index: fire ID}
    for r in src[1:]:
        t, i = split_fire(r[2])
        if t: where[(r[0].split(".")[0], " ".join(t).lower())][i] = r[0]
    counts = collections.Counter(); per_fix = collections.defaultdict(list); longest = 0
    for s, d in zip(src[1:], dst[1:]):
        fid = s[0]
        if len(d) != 7: err.append(f"{fid}: {len(d)} columns"); continue
        if d[:3] != s[:3]: err.append(f"{fid}: sera's cells changed")
        v, rep, why, le = d[3].strip(), d[4].strip(), d[5].strip(), d[6].strip()
        counts[(s[1], v or "blank")] += 1
        if le not in ("", "yes"): err.append(f"{fid}: list_error is '{le}'")
        if v not in ("clear", "repaired") and not (v == "" and le == "yes"): err.append(f"{fid}: verdict '{v}'")
        if not why: err.append(f"{fid}: no reasoning")
        longest = max(longest, words(why))
        if words(why) > 50: err.append(f"{fid}: reasoning {words(why)} words")
        fixed = "fixed wording" in why.lower()
        if fixed and v == "repaired": err.append(f"{fid}: fixed wording but repaired")
        if not fixed and why: per_fix[s[1]].append(why)
        if v == "clear" and rep: warn.append(f"{fid}: clear but has a repair")
        if v != "repaired": continue
        if not rep: err.append(f"{fid}: repaired without a repair"); continue
        if FIRE.search(rep): err.append(f"{fid}: repair keeps the fire's brackets")
        t, i = split_fire(s[2])
        if not t: continue
        a, b = [x.lower() for x in t], [x.lower() for x in toks(rep)]
        if a == b: err.append(f"{fid}: repair is the original"); continue
        changed, touched = set(), set()   # touched: tokens replaced or deleted; changed also marks insert points
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
            if op != "equal": changed.update(range(i1, i2 + (1 if op == "insert" else 0)))
            if op in ("replace", "delete"): touched.update(range(i1, i2))
        if not any(abs(c - i) <= 1 for c in changed): warn.append(f"{fid}: repair doesn't change anything at the fire")
        others = where.get((fid.split(".")[0], " ".join(t).lower()), {})
        named = set(IDS.findall(why))
        for j, oid in others.items():
            if j != i and j < len(a) and j in touched and oid not in named:
                err.append(f"{fid}: changes {oid} without naming it")
        for m in re.finditer(r"\b(\w+)\s+\1\b", rep.lower()):
            if m.group(0) not in " ".join(a): warn.append(f"{fid}: doubled word '{m.group(0)}'")
    # templates: reasons that differ only in quoted stretches
    allr = [w for ws in per_fix.values() for w in ws]
    if allr:
        tc = collections.Counter(template(w) for w in allr)
        share = sum(n for _, n in tc.most_common(5)) / len(allr)
        line = f"templates: {len(tc)} across {len(allr)} non-fixed rows; top five cover {share:.0%}"
        (warn.append if share > TEMPLATE_WARN else print)(line)
        for fix, ws in sorted(per_fix.items()):
            t2 = collections.Counter(template(w) for w in ws)
            top, n = t2.most_common(1)[0]
            if n / len(ws) > TEMPLATE_WARN: warn.append(f"{fix}: one template on {n} of {len(ws)} rows: {top[:90]}")
    if md_path:
        md = open(md_path, encoding="utf-8").read()
        for f in MD_FIELDS:
            if not re.search(rf"^{f}:", md, re.M): err.append(f"pass .md lacks '{f}:'")
    v_by_fix = {fx: {k[1]: n for k, n in counts.items() if k[0] == fx} for fx in ("the", "and", "of")}
    print(f"rows: {len(dst)-1}  verdicts: {v_by_fix}  longest reasoning: {longest} words")
    for e in err: print("ERROR  ", e)
    for w in warn: print("WARN   ", w)
    print(f"{'PASSES CHECKS' if not err else 'FAILS CHECKS'}: {len(err)} errors, {len(warn)} warnings")
    return 1 if err else 0

if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:4]))
