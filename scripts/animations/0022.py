#!/usr/bin/env python3
"""#22 Generate Parentheses: add '(' while any are left, ')' while one is open.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

N = 3                 # LeetCode example 1

# Hard example (interactive page only): n = 4, 14 strings. Building each answer by
# wrapping a smaller one or putting "()" beside it finds only 13: never (())(()).
HARD_N = 4
MISSED = '(())(())'


def trace(n):
    events, calls = [], []

    def rec(kind, arr, pos, o, c, result, **kw):
        events.append(dict(kind=kind, arr=list(arr), pos=pos, open=o, close=c,
                           result=list(result), calls=list(calls), **kw))

    # ---- the notebook's solution, with rec() calls added ----
    result = []
    arr = [''] * (2 * n)

    def backtrack(pos: int, open_count: int, close_count: int) -> None:
        calls.append((pos, open_count, close_count))
        if pos == 2 * n:
            result.append(''.join(arr))
            rec('save', arr, pos, open_count, close_count, result)
            calls.pop()
            return
        rec('call', arr, pos, open_count, close_count, result)
        if not open_count < n:
            rec('no_open', arr, pos, open_count, close_count, result)
        if open_count < n:
            arr[pos] = '('
            backtrack(pos + 1, open_count + 1, close_count)
        if not close_count < open_count:
            rec('no_close', arr, pos, open_count, close_count, result)
        if close_count < open_count:
            was = arr[pos]                                               # display only
            arr[pos] = ')'
            if was == '(':
                rec('overwrite', arr, pos, open_count, close_count, result)
            backtrack(pos + 1, open_count, close_count + 1)
        calls.pop()

    rec('start', arr, 0, 0, 0, result)
    backtrack(0, 0, 0)
    rec('done', arr, 2 * n, n, n, result)
    assert result == Solution().generateParenthesis(n)
    return events


class Solution:
    """The notebook's solution (comments dropped), to cross-check the traced run."""
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        arr = [''] * (2 * n)

        def backtrack(pos: int, open_count: int, close_count: int) -> None:
            if pos == 2 * n:
                result.append(''.join(arr))
                return
            if open_count < n:
                arr[pos] = '('
                backtrack(pos + 1, open_count + 1, close_count)
            if close_count < open_count:
                arr[pos] = ')'
                backtrack(pos + 1, open_count, close_count + 1)

        backtrack(0, 0, 0)
        return result


def wrap_or_append(n):
    """First attempt: every answer for n comes from one for n - 1, wrapped in
    brackets or with "()" put before or after it."""
    found = {''}
    for _ in range(n):
        found = {g for s in found for g in ('(' + s + ')', '()' + s, s + '()')}
    return sorted(found)


def words(e, n, notes, firsts):
    k, pos, o, c = e['kind'], e['pos'], e['open'], e['close']
    pre = ''.join(e['arr'][:pos])
    if k == 'start':
        return (f"Build the string one bracket at a time, {2 * n} positions in all.",
                f"'(' is allowed while fewer than {n} are used; ')' only while one is still open.", KEY)
    if k == 'call':
        if pos == 0:
            return ("Empty so far. Only '(' is allowed: there's nothing to close yet.", "", STEP)
        last = e['arr'][pos - 1]
        tail = f" No '(' left, so ')' is the only move." if o == n and firsts.get('no_open_seen') else ""
        return (f"Added '{last}': prefix \"{pre}\", open {o}, close {c}.{tail}", "",
                STEP if firsts.get('call', 0) < 4 else QUICK * 2)
    if k == 'no_open':
        if firsts.get('no_open') == id(e):
            return (f"\"{pre}\" already uses all {n} '('. Another one is refused.",
                    "A string with too many '(' can never close properly, so don't build it.", KEY)
        return (f"All {n} '(' used: no more '(' here.", "", QUICK * 2)
    if k == 'no_close':
        if firsts.get('no_close') == id(e):
            return (f"\"{pre}\" has nothing open (close = open = {o}). ')' is refused.",
                    "A ')' with nothing to close breaks the string for good.", KEY)
        return (f"Nothing open in \"{pre}\", so no ')' here.", "", QUICK * 2)
    if k == 'overwrite':
        if firsts.get('overwrite') == id(e):
            return (f"Back at position {pos}: the '(' branch is finished. Write ')' over it.",
                    "No undo step: this slot is simply overwritten, and the later slots will be too.", KEY)
        return (f"Back at position {pos}: try ')' in the same slot.", "", QUICK * 2.5)
    if k == 'save':
        s = ''.join(e['arr'])
        note = notes.get(s)
        return (f"Full length: \"{s}\" is answer {len(e['result'])}. Save a copy.",
                note or "The rules never let a broken prefix exist, so no check is needed.",
                KEY if note or len(e['result']) == 1 else STEP)
    return (f"Done: {len(e['result'])} strings, every one valid, none checked afterwards.",
            notes.get('done', "Moves that could never work out were refused before anything was built on them."), END)


def build(n, subtitle, notes=None):
    notes = notes or {}
    sc = Scene(f'#22 Generate Parentheses: backtracking', subtitle)
    legend = [(style('good')[1], 'the prefix so far'), (ACTIVE, 'just written'),
              (style('muted')[1], 'left over from an earlier branch')]
    events = trace(n)
    firsts = {}
    for e in events:
        if e['kind'] in ('no_open', 'no_close', 'overwrite') and e['kind'] not in firsts:
            firsts[e['kind']] = id(e)
    calls_seen = 0
    for e in events:
        k, pos = e['kind'], e['pos']
        if k == 'no_open':
            if firsts['no_open'] != id(e):
                continue                 # folded into the call caption after the first time
            firsts['no_open_seen'] = True
        firsts['call'] = calls_seen
        calls_seen += k == 'call' and pos > 0
        styles = {}
        for j in range(2 * n):
            if j < pos:
                styles[j] = 'good'
            elif e['arr'][j]:
                styles[j] = 'muted'
        if k == 'call' and pos > 0:
            styles[pos - 1] = 'active'
        if k == 'overwrite':
            styles[pos] = 'active'
        if k == 'save':
            styles = {j: 'good' for j in range(2 * n)}
        ptrs = {'pos': pos} if pos < 2 * n and k not in ('done',) else {}
        arr = ArrayView([x or None for x in e['arr']], styles, pointers=ptrs, title='arr')
        counts = TextView([f"open {e['open']} of {n}   close {e['close']}",
                           (f"'(' {'allowed' if e['open'] < n else 'refused'},  "
                            f"')' {'allowed' if e['close'] < e['open'] else 'refused'}", None)], size=17)
        newest = len(e['result']) - 1 if k == 'save' else None
        chips = ChipsView([(s, 'good' if j == newest or k == 'done' else None) for j, s in enumerate(e['result'])],
                          'Saved', empty='(none yet)', size=16)
        views = [arr, chips] if k in ('done', 'start') else [arr, counts, chips]
        stack = [f'backtrack(pos={p}, open={o}, close={c})' for p, o, c in e['calls']]
        cap, sub, hold = words(e, n, notes, firsts)
        sc.frame(views, cap, sub, hold,
                 side=StackView(stack, 'Call stack', note=None,
                                base=f'generateParenthesis({n})', empty='(empty)'),
                 counters={'saved': len(e['result'])}, legend=legend)
    return sc


def hard():
    """Harder input for the interactive page (scripts/motion_build.py)."""
    right, wrong = Solution().generateParenthesis(HARD_N), wrap_or_append(HARD_N)
    assert len(right) == 14 and len(wrong) == 13 and set(right) - set(wrong) == {MISSED}
    sc = build(HARD_N, 'n = 4. 14 strings. Building from smaller answers (wrap, or add "()" beside) finds only 13.', {
        MISSED: "This is the one that wrap-or-append can't make: two wrapped pairs side by side.",
        'done': "Backtracking never builds from smaller answers, so (())(()) is reached like any other.",
    })
    return sc, ("n = 4: a first attempt that builds each answer from an n - 1 answer, wrapping it or putting () "
                "beside it, finds 13 strings and never makes (())(()). Backtracking finds all 14.")


def main():
    args = cli()
    sc = build(N, f'n = {N}. List every string of {N} matched bracket pairs.')
    finish(sc, 22, "Watch for the refused moves: a ')' with nothing open, or a fourth '(', is never written, "
                   "so every string that reaches full length is already valid.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
