#!/usr/bin/env python3
"""#40 Combination Sum II: prune once the numbers get too big, skip a repeat at the same step.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

CANDIDATES, TARGET = [2, 5, 2, 1, 2], 5          # LeetCode example 2


def fmt(xs):
    return '[' + ','.join(map(str, xs)) + ']'


def trace(candidates, target):
    events, calls = [], []
    st = {'i': None, 'start': None, 'remain': target}

    def rec(kind, path, result, **kw):
        events.append(dict(kind=kind, cand=list(candidates), path=list(path),
                           result=[list(r) for r in result], calls=list(calls), **st, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    candidates.sort()
    result = []
    rec('sorted', [], result)

    def backtrack(start, path, remain):
        calls.append((start, remain))
        st.update(start=start, i=None, remain=remain)
        if remain == 0:
            result.append(list(path))
            rec('found', path, result)
            calls.pop()
            return
        rec('enter', path, result)
        for i in range(start, len(candidates)):
            st.update(start=start, i=i, remain=remain)
            if candidates[i] > remain:
                rec('prune', path, result)
                break
            if i > start and candidates[i] == candidates[i - 1]:
                rec('skip', path, result)
                continue
            path.append(candidates[i])
            rec('choose', path, result)
            backtrack(i + 1, path, remain - candidates[i])
            st.update(start=start, i=i, remain=remain)
            path.pop()
            rec('undo', path, result, popped=candidates[i])
        calls.pop()
        st.update(i=None)
        rec('return', path, result)

    backtrack(0, [], target)
    st.update(i=None, start=None, remain=None)
    rec('done', [], result)
    return events


def words(e, first):
    k, i, path, c = e['kind'], e['i'], e['path'], e['cand']
    if k == 'sorted':
        return (f"Sort first: {fmt(c)}. The three 2s now sit side by side.",
                "Sorting makes repeats neighbours and puts the big numbers last, where they can be cut off.", KEY)
    if k == 'enter':
        if not path:
            return (f"Start with an empty combination and {e['remain']} still to make.",
                    "Each step picks one more number, always to the right of the last pick.", STEP)
        return (f"Path {fmt(path)}, {e['remain']} still to make. Try the numbers from index {e['start']} on.", "", STEP)
    if k == 'found':
        if first.get('found') != id(e):
            return (f"Nothing left to make: {fmt(path)} adds up to {TARGET}. Record it.", "", STEP * 1.4)
        return (f"Nothing left to make: {fmt(path)} adds up to {TARGET}. Record a copy.",
                "Then return: adding anything more would overshoot.", KEY)
    if k == 'prune':
        if first.get('prune') == id(e):
            return (f"{c[i]} is bigger than the {e['remain']} still needed. Stop this whole loop.",
                    "The list is sorted, so every number after it is too big as well.", KEY)
        return (f"{c[i]} > {e['remain']} still needed: break, nothing further right can fit.", "", STEP)
    if k == 'skip':
        if first.get('skip') == id(e):
            return (f"candidates[{i}] = {c[i]} repeats its left neighbour at the same step. Skip it.",
                    f"It would build {fmt(path + [c[i]])} again, which the first {c[i]} already explored.", KEY)
        return (f"candidates[{i}] = {c[i]} repeats its left neighbour at this step: skip.", "", STEP)
    if k == 'choose':
        if i == e['start'] and i > 0 and c[i] == c[i - 1]:
            return (f"candidates[{i}] = {c[i]} equals its neighbour, but it's the FIRST pick at this step.",
                    f"i == start, so it's allowed: the other {c[i]} is already in the path, making {fmt(path)}.", KEY)
        return (f"Pick candidates[{i}] = {c[i]}: path {fmt(path)}, now {e['remain'] - c[i]} to make.", "", STEP)
    if k == 'undo':
        if first.get('undo') == id(e):
            return (f"Back from the deeper call: pop {e['popped']}, path is {fmt(path)} again.",
                    "Undoing the pick lets the loop try the next number from the same spot.", KEY)
        return (f"Pop {e['popped']}: path back to {fmt(path)}.", "", QUICK * 1.6)
    if k == 'return':
        return ("This call has nothing left to try, so it returns.", "", QUICK * 1.4)
    return (f"Done: {len(e['result'])} combinations, " + ' and '.join(fmt(r) for r in e['result']) + ".",
            "[1,2,2] appears once even though there are three 2s to choose two from.", END)


def main():
    args = cli()
    events = trace(list(CANDIDATES), TARGET)
    first = {}
    for e in events:
        for k in ('skip', 'undo', 'prune', 'found'):
            if e['kind'] == k and k not in first:
                first[k] = id(e)
    sc = Scene('#40 Combination Sum II: prune and skip repeats',
               f'candidates = {CANDIDATES}, target = {TARGET}. Each number used at most once.')
    legend = [(ACTIVE, 'number being tried'), (style('bad')[1], 'skipped or too big'),
              (style('good')[1], 'in the current path')]
    for e in events:
        k, i = e['kind'], e['i']
        styles = {}
        if i is not None:
            styles[i] = 'bad' if k in ('skip', 'prune') else 'active'
        if k == 'prune':
            for j in range(i + 1, len(e['cand'])):
                styles[j] = 'muted'
        ptrs = {}
        if e['start'] is not None:
            ptrs['start'] = e['start']
        if i is not None:
            ptrs['i'] = i
        cand = ArrayView(e['cand'], styles, pointers=ptrs, title='sorted', cell=58)
        if e['path']:
            path = ArrayView(e['path'], {j: 'good' for j in range(len(e['path']))},
                             title='path', indices=False, cell=50)
        else:
            path = TextView(['path  []  (empty)'], size=16)
        got = [(fmt(r), 'good' if k in ('found', 'done') else None) for r in e['result']]
        chips = ChipsView(got, 'Combinations found')
        stack = [f'backtrack(start={s}, remain={r})' for s, r in e['calls']]
        cap, sub, hold = words(e, first)
        rem = e['remain'] if e['remain'] is not None else '-'
        sc.frame([cand, path, chips], cap, sub, hold,
                 side=StackView(stack, 'Call stack', base='combinationSum2'),
                 counters={'remain': rem, 'found': len(e['result'])}, legend=legend)
    finish(sc, 40, "Watch the second and third 2 get skipped at the top level, and 5 cut off the loop "
                   "once it's bigger than what's left: one check stops repeats, the other stops wasted work.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
