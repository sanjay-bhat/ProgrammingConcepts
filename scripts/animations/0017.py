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

# Hard examples (interactive page only). Notes are keyed by 'begin', 'done', or
# (kind, digit index, letter) for the first time that step happens; each
# replaces that frame's second caption line and holds it as a KEY moment.
# 1) "79": both four-letter keys. "3 letters per key" ('a' + 3 * (d - 2) + k)
#    gives p q r for 7 and v w x for 9: 9 strings, three of them (pv, qv, rv)
#    not real. Answer: 16 combinations.
HARD1 = "79"
HARD1_NOTES = {
    'begin': "7 and 9 are the two keys with four letters: pqrs and wxyz.",
    ('choose', 1, 'w'): "9 starts at w. A 3-letters-per-key formula starts it at v, because 7's s shifts every key after it.",
    ('choose', 1, 'z'): "z is 9's fourth letter. A formula that assumes three per key never reaches it.",
    ('choose', 0, 's'): "s is 7's fourth letter, so 4 more combinations start here.",
    'done': "The 3-per-key formula returns only 9, and pv, qv, rv aren't even real.",
}
# 2) "234": three digits. Nested loops written for one or two digits return the
#    9 pairs from "23" and never look at the 4. Answer: 27 combinations.
HARD2 = "234"
HARD2_NOTES = {
    'begin': "Three digits means three levels of recursion, one per digit.",
    ('choose', 2, 'g'): "The third level. Two hard-coded loops stop at \"ad\" and never reach the 4.",
    'done': "Hard-coding a loop per digit for up to two digits returns 9 here.",
}


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


def words(e, first, digits=DIGITS, notes=None, seen=None):
    cap, sub, hold = _words(e, first, digits)
    if notes:
        k = e['kind']
        key = k if k in ('begin', 'done') else (k, e['index'], e.get('letter'))
        if key in notes and key not in seen:
            seen.add(key)
            return cap, notes[key], (END if k == 'done' else KEY)
    return cap, sub, hold


def _words(e, first, digits):
    k = e['kind']
    if k == 'begin':
        return (f'"{digits}" has {len(digits)} digits, so every answer is {len(digits)} letters long.',
                "One level of recursion per digit replaces a loop per digit, however many digits there are.", KEY)
    if k == 'choose':
        d = digits[e['index']]
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
            nxt = PHONE[digits[0]][PHONE[digits[0]].index(e['letter']) + 1]
            return (f"Back at the first digit: remove '{e['letter']}' and start over with '{nxt}'.",
                    f"'{nxt}' now gets paired with every letter of the next digit, just as '{e['letter']}' was.", KEY)
        return (f"Remove '{e['letter']}'.", "", QUICK)
    if k == 'return':
        return ("No letters left for this digit, so back up one level.", "", QUICK * 1.4)
    sizes = ' × '.join(f'{len(PHONE[d])} letters' for d in digits)
    return (f"Done: {len(e['result'])} combinations = {sizes}.", "", END)


def build(digits, subtitle, notes=None):
    events = trace(digits)
    first = {}
    for e in events:
        for k in ('choose', 'record', 'undo'):
            if e['kind'] == k and k not in first:
                first[k] = id(e)
        if e['kind'] == 'undo' and e['index'] == 0 and 'undo0' not in first:
            first['undo0'] = id(e)
    sc = Scene('#17 Letter Combinations: one level per digit', subtitle)
    legend = [(style('good')[1], 'letters chosen'), (ACTIVE, 'letter being tried')]
    seen = set()
    for e in events:
        k, idx = e['kind'], e['index']
        dstyles = {j: 'good' for j in range(len(e['current']))}
        if k in ('choose', 'undo', 'return') and idx is not None and idx < len(digits):
            dstyles[idx] = 'active' if k == 'choose' else 'window'
        dv = ArrayView(list(digits), dstyles, title='digits', cell=58,
                       pointers={'index': idx} if idx is not None and idx < len(digits) else {})
        views = [dv]
        if idx is not None and idx < len(digits):
            letters = PHONE[digits[idx]]
            lst = {}
            if k in ('choose', 'undo'):
                lst[letters.index(e['letter'])] = 'active' if k == 'choose' else 'muted'
            views.append(ArrayView(list(letters), lst, title=f'key {digits[idx]}', indices=False, cell=50))
        else:
            views.append(TextView([''], size=16))
        cur = ''.join(e['current'])
        views.append(TextView([f'current  "{cur}"'], size=20))
        got = [(r, 'good' if (k == 'record' and j == len(e['result']) - 1) or k == 'done' else None)
               for j, r in enumerate(e['result'])]
        views.append(ChipsView(got, 'Combinations recorded'))
        stack = [f'backtrack(index={i})' for i in e['calls']]
        cap, sub, hold = words(e, first, digits, notes, seen)
        sc.frame(views, cap, sub, hold, side=StackView(stack, 'Call stack', base='letterCombinations'),
                 counters={'found': len(e['result'])}, legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    sc1 = build(HARD1, f'digits = "{HARD1}". Both keys have four letters, not three.', HARD1_NOTES)
    sc2 = build(HARD2, f'digits = "{HARD2}". Three digits, so the call stack goes three levels deep.', HARD2_NOTES)
    return [(sc1, '"79": assume three letters per key and 7 loses its s and 9 becomes v w x, giving 9 strings '
                  'instead of 16. Watch for s and z, the fourth letters.'),
            (sc2, '"234": nested loops hard-coded for up to two digits return 9 strings. One level of '
                  'recursion per digit handles the third digit and finds all 27.')]


def main():
    args = cli()
    sc = build(DIGITS, f'digits = "{DIGITS}". Each digit stands for the letters on its phone key.')
    finish(sc, 17, "Watch the call stack: it's exactly as deep as the number of digits, and removing "
                   "the last letter after each answer is what lets the same list build all nine.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
