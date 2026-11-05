#!/usr/bin/env python3
"""#29 Divide Two Integers: instead of subtracting the divisor once at a time,
keep doubling it until the next doubling would overshoot, subtract that, and
add the matching power of two to the quotient.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

DIVIDEND, DIVISOR = 10, 3                  # LeetCode example 1: answer 3

INT_MAX, INT_MIN = 2 ** 31 - 1, -(2 ** 31)
# Hard examples (interactive page only), each breaking a plausible first attempt.
# 1) Subtracting the divisor one at a time. Both LeetCode samples finish in a
#    handful of steps, but 2147483647 / 2 needs 1,073,741,823 subtractions.
#    Doubling needs 30 subtractions. Answer 1073741823.
HARD_BIG = (INT_MAX, 2)
# 2) No guard for INT_MIN / -1. Both samples pass; here the true quotient is
#    2^31, one more than a 32-bit int holds. Without the guard Python returns
#    2147483648 (and C#/Java wrap to -2147483648). Answer 2147483647.
HARD_MIN = (INT_MIN, -1)


class Solution:
    """The notebook's solution (comments dropped), to cross-check the traced run."""
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        negative = (dividend < 0) != (divisor < 0)
        dvd = abs(dividend)
        dvs = abs(divisor)
        quotient = 0
        while dvd >= dvs:
            shifted = dvs
            multiple = 1
            while dvd >= (shifted << 1):
                shifted <<= 1
                multiple <<= 1
            dvd -= shifted
            quotient += multiple
        return -quotient if negative else quotient


def one_at_a_time(dividend, divisor, cap):
    """First attempt: subtract |divisor| until it doesn't fit. Gives up after
    `cap` subtractions and returns None (it would need far more)."""
    if dividend == INT_MIN and divisor == -1:
        return INT_MAX
    negative = (dividend < 0) != (divisor < 0)
    dvd, dvs, q = abs(dividend), abs(divisor), 0
    while dvd >= dvs:
        dvd -= dvs
        q += 1
        if q > cap:
            return None
    return -q if negative else q


def trace(dividend, divisor, guard=True):
    """guard=False runs the same lines without the INT_MIN / -1 check."""
    events = []

    def rec(kind, **kw):
        events.append(dict(kind=kind, quotient=quotient, dvd=dvd, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    quotient, dvd = 0, None
    if guard and dividend == INT_MIN and divisor == -1:
        rec('guard', ans=INT_MAX)
        return events
    negative = (dividend < 0) != (divisor < 0)
    dvd = abs(dividend)
    dvs = abs(divisor)
    quotient = 0
    rec('sign', negative=negative, dvs=dvs, guard=guard)
    while dvd >= dvs:
        shifted = dvs
        multiple = 1
        rungs = [(shifted, multiple)]                       # display only
        while dvd >= (shifted << 1):
            shifted <<= 1
            multiple <<= 1
            rungs.append((shifted, multiple))
            rec('double', dvs=dvs, rungs=rungs[:], shifted=shifted, multiple=multiple)
        rec('top', dvs=dvs, rungs=rungs[:], shifted=shifted, multiple=multiple, over=shifted << 1)
        dvd -= shifted
        quotient += multiple
        rec('take', dvs=dvs, rungs=rungs[:], shifted=shifted, multiple=multiple)
    ans = -quotient if negative else quotient
    rec('done', dvs=dvs, ans=ans, negative=negative, guard=guard)
    if guard:
        assert ans == Solution().divide(dividend, divisor)
    return events


def fmt(x):
    return f'{x:,}'


def mult(m):
    k = m.bit_length() - 1
    return f'×{m}' if m < 1024 else f'×2^{k}'


def build(dividend, divisor, subtitle, notes=None, quick_doubling=False, unguarded=False):
    notes = notes or {}
    sc = Scene('#29 Divide Two Integers: double, then subtract', subtitle)
    legend = [(style('window')[1], 'divisor doubled'), (style('good')[1], 'biggest that fits'),
              (style('bad')[1], 'next doubling: too big')]
    seen = set()
    events = trace(dividend, divisor)
    if unguarded:
        events = events + [dict(e, wrong=True) for e in trace(dividend, divisor, guard=False)]
    small = abs(dividend) <= 200
    passes = 0
    for idx, e in enumerate(events):
        k = e['kind']
        if quick_doubling and k == 'double':
            continue
        if k == 'take':
            passes += 1
        main = []
        rungs = e.get('rungs')
        if rungs:
            show = rungs[-6:]
            vals = [mult(m) for _, m in show]
            subs = {i: (fmt(s) if s < 10 ** 6 else '') for i, (s, _) in enumerate(show)}
            styles = {i: 'window' for i in range(len(show))}
            if k in ('top', 'take'):
                styles[len(show) - 1] = 'good'
            if k == 'top':
                vals.append(mult(e['multiple'] * 2))
                subs[len(show)] = fmt(e['over']) if e['over'] < 10 ** 6 else ''
                styles[len(show)] = 'bad'
            title = 'divisor' + (' (last 6)' if len(rungs) > 6 else '')
            main.append(ArrayView(vals, styles, indices=False, subs=subs, title=title))
        if small and e['dvd'] is not None:
            bars = [(0, e['dvd'], f"left {e['dvd']}", 'plain')]
            if k in ('double', 'top') and rungs:
                bars.append((0, e['shifted'], f"{e['shifted']}", 'good' if k == 'top' else 'window'))
            main.append(IntervalView(bars, lo=0, hi=abs(dividend), title='what is left to divide'))
        lines = []
        if k == 'take':
            lines = [f"left: {fmt(e['dvd'] + e['shifted'])} - {fmt(e['shifted'])} = {fmt(e['dvd'])}",
                     f"quotient: {fmt(e['quotient'] - e['multiple'])} + {fmt(e['multiple'])} = {fmt(e['quotient'])}"]
        elif k == 'top':
            lines = [f"{fmt(e['shifted'])} fits in {fmt(e['dvd'])}; {fmt(e['over'])} would not"]
        elif k == 'done':
            lines = [f"answer: {fmt(e['ans'])}", f"32-bit range: {fmt(INT_MIN)} to {fmt(INT_MAX)}"]
        elif k == 'guard':
            lines = [f"true answer: 2^31 = {fmt(2 ** 31)}", f"largest 32-bit int: {fmt(INT_MAX)}"]
        main.append(TextView(lines or [''], size=17))
        rows = []
        if e['dvd'] is not None:
            rows = [('dvd (left)', fmt(e['dvd'])), ('dvs', fmt(e.get('dvs', abs(divisor)))),
                    ('quotient', fmt(e['quotient']), 'good')]
            if k in ('double', 'top', 'take'):
                rows += [('shifted', fmt(e['shifted']), 'window'), ('multiple', fmt(e['multiple']), 'window')]
        if k == 'guard':
            rows = [('dividend', fmt(dividend)), ('divisor', fmt(divisor)), ('return', fmt(e['ans']), 'good')]
        if k == 'done':
            rows.append(('answer', fmt(e['ans']), 'bad' if e.get('wrong') else 'good'))
        cap, sub, hold = words(e, dividend, divisor, seen, passes)
        key = (k, passes) if k in ('take', 'top') else (k + ('_wrong' if e.get('wrong') else ''))
        if key in notes:
            sub, hold = notes[key], (END if k == 'done' else KEY)
        sc.frame(main, cap, sub, hold, side=MapView(rows, 'State', headers=('', '')),
                 counters={'subtractions': passes}, legend=legend)
    return sc


def words(e, dividend, divisor, seen, passes):
    k = e['kind']
    if k == 'guard':
        return (f"{fmt(dividend)} / -1 is 2^31, one more than a 32-bit int can hold.",
                "This is the only overflowing case, so return 2^31 - 1 straight away.", KEY)
    if k == 'sign':
        if e.get('wrong'):
            return ("Now the same loop WITHOUT that check.", "", KEY)
        neg = 'negative' if e['negative'] else 'positive'
        return (f"Signs differ: the answer is {neg}." if e['negative'] else "Same signs: the answer is positive.",
                f"Divide the sizes, {fmt(abs(dividend))} by {fmt(e['dvs'])}, and put the sign back at the end.", STEP)
    if k == 'double':
        first = 'double' not in seen
        seen.add('double')
        return (f"{fmt(e['shifted'])} still fits: double again (×{fmt(e['multiple'])}).",
                "Doubling is a left shift, which is allowed. Multiplying isn't." if first else "",
                KEY if first else QUICK * 2.5)
    if k == 'top':
        first = 'top' not in seen
        seen.add('top')
        return (f"Doubling again gives {fmt(e['over'])}, more than the {fmt(e['dvd'])} left. Stop at {fmt(e['shifted'])}.",
                "Take the biggest doubled divisor that fits, all in one go." if first else "",
                KEY if first else QUICK * 2.5)
    if k == 'take':
        first = 'take' not in seen
        seen.add('take')
        return (f"Subtract {fmt(e['shifted'])}: that's {fmt(e['multiple'])} divisor{'s' if e['multiple'] > 1 else ''} at once.",
                "Each pass removes the top bit of what's left, so there are only about 31 passes."
                if first else "", KEY if first else (STEP if passes < 4 else QUICK * 2))
    if e.get('wrong'):
        return (f"Without the check it returns {fmt(e['ans'])}: too big for a 32-bit int.",
                "Python just prints it; C# and Java wrap it round to -2,147,483,648.", END)
    return (f"{fmt(e['dvd'])} left is less than {fmt(e['dvs'])}. Answer: {fmt(e['ans'])}.",
            f"{passes} subtraction{'s' if passes != 1 else ''} instead of {fmt(abs(e['ans']))}.", END)


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    for a, b, want in ((10, 3, 3), (7, -3, -2)):      # both first attempts pass both samples
        assert Solution().divide(a, b) == want == one_at_a_time(a, b, 10 ** 6)
        assert trace(a, b, guard=False)[-1]['ans'] == want
    assert Solution().divide(*HARD_BIG) == 1073741823
    assert one_at_a_time(*HARD_BIG, cap=10 ** 6) is None      # still going after a million subtractions
    assert Solution().divide(*HARD_MIN) == INT_MAX
    assert trace(*HARD_MIN, guard=False)[-1]['ans'] == 2 ** 31   # out of 32-bit range
    big = build(*HARD_BIG, 'dividend = 2,147,483,647, divisor = 2. Answer 1,073,741,823 in 30 subtractions.', {
        ('take', 1): "That one subtraction removed 1,073,741,824 at once. Subtracting 2 at a time "
                     "would take 536,870,912 steps to get this far.",
        'done': "30 subtractions. Subtracting the divisor one at a time needs 1,073,741,823 of them and "
                "times out; it's still going after the first million.",
    }, quick_doubling=True)
    mn = build(*HARD_MIN, 'dividend = -2,147,483,648, divisor = -1. Answer 2,147,483,647 (clamped).', {
        'done_wrong': "2,147,483,648 doesn't fit in 32 bits. The guard is the only thing that keeps the answer in range.",
    }, unguarded=True, quick_doubling=True)
    return [
        (big, "The biggest dividend over 2. Subtracting 2 one at a time passes both LeetCode samples, then needs "
              "over a billion steps here. Doubling needs 30; the answer is 1,073,741,823."),
        (mn, "INT_MIN / -1: the true answer, 2^31, doesn't fit in a 32-bit int. Leave out the guard and both samples "
             "still pass, but this returns 2,147,483,648; the answer is clamped to 2,147,483,647."),
    ]


def main():
    args = cli()
    sc = build(DIVIDEND, DIVISOR, f'dividend = {DIVIDEND}, divisor = {DIVISOR}. No *, / or %: only shifts, '
                                  'adds and subtracts.')
    finish(sc, 29, "Watch the first pass: 3 doubles to 6, doubling again to 12 would overshoot 10, so 6 comes off "
                   "in one go and 2 goes on the quotient.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
