#!/usr/bin/env python3
"""#61 Rotate List: count to the tail, reduce k mod n, join the tail to the
head, walk n - k - 1 steps to the new tail and cut the ring after it.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

VALUES, K = [1, 2, 3, 4, 5], 2   # LeetCode example 1

# The hard example (interactive page only): six nodes and k = 2,000,000,000.
# Two billion is 333,333,333 full turns plus 2, so the answer is [5,6,1,2,3,4].
# Rotating one step at a time (move the last node to the front, k times) gets
# both LeetCode samples right (k = 2 and k = 4) but needs two billion passes here.
HARD_VALUES, HARD_K = [1, 2, 3, 4, 5, 6], 2_000_000_000
HARD_NOTES = {
    'mod': "2,000,000,000 = 333,333,333 full turns of 6, plus 2. A full turn changes nothing, so only the 2 is "
           "left. Rotating one step at a time would do all two billion.",
    'done': "One counting walk and three steps. The one-at-a-time version gets the same answer after two billion "
            "passes, about 10 billion node visits.",
}


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """The notebook's solution, to cross-check the traced run."""
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1
        k %= n
        if k == 0:
            return head
        tail.next = head
        new_tail = head
        for _ in range(n - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head


class OutOfTime(Exception):
    pass


def one_step_at_a_time(head, k, budget=10**6):
    """First attempt: move the last node to the front, k times. Counts node visits."""
    visits = 0
    for _ in range(k):
        if not head or not head.next:
            return head
        prev, cur = None, head
        while cur.next:
            prev, cur = cur, cur.next
            visits += 1
            if visits > budget:
                raise OutOfTime
        prev.next = None
        cur.next = head
        head = cur
    return head


def make(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def read(head, limit=600):
    out = []
    while head and len(out) < limit:
        out.append(head.val)
        head = head.next
    return out


def trace(values, k_in):
    nodes = [ListNode(v) for v in values]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    head = nodes[0] if nodes else None
    events = []
    ids = {id(x): i for i, x in enumerate(nodes)}

    def rec(kind, **ptrs):
        extra = ptrs.pop('extra', {})
        events.append(dict(kind=kind, nxt=[ids[id(x.next)] if x.next else None for x in nodes],
                           ptrs={n: (ids[id(v)] if v else None) for n, v in ptrs.items()}, **extra))

    # ---- the notebook's solution, with rec() calls added ----
    k = k_in
    rec('start', head=head)
    if not head or not head.next or k == 0:
        rec('early', head=head)
        return events
    n = 1
    tail = head
    rec('count', head=head, tail=tail, extra=dict(n=n))
    while tail.next:
        tail = tail.next
        n += 1
        rec('count', head=head, tail=tail, extra=dict(n=n))
    k %= n
    rec('mod', head=head, tail=tail, extra=dict(n=n, k=k, k_in=k_in))
    if k == 0:
        rec('zero', head=head, extra=dict(n=n, k=k))
        return events
    tail.next = head
    rec('ring', head=head, tail=tail, extra=dict(n=n, k=k))
    new_tail = head
    rec('walk', head=head, new_tail=new_tail, extra=dict(n=n, k=k, s=0))
    for s in range(n - k - 1):
        new_tail = new_tail.next
        rec('walk', head=head, new_tail=new_tail, extra=dict(n=n, k=k, s=s + 1))
    new_head = new_tail.next
    rec('found', new_tail=new_tail, new_head=new_head, extra=dict(n=n, k=k))
    new_tail.next = None
    rec('cut', new_tail=new_tail, new_head=new_head, extra=dict(n=n, k=k))
    ans = read(new_head)
    assert ans == read(Solution().rotateRight(make(values), k_in))
    rec('done', new_head=new_head, extra=dict(n=n, k=k, ans=ans))
    return events


def order(e, start):
    out, i, seen = [], start, set()
    while i is not None and i not in seen:
        seen.add(i)
        out.append(i)
        i = e['nxt'][i]
    return out


def build(values, k_in, subtitle, notes=None):
    notes = notes or {}
    sc = Scene('#61 Rotate List: close the ring, cut it elsewhere', subtitle, side_width=270)
    legend = [(style('gold')[1], 'last k nodes (move to the front)'), (style('window')[1], 'new tail'),
              (ACTIVE, 'pointer')]
    n_all = len(values)
    for e in trace(values, k_in):
        kd, p = e['kind'], e['ptrs']
        styles = {}
        k = e.get('k')
        if k:
            for i in range(n_all - k, n_all):
                styles[i] = 'gold'
        if kd in ('found', 'cut', 'done') or (kd == 'walk' and e['s'] == e['n'] - k - 1):
            styles[n_all - k - 1] = 'window'
        hold, sub = STEP, ''
        if kd == 'start':
            cap = f"Rotate right by k = {k_in:,}: the last k nodes move, in order, to the front."
            sub = "Only links change. First, count the nodes and find the tail."
        elif kd == 'count':
            cap = f"tail is on {values[p['tail']]}: n = {e['n']}."
            sub = ("Start n at 1 and stop ON the tail: it's the node we'll link back to the head."
                   if e['n'] == 1 else '')
            hold = STEP if e['n'] in (1, n_all) else QUICK * 1.5
        elif kd == 'mod':
            cap = f"k = {e['k_in']:,} % {e['n']} = {e['k']}."
            sub = notes.get('mod', "Rotating by n is a full turn and changes nothing, so only the remainder matters.")
            hold = KEY
        elif kd == 'ring':
            cap = f"Link the tail ({values[p['tail']]}) back to the head: the list is now a ring."
            sub = "Every rotation is this same ring, cut open in a different place."
            hold = KEY
        elif kd == 'walk':
            need = e['n'] - k - 1
            cap = (f"new_tail starts on the head, node 1 of {e['n']}." if e['s'] == 0 else
                   f"Step {e['s']} of {need}: new_tail moves to {values[p['new_tail']]}.")
            sub = (f"The new tail is node n − k = {e['n'] - k}. Starting on node 1, that's n − k − 1 = {need} steps."
                   if e['s'] == 0 else '')
            hold = STEP if e['s'] in (0, need) else QUICK * 2
        elif kd == 'found':
            cap = f"new_tail is {values[p['new_tail']]}; the node after it, {values[p['new_head']]}, is the new head."
            sub = f"The {k} gold nodes after the cut are the ones that end up in front."
            hold = STEP
        elif kd == 'cut':
            cap = f"Cut the ring: {values[p['new_tail']]}.next = null."
            sub = "Skip this and we'd return a ring with no end."
            hold = KEY
        elif kd == 'done':
            cap = f"Answer: {e['ans']}."
            sub = notes.get('done', "Two walks along the list, O(n), and no extra memory beyond a few pointers.")
            hold = END
        elif kd == 'zero':
            cap = "k % n = 0: a whole number of full turns. Return the list as it is."
            hold = END
        else:
            cap = "Empty list, one node or k = 0: nothing to rotate."
            hold = END
        start = p.get('new_head', p.get('head'))
        view = ListView(values, e['nxt'], styles, {kk: v for kk, v in p.items() if v is not None},
                        null=True, room=70)
        walk = order(e, start) if start is not None else []
        ring = start is not None and len(walk) == n_all and e['nxt'][walk[-1]] == walk[0]
        text = TextView([f"reading from {'new_head' if 'new_head' in p else 'head'}:  "
                         + ' -> '.join(str(values[i]) for i in walk) + (' -> (back to start)' if ring else ' -> null')],
                        size=16)
        rows = [('n', str(e.get('n', '?'))), ('k', f'{k_in:,}' if k is None else f'{k}')]
        rows += [(nm, str(values[v])) for nm, v in p.items() if v is not None]
        sc.frame([view, text], cap, sub, hold, side=MapView(rows, 'State', headers=('name', 'value')), legend=legend)
    return sc


def hard():
    """Harder input for the interactive page (scripts/motion_build.py)."""
    want = [5, 6, 1, 2, 3, 4]
    assert read(Solution().rotateRight(make(HARD_VALUES), HARD_K)) == want
    # the one-at-a-time attempt is right on both samples, but runs out of time here
    assert read(one_step_at_a_time(make([1, 2, 3, 4, 5]), 2)) == [4, 5, 1, 2, 3]
    assert read(one_step_at_a_time(make([0, 1, 2]), 4)) == [2, 0, 1]
    assert read(one_step_at_a_time(make(HARD_VALUES), HARD_K % 6)) == want
    try:
        one_step_at_a_time(make(HARD_VALUES), HARD_K, budget=10**6)
        raise AssertionError('expected the one-at-a-time rotation to blow its budget')
    except OutOfTime:
        pass
    sc = build(HARD_VALUES, HARD_K, 'head = [1,2,3,4,5,6], k = 2,000,000,000. Answer [5,6,1,2,3,4].', HARD_NOTES)
    return sc, ("k = 2,000,000,000 on six nodes. Moving the last node to the front k times passes both LeetCode "
                "samples but needs two billion passes here; k % 6 = 2 makes it three steps.")


def main():
    args = cli()
    sc = build(VALUES, K, f'head = {VALUES}, k = {K}. Move the last k nodes to the front by relinking.')
    finish(sc, 61, "Watch the tail link back to the head: once the list is a ring, rotating is just choosing where "
                   "to cut it.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
