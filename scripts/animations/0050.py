#!/usr/bin/env python3
"""#50 Pow(x, n): read n one binary digit at a time. x keeps squaring
(x, x², x⁴, x⁸, ...) and result picks up the powers whose digit is 1.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

X, N = 2.0, 10                    # LeetCode example 1: 1024.0

# The hard example (interactive page only): x = 2, n = -2^31, the smallest
# allowed exponent. The answer is 2^-2147483648, which is 0.0 as a double.
# First attempt it breaks: negating n in a 32-bit int (C#/Java `int`, Rust i32
# with wrapping). -(-2^31) doesn't fit, wraps back to -2^31, the loop never
# runs, and the function returns 1.0. It passes all three LeetCode samples.
# The other first attempt, multiplying by x |n| times, would need 2,147,483,648
# multiplications here; this loop runs 32 times.
HARD_X, HARD_N = 2.0, -2 ** 31
HARD_NOTES = {
    'flip': "n is now 2,147,483,648, one more than a 32-bit int can hold. Negating it in an int wraps back to -2^31.",
    ('skip', 10): "x is now 0.5^1024, about 5.6e-309, nearly the smallest number a double can hold.",
    ('skip', 11): "Squaring again gives 0.5^2048, too small for a double: x is exactly 0 from here on.",
    ('take', 31): "The only 1 is the top digit, so result picks up x once: 0.5^(2^31), which is 0.",
    'done': "0.0, in 32 rounds. A 32-bit negation returns 1.0; multiplying |n| times needs 2^31 steps.",
}


def int32_negation_attempt(x, n):
    """First attempt: the same loop, but n is a 32-bit int, so -n can overflow."""
    if n < 0:
        x = 1.0 / x
        n = -n
        if n >= 2 ** 31:                  # what a 32-bit int does with 2^31
            n -= 2 ** 32
    result = 1.0
    while n > 0:
        if n & 1:
            result *= x
        x *= x
        n >>= 1
    return result


def trace(x, n):
    events = []
    base, sign, k, rexp = x, 1, 0, 0          # display only: x == base^(sign * 2^k)

    def rec(kind, **kw):
        events.append(dict(kind=kind, k=k, sign=sign, rexp=rexp, **kw))

    rec('start', x=x, n=n, result=None)
    # ---- the notebook's solution, with rec() calls added ----
    if n < 0:
        x = 1.0 / x
        n = -n
        sign = -1
        rec('flip', x=x, n=n, result=None)
    total = n
    result = 1.0
    while n > 0:
        if n & 1:
            result *= x
            rexp += sign * 2 ** k
            rec('take', x=x, n=n, result=result)
        else:
            rec('skip', x=x, n=n, result=result)
        x *= x
        n >>= 1
        k += 1
    rec('done', x=x, n=n, result=result)
    return events, result, total, base


def num(v):
    if v is None:
        return '-'
    if v == 0:
        return '0.0'
    return f'{v:.6g}' if (abs(v) < 1e-4 or abs(v) >= 1e6) else f'{v:g}'


def power(base, e):
    b = f'{base:g}'
    return f'{b}^{e}' if e != 1 else b


def words(e, base, notes):
    k = e['kind']
    key = k if k in ('start', 'flip', 'done') else (k, e['k'])
    cap, sub, hold = _words(e, base)
    if notes and key in notes:
        return cap, notes[key], (END if k == 'done' else KEY)
    return cap, sub, hold


def _words(e, base):
    k, d = e['kind'], e['k']
    xs = power(base, e['sign'] * 2 ** d)
    if k == 'start':
        return (f"Compute {base:g}^{e['n']}. Write the exponent in binary: {bin(e['n'])[2:] if e['n'] >= 0 else '-' + bin(-e['n'])[2:]}.",
                "Every power you need is a square of the one before: x, x², x⁴, x⁸, ...", KEY)
    if k == 'flip':
        return (f"n is negative: use 1/x = {num(e['x'])} and make n positive.",
                "x^-n is (1/x)^n, so the loop only ever sees a positive exponent.", KEY)
    if k == 'take':
        cap = f"Digit {d} is 1: result *= x ({xs}), so result = {num(e['result'])}. Then square x."
        sub = ("A 1 digit means this power is part of the answer; a 0 digit means skip it." if d == 0 or e['first']
               else "")
        return cap, sub, KEY if sub else STEP
    if k == 'skip':
        cap = f"Digit {d} is 0: x ({xs}) isn't part of the answer. Just square x."
        return cap, "", QUICK * 2 if e['n'] > 64 else STEP
    return (f"No digits left. Answer: {num(e['result'])}.",
            f"{e['k']} rounds of the loop, one per binary digit of n, instead of {e['total']:,} multiplications.", END)


def build(x, n, subtitle, notes=None):
    events, ans, total, base = trace(x, n)
    width = max(1, total.bit_length())
    sc = Scene(f'#50 Pow(x, n): x = {x:g}, n = {n:,}', subtitle)
    legend = [(ACTIVE, 'digit being read'), (style('good')[1], 'digit 1: used'), (style('muted')[1], 'already read')]
    first_take = True
    for e in events:
        e['total'] = total
        e['first'] = False
        if e['kind'] == 'take':
            e['first'], first_take = first_take, False
        reading = e['k'] if e['kind'] in ('take', 'skip') else None
        digits = [(total >> b) & 1 for b in range(width - 1, -1, -1)] if e['kind'] != 'start' or n >= 0 else \
                 [(-n >> b) & 1 for b in range(width - 1, -1, -1)]
        styles = {}
        for i, dgt in enumerate(digits):
            b = width - 1 - i
            if e['kind'] == 'done' or (reading is not None and b < reading):
                styles[i] = 'good' if dgt else 'muted'
            if reading is not None and b == reading:
                styles[i] = 'active'
        if width <= 12:
            bits = ArrayView([str(d) for d in digits], styles=styles, title='n in binary',
                             subs={i: f'2^{width - 1 - i}' for i in range(width)}, indices=False,
                             pointers={'reading': width - 1 - reading} if reading is not None else {}, cell=58)
        else:
            per = 8
            nrows = -(-width // per)
            pad = nrows * per - width
            flat = [None] * pad + digits
            cells = [[None if flat[r * per + c] is None else
                      {'style': styles.get(r * per + c - pad, 'plain'), 'label': str(flat[r * per + c])}
                      for c in range(per)] for r in range(nrows)]
            rings = [((divmod(width - 1 - reading + pad, per)), ACTIVE, 4)] if reading is not None else []
            bits = GridView(cells, outlines=rings, bridges=False, indices=False, cell=40)
        rows = [('x now holds', power(base, e['sign'] * 2 ** e['k']) if e['kind'] != 'start' else f'{base:g}'),
                ('x', num(e['x'])),
                ('n left', f"{e['n']:,}" if e['kind'] != 'start' else f"{n:,}"),
                ('result', num(e['result']) if e['result'] is not None else '1 (not set yet)', 'good'),
                ('result is', power(base, e['rexp']) if e['rexp'] else '-', 'gold')]
        cap, sub, hold = words(e, base, notes)
        sc.frame([TextView([f'answer = product of the powers whose digit is 1'], size=15), bits], cap, sub, hold,
                 side=MapView(rows, 'Variables', headers=('', '')),
                 counters={'rounds done': e['k']}, legend=legend)
    return sc


def hard():
    """Harder input for the interactive page (scripts/motion_build.py)."""
    for x, n in ((2.0, 10), (2.1, 3), (2.0, -2)):               # LeetCode samples
        assert abs(int32_negation_attempt(x, n) - trace(x, n)[1]) < 1e-9
    assert trace(HARD_X, HARD_N)[1] == 0.0
    assert int32_negation_attempt(HARD_X, HARD_N) == 1.0
    sc = build(HARD_X, HARD_N, 'The smallest allowed exponent. Its 32 binary digits are shown in rows of 8, highest digit first.',
               HARD_NOTES)
    return sc, ("n = -2^31. Negating it in a 32-bit int overflows back to -2^31, so that version skips the loop "
                "and returns 1.0 while passing all three samples. Here the loop runs 32 times and returns 0.0.")


def main():
    args = cli()
    sc = build(X, N, '10 is 1010 in binary, so 2^10 = 2^8 × 2^2. The loop reads the digits right to left.')
    finish(sc, 50, "Watch result only change on the 1 digits of 1010: it picks up 2² = 4, then 2⁸ = 256, "
                   "while x squares every round.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
