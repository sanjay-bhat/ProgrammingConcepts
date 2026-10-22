#!/usr/bin/env python3
"""#131 Palindrome Partitioning: cut off a palindrome, partition the rest, undo the cut.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

S = "aab"          # LeetCode example 1


def fmt(parts):
    return '[' + ','.join(f'"{p}"' for p in parts) + ']'


def trace(s):
    events, calls = [], []

    def rec(kind, path, result, **kw):
        events.append(dict(kind=kind, path=list(path), result=[list(r) for r in result],
                           calls=list(calls), **kw))

    # ---- the notebook's solution, with rec() calls added ----
    result = []

    def backtrack(start, path):
        calls.append(start)
        if start == len(s):
            result.append(path[:])
            rec('record', path, result, start=start)
            calls.pop()
            return
        rec('enter', path, result, start=start)
        for end in range(start + 1, len(s) + 1):
            sub = s[start:end]
            if sub == sub[::-1]:
                path.append(sub)
                rec('choose', path, result, start=start, end=end, sub=sub)
                backtrack(end, path)
                path.pop()
                rec('undo', path, result, start=start, end=end, sub=sub)
            else:
                rec('reject', path, result, start=start, end=end, sub=sub)
        calls.pop()
        rec('return', path, result, start=start)

    rec('begin', [], result, start=0)
    backtrack(0, [])
    rec('done', [], result, start=None)
    return events


def words(e, first):
    k = e['kind']
    if k == 'begin':
        return (f'Split "{S}" into pieces that are all palindromes (read the same both ways).',
                "Plan: cut off a first piece that's a palindrome, then split whatever is left the same way.", KEY)
    if k == 'enter':
        if e['start'] == 0:
            return ("Try every possible first piece, shortest first.", "", STEP)
        return (f'Pieces so far {fmt(e["path"])}. Now split the rest, "{S[e["start"]:]}".', "", STEP)
    if k == 'choose':
        if first.get('choose') == id(e):
            return (f'"{e["sub"]}" is a palindrome too: a longer first piece, starting a new set of partitions.',
                    f'Keep it and split what\'s after it, "{S[e["end"]:]}".', KEY)
        return (f'"{e["sub"]}" reads the same backwards: keep it as a piece and split what\'s after it.', "", STEP)
    if k == 'reject':
        if first.get('reject') == id(e):
            return (f'"{e["sub"]}" backwards is "{e["sub"][::-1]}": not a palindrome. Don\'t go any deeper.',
                    "Nothing that starts with this piece can be an answer, so the whole branch is skipped.", KEY)
        return (f'"{e["sub"]}" isn\'t a palindrome. Skip it.', "", STEP)
    if k == 'record':
        return (f"Reached the end of the string: {fmt(e['path'])} is a full partition. Record a copy.",
                "Every piece was checked when it was cut, so there's nothing left to verify.", KEY)
    if k == 'undo':
        if first.get('undo') == id(e):
            return (f'Back up: remove "{e["sub"]}" so the loop can try a longer piece from the same spot.',
                    "Undoing the cut is what lets one list of pieces be reused for every partition.", KEY)
        return (f'Remove "{e["sub"]}" and try the next length.', "", QUICK * 1.6)
    if k == 'return':
        return ("Every length from here has been tried, so this call returns.", "", QUICK * 1.4)
    return (f"Done: {len(e['result'])} partitions, " + ' and '.join(fmt(r) for r in e['result']) + '.', "", END)


def main():
    args = cli()
    events = trace(S)
    first = {}
    for e in events:
        for k in ('reject', 'undo'):
            if e['kind'] == k and k not in first:
                first[k] = id(e)
        if e['kind'] == 'choose' and len(e['sub']) > 1 and 'choose' not in first:
            first['choose'] = id(e)
    sc = Scene('#131 Palindrome Partitioning: cut, recurse, undo',
               f's = "{S}". Orange cuts mark the pieces kept so far.')
    legend = [(style('good')[1], 'pieces kept'), (ACTIVE, 'piece being tested'),
              (style('bad')[1], 'not a palindrome')]
    for e in events:
        k = e['kind']
        styles, cuts, pos = {}, [], 0
        for piece in e['path']:
            for j in range(pos, pos + len(piece)):
                styles[j] = 'good'
            pos += len(piece)
            cuts.append(pos)
        if k in ('choose', 'reject'):
            for j in range(e['start'], e['end']):
                styles[j] = 'bad' if k == 'reject' else 'active'
        ptrs, window = {}, None
        if k in ('choose', 'reject', 'undo'):
            ptrs = {'start': e['start'], 'end-1': e['end'] - 1}
            window = (e['start'], e['end'] - 1)
        elif e['start'] is not None and e['start'] < len(S):
            ptrs = {'start': e['start']}
        cuts = [c for c in cuts if 0 < c < len(S)]
        sv = ArrayView(list(S), styles, pointers=ptrs, window=window, title='s', cell=62, cuts=cuts)
        pieces = ChipsView([(f'"{p}"', 'good') for p in e['path']], 'Pieces so far (path)', empty='(none)')
        got = [(fmt(r), 'good' if k in ('record', 'done') else None) for r in e['result']]
        chips = ChipsView(got, 'Partitions found')
        stack = [f'backtrack(start={st})' for st in e['calls']]
        cap, sub, hold = words(e, first)
        sc.frame([sv, pieces, chips], cap, sub, hold,
                 side=StackView(stack, 'Call stack', base='partition'),
                 counters={'found': len(e['result'])}, legend=legend)
    finish(sc, 131, 'Watch "ab" get rejected: it isn\'t a palindrome, so nothing that starts with it is ever '
                    'explored, and the undo after each recorded partition frees the list for the next.',
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
