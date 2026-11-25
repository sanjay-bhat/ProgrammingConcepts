#!/usr/bin/env python3
"""#87 Scramble String: try every split, both unswapped and swapped, and remember each answer.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. lru_cache is replaced by an explicit
dict with the same behaviour, so cache hits can be shown.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403
from functools import lru_cache  # noqa: E402

S1, S2 = 'great', 'rgeat'                 # LeetCode example 1

# Hard examples (interactive page only), each breaking a plausible first attempt.
HARD_INDEX = ('abcde', 'cdeab')           # true; pairing the swapped left part with s2[i2+k:] (not s2[i2+len-k:]) says false
HARD_GREEDY = ('bagbc', 'bgcab')          # true; committing to the first split whose letters match says false


class Solution:
    """The notebook's solution (comments dropped), to cross-check the traced run."""
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache(maxsize=None)
        def solve(i1: int, i2: int, length: int) -> bool:
            if length == 1:
                return s1[i1] == s2[i2]
            if sorted(s1[i1:i1+length]) != sorted(s2[i2:i2+length]):
                return False
            for k in range(1, length):
                if solve(i1, i2, k) and solve(i1+k, i2+k, length-k):
                    return True
                if solve(i1, i2+length-k, k) and solve(i1+k, i2, length-k):
                    return True
            return False
        return solve(0, 0, len(s1))


def swap_at_k(s1, s2):
    """First attempt: in the swapped case, pair s1's left part with s2 starting at i2 + k."""
    @lru_cache(maxsize=None)
    def solve(i1, i2, length):
        if length == 1:
            return i2 < len(s2) and s1[i1] == s2[i2]
        if sorted(s1[i1:i1 + length]) != sorted(s2[i2:i2 + length]):
            return False
        for k in range(1, length):
            if solve(i1, i2, k) and solve(i1 + k, i2 + k, length - k):
                return True
            if solve(i1, i2 + k, k) and solve(i1 + k, i2, length - k):
                return True
        return False
    return solve(0, 0, len(s1))


def first_matching_split(s1, s2):
    """First attempt: take the first split whose letters match, and commit to it."""
    def solve(a, b):
        if len(a) == 1:
            return a == b
        if sorted(a) != sorted(b):
            return False
        for k in range(1, len(a)):
            if sorted(a[:k]) == sorted(b[:k]):
                return solve(a[:k], b[:k]) and solve(a[k:], b[k:])
            if sorted(a[:k]) == sorted(b[-k:]):
                return solve(a[:k], b[-k:]) and solve(a[k:], b[:-k])
        return False
    return solve(s1, s2)


def trace(s1, s2):
    events, stack = [], []
    cache = {}

    def rec(kind, **kw):
        events.append(dict(kind=kind, stack=list(stack), memo=dict(cache), **kw))

    # ---- the notebook's solution, with rec() calls added ----
    def cached(f):                        # behaves like lru_cache(maxsize=None), but visible
        def wrap(i1, i2, length):
            key = (i1, i2, length)
            if key in cache:
                rec('hit', key=key, val=cache[key])
                return cache[key]
            stack.append(key)
            rec('call', key=key)
            v = f(i1, i2, length)
            cache[key] = v
            rec('ret', key=key, val=v)
            stack.pop()
            return v
        return wrap

    @cached
    def solve(i1: int, i2: int, length: int) -> bool:
        if length == 1:
            rec('base', key=(i1, i2, 1), val=s1[i1] == s2[i2])
            return s1[i1] == s2[i2]

        if sorted(s1[i1:i1+length]) != sorted(s2[i2:i2+length]):
            rec('prune', key=(i1, i2, length))
            return False

        for k in range(1, length):
            rec('try', key=(i1, i2, length), k=k, case=1)
            if solve(i1, i2, k) and solve(i1+k, i2+k, length-k):
                return True
            rec('try', key=(i1, i2, length), k=k, case=2)
            if solve(i1, i2+length-k, k) and solve(i1+k, i2, length-k):
                return True
        return False

    ans = solve(0, 0, len(s1))
    rec('done', val=ans)
    assert ans == Solution().isScramble(s1, s2)
    return events


def parts(e, n):
    """Colour s1's and s2's windows: the left part of s1 and its partner in s2 share a colour."""
    k = e['kind']
    st1, st2, cuts1, cuts2 = {}, {}, [], []
    if k == 'done':
        return st1, st2, cuts1, cuts2
    i1, i2, L = e['key']
    for j in range(n):
        st1[j] = st2[j] = 'muted'
    for j in range(L):
        st1[i1 + j] = st2[i2 + j] = 'window'
    if k == 'try':
        kk = e['k']
        for j in range(kk):
            st1[i1 + j] = 'region4'
        for j in range(kk, L):
            st1[i1 + j] = 'region3'
        cuts1 = [i1 + kk]
        if e['case'] == 1:
            for j in range(kk):
                st2[i2 + j] = 'region4'
            for j in range(kk, L):
                st2[i2 + j] = 'region3'
            cuts2 = [i2 + kk]
        else:
            for j in range(L - kk, L):
                st2[i2 + j] = 'region4'
            for j in range(L - kk):
                st2[i2 + j] = 'region3'
            cuts2 = [i2 + L - kk]
    elif k in ('ret', 'hit', 'base'):
        good = e['val']
        for j in range(L):
            st1[i1 + j] = st2[i2 + j] = 'good' if good else 'bad'
    elif k == 'prune':
        for j in range(L):
            st1[i1 + j] = st2[i2 + j] = 'bad'
    return st1, st2, cuts1, cuts2


def memo_layer(e, n):
    """The cache for the current length: rows i1, columns i2, T/F once known."""
    L = e['key'][2] if e['kind'] != 'done' else n
    size = n - L + 1
    vals = [[None] * size for _ in range(size)]
    styles = {}
    for (a, b, ln), v in e['memo'].items():
        if ln == L:
            vals[a][b] = 'T' if v else 'F'
            styles[(a, b)] = 'good' if v else 'bad'
    rings = []
    if e['kind'] != 'done':
        a, b, _ = e['key']
        rings = [((a, b), ACTIVE)]
    return DPTableView(vals, row_labels=[str(r) for r in range(size)], col_labels=[str(c) for c in range(size)],
                       styles=styles, rings=rings, title=f'Cache for length {L}  (row = i1, column = i2)', max_cell=44)


def words(e, s1, s2, notes, trap, seen):
    k = e['kind']
    if k == 'done':
        return (f"Done: \"{s1}\" {'is' if e['val'] else 'is not'} a scramble of \"{s2}\".",
                notes.get('done', "At most n³ = (start in s1, start in s2, length) states, each trying n splits: O(n⁴)."), END)
    i1, i2, L = e['key']
    a, b = s1[i1:i1 + L], s2[i2:i2 + L]
    if k == 'call':
        first = 'call' not in seen
        seen.add('call')
        return (f"solve({i1}, {i2}, {L}): can \"{a}\" be scrambled into \"{b}\"?",
                "The question is always about a piece of s1 and an equally long piece of s2." if first else "", STEP if first else QUICK * 2)
    if k == 'hit':
        return (f"solve({i1}, {i2}, {L}) was answered before: {'true' if e['val'] else 'false'}. Reuse it.",
                notes.get('hit', "That's the cache: without it, the same pieces are compared again and again."), KEY)
    if k == 'base':
        return (f"One letter each: \"{a}\" vs \"{b}\": {'same' if e['val'] else 'different'}.", "", QUICK * 2)
    if k == 'prune':
        return (f"\"{a}\" and \"{b}\" don't have the same letters, so no scramble can work. False.",
                "Swapping never changes which letters a piece holds, so this check prunes for free.",
                KEY if 'prune' not in seen and not seen.add('prune') else STEP)
    if k == 'try':
        kk, case = e['k'], e['case']
        left, right = a[:kk], a[kk:]
        if case == 1:
            cap = f"Split \"{a}\" after {kk}: \"{left}\" | \"{right}\". Unswapped: match them to \"{b[:kk]}\" | \"{b[kk:]}\"."
            sub = ""
            hold = STEP
            if trap == 'greedy' and sorted(left) == sorted(b[:kk]) and 'greedy' not in seen:
                seen.add('greedy')
                sub = notes.get('greedy', f"The letters match, so a version that commits to the first matching split stops looking here.")
                hold = KEY
        else:
            cap = (f"Swapped: \"{left}\" must match the END of \"{b}\", \"{b[L - kk:]}\", and \"{right}\" the start, \"{b[:L - kk]}\".")
            sub = "The left part's partner is the last k letters of s2's piece: s2 from i2 + len - k."
            hold = KEY if 'swap' not in seen else STEP
            seen.add('swap')
            if ('swap', e['key'], kk) in notes:
                sub, hold = notes[('swap', e['key'], kk)], KEY
            if trap == 'index' and kk != L - kk:
                sub = (f"Starting s2 at i2 + k = {i2 + kk} instead of i2 + len - k = {i2 + L - kk} would pair \"{left}\" "
                       f"with \"{s2[i2 + kk:i2 + 2 * kk]}\". With equal halves the two agree, which is why the samples pass.")
                hold = KEY
        return cap, sub, hold
    # ret
    if ('ret', e['key']) in notes:
        return (f"solve({i1}, {i2}, {L}) = {'true' if e['val'] else 'false'}: \"{a}\" {'can' if e['val'] else 'cannot'} become \"{b}\".",
                notes[('ret', e['key'])], KEY)
    return (f"solve({i1}, {i2}, {L}) = {'true' if e['val'] else 'false'}: \"{a}\" {'can' if e['val'] else 'cannot'} become \"{b}\".",
            "Saved in the cache.", KEY if e['val'] and L == len(s1) else STEP)


def build(s1, s2, subtitle, notes=None, trap=None):
    notes = notes or {}
    n = len(s1)
    sc = Scene('#87 Scramble String: split, maybe swap, remember', subtitle)
    legend = [(style('window')[1], 'pieces being compared'), (style('region4')[1], 'left part + its partner'),
              (style('region3')[1], 'right part + its partner'), (style('good')[1], 'true'), (style('bad')[1], 'false')]
    seen = set()
    for e in trace(s1, s2):
        if e['kind'] in ('call', 'ret') and e['key'][2] == 1:
            continue                      # a one-letter call is shown by its 'base' frame alone
        st1, st2, c1, c2 = parts(e, n)
        views = [ArrayView(list(s1), st1, title='s1', cuts=c1, cell=40),
                 ArrayView(list(s2), st2, title='s2', cuts=c2, cell=40),
                 memo_layer(e, n)]
        if e['kind'] == 'try':
            i1, i2, L = e['key']
            kk = e['k']
            deps = ([(i1, i2, kk), (i1 + kk, i2 + kk, L - kk)] if e['case'] == 1
                    else [(i1, i2 + L - kk, kk), (i1 + kk, i2, L - kk)])
            known = lambda d: {True: ' = T', False: ' = F'}.get(e['memo'].get(d), ' = ?')
            views.insert(2, TextView([f"depends on  solve{deps[0]}{known(deps[0])}  and  solve{deps[1]}{known(deps[1])}"], size=15))
        cap, sub, hold = words(e, s1, s2, notes, trap, seen)
        stack = [f'solve{key}' for key in e['stack']]
        sc.frame(views, cap, sub, hold,
                 side=StackView(stack, 'Call stack', note='solve(i1, i2, len), newest on top', empty='(empty)'),
                 counters={'cached': len(e['memo'])}, legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    a1, b1 = HARD_INDEX
    a2, b2 = HARD_GREEDY
    assert Solution().isScramble(a1, b1) and not swap_at_k(a1, b1)
    assert Solution().isScramble(a2, b2) and not first_matching_split(a2, b2)
    idx = build(a1, b1, f's1 = "{a1}", s2 = "{b1}". Answer true: "ab" | "cde" swapped. Uneven halves.', {
        'done': "True. A version that starts s2 at i2 + k in the swapped case pairs \"ab\" with \"de\" and returns false.",
    }, trap='index')
    grd = build(a2, b2, f's1 = "{a2}", s2 = "{b2}". Answer true. The first split whose letters match is the wrong one.', {
        'greedy': "The letters match (\"b\" and \"b\"), so a greedy version commits to this split. Here it fails further down; the right split is elsewhere.",
        'done': "True, found at a later split. Committing to the first split with matching letters returns false.",
    }, trap='greedy')
    return [
        (idx, f'"{a1}" vs "{b1}": the swap splits "ab" | "cde", halves of different lengths. A first attempt that pairs the '
              'swapped left part with s2 from i2 + k passes all three LeetCode samples (their swaps are even), then returns false here.'),
        (grd, f'"{a2}" vs "{b2}": the first split whose letters match, "b" | "agbc", leads nowhere. A first attempt that '
              'commits to it returns false; trying every split finds the real one. The answer is true.'),
    ]


def main():
    args = cli()
    sc = build(S1, S2, f's1 = "{S1}", s2 = "{S2}". Can s2 be made by splitting s1 into two parts, maybe swapping them, and repeating?', {
        ('swap', (0, 0, 2), 1): "Unswapped failed (g isn't r). Swapped: g pairs with the END of \"rg\", which is g, and r with its start.",
        ('ret', (0, 0, 2)): "\"gr\" becomes \"rg\" by swapping its two halves. With \"eat\" matching \"eat\", split 2 works.",
    })
    finish(sc, 87, "Watch \"gr\" meet \"rg\": unswapped fails, so the swapped case pairs g with the END of \"rg\", "
                   "and that one match is what makes the whole answer true.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
