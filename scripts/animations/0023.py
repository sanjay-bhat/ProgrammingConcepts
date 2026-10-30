#!/usr/bin/env python3
"""#23 Merge k Sorted Lists: a min-heap holds one head per list.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. The heap panel draws Python's actual
heapq array as the tree it represents.
"""
import heapq
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

LISTS = [[1, 4, 5], [1, 3, 4], [2, 6]]          # LeetCode example 1

# The hard example (interactive page only): three of the five lists are empty
# and three heads tie at 2 at once. Seeding the heap without skipping empty
# lists reads None.val and crashes on L0; pushing bare (value, node) pairs
# raises TypeError at the first tie. Answer [1,2,2,2,2,5].
# Notes are keyed by event number and replace that frame's second caption line.
HARD = [[], [2, 5], [], [1, 2, 2], [2]]
HARD_NOTES = {
    0: "L0 and L2 are empty, so they're skipped. Pushing L0's head as-is would read None.val and crash.",
    3: "Order: L1, L3, L4. With bare (value, node) pairs, Python compares two nodes here and crashes.",
    7: "L3's second 2 ties with L4's 2. Index 3 beats index 4, so L3 goes first again.",
    13: "The heap held 3 entries at most: one per NON-EMPTY list, not one per list.",
}


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Panel(View):
    """A titled side panel wrapping another view (here: the heap tree)."""

    def __init__(self, title, inner, note='', empty='(empty)'):
        self.title, self.inner, self.note, self.empty = title, inner, note, empty

    def draw(self, p, box):
        x0, y0, x1, y1 = box
        p.box(box, PANEL, PANEL_BORDER, 2, 12)
        p.text((x0 + 16, y0 + 14), self.title, 'bold', 18)
        if self.note:
            p.text((x0 + 16, y0 + 40), self.note, 'sans', 13, MUTED)
        if self.inner is None:
            p.text(((x0 + x1) / 2, (y0 + y1) / 2), self.empty, 'sans', 14, MUTED, 'mm')
        else:
            self.inner.draw(p, (x0 + 30, y0 + 74, x1 - 30, y0 + 74 + 190))
        self.used = y1 - y0


def trace(lists_vals):
    heads = []
    for v in lists_vals:
        nodes = [ListNode(x) for x in v]
        for a, b in zip(nodes, nodes[1:]):
            a.next = b
        heads.append(nodes[0] if nodes else None)
    events = []

    def rec(kind, heap, dummy, tail, cur_heads, **kw):
        # the answer so far runs from dummy.next to tail (the last appended node still
        # points at its old successor until the next append relinks it)
        out, x = [], dummy
        while x is not tail:
            x = x.next
            out.append(x.val)
        rest = []
        for h in cur_heads:
            r = []
            while h:
                r.append(h.val)
                h = h.next
            rest.append(r)
        events.append(dict(kind=kind, heap=[(v, i) for v, i, _ in heap], out=out, rest=rest, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    def mergeKLists(lists):
        cur_heads = list(lists)                       # display only: what's left of each list
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
                cur_heads[i] = node.next
        dummy = ListNode()
        curr = dummy
        rec('start', heap, dummy, curr, cur_heads)

        while heap:
            rec('peek', heap, dummy, curr, cur_heads)
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            nxt = node.next                           # display only
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
            cur_heads[i] = nxt.next if nxt else None
            rec('pop', heap, dummy, curr, cur_heads, val=val, i=i, pushed=nxt.val if nxt else None)

        rec('done', heap, dummy, curr, cur_heads)
        return dummy.next

    mergeKLists(heads)
    return events


def words(e, flags, k_lists=3):
    k = e['kind']
    if k == 'start':
        heads = ', '.join(f'{v} (L{i})' for v, i in sorted(e['heap'], key=lambda x: x[1]))
        return (f"Put the head of every list in a min-heap: {heads}.",
                "The next node of the answer is always the smallest head, and the heap keeps it on top.", KEY)
    if k == 'peek':
        v, i = e['heap'][0]
        tie = [x for x in e['heap'] if x[0] == v]
        if len(tie) > 1 and 'tie' not in flags:
            flags.add('tie')
            many = {2: 'Two', 3: 'Three'}.get(len(tie), str(len(tie)))
            return (f"{many} heads tie at {v}. The list index breaks the tie, so L{i} comes out first.",
                    "In Python that index also stops heapq from ever comparing two nodes.", KEY)
        return (f"The smallest head is {v}, from L{i}. Pop it.", "", QUICK * 2)
    if k == 'pop':
        if e['pushed'] is None:
            first = 'done' not in flags
            flags.add('done')
            return (f"Append {e['val']}. L{e['i']} has nothing left, so nothing is pushed: the heap shrinks.",
                    "" if not first else "The heap only ever holds one entry per list.", KEY if first else STEP)
        if 'push' not in flags:
            flags.add('push')
            return (f"Append {e['val']}, then push its successor {e['pushed']} from the same list L{e['i']}.",
                    "Only one head changed, so the heap needs one push, about log k steps.", KEY)
        return (f"Append {e['val']}; push {e['pushed']} from L{e['i']}.", "", STEP)
    return ("Heap empty: every node has been placed. Return dummy.next.",
            f"Each node went in and out of a heap of at most k = {k_lists}: O(n log k).", END)


def build(lists, subtitle, notes=None):
    sc = Scene('#23 Merge k Sorted Lists: min-heap of the heads', subtitle,
               width=1100, height=720, side_width=300)
    legend = [(style('good')[1], 'merged so far'), (ACTIVE, 'just appended / smallest head, about to pop'),
              ('#2f7e9e', 'colour = which list a node came from')]
    flags = set()
    for idx, e in enumerate(trace(lists)):
        views = []
        for i, rest in enumerate(e['rest']):
            views.append(ListView(rest if rest else [], None, {j: f'region{i + 1}' for j in range(len(rest))},
                                  title=f'L{i} rest', room=6, null=True))
        out = e['out']
        so = {j: 'good' for j in range(len(out))}
        if e['kind'] == 'pop' and out:
            so[len(out) - 1] = 'active'
        views.append(ListView(['D'] + out, None, {0: 'muted', **{j + 1: s for j, s in so.items()}},
                              title='merged', room=18))
        heap = e['heap']
        tree = None
        if heap:
            rings = [(0, ACTIVE)] if e['kind'] == 'peek' else []
            tree = TreeView([v for v, _ in heap], labels={j: f'L{i}' for j, (_, i) in enumerate(heap)},
                            styles={j: f'region{i + 1}' for j, (_, i) in enumerate(heap)}, rings=rings)
        cap, sub, hold = words(e, flags, len(lists))
        if notes and idx in notes:
            sub, hold = notes[idx], (END if e['kind'] == 'done' else KEY)
        sc.frame(views, cap, sub, hold,
                 side=Panel('Min-heap', tree, 'smallest on top, one entry per list'),
                 counters={'in heap': len(heap)}, legend=legend)
    return sc


def hard():
    """Harder input for the interactive page (scripts/motion_build.py)."""
    sc = build(HARD, f'lists = {HARD}. Three lists are empty, and three heads tie at 2.', HARD_NOTES)
    return sc, ("Three empty lists and a three-way tie at 2. Seed the heap without skipping empty lists and "
                "None.val crashes on L0; push bare (value, node) pairs and the tie raises TypeError. "
                "Answer: [1,2,2,2,2,5].")


def main():
    args = cli()
    sc = build(LISTS, f'lists = {LISTS}. The heap holds one head per list; pop the smallest, push its successor.')
    finish(sc, 23, "Watch the heap panel: it never holds more than one head per list, so each pop and "
                   "push costs about log k, not log n.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
