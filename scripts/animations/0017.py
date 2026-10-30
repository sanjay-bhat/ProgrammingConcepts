#!/usr/bin/env python3
"""#17 Letter Combinations: one level of recursion per digit, one branch per letter.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

DIGITS = "23"          # LeetCode example 1
PHONE = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
         '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}


def trace(digits):
    events, calls = [], []

    def rec(kind, current, result, **kw):
        events.append(dict(kind=kind, current=list(current), result=list(result), calls=list(calls), **kw))

    # ---- the notebook's solution, with rec() calls added ----
    phone_map = PHONE
    result = []

    def backtrack(index, current):
        calls.append(index)
        if index == len(digits):
            result.append(''.join(current))
            rec('record', current, result, index=index)
            calls.pop()
            return
        for letter in phone_map[digits[index]]:
            current.append(letter)
            rec('choose', current, result, index=index, letter=letter)
            backtrack(index + 1, current)
            current.pop()
            rec('undo', current, result, index=index, letter=letter)
        calls.pop()
        rec('return', current, result, index=index)

    rec('begin', [], result, index=0)
    backtrack(0, [])
    rec('done', [], result, index=None)
    return events


def words(e, first):
    k = e['kind']
    if k == 'begin':
        return (f'"{DIGITS}" has {len(DIGITS)} digits, so every answer is {len(DIGITS)} letters long.',
                "One level of recursion per digit replaces a loop per digit, however many digits there are.", KEY)
    if k == 'choose':
        d = DIGITS[e['index']]
        if first.get('choose') == id(e):
            return (f"Digit {d} gives {PHONE[d]}. Pick '{e['letter']}' and go on to the next digit.",
                    "", STEP)
        return (f"Digit {d}: pick '{e['letter']}'. So far: \"{''.join(e['current'])}\".", "", QUICK * 1.6)
    if k == 'record':
        if first.get('record') == id(e):
            return (f"Every digit has a letter: \"{e['result'][-1]}\" is a full combination. Record it.",
                    "The string is exactly as long as the input, so this is the bottom of the recursion.", KEY)
        return (f"Full length: record \"{e['result'][-1]}\".", "", QUICK * 1.6)
    if k == 'undo':
        if first.get('undo') == id(e):
            return (f"Remove '{e['letter']}' so the same digit can try its next letter.",
                    "Undoing the last letter is what lets one list build every combination.", KEY)
        if e['index'] == 0 and first.get('undo0') == id(e):
            nxt = PHONE[DIGITS[0]][PHONE[DIGITS[0]].index(e['letter']) + 1]
            return (f"Back at the first digit: remove '{e['letter']}' and start over with '{nxt}'.",
                    f"'{nxt}' now gets paired with every letter of the next digit, just as '{e['letter']}' was.", KEY)
        return (f"Remove '{e['letter']}'.", "", QUICK)
    if k == 'return':
        return ("No letters left for this digit, so back up one level.", "", QUICK * 1.4)
    return (f"Done: {len(e['result'])} combinations = 3 letters × 3 letters.", "", END)


def main():
    args = cli()
    events = trace(DIGITS)
    first = {}
    for e in events:
        for k in ('choose', 'record', 'undo'):
            if e['kind'] == k and k not in first:
                first[k] = id(e)
        if e['kind'] == 'undo' and e['index'] == 0 and 'undo0' not in first:
            first['undo0'] = id(e)
    sc = Scene('#17 Letter Combinations: one level per digit',
               f'digits = "{DIGITS}". Each digit stands for the letters on its phone key.')
    legend = [(style('good')[1], 'letters chosen'), (ACTIVE, 'letter being tried')]
    for e in events:
        k, idx = e['kind'], e['index']
        dstyles = {j: 'good' for j in range(len(e['current']))}
        if k in ('choose', 'undo', 'return') and idx is not None and idx < len(DIGITS):
            dstyles[idx] = 'active' if k == 'choose' else 'window'
        dv = ArrayView(list(DIGITS), dstyles, title='digits', cell=58,
                       pointers={'index': idx} if idx is not None and idx < len(DIGITS) else {})
        views = [dv]
        if idx is not None and idx < len(DIGITS):
            letters = PHONE[DIGITS[idx]]
            lst = {}
            if k in ('choose', 'undo'):
                lst[letters.index(e['letter'])] = 'active' if k == 'choose' else 'muted'
            views.append(ArrayView(list(letters), lst, title=f'key {DIGITS[idx]}', indices=False, cell=50))
        else:
            views.append(TextView([''], size=16))
        cur = ''.join(e['current'])
        views.append(TextView([f'current  "{cur}"'], size=20))
        got = [(r, 'good' if (k == 'record' and j == len(e['result']) - 1) or k == 'done' else None)
               for j, r in enumerate(e['result'])]
        views.append(ChipsView(got, 'Combinations recorded'))
        stack = [f'backtrack(index={i})' for i in e['calls']]
        cap, sub, hold = words(e, first)
        sc.frame(views, cap, sub, hold, side=StackView(stack, 'Call stack', base='letterCombinations'),
                 counters={'found': len(e['result'])}, legend=legend)
    finish(sc, 17, "Watch the call stack: it's exactly as deep as the number of digits, and removing "
                   "the last letter after each answer is what lets the same list build all nine.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
