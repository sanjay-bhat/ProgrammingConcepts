#!/usr/bin/env python3
"""#100 Same Tree: walk both trees together and compare the pair in each position.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. The two trees hold the same values
(1, 2, 3) but the 3 sits in a different place, the smallest pair that shows
both a both-empty match and a one-empty mismatch.

Empty spots are drawn as faint '-' nodes so the reader can see which pair is
being compared; they are NOT nodes in the trees the solution runs on.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

E = '-'                                        # an empty spot, drawn but not a node
P_DRAW = [1, 2, 3, E, E]                       # p = [1,2,3] (only 2's empty children drawn)
Q_DRAW = [1, 2, E, E, 3]                       # q = [1,2,null,null,3]


class TreeNode:
    def __init__(self, val, idx):
        self.val, self.idx, self.left, self.right = val, idx, None, None


def build(draw):
    kids = TreeView.structure(draw)
    nodes = {i: TreeNode(draw[i], i) for i in kids if draw[i] != E}
    for i in nodes:
        l, r = kids[i]
        nodes[i].left, nodes[i].right = nodes.get(l), nodes.get(r)
    return nodes[0]


class Row(View):
    """Views side by side, each with a small title above it."""

    def __init__(self, views, titles):
        self.views, self.titles = views, titles

    def draw(self, p, box):
        x0, y0, x1, y1 = box
        gap = 30
        w = (x1 - x0 - gap * (len(self.views) - 1)) / len(self.views)
        used = 0
        for k, (v, t) in enumerate(zip(self.views, self.titles)):
            bx = x0 + k * (w + gap)
            p.text((bx + w / 2, y0 + 8), t, 'bold', 16, MUTED, 'mm')
            v.draw(p, (bx, y0 + 24, bx + w, y1))
            used = max(used, v.used + 24)
        self.used = used


def trace():
    kp, kq = TreeView.structure(P_DRAW), TreeView.structure(Q_DRAW)
    events, calls, verdict = [], [], {}

    def spot(node, kids, k):                   # recorder only: where this node or empty spot is drawn
        if node:
            return node.idx
        if not calls:
            return None
        par, side = calls[-1][k], calls[-1][3] - 1
        return kids[par][side] if par is not None else None

    def rec(kind, **kw):
        events.append(dict(kind=kind, calls=[list(c) for c in calls], verdict=dict(verdict), **kw))

    class Solution:
        # ---- the notebook's solution, with rec() calls added ----
        def isSameTree(self, p, q) -> bool:
            if calls:
                calls[-1][3] += 1
            pi, qi = spot(p, kp, 0), spot(q, kq, 1)
            calls.append([pi, qi, None, 0])
            if not p and not q:
                verdict[(pi, qi)] = True; rec('both-empty', pi=pi, qi=qi); calls.pop()
                return True
            if not p or not q:
                verdict[(pi, qi)] = False
                rec('one-empty', pi=pi, qi=qi, which='p' if not p else 'q', other=(q or p).val); calls.pop()
                return False
            if p.val != q.val:
                verdict[(pi, qi)] = False; rec('values', pi=pi, qi=qi, a=p.val, b=q.val); calls.pop()
                return False
            rec('match', pi=pi, qi=qi, v=p.val)
            ans = self.isSameTree(p.left, q.left) and \
                self.isSameTree(p.right, q.right)
            verdict[(pi, qi)] = ans
            rec('return', pi=pi, qi=qi, v=p.val, ans=ans, skipped=calls[-1][3] < 2)
            calls.pop()
            return ans

    rec('start')
    answer = Solution().isSameTree(build(P_DRAW), build(Q_DRAW))
    rec('done', ans=answer)
    return events


def words(e):
    k = e['kind']
    if k == 'start':
        return ("Same values in both trees, but are they in the same places?",
                "Compare the pair of nodes in each position, starting with the two roots.", STEP)
    if k == 'match':
        return (f"Pair ({e['v']}, {e['v']}): both exist and the values match.",
                "Now the left pair must match, and then the right pair.", STEP)
    if k == 'both-empty':
        return ("Pair (empty, empty): nothing on either side, so this spot matches.",
                "This check comes first; otherwise two empty spots would look like a mismatch.", KEY)
    if k == 'one-empty':
        side = "p's spot is empty but q has a 3" if e['which'] == 'p' else f"q's spot is empty but p has a {e['other']}"
        return (f"Pair (empty, {e['other']}): {side}. The shapes differ: false." if e['which'] == 'p'
                else f"Pair ({e['other']}, empty): {side}. The shapes differ: false.",
                "Only now would it be safe to read .val, and it never has to.", KEY)
    if k == 'values':
        return (f"Pair ({e['a']}, {e['b']}): different values: false.", "", KEY)
    if k == 'return':
        if not e['ans'] and e['skipped']:
            return (f"Pair ({e['v']}, {e['v']}) gets false from the left, so it returns false at once.",
                    "'and' stops at the first false: the right pair is never compared.", KEY)
        why = "Its right pair didn't match, so neither does this one." if not e['ans'] else ""
        return (f"Pair ({e['v']}, {e['v']}) returns {str(e['ans']).lower()}.", why, STEP)
    return (f"isSameTree returns {str(e['ans']).lower()}.",
            "Same values, different positions. The faded pairs were never compared.", END)


def main():
    args = cli()
    sc = Scene('#100 Same Tree: compare the pair in each position',
               "Faint '-' marks an empty spot. Green = this pair matched, red = it didn't.")
    legend = [(ACTIVE, 'pair being compared'), (style('window')[1], 'waiting'),
              (style('good')[1], 'matched'), (style('bad')[1], 'mismatch')]
    kp, kq = TreeView.structure(P_DRAW), TreeView.structure(Q_DRAW)
    for e in trace():
        sp = {i: 'muted' for i in kp if P_DRAW[i] == E}
        sq = {i: 'muted' for i in kq if Q_DRAW[i] == E}
        for (pi, qi), ok in e['verdict'].items():
            if pi is not None: sp[pi] = 'good' if ok else 'bad'
            if qi is not None: sq[qi] = 'good' if ok else 'bad'
        for pi, qi, _, _ in e['calls']:
            if (pi, qi) not in e['verdict']:
                sp[pi] = sq[qi] = 'window'
        rp, rq = [], []
        if 'pi' in e:
            rp, rq = [(e['pi'], ACTIVE)], [(e['qi'], ACTIVE)]
            if e['kind'] == 'match':
                sp[e['pi']] = sq[e['qi']] = 'active'
        if e['kind'] == 'done':
            seen = {pi for pi, _ in e['verdict']}
            sp.update({i: 'muted' for i in kp if i not in seen})
            seenq = {qi for _, qi in e['verdict']}
            sq.update({i: 'muted' for i in kq if i not in seenq})
        name = lambda d, i: 'empty' if d[i] == E else str(d[i])
        stack = []
        for pi, qi, _, _ in e['calls']:
            s = f'same({name(P_DRAW, pi)}, {name(Q_DRAW, qi)})'
            v = e['verdict'].get((pi, qi))
            stack.append((s + ('' if v is None else f'  = {str(v).lower()}'),
                          None if v is None else ('good' if v else 'bad')))
        cap, sub, hold = words(e)
        res = str(e['ans']).lower() if e['kind'] == 'done' else '?'
        sc.frame(Row([TreeView(P_DRAW, styles=sp, rings=rp), TreeView(Q_DRAW, styles=sq, rings=rq)],
                     ['p = [1,2,3]', 'q = [1,2,null,null,3]']),
                 cap, sub, hold, side=StackView(stack, 'Call stack', base='isSameTree(p, q)'),
                 counters={'answer': res}, legend=legend)
    finish(sc, 100, "Watch the pair (empty, 3) under the 2s: one side is empty and the other isn't, "
                    "so the shapes differ, and the roots' right sides are never compared.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
