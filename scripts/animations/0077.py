#!/usr/bin/env python3
"""#77 Combinations: build each combination in increasing order. A call picks
the next number from `start` upward, recurses with start = i + 1, then undoes
the pick. The loop stops early once too few numbers are left to fill the
remaining slots (the pruning bound).

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

N, K = 4, 2          # LeetCode example 1: 6 combinations

# Hard example 1: the pruning bound off by one. C#, Go and Rust write
# `i <= n - remaining + 1`; carried into Python's exclusive range() as
# range(start, n - remaining + 1), it never offers the last allowed number at
# any depth, so every combination containing 5 is lost: 4 lists instead of 10.
HARD1 = (5, 3)
HARD1_COUNT, HARD1_WRONG_COUNT = 10, 4

# Hard example 2: recursing with start + 1 instead of i + 1. The next pick may
# then repeat a number already in the path, adding [1, 3, 3], [2, 2, 3],
# [2, 2, 4] and [2, 3, 3]: 8 lists instead of 4.
HARD2 = (4, 3)
HARD2_COUNT, HARD2_WRONG_COUNT = 4, 8


class Solution:
    # ---- the notebook's solution, unchanged (used to check the answers) ----
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []

        def backtrack(start: int, path: list[int]) -> None:
            if len(path) == k:
                result.append(list(path))
                return
            remaining = k - len(path)
            for i in range(start, n - remaining + 2):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        backtrack(1, [])
        return result


def wrong_bound(n, k):
    """First attempt: `i <= n - remaining + 1` translated to range(start, n - remaining + 1)."""
    result = []

    def backtrack(start, path):
        if len(path) == k:
            result.append(list(path))
            return
        remaining = k - len(path)
        for i in range(start, n - remaining + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    backtrack(1, [])
    return result


def wrong_start(n, k):
    """First attempt: recurse with start + 1 instead of i + 1."""
    result = []

    def backtrack(start, path):
        if len(path) == k:
            result.append(list(path))
            return
        remaining = k - len(path)
        for i in range(start, n - remaining + 2):
            path.append(i)
            backtrack(start + 1, path)
            path.pop()

    backtrack(1, [])
    return result


assert Solution().combine(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
assert Solution().combine(1, 1) == [[1]]
assert len(Solution().combine(*HARD1)) == HARD1_COUNT and len(wrong_bound(*HARD1)) == HARD1_WRONG_COUNT
assert len(Solution().combine(*HARD2)) == HARD2_COUNT and len(wrong_start(*HARD2)) == HARD2_WRONG_COUNT
assert [1, 3, 3] in wrong_start(*HARD2) and [2, 2, 4] in wrong_start(*HARD2) and all(5 not in c for c in wrong_bound(*HARD1))


def fmt(xs):
    return '[' + ','.join(map(str, xs)) + ']'


def trace(n, k):
    events, calls = [], []

    def rec(kind, path, **kw):
        events.append(dict(kind=kind, path=list(path), result=[list(r) for r in result],
                           calls=list(calls), **kw))

    # ---- the notebook's solution, with rec() calls added ----
    result = []

    def backtrack(start: int, path: list[int]) -> None:
        calls.append((start, list(path)))
        if len(path) == k:
            result.append(list(path))
            rec('record', path, start=start)
            calls.pop()
            return
        remaining = k - len(path)
        bound = n - remaining + 1                     # largest i the loop will try
        rec('enter', path, start=start, remaining=remaining, bound=bound)
        for i in range(start, n - remaining + 2):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()
            rec('undo', path, start=start, i=i, bound=bound, popped=i)
        calls.pop()
        rec('return', path, start=start, bound=bound, remaining=remaining)

    rec('start', [])
    backtrack(1, [])
    rec('done', [])
    return events


def build(n, k, subtitle, notes=None):
    """notes: {kind: text} or {(kind, path tuple): text} replaces that frame's second caption line, held as KEY."""
    notes = notes or {}
    sc = Scene('#77 Combinations: pick in increasing order, undo, try the next', subtitle)
    legend = [(style('good')[1], 'in the current path'), (ACTIVE, 'just picked'),
              (style('muted')[1], 'past the bound: never tried here')]
    first = set()
    for e in trace(n, k):
        kd, path = e['kind'], e['path']
        styles = {v - 1: 'good' for v in path}
        ptrs, cuts, hold, sub = {}, (), STEP, ''
        if kd in ('enter', 'undo', 'return'):
            for v in range(e['bound'] + 1, n + 1):
                if v not in path:
                    styles[v - 1] = 'muted'
            cuts = (e['bound'],) if e['bound'] < n else ()
            ptrs['start'] = e['start'] - 1
        if kd == 'start':
            cap = f"Choose {k} of the numbers 1..{n}. Each combination is built in increasing order."
            sub = "Increasing order is what stops [1,2] and [2,1] both appearing: only one of them is increasing."
            hold = KEY
        elif kd == 'enter':
            if path:
                styles[path[-1] - 1] = 'active'
                cap = f"Picked {path[-1]}: path {fmt(path)}. Next pick starts at {e['start']}, one past it."
            else:
                cap = f"backtrack(1, []): {k} slots to fill, numbers 1..{n}."
            if e['bound'] < n:
                sub = (f"Need {e['remaining']} more, so i only goes up to {e['bound']}: starting any higher "
                       f"leaves too few numbers.")
                if 'prune' not in first:
                    first.add('prune')
                    hold = KEY
            else:
                sub = f"Need {e['remaining']} more; any number from {e['start']} to {n} still fits."
        elif kd == 'record':
            styles[path[-1] - 1] = 'active'
            cap = f"Picked {path[-1]}: path {fmt(path)} has {k} numbers. Record a COPY of it."
            if 'record' not in first:
                first.add('record')
                sub = "A copy, because path keeps changing; storing path itself would leave every entry empty at the end."
                hold = KEY
            else:
                hold = STEP * 0.8
        elif kd == 'undo':
            cap = f"Back from {fmt(path + [e['popped']])}: pop {e['popped']}, path is {fmt(path)} again."
            if 'undo' not in first:
                first.add('undo')
                sub = "Undoing the pick lets the loop try the next number in the same slot."
                hold = KEY
            else:
                hold = QUICK * 1.6
        elif kd == 'return':
            if e['bound'] < n:
                cut = ', '.join(str(v) for v in range(e['bound'] + 1, n + 1))
                cap = f"The loop stops at {e['bound']}: {cut} never tried in this slot. backtrack returns."
                sub = f"After {cut}, fewer than {e['remaining']} numbers would be left, so no combination could finish."
                if 'cut' not in first:
                    first.add('cut')
                    hold = KEY
            else:
                cap = f"Every number from {e['start']} to {n} has been tried after {fmt(path)}. Return."
                hold = QUICK * 1.6
        else:
            cap = f"Done: {len(e['result'])} combinations, each listed once, in increasing order."
            sub = f"That's C({n}, {k}) = {len(e['result'])}; each takes up to {k} steps to build and copy."
            hold = END
        for key in ((kd, tuple(path)), kd):
            if key in notes:
                sub, hold = notes[key], max(hold, KEY)
                break
        nums = ArrayView(list(range(1, n + 1)), styles, pointers=ptrs, title='numbers', indices=False,
                         cell=min(58, int(500 / n) - 6), cuts=cuts)
        pathv = (ArrayView(path, {j: 'good' for j in range(len(path))}, title='path', indices=False, cell=50)
                 if path else TextView(['path  []  (empty)'], size=16))
        got = [(fmt(r), 'good' if (kd == 'record' and j == len(e['result']) - 1) or kd == 'done' else None)
               for j, r in enumerate(e['result'])]
        chips = ChipsView(got, 'Combinations recorded', empty='(none yet)', max_rows=3)
        stack = [f'backtrack({s}, {fmt(p)})' for s, p in e['calls']]
        sc.frame([nums, pathv, chips], cap, sub, hold,
                 side=StackView(stack, 'Call stack', base=f'combine({n}, {k})', empty='(empty)'),
                 counters={'found': len(e['result'])}, legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    sc1 = build(*HARD1, 'n = 5, k = 3. Watch where the loop stops at each depth: 3, then 4, then 5.',
                {'start': "The bound moves with the path: the more numbers picked, the further each loop may go.",
                 'done': "Python's range() stops BEFORE its end. Writing n - remaining + 1 there loses every list with a 5: 4, not 10."})
    sc2 = build(*HARD2, 'n = 4, k = 3. Each call starts one past the number just picked.',
                {('enter', (1, 3)): "Start at i + 1 = 4. Passing start + 1 = 3 instead would pick 3 again: [1,3,3].",
                 'done': "Recursing with start + 1 instead of i + 1 lists 8 here, with repeats like [1,3,3] and [2,2,4]."})
    return [(sc1, "n = 5, k = 3. Carrying C#'s `i <= n - remaining + 1` into Python's range(), which stops one "
                  "early, loses every combination that ends in 5: 4 lists instead of 10."),
            (sc2, "n = 4, k = 3. Recursing with start + 1 instead of i + 1 lets a number be picked twice, "
                  "producing 8 lists instead of 4, among them [1,3,3] and [2,2,4].")]


def main():
    args = cli()
    sc = build(N, K, 'LeetCode example 1: every way to choose 2 of the numbers 1 to 4.')
    finish(sc, 77, "Watch the first slot's loop stop at 3: a combination starting with 4 has nothing "
                   "left for its second number, so it's never tried.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
