#!/usr/bin/env python3
"""#215 Kth Largest Element: a min-heap that never holds more than k numbers.
Push each number; if there are k + 1, the smallest leaves. The top is the answer.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. The input is LeetCode's example 1.
"""
import heapq
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

NUMS, K = [3, 2, 1, 5, 6, 4], 2   # LeetCode example 1


class Narrow(View):
    """Draw a view in a fixed-width box (a 3-node heap spread over 500px reads badly)."""

    def __init__(self, view, width, height=None):
        self.view, self.width, self.height = view, width, height

    def draw(self, p, box):
        x0, y0, x1, y1 = box
        self.view.draw(p, (x0 + 60, y0, min(x1, x0 + 60 + self.width), y1 if not self.height else y0 + self.height))
        self.used = self.height or self.view.used


def trace(nums, k):
    events, gone = [], []
    st = {'i': None}

    def rec(kind, heap, **kw):
        events.append(dict(kind=kind, heap=list(heap), i=st['i'], gone=list(gone), **kw))

    class Solution:
        # ---- the notebook's solution, with rec() calls added ----
        def findKthLargest(self, nums: list[int], k: int) -> int:
            heap = []
            rec('start', heap)
            for i, num in enumerate(nums):
                st['i'] = i
                heapq.heappush(heap, num)
                rec('push', heap, num=num, over=len(heap) > k)
                if len(heap) > k:
                    out = heapq.heappop(heap)
                    gone.append(i if out == num else nums.index(out, 0))
                    rec('pop', heap, num=num, out=out)
            st['i'] = None
            rec('done', heap, ans=heap[0])
            return heap[0]

    Solution().findKthLargest(nums, k)
    return events


def words(e):
    k = e['kind']
    if k == 'start':
        return (f"Keep a min-heap of the {K} largest numbers seen so far.",
                "Min-heap: its top is the smallest it holds. That top will be the answer.", STEP)
    if k == 'push':
        if e['over']:
            return (f"Push {e['num']}. Now the heap holds {K + 1}, one too many.", "", STEP)
        return (f"Push {e['num']}. The heap holds {len(e['heap'])}, not more than {K}: keep everything.", "", STEP)
    if k == 'pop':
        if e['out'] == e['num']:
            return (f"Pop the smallest: {e['out']}, the number that just came in.",
                    f"It's smaller than both {e['heap'][0]} and {max(e['heap'])}, so it can't be in the top {K}.", KEY)
        if len(e['gone']) == 1:
            return (f"Pop the smallest: {e['out']}. Two numbers already beat it,",
                    f"so it can never be the {K}nd largest. Throw it away for good.", KEY)
        return (f"Pop the smallest: {e['out']}. It has {K} bigger numbers now.", "", STEP)
    return (f"Done. The heap holds the {K} largest, {sorted(e['heap'])}; its top is {e['ans']}.",
            "Each number cost one push and at most one pop, about log k steps each: O(n log k).", END)


def main():
    args = cli()
    sc = Scene('#215 Kth Largest: a min-heap capped at k',
               f'nums = {NUMS}, k = {K}. The heap is drawn as a tree over its array; its top is the smallest.')
    legend = [(ACTIVE, 'number being added'), (style('good')[1], 'heap top'), (style('muted')[1], 'thrown out')]
    for e in trace(NUMS, K):
        styles = {j: 'muted' for j in e['gone']}
        ptr = {}
        if e['i'] is not None:
            ptr = {'next': e['i']}
            if e['i'] not in e['gone']:
                styles[e['i']] = 'active'
        arr = ArrayView(NUMS, styles=styles, pointers=ptr, title='nums', cell=52)
        h = e['heap']
        hst = {0: 'good'} if h else {}
        rings = []
        if e['kind'] == 'push' and 'num' in e:
            j = h.index(e['num'])
            if j != 0:
                hst[j] = 'active'
            rings = [(j, ACTIVE)]
        tree = Narrow(TreeView(h, styles=hst, rings=rings) if h else TextView(['(empty heap)']), 220, 150)
        harr = ArrayView(h, styles=hst, title='heap', cell=52)
        cap, sub, hold = words(e)
        side_rows = [(str(v), 'out' if j in e['gone'] else 'kept') for j, v in enumerate(NUMS[:(e['i'] + 1) if e['i'] is not None else len(NUMS)])]
        side = MapView([(f'nums[{j}] = {v}', s, 'muted' if s == 'out' else None) for j, (v, s) in enumerate(side_rows)],
                       'Seen so far', headers=('number', 'status'), empty='(nothing yet)')
        sc.frame([arr, tree, harr], cap, sub, hold, side=side,
                 counters={'heap top': h[0] if h else '-'}, legend=legend)
    finish(sc, 215, "Watch the last number, 4: it goes in and comes straight back out, because the heap "
                    "already holds two bigger numbers, 5 and 6. The top of what's left, 5, is the answer.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
