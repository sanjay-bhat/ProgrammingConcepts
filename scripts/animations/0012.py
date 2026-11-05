#!/usr/bin/env python3
"""#12 Integer to Roman: treat the six two-letter forms (CM, CD, XC, XL, IX, IV)
as coins of their own, then make change largest coin first.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. Runs of coins that are too big are
merged into one frame, since nothing happens at them.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

NUM = 1994                     # LeetCode example 3: "MCMXCIV"

# Hard example (interactive page only). A table typed from memory that leaves
# out CD (400) passes all three LeetCode samples (3749, 58, 1994 never need a
# 400) and then writes 444 as "CCCCXLIV". Answer "CDXLIV": every place is a 4.
HARD = 444

VALUES = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
SYMBOLS = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
PAIRS = {"CM", "CD", "XC", "XL", "IX", "IV"}


class Solution:
    """The notebook's solution (comments dropped), to cross-check the traced run."""
    def intToRoman(self, num: int) -> str:
        values  = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        result = []
        for value, symbol in zip(values, symbols):
            while num >= value:
                result.append(symbol)
                num -= value
        return "".join(result)


def without_cd(num):
    """First attempt: the same greedy loop over a table that forgot CD (400)."""
    result = []
    for value, symbol in zip(VALUES, SYMBOLS):
        if symbol == "CD":
            continue
        while num >= value:
            result.append(symbol)
            num -= value
    return "".join(result)


def trace(num):
    events = []
    start = num

    def rec(kind, **kw):
        events.append(dict(kind=kind, num=num, result=result[:], **kw))

    # ---- the notebook's solution, with rec() calls added ----
    values  = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    result = []
    rec('start', k=None)
    for k, (value, symbol) in enumerate(zip(values, symbols)):
        if not num >= value:                                      # display only
            rec('skip', k=k)
        while num >= value:
            result.append(symbol)
            num -= value
            rec('take', k=k)
    rec('done', k=None, ans="".join(result))
    assert "".join(result) == Solution().intToRoman(start)
    return events


def merged(events):
    """Fold each run of 'skip' events into one."""
    out = []
    for e in events:
        if e['kind'] == 'skip' and out and out[-1]['kind'] == 'skip':
            out[-1]['ks'].append(e['k'])
        else:
            out.append(dict(e, ks=[e['k']]) if e['kind'] == 'skip' else e)
    return out


def build(num, subtitle, notes=None):
    notes = notes or {}
    sc = Scene('#12 Integer to Roman: biggest coin first', subtitle)
    legend = [(ACTIVE, 'coin being used'), (style('good')[1], 'used'), (style('muted')[1], 'too big, passed'),
              (style('gold')[1], 'two-letter coin')]
    used, passed = set(), set()
    seen = set()
    start = num
    for e in merged(trace(num)):
        k = e['kind']
        styles = {i: 'gold' for i, s in enumerate(SYMBOLS) if s in PAIRS}
        for i in passed:
            styles[i] = 'muted'
        for i in used:
            styles[i] = 'good'
        ptrs = {}
        if k == 'skip':
            passed.update(e['ks'])
            for i in e['ks']:
                styles[i] = 'muted'
            ptrs = {'too big': e['ks'][-1]} if len(e['ks']) == 1 else {'skip': e['ks'][0], 'to': e['ks'][-1]}
        elif k == 'take':
            used.add(e['k'])
            styles[e['k']] = 'active'
            ptrs = {'use': e['k']}
        coins = ArrayView(VALUES, styles, ptrs, title='coin', subs={i: s for i, s in enumerate(SYMBOLS)},
                          indices=False)
        res = ''.join(e['result'])
        chips = ChipsView([(s, 'gold' if s in PAIRS else 'good') for s in e['result']],
                          title='result, symbol by symbol', empty='(nothing yet)', size=17)
        left = TextView([f'num left: {e["num"]}', f'written so far: "{res}"'], size=18)
        cap, sub, hold = words(e, start, seen)
        key = (k, e['k'], e['num']) if k == 'take' else k
        if key in notes:
            sub, hold = notes[key], (END if k == 'done' else KEY)
        sc.frame([coins, left, chips], cap, sub, hold, counters={'num left': e['num']}, legend=legend)
    return sc


def words(e, start, seen):
    k = e['kind']
    if k == 'start':
        return (f"Write {start} in Roman numerals. The 13 coins are sorted biggest first.",
                "The gold ones are the two-letter forms. Treat each as a coin of its own.", KEY)
    if k == 'skip':
        ks = e['ks']
        if len(ks) == 1:
            return (f"{SYMBOLS[ks[0]]} = {VALUES[ks[0]]} is bigger than {e['num']}. Move on.", "", QUICK * 2)
        return (f"{', '.join(SYMBOLS[i] for i in ks)} are all bigger than {e['num']}. Move past them.",
                "", QUICK * 2.5)
    if k == 'take':
        i = e['k']
        sym, val = SYMBOLS[i], VALUES[i]
        cap = f"{sym} = {val} fits: write {sym}, {e['num'] + val} - {val} = {e['num']} left."
        if sym in PAIRS and 'pair' not in seen:
            seen.add('pair')
            return (cap, f"{sym} is one coin worth {val}, so {val} never needs four or five letters. "
                         "Greedy just picks it like any other coin.", KEY)
        if e['num'] >= val and 'repeat' not in seen:
            seen.add('repeat')
            return (cap, f"Still {e['num']} left and {sym} still fits, so stay on it: it's a while, not an if.", KEY)
        return (cap, "", STEP)
    return (f"num is 0. {start} = \"{e['ans']}\".",
            "At most 15 symbols for any num up to 3999, so the work is constant.", END)


def hard():
    """Harder input for the interactive page (scripts/motion_build.py)."""
    for n, want in ((3749, "MMMDCCXLIX"), (58, "LVIII"), (1994, "MCMXCIV")):
        assert Solution().intToRoman(n) == without_cd(n) == want     # the slip passes every sample
    assert Solution().intToRoman(HARD) == "CDXLIV" and without_cd(HARD) == "CCCCXLIV"
    sc = build(HARD, f'num = {HARD}. Answer "CDXLIV". A table without CD writes "CCCCXLIV".', {
        ('take', 3, 44): "Leave CD out of the table and C fits four times here: \"CCCC\", which isn't a Roman numeral.",
        'done': "CDXLIV: every place is a 4. A table that forgot CD passes all three LeetCode samples, "
                "then writes CCCCXLIV here.",
    })
    return sc, ("444: every place is a 4, so it needs CD, XL and IV. A table typed from memory without CD "
                "passes all three LeetCode samples, none of which has a 400, then writes \"CCCCXLIV\".")


def main():
    args = cli()
    sc = build(NUM, f'num = {NUM}. Take the biggest coin that fits, as many times as it fits.')
    finish(sc, 12, "Watch the CM coin: 900 is in the table as a single coin, so after M the greedy loop takes it "
                   "straight away instead of writing DCCCC.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
