#!/usr/bin/env python3
"""#295 Find Median from Data Stream: lower half in a max-heap, upper half in a
min-heap. Each number passes through the lower heap, its top crosses over, and
one number moves back if the upper heap got bigger.

The trace comes from running the notebook's Python MedianFinder with a recorder
added; the algorithm lines are unchanged. The calls are LeetCode's example.
"""
import heapq
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

OPS = [('addNum', 1), ('addNum', 2), ('findMedian', None), ('addNum', 3), ('findMedian', None)]   # LeetCode


class Row(View):
    """Two heaps side by side, each with a caption above it."""

    def __init__(self, left, right, titles):
        self.left, self.right, self.titles = left, right, titles

    def draw(self, p, box):
        x0, y0, x1, y1 = box
        mid = (x0 + x1) / 2
        for (a, b), v, t in (((x0, mid - 14), self.left, self.titles[0]), ((mid + 14, x1), self.right, self.titles[1])):
            p.text((a, y0 + 8), t, 'bold', 15)
            v.draw(p, (a + 30, y0 + 34, min(b - 10, a + 30 + 160), min(y1, y0 + 200)))
        self.used = 230


def trace(ops):
    events, log = [], []
    st = {'m': None}

    def rec(kind, **kw):
        m = st['m']
        events.append(dict(kind=kind, small=[-v for v in m.small], large=list(m.large), log=list(log), **kw))

    # ---- the notebook's solution, with rec() calls added ----
    class MedianFinder:
        def __init__(self):
            self.small = []  # max-heap (negated)
            self.large = []  # min-heap

        def addNum(self, num: int) -> None:
            heapq.heappush(self.small, -num)
            rec('into_small', num=num)
            heapq.heappush(self.large, -heapq.heappop(self.small))
            rec('cross', num=num)
            if len(self.large) > len(self.small):
                heapq.heappush(self.small, -heapq.heappop(self.large))
                rec('back', num=num)
            else:
                rec('balanced', num=num)

        def findMedian(self) -> float:
            if len(self.small) > len(self.large):
                return -self.small[0]
            return (-self.small[0] + self.large[0]) / 2.0

    st['m'] = MedianFinder()
    rec('start')
    for op, arg in ops:
        if op == 'addNum':
            st['m'].addNum(arg)
            log.append((f'addNum({arg})', 'null'))
        else:
            med = st['m'].findMedian()
            log.append(('findMedian()', str(med), 'good'))
            rec('median', med=med)
    rec('done')
    return events


def words(e):
    k = e['kind']
    s, l = e['small'], e['large']
    if k == 'start':
        return ("Lower half: a max-heap. Upper half: a min-heap. Their tops are the two middle numbers.",
                "Rules: everything lower <= everything upper; lower has the same count or one more.", STEP)
    if k == 'into_small':
        return (f"addNum({e['num']}): push {e['num']} into the lower heap first.",
                "We don't compare it to anything; the next step sorts out which half it belongs in.", STEP)
    if k == 'cross':
        return (f"Move the lower heap's top across. Whatever crosses is the biggest of the lower half,",
                "so everything left behind is still <= everything in the upper half.", KEY if e['num'] == 3 else STEP)
    if k == 'back':
        return (f"Now the upper heap has more ({len(l) + 1} vs {len(s) - 1}): move its top, {max(s)}, back down.",
                "That restores the size rule without breaking the order rule.", KEY if e['num'] in (1, 3) else STEP)
    if k == 'balanced':
        return (f"Sizes are {len(s)} and {len(l)}: balanced, nothing to move.", "", STEP)
    if k == 'median':
        if len(s) > len(l):
            return (f"findMedian(): odd count, so the lower heap holds the extra one. Its top: {e['med']}.",
                    "No searching or sorting: the answer is sitting on top.", KEY)
        return (f"findMedian(): even count, so average the tops: ({s and max(s)} + {min(l)}) / 2 = {e['med']}.", "", KEY)
    return ("Done: null, null, 1.5, null, 2.",
            "Each add is at most five heap operations, about log n steps each; findMedian is O(1).", END)


def main():
    args = cli()
    sc = Scene('#295 Find Median: two heaps, one per half',
               'Each heap is drawn as a tree over its array, with its top at the root.')
    legend = [(style('good')[1], 'lower half (max-heap)'), (style('window')[1], 'upper half (min-heap)'),
              (ACTIVE, 'top / just moved')]
    for e in trace(OPS):
        def view(vals, st, top_is_max):
            if not vals:
                return TextView(['(empty)'])
            arr = list(vals)
            styles = {i: st for i in range(len(arr))}
            return TreeView(arr, styles=styles, rings=[(0, ACTIVE)])
        small_arr = e['small']   # the real heap arrays, so the tree is the heap's actual layout
        large_arr = e['large']
        row = Row(view(small_arr, 'good', True), view(large_arr, 'window', False),
                  (f'lower half ({len(small_arr)})  top = largest', f'upper half ({len(large_arr)})  top = smallest'))
        cap, sub, hold = words(e)
        sc.frame(row, cap, sub, hold, side=MapView(e['log'], 'Calls so far', headers=('call', 'returns'),
                                                   empty='(no calls yet)'),
                 counters={'count': len(e['small']) + len(e['large'])}, legend=legend)
    finish(sc, 295, "Watch addNum(3): 3 goes into the lower heap, crosses straight to the upper heap as its "
                    "biggest number, and then 2 comes back down to keep the halves balanced.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
