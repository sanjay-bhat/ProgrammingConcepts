#!/usr/bin/env python3
"""#60 Permutation Sequence: the arrangements come in equal blocks by first
digit, so k // (block size) picks each digit directly.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import math
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

N, K = 4, 9   # LeetCode example 2: "2314"

# The hard example (interactive page only): n = 5, k = 48, answer "25431", the
# LAST arrangement that starts with 2. Dividing the one-based k skips the minus
# one: 48 // 24 = 2 picks the 3, and the answer comes out "31245".
HARD_N, HARD_K = 5, 48
HARD_NOTES = {
    ('choose', 4): "k = 47 is the very last slot of block 1 (24–47), the block that starts with 2. One-based, "
                   "48 // 24 = 2 would pick the 3: the last arrangement of a block lands in the next one.",
    'done': "The last arrangement starting with 2. Without the minus one the first division is off by one block "
            "and the answer is 31245.",
}


class Solution:
    """The notebook's solution, to cross-check the traced run."""
    def getPermutation(self, n, k):
        digits = list(range(1, n + 1))
        k -= 1
        result = []
        for i in range(n - 1, -1, -1):
            block = math.factorial(i)
            idx = k // block
            result.append(str(digits[idx]))
            digits.pop(idx)
            k %= block
        return ''.join(result)


def one_based(n, k):
    """First attempt: divide k as given, without converting to zero-based."""
    digits, result = list(range(1, n + 1)), []
    for i in range(n - 1, -1, -1):
        block = math.factorial(i)
        idx = k // block
        result.append(str(digits[idx]))
        digits.pop(idx)
        k %= block
    return ''.join(result)


def trace(n, k):
    events = []
    k_in = k

    def rec(kind, **kw):
        events.append(dict(kind=kind, digits=list(digits), k=k, result=list(result), **kw))

    # ---- the notebook's solution, with rec() calls added ----
    digits = list(range(1, n + 1))
    result = []
    rec('given')
    k -= 1
    rec('zero')
    for i in range(n - 1, -1, -1):
        block = math.factorial(i)
        idx = k // block
        rec('choose', i=i, block=block, idx=idx)
        result.append(str(digits[idx]))
        digits.pop(idx)
        k %= block
        rec('take', i=i, block=block, idx=idx)
    rec('done')
    assert ''.join(result) == Solution().getPermutation(n, k_in)
    return events


def build(n, k, subtitle, notes=None):
    notes = notes or {}
    sc = Scene('#60 Permutation Sequence: which block is k in?', subtitle, side_width=280)
    legend = [(style('good')[1], 'block k falls in'), (style('window')[1], 'unused digits'),
              (style('muted')[1], 'other blocks')]
    first = True
    total = math.factorial(n)
    for e in trace(n, k):
        kd = e['kind']
        digits, kk = e['digits'], e['k']
        answer = ''.join(e['result'])
        rows = [('k', f'{kk:,}')]
        styles, subs, ptr = {}, {}, {}
        hold, sub = STEP, ''
        if kd == 'given':
            styles = {j: 'window' for j in range(len(digits))}
            cap = f"k = {kk:,}: the {kk:,}th of the {total:,} arrangements of 1 to {n}, counting from 1."
            sub = "Each digit can be worked out directly, without listing the ones before it."
        elif kd == 'zero':
            styles = {j: 'window' for j in range(len(digits))}
            cap = f"First, k -= 1: now k = {kk:,}, counting from 0 (0 to {total - 1:,})."
            sub = "Counting from 0 makes 'which block?' a plain division with no adjustment."
            hold = KEY
        elif kd in ('choose', 'take'):
            b, idx, i = e['block'], e['idx'], e['i']
            show = digits if kd == 'choose' else None
            rows += [('block size', f'{i}! = {b:,}'), ('k // block', str(idx)), ('k % block', f'{(kk if kd == "take" else kk % b):,}')]
            if kd == 'choose':
                for j in range(len(digits)):
                    lo, hi = j * b, (j + 1) * b - 1
                    subs[j] = f'{lo}' if lo == hi else f'{lo}–{hi}'
                    styles[j] = 'good' if j == idx else 'muted'
                ptr = {'idx': idx}
                cap = (f"{i} digits are left after this one, so each choice owns a block of {i}! = {b:,}. "
                       f"{kk:,} // {b:,} = {idx}.")
                sub = (f"k = {kk:,} falls in block {idx}, so the next digit is the unused one at index {idx}: "
                       f"{digits[idx]}.")
                hold = KEY if first else STEP
                first = False
            else:
                styles = {j: 'window' for j in range(len(digits))}
                cap = f"Take the digit out of the list. k = k % {b:,} = {kk:,}: the position inside that block."
                sub = "The rest is the same problem, one digit shorter." if i == n - 1 else ''
                hold = STEP if i == n - 1 else QUICK * 2
            key = (kd, i)
            if key in notes:
                sub, hold = notes[key], KEY
        else:
            cap = f'Answer: "{answer}".'
            sub = notes.get('done', f"{n} divisions, no matter how big k is. The list removals make it O(n²).")
            hold = END
        values = digits if digits else ['—']
        if not digits:
            styles = {0: 'muted'}
        arr = ArrayView(values, styles=styles, pointers=ptr, subs=subs, title='unused', cell=72)
        txt = TextView([(f'answer so far: {answer or "(empty)"}', 'good' if kd == 'done' else None)], size=20)
        rows.append(('answer', answer or '—', 'good' if kd == 'done' else None) if kd == 'done' else ('answer', answer or '—'))
        sc.frame([arr, txt], cap, sub, hold, side=MapView(rows, 'Working', headers=('', '')), legend=legend)
    return sc


def hard():
    """Harder input for the interactive page (scripts/motion_build.py)."""
    assert Solution().getPermutation(HARD_N, HARD_K) == '25431'
    assert one_based(HARD_N, HARD_K) == '31245'
    sc = build(HARD_N, HARD_K, 'n = 5, k = 48: the last of the 24 arrangements that start with 2.', HARD_NOTES)
    return sc, ("k = 48 is the last arrangement starting with 2, \"25431\". Divide the one-based 48 by 24 and you "
                "get block 2, the 3s, and the answer \"31245\". Watch the first division.")


def main():
    args = cli()
    sc = build(N, K, f'n = {N}, k = {K}: the {K}th arrangement of 1 to {N} in dictionary order.')
    finish(sc, 60, "Watch the first division: the 24 arrangements come in four blocks of six, and 8 // 6 = 1 says "
                   "the answer starts with the second digit, 2.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
