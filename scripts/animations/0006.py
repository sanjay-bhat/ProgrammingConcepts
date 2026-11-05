#!/usr/bin/env python3
"""#6 ZigZag Conversion: walk a row cursor down and back up, dropping each
letter into its row's bucket, then read the rows top to bottom.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. The column each letter is drawn in
is for the picture only: the solution never computes it.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

S, ROWS = "PAYPALISHIRING", 3          # LeetCode example 1

# Hard example (interactive page only). With one row, row 0 is both the top
# and the bottom, so the bounce flips the cursor "down" into a row that
# doesn't exist. A first attempt that only guards len(s) <= numRows passes all
# three LeetCode samples ("A", 1 is caught by the length check) and then
# crashes on the second letter here.
HARD = ("LEETCODE", 1)


class Solution:
    """The notebook's solution (comments dropped), to cross-check the traced run."""
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1 or len(s) <= num_rows:
            return s

        rows = [""] * num_rows
        curr_row, going_down = 0, False

        for c in s:
            rows[curr_row] += c
            if curr_row == 0 or curr_row == num_rows - 1:
                going_down = not going_down
            curr_row += 1 if going_down else -1

        return "".join(rows)


def length_guard_only(s, num_rows):
    """First attempt: the same walk, guarded only by len(s) <= num_rows."""
    if len(s) <= num_rows:
        return s
    rows = [""] * num_rows
    curr_row, going_down = 0, False
    for c in s:
        rows[curr_row] += c
        if curr_row == 0 or curr_row == num_rows - 1:
            going_down = not going_down
        curr_row += 1 if going_down else -1
    return "".join(rows)


def trace(s, num_rows, guard=True):
    """guard=True runs the notebook's solution; guard=False the first attempt
    above (same lines, minus the num_rows == 1 check), until it crashes."""
    events = []
    col = 0                                                    # display only

    def rec(kind, **kw):
        events.append(dict(kind=kind, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    rec('start')
    if (guard and num_rows == 1) or len(s) <= num_rows:
        rec('guard', ans=s, one=num_rows == 1)
        return events

    rows = [""] * num_rows
    curr_row, going_down = 0, False

    for i, c in enumerate(s):
        try:
            rows[curr_row] += c
        except IndexError:
            rec('crash', i=i, row=curr_row, col=col, rows=rows[:])
            return events
        before = going_down
        if curr_row == 0 or curr_row == num_rows - 1:
            going_down = not going_down
        rec('place', i=i, row=curr_row, col=col, rows=rows[:], flip=before != going_down,
            down=going_down, nxt=curr_row + (1 if going_down else -1))
        curr_row += 1 if going_down else -1
        if not going_down:                                     # display only
            col += 1

    ans = "".join(rows)
    rec('join', rows=rows[:], ans=ans)
    assert ans == Solution().convert(s, num_rows)
    return events


def build(s, num_rows, subtitle, notes=None, wrong=False):
    notes = notes or {}
    sc = Scene('#6 ZigZag Conversion: bounce a row cursor', subtitle)
    legend = [(ACTIVE, 'letter just placed'), (style('region0')[1], 'row 0'),
              (style('region1')[1], 'row 1'), (style('region2')[1], 'row 2')][:1 + min(num_rows, 3)]
    events = trace(s, num_rows)
    if wrong:
        events = events + [dict(e, wrong=True) for e in trace(s, num_rows, guard=False)]
    placed = {}                       # (row, col) -> (letter, row) for the picture
    width = max([e['col'] for e in events if e['kind'] == 'place'] + [len(s) - 1 if num_rows == 1 else 0]) + 1
    seen = set()
    for idx, e in enumerate(events):
        k = e['kind']
        if k == 'start' and e.get('wrong'):
            placed = {}
        if k == 'place':
            placed[(e['row'], e['col'])] = s[e['i']]
        grid_rows = num_rows + (1 if e.get('wrong') else 0)
        cells = [[{'style': 'muted'} for _ in range(width)] for _ in range(grid_rows)]
        outlines = []
        for (r, c), ch in placed.items():
            cells[r][c] = {'style': f'region{r}', 'label': ch}
        if k == 'place':
            outlines = [((e['row'], e['col']), ACTIVE, 4)]
        if k == 'guard':
            for c in range(min(width, len(s))):
                cells[0][c] = {'style': 'region0', 'label': s[c]}
        if e.get('wrong'):
            for c in range(width):
                cells[num_rows][c] = {'style': 'bad', 'label': '?' if (k == 'crash' and c == e['col']) else '',
                                      'water': True}
            if k == 'crash':
                outlines = [((e['row'], e['col']), REJECT, 4)]
        grid = GridView(cells, outlines, bridges=False)
        styles, ptrs = {}, {}
        upto = e.get('i', -1) if k in ('place', 'crash') else (len(s) if k in ('join', 'guard') else -1)
        for j in range(len(s)):
            if j < upto or (k == 'place' and j == upto):
                styles[j] = 'muted'
        if k in ('place', 'crash'):
            styles[e['i']] = 'active' if k == 'place' else 'bad'
            ptrs = {'c': e['i']}
        arr = ArrayView(list(s), styles, ptrs, title='s')
        rows_now = e.get('rows') or ([s] if k == 'guard' else [''] * num_rows)
        side_rows = [(f'row {r}', rows_now[r] if r < len(rows_now) else '', f'region{r}')
                     for r in range(num_rows)]
        if e.get('wrong'):
            side_rows.append((f'row {num_rows}', 'does not exist', 'bad'))
        if k == 'join':
            side_rows.append(('joined', e['ans'], 'good'))
        side = MapView(side_rows, 'Row buckets', headers=('row', 'letters so far'))
        counters = {}
        if k == 'place':
            counters = {'going': 'down' if e['down'] else 'up'}
        cap, sub, hold = words(e, s, num_rows, seen)
        if (k, e.get('i'), bool(e.get('wrong'))) in notes:
            sub, hold = notes[(k, e.get('i'), bool(e.get('wrong')))], KEY
        if k in notes and k in ('guard', 'crash', 'join'):
            sub = notes[k]
        sc.frame([grid, arr], cap, sub, hold, side=side, counters=counters, legend=legend)
    return sc


def words(e, s, num_rows, seen):
    k = e['kind']
    if k == 'start':
        if e.get('wrong'):
            return ("Now the same walk WITHOUT the numRows == 1 check.",
                    "len(s) > numRows, so a length-only guard lets it through.", KEY)
        return (f"Write \"{s}\" down {num_rows} rows and back up, then read the rows left to right.",
                "The trick: you never need the columns. Only which ROW each letter lands in.", KEY)
    if k == 'guard':
        if e['one']:
            return ("numRows == 1: one row has nothing to zigzag, so return s as it is.",
                    "That check has to come first. Watch what the walk does without it.", KEY)
        return ("The string fits in one column, so it reads back unchanged.", "", END)
    if k == 'crash':
        return (f"'{s[e['i']]}' goes to rows[{e['row']}], which doesn't exist: IndexError.",
                "Row 0 is the top AND the bottom, so the bounce sends the cursor down off the grid.", END)
    if k == 'place':
        ch, r, nxt = s[e['i']], e['row'], e['nxt']
        head = f"'{ch}' goes into row {r}."
        if e['flip'] and r == 0 and 'top' not in seen:
            seen.add('top')
            return (head + " Row 0 is the top, so the cursor turns and heads down.",
                    "going_down starts False, so this very first flip is what points it down.", KEY)
        if e['flip'] and r == num_rows - 1 and 'bottom' not in seen:
            seen.add('bottom')
            return (head + f" Row {r} is the bottom: turn around, next stop row {nxt}.",
                    "This is the bounce. The letters now climb the diagonal, one row per letter.", KEY)
        if e['flip'] and r == 0 and 'top2' not in seen:
            seen.add('top2')
            return (head + " Back at the top: turn down again.",
                    "Only rows 0 and numRows - 1 ever flip the direction.", KEY)
        if e['flip']:
            return (head + f" Turning row: next stop row {nxt}.", "", STEP)
        return (head + f" Keep going {'down' if e['down'] else 'up'} to row {nxt}.", "", QUICK * 2)
    rows = e['rows']
    return (f"Glue the rows together: {' + '.join(repr(r) for r in rows)} = \"{e['ans']}\".",
            "One pass over the letters, then one join: O(n) time.", END)


def hard():
    """Harder input for the interactive page (scripts/motion_build.py)."""
    s, r = HARD
    assert Solution().convert(s, r) == "LEETCODE"
    try:
        length_guard_only(s, r)
        raise AssertionError('the length-only guard was expected to crash')
    except IndexError:
        pass
    # the same first attempt passes all three LeetCode samples
    for args, want in ((("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR"), (("PAYPALISHIRING", 4), "PINALSIGYAHRPI"),
                       (("A", 1), "A")):
        assert length_guard_only(*args) == want == Solution().convert(*args)
    sc = build(s, r, f's = "{s}", numRows = {r}. Answer "{s}". A length-only guard crashes on the second letter.',
               wrong=True)
    return sc, ("One row: row 0 is the top and the bottom at once, so the bounce flips the cursor down into a row "
                "that doesn't exist. A version that only checks len(s) <= numRows passes all three LeetCode "
                "samples, then crashes here on the second letter.")


def main():
    args = cli()
    sc = build(S, ROWS, f's = "{S}", numRows = {ROWS}. Each letter only needs to know its row.')
    finish(sc, 6, "Watch 'Y' land in the bottom row: the cursor turns around there, and from then on the "
                  "letters climb the diagonal one row at a time.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
