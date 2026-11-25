#!/usr/bin/env python3
"""#89 Gray Code: the i-th code is i XOR (i >> 1); neighbours differ in exactly one bit.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged (the list comprehension is written
out as a loop so each step can be recorded).
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

N = 2                         # LeetCode example 1

# Hard examples (interactive page only), each breaking a plausible first attempt.
HARD_ROUND = 3                # flipping bits in turn (0, 1, 2, 0, 1, 2...) passes n = 1 and 2, then revisits 0
HARD_COUNT = 4                # counting 0, 1, 2, ... (= mirroring without reversing) changes 4 bits at 7 -> 8


class Solution:
    """The notebook's solution, to cross-check the traced run."""
    def grayCode(self, n: int) -> list[int]:
        return [i ^ (i >> 1) for i in range(1 << n)]


def round_robin(n):
    """First attempt: flip bit 0, then bit 1, ..., then bit 0 again, in turn."""
    seq = [0]
    for i in range((1 << n) - 1):
        seq.append(seq[-1] ^ (1 << (i % n)))
    return seq


def counting(n):
    """First attempt: count up, or mirror the list without reversing it (the same list)."""
    res = [0]
    for b in range(n):
        res += [x | (1 << b) for x in res]
    return res


def is_gray(seq, n):
    if seq[0] != 0 or sorted(seq) != list(range(1 << n)):
        return False
    return all(bin(seq[i] ^ seq[(i + 1) % len(seq)]).count('1') == 1 for i in range(len(seq)))


def bits(v, n):
    return [int(c) for c in format(v, f'0{n}b')]


def trace(n):
    events, out = [], []

    def rec(kind, **kw):
        events.append(dict(kind=kind, out=list(out), **kw))

    rec('start')
    # ---- the notebook's solution, with rec() calls added ----
    # return [i ^ (i >> 1) for i in range(1 << n)]
    for i in range(1 << n):
        g = i ^ (i >> 1)
        out.append(g)
        rec('code', i=i, g=g)
    rec('wrap')
    assert out == Solution().grayCode(n)
    return events


def build(n, subtitle, notes=None, wrong=None, wrong_name=''):
    notes = notes or {}
    size = 1 << n
    sc = Scene('#89 Gray Code: i XOR (i >> 1)', subtitle)
    legend = [(style('window')[1], 'i in binary'), (style('land')[1], 'i >> 1'), (style('good')[1], 'Gray code'),
              (ACTIVE, 'the one bit that changed')]
    flagged = False
    for e in trace(n):
        k, out = e['kind'], e['out']
        # the table of codes so far: one row per index, one column per bit
        rows = [bits(g, n) + [g] for g in out] + [[None] * (n + 1) for _ in range(size - len(out))]
        styles, rings = {}, []
        for r in range(len(out)):
            for c in range(n):
                styles[(r, c)] = 'good' if rows[r][c] else 'plain'
        if k == 'code' and e['i'] > 0:
            diff = out[-1] ^ out[-2]
            col = n - 1 - diff.bit_length() + 1
            rings.append(((e['i'], col), ACTIVE))
        if k == 'wrap' and size > 1:
            col = n - (out[-1] ^ out[0]).bit_length()
            rings += [((0, col), ACTIVE), ((size - 1, col), ACTIVE)]
        table = DPTableView(rows, row_labels=[f'{r}' for r in range(size)],
                            col_labels=[f'b{n - 1 - c}' for c in range(n)] + ['val'],
                            styles=styles, rings=rings, title='Codes so far (row = index i)', max_cell=34 if size <= 8 else 22)
        views = []
        if k == 'code':
            i, g = e['i'], e['g']
            views.append(ArrayView(bits(i, n), {c: 'window' for c in range(n)}, title=f'i      = {i:>2}', cell=48, indices=False))
            views.append(ArrayView(bits(i >> 1, n), {c: 'land' for c in range(n)}, title=f'i >> 1 = {i >> 1:>2}', cell=48, indices=False))
            views.append(ArrayView(bits(g, n), {c: 'good' for c in range(n)}, title=f'XOR    = {g:>2}', cell=48, indices=False))
        side = table
        if k == 'start':
            cap = f"n = {n}: list all {size} numbers of {n} bits, starting at 0, each one bit away from the last."
            sub, hold = notes.get('start', "Code number i is i XOR (i >> 1): compare i with itself shifted one place right."), KEY
            views.append(TextView(["XOR: 1 where the two bits differ, 0 where they match",
                                   ">> 1: shift right one place, dropping the last bit"], size=16))
        elif k == 'code':
            i, g = e['i'], e['g']
            if i == 0:
                cap, sub, hold = ("i = 0: 0 XOR 0 = 0. The list starts at 0, as required.", "", STEP)
            else:
                diff = out[-1] ^ out[-2]
                b = diff.bit_length() - 1
                cap = f"i = {i}: {format(i, f'0{n}b')} XOR {format(i >> 1, f'0{n}b')} = {format(g, f'0{n}b')} = {g}. Only bit {b} changed."
                sub = ""
                hold = STEP
                if i == size // 2:
                    sub = (f"i itself just changed {i.bit_length()} bits ({format(i - 1, f'0{n}b')} to {format(i, f'0{n}b')}), "
                           "but the XOR cancels all of them except the highest.")
                    hold = KEY
                elif i == 2:
                    sub = "Each Gray bit is (bit of i) XOR (the bit to its left). A carry flips both, so they cancel."
                    hold = KEY
                if wrong is not None and not flagged:
                    w = wrong[:i + 1]
                    bad_dup = len(set(w)) < len(w)
                    bad_bits = bin(w[-1] ^ w[-2]).count('1') != 1
                    if bad_dup or bad_bits:
                        flagged = True
                        why = ("a number it has already used" if bad_dup
                               else f"{bin(w[-1] ^ w[-2]).count('1')} bits away from {w[-2]}")
                        sub = f"{wrong_name} would put {w[-1]} here: {why}."
                        hold = KEY
        else:
            first, last = out[0], out[-1]
            cap = (f"The last code, {last} ({format(last, f'0{n}b')}), is one bit from the first, 0: the list wraps round too."
                   if size > 1 else "Done.")
            sub, hold = notes.get('done', f"Answer: {out}. One XOR per code: O(2^n) time, and the output itself is O(2^n)."), END
        sc.frame(views, cap, sub, hold, side=side,
                 counters={'codes': len(out)}, legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    assert is_gray(Solution().grayCode(HARD_ROUND), HARD_ROUND)
    assert is_gray(round_robin(1), 1) and is_gray(round_robin(2), 2) and not is_gray(round_robin(HARD_ROUND), HARD_ROUND)
    assert is_gray(Solution().grayCode(HARD_COUNT), HARD_COUNT) and not is_gray(counting(HARD_COUNT), HARD_COUNT)
    rr = round_robin(HARD_ROUND)
    a = build(HARD_ROUND, f'n = {HARD_ROUND}. Flipping bits in turn ({rr}) passes both samples, then comes back to 0.', {
        'start': "The bit to flip isn't 0, 1, 2, 0, 1, 2 in turn. Watch which bit changes: 0, 1, 0, 2, 0, 1, 0.",
        'done': f"Answer {Solution().grayCode(HARD_ROUND)}. Flipping bits in turn gives {rr}: it reaches 0 again after six steps.",
    }, wrong=rr, wrong_name='Flipping bits in turn (0, 1, 2, 0, ...)')
    b = build(HARD_COUNT, f'n = {HARD_COUNT}. Counting up (or mirroring without reversing) changes 4 bits at 7 -> 8.', {
        'start': "Counting changes several bits whenever there's a carry. The XOR keeps only one of them.",
        'done': "Answer: one bit changes every step. Counting 0..15 changes 2, 3 and even 4 bits at the carries.",
    }, wrong=counting(HARD_COUNT), wrong_name='Counting (or mirroring without reversing)')
    return [
        (a, f"n = 3: a first attempt that flips bit 0, then bit 1, then bit 2, in turn, gives [0,1] and [0,1,3,2] for the samples, "
            f"then {rr}, which repeats 0. The right order of flips is 0, 1, 0, 2, 0, 1, 0."),
        (b, "n = 4: a first attempt that counts up, which is also what mirroring the list without reversing it produces, "
            "changes two bits at 1 -> 2 and four at 7 -> 8. XOR with i >> 1 cancels every carry but one."),
    ]


def main():
    args = cli()
    sc = build(N, f'n = {N}. Return a sequence of all 2^n numbers where neighbours differ in exactly one bit.')
    finish(sc, 89, "Watch i = 2: counting from 01 to 10 changes two bits, but the XOR with i >> 1 cancels "
                   "the carried bit, so the Gray code changes only one.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
