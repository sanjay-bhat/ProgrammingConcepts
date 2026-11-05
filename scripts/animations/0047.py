#!/usr/bin/env python3
"""#47 Permutations II: sort, then never start a branch with the second copy of
a value while the first copy is still unused at the same spot.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. The tree's nodes are the choices
made so far; red stubs are branches the duplicate check cut off.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

NUMS = [1, 1, 2]          # LeetCode example 1

# The hard example (interactive page only): the duplicates are not next to
# each other. The skip test only compares neighbours, so leaving out the sort
# passes both LeetCode samples ([1,1,2] is already sorted, [1,2,3] has no
# duplicates) and then returns all 24 orderings here, only 6 of them different.
HARD = [1, 2, 1, 2]
HARD_NOTES = {
    'start': "Sorted first: [1, 1, 2, 2]. Unsorted, the two 1s aren't neighbours and the skip test never fires.",
    'done': "6 permutations. Without the sort, the same code returns 24 lists for [1, 2, 1, 2], only 6 different.",
}


def no_sort(nums):
    """First attempt the hard example breaks: the same backtracking, without sorting first."""
    result, used = [], [False] * len(nums)

    def bt(path):
        if len(path) == len(nums):
            result.append(list(path))
            return
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                continue
            used[i] = True
            path.append(nums[i])
            bt(path)
            path.pop()
            used[i] = False
    bt([])
    return result


def trace(nums_in):
    events, chain = [], []      # chain: indices chosen so far (the tree path)

    def rec(kind, nums, used, result, **kw):
        events.append(dict(kind=kind, nums=list(nums), used=list(used), chain=list(chain),
                           result=[list(r) for r in result], **kw))

    # ---- the notebook's solution, with rec() calls added ----
    class Solution:
        def permuteUnique(self, nums):
            nums.sort()
            result = []
            used = [False] * len(nums)
            rec('start', nums, used, result)

            def backtrack(path):
                if len(path) == len(nums):
                    result.append(list(path))
                    rec('record', nums, used, result)
                    return
                for i in range(len(nums)):
                    if used[i]:
                        continue
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        rec('skip', nums, used, result, i=i)
                        continue
                    used[i] = True
                    path.append(nums[i])
                    chain.append(i)
                    rec('take', nums, used, result, i=i)
                    backtrack(path)
                    chain.pop()
                    path.pop()
                    used[i] = False
                    rec('undo', nums, used, result, i=i)

            backtrack([])
            rec('done', nums, used, result)
            return result

    ans = Solution().permuteUnique(list(nums_in))
    return events, ans


def nid(chain, skip=None):
    return 'n' + '.'.join(map(str, chain)) + ('' if skip is None else f'x{skip}')


def layout(events):
    kids = {nid([]): []}
    for e in events:
        if e['kind'] == 'take':
            n, par = nid(e['chain']), nid(e['chain'][:-1])
        elif e['kind'] == 'skip':
            n, par = nid(e['chain'], e['i']), nid(e['chain'])
        else:
            continue
        if n not in kids:
            kids[par].append(n)
            kids[n] = []
    xs, depth, leaves = {}, {}, [0]

    def walk(n, d):
        depth[n] = d
        if not kids[n]:
            xs[n] = leaves[0]
            leaves[0] += 1
        else:
            for c in kids[n]:
                walk(c, d + 1)
            xs[n] = (xs[kids[n][0]] + xs[kids[n][-1]]) / 2
    walk(nid([]), 0)
    md = max(depth.values())
    return ({n: (0.03 + 0.94 * xs[n] / max(1, leaves[0] - 1), depth[n] / md) for n in kids},
            [(a, b) for a in kids for b in kids[a]])


def words(e, first_skip, notes):
    k = e['kind']
    if notes and k in notes:
        cap, _, _ = _words(e, first_skip)
        return cap, notes[k], (END if k == 'done' else KEY)
    return _words(e, first_skip)


def _words(e, first_skip):
    k, a = e['kind'], e['nums']
    path = [a[i] for i in e['chain']]
    if k == 'start':
        return (f"Sort first: {a}. Equal values now sit next to each other.",
                "Then build orderings one position at a time; used[] marks which copies are taken.", KEY)
    if k == 'take':
        i = e['i']
        return (f"Take nums[{i}] = {a[i]}. Path so far: {path}.", "", STEP if len(path) == 1 else QUICK * 2.4)
    if k == 'skip':
        i = e['i']
        if id(e) == first_skip:
            return (f"Skip nums[{i}] = {a[i]}: it equals nums[{i - 1}], and nums[{i - 1}] is NOT used.",
                    f"A {a[i]} in this position was already tried with the first copy. Same value, same subtree.", KEY)
        return (f"Skip nums[{i}] = {a[i]}: its twin nums[{i - 1}] is unused, so this branch would repeat.", "", STEP)
    if k == 'record':
        return (f"All positions filled: record {e['result'][-1]}.", "", STEP)
    if k == 'undo':
        return (f"Undo: give back nums[{e['i']}] = {a[e['i']]}. Path: {path}.", "", QUICK * 1.8)
    return (f"Done: {len(e['result'])} different permutations, each built exactly once.",
            "Duplicates were never built and thrown away; their branches were never started.", END)


def build(nums, subtitle, notes=None):
    events, ans = trace(nums)
    pos_all, edges_all = layout(events)
    first_skip = next((id(e) for e in events if e['kind'] == 'skip'), None)
    sc = Scene('#47 Permutations II: one branch per value, not per copy', subtitle)
    legend = [(ACTIVE, 'current choice'), (style('window')[1], 'path so far'),
              (style('good')[1], 'finished branch'), (style('bad')[1], 'skipped duplicate')]
    seen = {nid([])}
    done_nodes = set()
    for e in events:
        k = e['kind']
        if k == 'take':
            seen.add(nid(e['chain']))
        if k == 'skip':
            seen.add(nid(e['chain'], e['i']))
        if k == 'undo':
            done_nodes.add(nid(e['chain'] + [e['i']]))
        pos = {n: pos_all[n] for n in seen}
        edges = [(x, y) for x, y in edges_all if x in seen and y in seen]
        path = [nid(e['chain'][:j]) for j in range(len(e['chain']) + 1)]
        styles = {n: 'good' for n in done_nodes}
        for n in seen:
            if 'x' in n:
                styles[n] = 'bad'
        for n in path:
            styles[n] = 'window'
        estyles = {(path[j], path[j + 1]): 'active' for j in range(len(path) - 1)}
        rings = []
        if k == 'take':
            rings = [(path[-1], ACTIVE)]
        elif k == 'skip':
            rings = [(nid(e['chain'], e['i']), REJECT)]
            estyles[(path[-1], nid(e['chain'], e['i']))] = 'bad'
        text = {}
        for n in pos:
            if n == 'n':
                text[n] = 'start'
            else:
                last = n[1:].split('.')[-1]
                idx = int(last.split('x')[-1]) if 'x' in last else int(last)
                text[n] = str(e['nums'][idx])
        g = GraphView(pos, edges, styles=styles, edge_styles=estyles, rings=rings, text=text, height=250)
        st, ptr = {}, {}
        for j, u in enumerate(e['used']):
            st[j] = 'window' if u else 'plain'
        if k in ('take', 'skip', 'undo'):
            st[e['i']] = {'take': 'active', 'skip': 'bad', 'undo': 'muted'}[k]
            ptr = {'i': e['i']}
        arr = ArrayView(e['nums'], styles=st, pointers=ptr, title='nums', cell=54,
                        subs={j: ('used' if u else '') for j, u in enumerate(e['used'])})
        cap, sub, hold = words(e, first_skip, notes)
        sc.frame([g, arr], cap, sub, hold,
                 side=MapView([(str(j + 1), str(r), 'good') for j, r in enumerate(e['result'])], 'Recorded',
                              headers=('#', 'permutation'), empty='(nothing yet)'),
                 counters={'found': len(e['result'])}, legend=legend)
    return sc


def hard():
    """Harder input for the interactive page (scripts/motion_build.py)."""
    for s in ([1, 1, 2], [1, 2, 3]):                 # LeetCode samples: no_sort gets them right
        assert sorted(no_sort(list(s))) == sorted(trace(s)[1])
    ans = trace(HARD)[1]
    wrong = no_sort(list(HARD))
    assert len(ans) == 6 and len(wrong) == 24 and len({tuple(w) for w in wrong}) == 6
    sc = build(HARD, f'nums = {HARD}. Answer: 6 orderings. Red stubs are branches the duplicate check cut off.',
               HARD_NOTES)
    return sc, ("The two 1s and the two 2s aren't neighbours. Leave out the sort and the skip test never fires: "
                "both LeetCode samples still pass, but this returns 24 lists, only 6 different.")


def main():
    args = cli()
    sc = build(NUMS, 'Tree: the value chosen for each position. Red stub: a duplicate branch that is never started.')
    finish(sc, 47, "Watch the second 1 get skipped at the top of the tree: the first 1 already started a branch "
                   "there, and a second identical branch would build the same orderings again.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
