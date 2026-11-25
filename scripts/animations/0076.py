#!/usr/bin/env python3
"""#76 Minimum Window Substring: stretch the right edge until the window
covers t, then squeeze from the left while it still does, recording the
shortest. `formed` counts the letters that have ENOUGH copies, so "covered?"
is one comparison.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
from collections import Counter
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

S, T = "ADOBECODEBANC", "ABC"          # LeetCode example 1: "BANC"

# Hard example 1: LeetCode's string, but t needs TWO A's. Treating t as a set
# of letters passes the first two samples (and this exact string with t = "ABC"),
# then answers "BANC", which has only one A. The real answer is 11 long.
HARD1 = ("ADOBECODEBANC", "AABC")
HARD1_ANSWER, HARD1_WRONG = "ADOBECODEBA", "BANC"

# Hard example 2: when the window first covers "SSP", five letters in a row can
# be dropped from the left. Shrinking with `if` (one drop per new letter)
# instead of `while` answers "MISSISSIP"; the real answer is "SSIP".
HARD2 = ("MISSISSIPPI", "SSP")
HARD2_ANSWER, HARD2_WRONG = "SSIP", "MISSISSIP"


class Solution:
    # ---- the notebook's solution, unchanged (used to check the answers) ----
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        need = Counter(t)
        required = len(need)
        window = {}
        formed = 0
        l = 0
        min_len = float('inf')
        min_l = 0
        for r, c in enumerate(s):
            window[c] = window.get(c, 0) + 1
            if c in need and window[c] == need[c]:
                formed += 1
            while formed == required:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_l = l
                lc = s[l]
                window[lc] -= 1
                if lc in need and window[lc] < need[lc]:
                    formed -= 1
                l += 1
        return "" if min_len == float('inf') else s[min_l:min_l + min_len]


def variant(s, t, as_set=False, shrink_once=False):
    """The notebook's loop with one first-attempt change switched on."""
    need = Counter(set(t)) if as_set else Counter(t)
    required, window, formed, l = len(need), {}, 0, 0
    min_len, min_l = float('inf'), 0
    for r, c in enumerate(s):
        window[c] = window.get(c, 0) + 1
        if c in need and window[c] == need[c]:
            formed += 1
        while formed == required:
            if r - l + 1 < min_len:
                min_len, min_l = r - l + 1, l
            lc = s[l]
            window[lc] -= 1
            if lc in need and window[lc] < need[lc]:
                formed -= 1
            l += 1
            if shrink_once:
                break
    return "" if min_len == float('inf') else s[min_l:min_l + min_len]


def wrong_as_set(s, t):
    """First attempt: only check that each DIFFERENT letter of t is present."""
    return variant(s, t, as_set=True)


def wrong_if(s, t):
    """First attempt: shrink with `if` (at most one drop per step) instead of `while`."""
    return variant(s, t, shrink_once=True)


assert variant(S, T) == Solution().minWindow(S, T) == "BANC"
for _s, _t, _a in ((S, T, "BANC"), ("a", "a", "a")):     # the set version passes these two samples
    assert wrong_as_set(_s, _t) == _a
assert Solution().minWindow(*HARD1) == HARD1_ANSWER and wrong_as_set(*HARD1) == HARD1_WRONG
assert Solution().minWindow(*HARD2) == HARD2_ANSWER and wrong_if(*HARD2) == HARD2_WRONG


def trace(s, t):
    events = []

    def rec(kind, **kw):
        events.append(dict(kind=kind, l=l, r=r, window=dict(window), formed=formed, best=(min_len, min_l), **kw))

    # ---- the notebook's solution, with rec() calls added ----
    need = Counter(t)
    required = len(need)
    window = {}
    formed = 0
    l, r = 0, -1
    min_len = float('inf')
    min_l = 0
    rec('start', need=need, required=required)
    for r, c in enumerate(s):
        window[c] = window.get(c, 0) + 1
        became = c in need and window[c] == need[c]
        if c in need and window[c] == need[c]:
            formed += 1
        rec('add', c=c, became=became, need=need, required=required)
        while formed == required:
            improved = r - l + 1 < min_len
            if r - l + 1 < min_len:
                min_len = r - l + 1
                min_l = l
            covered_len = r - l + 1
            lc = s[l]
            window[lc] -= 1
            broke = lc in need and window[lc] < need[lc]
            if lc in need and window[lc] < need[lc]:
                formed -= 1
            l += 1
            rec('drop', c=lc, broke=broke, improved=improved, covered=(l - 1, r), clen=covered_len,
                need=need, required=required)
    rec('done', need=need, required=required, ans="" if min_len == float('inf') else s[min_l:min_l + min_len])
    return events


def build(s, t, subtitle, notes=None):
    """notes: {kind or (kind, r, l): text} replaces that frame's second caption line, held as KEY."""
    notes = notes or {}
    sc = Scene('#76 Minimum Window Substring: stretch right, squeeze left', subtitle, side_width=270)
    final = Solution().minWindow(s, t)
    legend = [(style('window')[1], 'in the window'), (ACTIVE, 'letter just added / dropped'),
              (style('good')[1], 'best window so far'), (style('muted')[1], 'left behind')]
    first = set()
    for e in trace(s, t):
        k, l, r, need = e['kind'], e['l'], e['r'], e['need']
        bl, bs = e['best']
        styles = {}
        for i in range(len(s)):
            styles[i] = 'window' if l <= i <= r else ('muted' if i < l else 'plain')
        subs = {}
        if bl != float('inf'):
            for i in range(bs, bs + bl):
                subs[i] = 'best'
        hold, sub = STEP, ''
        win = (l, r)
        if k == 'start':
            cap = f'Find the shortest stretch of s that holds every letter of t = "{t}", with repeats.'
            sub = f"formed counts letters with ENOUGH copies; the window covers t when formed = {e['required']}."
            hold = KEY
        elif k == 'add':
            styles[r] = 'active'
            if e['became']:
                cap = (f"r = {r}: add '{e['c']}'. That's {need[e['c']]} of {need[e['c']]} needed: "
                       f"formed = {e['formed']} of {e['required']}.")
                if e['formed'] == e['required'] and 'covered' not in first:
                    first.add('covered')
                    sub = "The window covers t. Now squeeze it from the left for as long as it still does."
                    hold = KEY
            elif e['c'] in need:
                cap = f"r = {r}: add '{e['c']}' (now {e['window'][e['c']]}, needed {need[e['c']]}). formed stays {e['formed']}."
                sub = "Only the copy that REACHES the need counts; extra copies don't bump formed again."
                hold = STEP
            else:
                cap = f"r = {r}: add '{e['c']}'. t doesn't need it; formed stays {e['formed']}."
                hold = QUICK * 1.6
        elif k == 'drop':
            a, b = e['covered']
            win = (a, b)
            styles[a] = 'active'
            for i in range(len(s)):
                if a < i <= b:
                    styles[i] = 'window'
            rec_txt = (f"s[{a}..{b}] covers t, length {e['clen']}: new best."
                       if e['improved'] else f"s[{a}..{b}] covers t, length {e['clen']}: not shorter.")
            if e['broke']:
                cap = rec_txt + f" Drop '{e['c']}': now too few, formed = {e['formed']}. Back to stretching."
                if 'broke' not in first:
                    first.add('broke')
                    sub = "Record BEFORE dropping: after the drop the window may no longer cover t."
                    hold = KEY
            else:
                cap = rec_txt + f" Drop '{e['c']}': still covered, keep squeezing."
                hold = STEP if e['improved'] else QUICK * 2
                if e['c'] in need and 'dup' not in first:
                    first.add('dup')
                    sub = f"'{e['c']}' is needed, but the window has a spare copy, so dropping it breaks nothing."
                    hold = KEY
            if e['improved'] and s[a:b + 1] == final and not sub:
                sub = "The answer, found while squeezing, not when the window first covered t."
                hold = KEY
        else:
            ans = e['ans']
            cap = f'r has reached the end. Answer: "{ans}".' if ans else 'r has reached the end. No window covered t: answer "".'
            sub = "l and r each move forward at most len(s) times: O(len(s) + len(t))."
            hold = END
        for key in ((k, r, l), k):
            if key in notes:
                sub, hold = notes[key], max(hold, KEY)
                break
        letters = sorted(need)
        side = [(f"'{ch}'", f"{e['window'].get(ch, 0)} of {need[ch]}",
                 'good' if e['window'].get(ch, 0) >= need[ch] else None) for ch in letters]
        side += [('formed', f"{e['formed']} of {e['required']}", 'good' if e['formed'] == e['required'] else None),
                 ('best', '-' if bl == float('inf') else f'"{s[bs:bs + bl]}" ({bl})', 'good' if bl != float('inf') else None)]
        arr = ArrayView(list(s), styles, pointers={'l': win[0], 'r': win[1]} if k != 'start' else {},
                        window=win if win[0] <= win[1] else None, title='s', subs=subs)
        best_txt = '-' if bl == float('inf') else f'"{s[bs:bs + bl]}"'
        sc.frame([arr, TextView([f'window = "{s[win[0]:win[1] + 1]}"', (f'best   = {best_txt}', 'good')], size=17)],
                 cap, sub, hold, side=MapView(side, 'Have vs need', headers=('letter', 'in window')), legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    sc1 = build(*HARD1, 's = "ADOBECODEBANC", t = "AABC". The sample string, but t needs two A\'s.',
                {('add', 10, 0): "The second A: only now is 'A' satisfied. A window with one A doesn't cover t.",
                 'done': 'Checking only that each different letter appears passes the samples, then answers "BANC" here: one A short.'})
    sc2 = build(*HARD2, 's = "MISSISSIPPI", t = "SSP". Once covered, five letters in a row can go.',
                {'done': 'Shrinking with `if` drops one letter per step and answers "MISSISSIP". The while keeps squeezing to "SSIP".'})
    return [(sc1, 'LeetCode\'s string with t = "AABC". Treating t as a set of letters passes the first two samples, '
                  'then answers "BANC", which has only one A. The real answer is "ADOBECODEBA".'),
            (sc2, 's = "MISSISSIPPI", t = "SSP". Once the first P arrives, five letters can be dropped in a row; '
                  'shrinking with `if` instead of `while` stops after one and answers "MISSISSIP".')]


def main():
    args = cli()
    sc = build(S, T, 'LeetCode example 1. The window is s[l..r]; it covers t when formed reaches 3.')
    finish(sc, 76, "Watch the window squeeze from the left after each stretch: the shortest cover, BANC, "
                   "only turns up while shrinking at the very end.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
