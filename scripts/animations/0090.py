#!/usr/bin/env python3
"""#90 Subsets II: record every path, and skip a repeat at the same step.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

NUMS = [1, 2, 2]          # LeetCode example 1


def fmt(xs):
    return '[' + ','.join(map(str, xs)) + ']'


def trace(nums):
    events, calls = [], []
    st = {'i': None, 'start': None}

    def rec(kind, path, result, **kw):
        events.append(dict(kind=kind, nums=list(nums), path=list(path), result=[list(r) for r in result],
                           calls=list(calls), **st, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    nums.sort()
    result = []
    rec('sorted', [], result)

    def backtrack(start, path):
        calls.append((start, list(path)))
        st.update(start=start, i=None)
        result.append(list(path))
        rec('record', path, result)
        for i in range(start, len(nums)):
            st.update(start=start, i=i)
            if i > start and nums[i] == nums[i - 1]:
                rec('skip', path, result)
                continue
            path.append(nums[i])
            rec('choose', path, result)
            backtrack(i + 1, path)
            st.update(start=start, i=i)
            path.pop()
            rec('undo', path, result, popped=nums[i])
        calls.pop()
        st.update(i=None)
        rec('return', path, result, start_was=start)

    backtrack(0, [])
    st.update(i=None, start=None)
    rec('done', [], result)
    return events


def words(e, first):
    k, i, path = e['kind'], e['i'], e['path']
    if k == 'sorted':
        return ("Sort first, so the two 2s sit side by side.",
                "The duplicate check only compares a number with its left neighbour.", KEY)
    if k == 'record':
        if not path:
            return ("Every path is a subset, so record it on the way in. The empty one counts.",
                    "Then try each number from start onward as the next pick.", KEY)
        return (f"New call with path {fmt(path)}: record it as a subset.",
                f"From here it may only pick numbers to the right, starting at index {e['start']}.", STEP)
    if k == 'choose':
        if i == e['start'] and i > 0 and e['nums'][i] == e['nums'][i - 1]:
            return (f"nums[{i}] = 2 equals its left neighbour, but it's the FIRST pick at this step.",
                    f"i == start, so it's allowed: the other 2 is already in the path, making {fmt(path)}.", KEY)
        return (f"Pick nums[{i}] = {e['nums'][i]}: path is now {fmt(path)}. Go one level deeper.", "", STEP)
    if k == 'skip':
        dup = fmt(path + [e['nums'][i]])
        if first.get('skip') == id(e):
            return (f"nums[{i}] = 2 is the same as nums[{i - 1}], offered at the same step. Skip it.",
                    f"Picking it here would make {dup} a second time: the first 2 already built it.", KEY)
        return (f"nums[{i}] = 2 equals its left neighbour at the same step: skip again.",
                f"This time the skip stops a second {dup}, and everything that would grow from it.", KEY)
    if k == 'undo':
        if first.get('undo') == id(e):
            return (f"Back from the deeper call: pop {e['popped']}, so path is {fmt(path)} again.",
                    "Undoing the pick lets the loop try the next number from the same starting point.", KEY)
        return (f"Pop {e['popped']}: path back to {fmt(path)}.", "", QUICK * 1.6)
    if k == 'return':
        return ("No numbers left to try here, so this call returns.", "", QUICK * 1.4)
    return (f"Done: {len(e['result'])} subsets, each one exactly once.",
            "Brute force would make 2³ = 8 and throw two duplicates away.", END)


def main():
    args = cli()
    events = trace(list(NUMS))
    first = {}
    for e in events:
        for k in ('skip', 'undo'):
            if e['kind'] == k and k not in first:
                first[k] = id(e)
    sc = Scene('#90 Subsets II: backtracking with a duplicate skip',
               f'nums = {NUMS}. List every different subset once.')
    legend = [(ACTIVE, 'number being tried'), (style('bad')[1], 'skipped repeat'),
              (style('good')[1], 'in the current path')]
    for e in events:
        k, i = e['kind'], e['i']
        styles = {}
        if i is not None:
            styles[i] = 'bad' if k == 'skip' else 'active'
        ptrs = {}
        if e['start'] is not None:
            ptrs['start'] = e['start']
        if i is not None:
            ptrs['i'] = i
        nums = ArrayView(e['nums'], styles, pointers=ptrs, title='nums', cell=58)
        path = ArrayView(e['path'] or [None], {j: 'good' for j in range(len(e['path']))},
                         title='path', indices=False, cell=50)
        if not e['path']:
            path = TextView(['path  []  (empty)'], size=16)
        got = [(fmt(r), 'good' if (k == 'record' and j == len(e['result']) - 1) or k == 'done' else None)
               for j, r in enumerate(e['result'])]
        chips = ChipsView(got, 'Subsets recorded', empty='(none yet)')
        stack = [f'backtrack({s}, {fmt(pth)})' for s, pth in e['calls']]
        cap, sub, hold = words(e, first)
        sc.frame([nums, path, chips], cap, sub, hold,
                 side=StackView(stack, 'Call stack', base='subsetsWithDup',
                                empty='(empty)'),
                 counters={'subsets': len(e['result'])}, legend=legend)
    finish(sc, 90, "Watch the second 2 get skipped when it's offered at the same step as the first: "
                   "that one check is what stops [2] and [1,2] appearing twice.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
