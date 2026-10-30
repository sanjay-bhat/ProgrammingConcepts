#!/usr/bin/env python3
"""#3 Longest Substring Without Repeating Characters: a window plus a last-seen map.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

S_MAIN = "abcabcbb"          # LeetCode example 1

# Hard examples (interactive page only), each breaking a plausible first attempt.
HARD_ABBA = "abba"           # answer 2; without the >= left check: 3
HARD_DVDF = "dvdf"           # answer 3; restarting the window at the repeat: 2


def trace(s):
    events = []
    st = {'left': 0, 'right': None, 'best': 0, 'best_at': None}

    def rec(kind, char_map, **kw):
        events.append(dict(kind=kind, map=dict(char_map), **st, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    char_map = {}
    max_length = 0
    left = 0
    rec('start', char_map)

    for right, current in enumerate(s):
        st['right'] = right
        stale = current in char_map and char_map[current] < left          # display only
        if current in char_map and char_map[current] >= left:
            rec('clash', char_map, old=char_map[current])
            left = char_map[current] + 1
            st['left'] = left

        clashed = events[-1]['kind'] == 'clash' and events[-1]['right'] == right   # display only
        if stale:
            rec('stale', char_map, old=char_map[current])
        old = char_map.get(current)                                        # display only
        char_map[current] = right

        before = max_length                                                # display only
        max_length = max(max_length, right - left + 1)
        if max_length > before:
            st['best_at'] = (left, right)
        st['best'] = max_length
        rec('jump' if clashed else 'extend', char_map, old=old, grew=max_length > before)

    st['right'] = None
    rec('done', char_map)
    assert max_length == Solution().lengthOfLongestSubstring(s)
    return events


class Solution:
    """The notebook's solution (comments dropped), to cross-check the traced run."""
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_length = 0
        left = 0
        for right, current in enumerate(s):
            if current in char_map and char_map[current] >= left:
                left = char_map[current] + 1
            char_map[current] = right
            max_length = max(max_length, right - left + 1)
        return max_length


def no_left_check(s):
    """First attempt: trust the map without checking the sighting is inside the window."""
    char_map, max_length, left = {}, 0, 0
    for right, current in enumerate(s):
        if current in char_map:
            left = char_map[current] + 1
        char_map[current] = right
        max_length = max(max_length, right - left + 1)
    return max_length


def restart_at_repeat(s):
    """First attempt: on a repeat, throw the window away and start again at the repeat."""
    seen, max_length, left = set(), 0, 0
    for right, current in enumerate(s):
        if current in seen:
            seen, left = set(), right
        seen.add(current)
        max_length = max(max_length, right - left + 1)
    return max_length


def words(e, s, notes, first):
    k, r, L = e['kind'], e['right'], e['left']
    win = s[L:r + 1] if r is not None else ''
    if k == 'start':
        return ("Slide a window across the string. right moves one letter at a time.",
                "The map remembers the last index where each letter was seen.", KEY)
    ch = s[r] if r is not None else ''
    if k == 'clash':
        o = e['old']
        return (f"'{ch}' at {r} was last seen at {o}, and {o} ≥ left = {L}: it's inside the window.",
                f"Any window starting at or before {o} holds both '{ch}'s, so left must jump to {o + 1}.",
                KEY if first else STEP * 1.4)
    if k == 'jump':
        tail = f" Best is still {e['best']}." if not e['grew'] else f" New best: {e['best']}."
        return (f"left jumps to {L}. Record '{ch}' at {r}. Window \"{win}\", length {r - L + 1}.{tail}",
                notes.get('jump', "One jump, no removing letters one by one."), STEP)
    if k == 'stale':
        return (f"'{ch}' was last seen at {e['old']}, but that's left of left = {L}: already outside the window.",
                notes.get('stale', "So it's no repeat. Ignore the old sighting and just record the new one."), KEY)
    if k == 'extend':
        new = (f"'{ch}' is not in the map yet." if e['old'] is None else
               f"The old '{ch}' at {e['old']} is outside the window, so no repeat.")
        tail = f" New best: {e['best']}." if e['grew'] else ""
        return (f"{new} Record '{ch}' at {r}. Window \"{win}\", length {r - L + 1}.{tail}",
                notes.get('extend', ""), STEP)
    a, b = e['best_at'] if e['best_at'] else (0, -1)
    return (f"Done. The longest window without a repeat was \"{s[a:b + 1]}\": answer {e['best']}.",
            notes.get('done', "left only ever moved forward, so each letter was handled once: O(n)."), END)


def build(s, subtitle, notes=None):
    notes = notes or {}
    sc = Scene('#3 Longest Substring Without Repeating Characters', subtitle)
    legend = [(style('window')[1], 'window s[left..right]'), (ACTIVE, 'letter at right'),
              (style('bad')[1], 'old copy inside window'), (style('muted')[1], 'left behind')]
    clashes = 0
    for e in trace(s):
        k, L, r = e['kind'], e['left'], e['right']
        clashes += k == 'clash'
        styles = {}
        for i in range(len(s)):
            if r is not None and L <= i <= r:
                styles[i] = 'window'
            elif i < L:
                styles[i] = 'muted'
        if r is not None:
            styles[r] = 'active'
        if k == 'clash':
            styles[e['old']] = 'bad'
        if k == 'stale':
            styles[e['old']] = 'muted'
        if k == 'done' and e['best_at']:
            a, b = e['best_at']
            styles = {i: 'good' if a <= i <= b else 'muted' for i in range(len(s))}
        ptrs = {}
        if k != 'done':
            ptrs = {'left': L}
            if r is not None:
                ptrs['right'] = r
        win = (L, r) if r is not None and k != 'done' else None
        arr = ArrayView(list(s), styles, pointers=ptrs, window=win, title='s')
        lines = []
        if r is not None:
            lines.append(f'window  "{s[L:r + 1]}"   length {r - L + 1}')
        elif k == 'start':
            lines.append('window  ""   length 0')
        if e['best_at']:
            a, b = e['best_at']
            lines.append((f'best    "{s[a:b + 1]}"   length {e["best"]}', 'good'))
        else:
            lines.append('best    0')
        text = TextView(lines, size=18)
        cur = s[r] if r is not None else None
        rows = []
        for ch, idx in e['map'].items():
            if k == 'done':
                st = None
            elif ch == cur and k in ('clash', 'stale'):
                st = 'bad' if k == 'clash' else 'muted'
            elif ch == cur:
                st = 'active'
            elif idx < L:
                st = 'muted'
            else:
                st = 'window'
            note = '  (left of window)' if idx < L and k != 'done' else ''
            rows.append((f"'{ch}'", f'{idx}{note}', st))
        side = MapView(rows, 'Last seen at', headers=('letter', 'index'), empty='(empty)')
        cap, sub, hold = words(e, s, notes, clashes == 1)
        sc.frame([arr, text], cap, sub, hold, side=side,
                 counters={'left': L, 'best': e['best']}, legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    assert Solution().lengthOfLongestSubstring(HARD_ABBA) == 2 and no_left_check(HARD_ABBA) == 3
    assert Solution().lengthOfLongestSubstring(HARD_DVDF) == 3 and restart_at_repeat(HARD_DVDF) == 2
    abba = build(HARD_ABBA, 's = "abba". Answer 2. Dropping the >= left check gives 3.', {
        'jump': "The map still says 'a' is at 0. That sighting is now left of the window.",
        'stale': "Without the >= left check, left would jump BACK to 1 and count \"bba\": 3, wrong.",
        'done': "The >= left check stopped the stale 'a' from dragging the left edge backwards."})
    dvdf = build(HARD_DVDF, 's = "dvdf". Answer 3. Restarting the window at the repeat gives 2.', {
        'jump': "left goes just past the OLD 'd', not to the new one: 'v' stays in the window.",
        'done': "Restarting at the repeated 'd' would throw 'v' away and never see \"vdf\"."})
    return [
        (abba, "\"abba\": when the last 'a' arrives, its old copy at 0 is already outside the window. "
               "Trusting the map without the >= left check pulls left back to 1 and answers 3; the right answer is 2."),
        (dvdf, "\"dvdf\": a first attempt that clears the window and restarts at the repeated 'd' finds only \"df\" (2). "
               "Jumping just past the old 'd' keeps 'v' and finds \"vdf\": the answer is 3."),
    ]


def main():
    args = cli()
    sc = build(S_MAIN, 's = "abcabcbb". Find the longest run of letters with no letter twice.')
    finish(sc, 3, "Watch index 3: the second 'a' was last seen inside the window, so left jumps "
                  "straight past the old copy in one move instead of shrinking letter by letter.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
