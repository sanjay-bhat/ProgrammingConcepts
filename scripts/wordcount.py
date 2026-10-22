#!/usr/bin/env python3
"""Word counts for the prose sections, checked against the difficulty bands.

    python3 scripts/wordcount.py 200 1 146        # specific notebooks
    python3 scripts/wordcount.py --all            # every notebook with the sections

Counts prose only: fenced code blocks and markdown punctuation are stripped,
so a whiteboard snippet doesn't eat the budget. The bands live in
.claude/CLAUDE.md; keep BANDS below in sync with that table.
"""
import argparse
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nbcells  # noqa: E402

# (newbie, interview) word ranges per difficulty. Easy problems get the
# shortest sections; the pilot ran Two Sum longest, which is backwards.
BANDS = {
    'Easy':   ((300, 450), (800, 1100)),
    'Medium': ((350, 500), (1000, 1500)),   # #200, the reference, is ~1450
    'Hard':   ((450, 650), (1200, 1800)),
}
PRIMER_ALLOWANCE = 150   # extra newbie words when it opens with a data-structure primer

FENCE = re.compile(r'```.*?```', re.S)
WORD = re.compile(r"[A-Za-z0-9][A-Za-z0-9'’×\-]*")


def words(md):
    return len(WORD.findall(FENCE.sub(' ', md)))


def load_difficulties(root):
    """{problem number: 'Easy'|'Medium'|'Hard'} from tracker.html.

    The notebooks don't state difficulty; the tracker is the only record.
    Rows whose title is a bare number (#293 and #485 were mangled into
    `n:1,t:"293"`) are skipped, and the first good row for a number wins.
    """
    with open(os.path.join(root, 'tracker.html')) as f:
        html = f.read()
    out = {}
    for n, t, d in re.findall(
            r'\bn:(\d+),t:"([^"]*)"[^{}]*?\bd:"(easy|medium|hard)"', html):
        if not t.isdigit():
            out.setdefault(int(n), d.capitalize())
    return out


def report(path, diffs):
    nb = nbcells.load(path)
    num = int(os.path.basename(path)[:4])
    diff = diffs.get(num)
    out = []
    for name, find, k in (('newbie', nbcells.find_newbie, 0),
                          ('interview', nbcells.find_interview, 1)):
        i = find(nb)
        if i is None:
            continue
        md = nbcells.text(nb['cells'][i])
        n = words(md)
        lo, hi = BANDS[diff][k] if diff else (0, 10**9)
        if k == 0 and re.search(r'^#+ .*primer', md, re.I | re.M):
            hi += PRIMER_ALLOWANCE
        flag = '' if lo <= n <= hi else ('  SHORT' if n < lo else '  LONG')
        out.append(f'{name} {n}' + (f' ({lo}-{hi}){flag}' if diff else ''))
    if out:
        print(f'#{num:<5} {diff or "?":<7} ' + ' | '.join(out))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('nums', nargs='*', type=int)
    ap.add_argument('--all', action='store_true')
    args = ap.parse_args()
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    root = os.path.join(repo, 'leetcode')
    diffs = load_difficulties(repo)
    paths = (sorted(glob.glob(os.path.join(root, '????.ipynb'))) if args.all
             else [os.path.join(root, f'{n:04d}.ipynb') for n in args.nums])
    for p in paths:
        report(p, diffs)


if __name__ == '__main__':
    main()
