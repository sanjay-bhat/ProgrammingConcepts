#!/usr/bin/env python3
"""#79 Word Search: mark a square before going deeper, put its letter back after.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import copy
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

BOARD = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
WORD = "ABCB"          # LeetCode example 3: the B would have to be used twice

# Hard example 1: forgetting to put a letter back after a failed attempt. All
# three LeetCode samples still pass. Here the first start leaves both top A's
# marked, and the real path, A(0,1) -> A(1,1) -> B(1,0), is blocked: false.
HARD1 = ([["A", "A"], ["B", "A"]], "AAB")

# Hard example 2: no backtracking at all, i.e. always stepping to the FIRST
# neighbour that matches. Passes all three samples, but here the E below the S
# is a dead end and the search never tries the E to its right: false.
HARD2 = ([["S", "E", "N", "D"], ["E", "X", "X", "X"]], "SEND")


def exist_variant(board, word, restore=True):
    """The notebook's search; restore=False is the first attempt that never puts letters back."""
    board = copy.deepcopy(board)
    m, n = len(board), len(board[0])

    def dfs(r, c, idx):
        if idx == len(word):
            return True
        if r < 0 or r >= m or c < 0 or c >= n:
            return False
        if board[r][c] != word[idx]:
            return False
        tmp, board[r][c] = board[r][c], '#'
        found = (dfs(r + 1, c, idx + 1) or dfs(r - 1, c, idx + 1)
                 or dfs(r, c + 1, idx + 1) or dfs(r, c - 1, idx + 1))
        if restore:
            board[r][c] = tmp
        return found

    return any(dfs(r, c, 0) for r in range(m) for c in range(n))


def wrong_greedy(board, word):
    """First attempt: from each start, always step to the first matching neighbour; never back up."""
    m, n = len(board), len(board[0])
    for sr in range(m):
        for sc in range(n):
            if board[sr][sc] != word[0]:
                continue
            b = copy.deepcopy(board)
            r, c, ok = sr, sc, True
            b[r][c] = '#'
            for i in range(1, len(word)):
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < m and 0 <= cc < n and b[rr][cc] == word[i]:
                        r, c = rr, cc
                        b[r][c] = '#'
                        break
                else:
                    ok = False
                    break
            if ok:
                return True
    return False


for _w, _ans in (("ABCCED", True), ("SEE", True), ("ABCB", False)):   # both first attempts pass all samples
    assert exist_variant(BOARD, _w) == exist_variant(BOARD, _w, restore=False) == wrong_greedy(BOARD, _w) == _ans
assert exist_variant(*HARD1) is True and exist_variant(*HARD1, restore=False) is False
assert exist_variant(*HARD2) is True and wrong_greedy(*HARD2) is False


def trace(board, word):
    orig = copy.deepcopy(board)
    events, calls = [], []
    st = {'sweep': None}

    def rec(kind, **kw):
        events.append(dict(kind=kind, board=[r[:] for r in board], calls=list(calls), **st, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    m, n = len(board), len(board[0])

    def dfs(r, c, idx):
        if idx == len(word):
            rec('complete', idx=idx)
            return True
        if r < 0 or r >= m or c < 0 or c >= n:
            rec('offgrid', tried=(r, c), idx=idx)
            return False
        if board[r][c] != word[idx]:
            rec('marked' if board[r][c] == '#' else 'mismatch', cell=(r, c), idx=idx,
                had=board[r][c], orig=orig[r][c])
            return False

        tmp, board[r][c] = board[r][c], '#'
        calls.append((r, c, idx))
        rec('mark', cell=(r, c), idx=idx)
        found = (dfs(r + 1, c, idx + 1) or dfs(r - 1, c, idx + 1)
                 or dfs(r, c + 1, idx + 1) or dfs(r, c - 1, idx + 1))
        board[r][c] = tmp
        calls.pop()
        rec('restore', cell=(r, c), idx=idx, found=found)
        return found

    rec('start')
    for r in range(m):
        for c in range(n):
            st['sweep'] = (r, c)
            if dfs(r, c, 0):
                rec('done', answer=True)
                return events
    st['sweep'] = None
    rec('done', answer=False)
    return events


def words(e, first, WORD=WORD, notes=None):
    """notes: {(kind, cell, idx) or kind: text} replaces that frame's second line and holds it as KEY."""
    cap, sub, hold = words_base(e, first, WORD)
    if notes:
        for kk in ((e['kind'], e.get('cell'), e.get('idx')), e['kind']):
            if kk in notes:
                return cap, notes[kk], max(hold, KEY)
    return cap, sub, hold


def words_base(e, first, WORD):
    k = e['kind']
    if k == 'start':
        return (f'Look for "{WORD}": try every square as the first letter.',
                "Each letter must touch the last one (up, down, left, right), and no square twice.", KEY)
    if k == 'mark':
        (r, c), idx = e['cell'], e['idx']
        if idx == 0:
            return (f"({r},{c}) is '{WORD[0]}', the first letter. Mark it '#' and look around it.",
                    "The mark means: this square is already in the path, don't step on it again.", KEY)
        return (f"({r},{c}) matches '{WORD[idx]}', letter {idx + 1} of {len(WORD)}. Mark it '#' and go deeper.",
                "", STEP)
    if k == 'mismatch':
        (r, c), idx = e['cell'], e['idx']
        if idx == 0:
            return (f"Start at ({r},{c})? It's '{e['had']}', not '{WORD[0]}'. Move on.", "", QUICK * 0.8)
        return (f"({r},{c}) is '{e['had']}', but we need '{WORD[idx]}'. Dead end.", "", QUICK)
    if k == 'marked':
        (r, c), idx = e['cell'], e['idx']
        if first.get('marked') == id(e) and e['orig'] != WORD[idx]:
            return (f"({r},{c}) is marked '#': already in the path. (Its '{e['orig']}' isn't the '{WORD[idx]}' "
                    "we need anyway.)", "", STEP)
        if first.get('marked') == id(e):
            return (f"({r},{c}) was '{e['orig']}', the letter we need, but it's marked '#': already in the path.",
                    f"Without the mark, the search would reuse it and wrongly spell {WORD}.", KEY)
        return (f"({r},{c}) is marked '#', already in this path. Skip it.", "", QUICK)
    if k == 'offgrid':
        r, c = e['tried']
        return (f"({r},{c}) is off the board. Dead end.", "", QUICK * 0.8)
    if k == 'restore':
        (r, c), idx = e['cell'], e['idx']
        if e['found']:
            return (f"The word was found through ({r},{c}): put its '{WORD[idx]}' back anyway and return true.",
                    "", STEP)
        if first.get('restore') == id(e):
            return (f"Every direction from ({r},{c}) failed. Put its '{WORD[idx]}' back and return.",
                    "Another path may still need that square, so the mark must not outlive this attempt.", KEY)
        return (f"Nothing works from ({r},{c}): restore '{WORD[idx]}' and back up.", "", STEP)
    if k == 'complete':
        return ("All letters matched.", "", KEY)
    if e['answer']:
        return (f'Found "{WORD}". Answer: true.', "", END)
    return (f'No start square works, so "{WORD}" isn\'t on the board. Answer: false.',
            "Every mark was undone on the way back: the board is exactly as it started.", END)


def cells(e, BOARD=BOARD):
    out = []
    for r, row in enumerate(e['board']):
        out.append([])
        for c, v in enumerate(row):
            if v == '#':
                out[-1].append({'style': 'good', 'label': '#', 'sub': f'was {BOARD[r][c]}'})
            else:
                out[-1].append({'style': 'plain', 'label': v})
    return out


def build(BOARD, WORD, subtitle, notes=None):
    events = trace(copy.deepcopy(BOARD), WORD)
    first = {}
    for e in events:
        for k in ('marked', 'restore'):
            if e['kind'] == k and k not in first:
                first[k] = id(e)
    sc = Scene('#79 Word Search: mark, explore, restore', subtitle)
    legend = [(CURSOR, 'start square'), (ACTIVE, 'being matched'), (REJECT, 'dead end')]
    for e in events:
        rings, marks = [], {}
        if e['sweep']:
            rings.append((e['sweep'], CURSOR, 3))
        if e['kind'] in ('mark', 'restore'):
            rings.append((e['cell'], ACTIVE, 5))
        if e['kind'] in ('mismatch', 'marked') and e['idx'] > 0:
            rings.append((e['cell'], REJECT, 4))
            marks[e['cell']] = '×'
        depth = len(e['calls'])
        wstyles = {j: 'good' for j in range(depth)}
        if e['kind'] in ('mismatch', 'marked', 'offgrid') and e['idx'] < len(WORD):
            wstyles[e['idx']] = 'bad' if e['idx'] > 0 or e['kind'] != 'mismatch' else 'active'
        wv = ArrayView(list(WORD), wstyles, title='word', cell=50,
                       pointers={'idx': e['idx']} if e.get('idx') is not None and e['idx'] < len(WORD) else {})
        stack = [(f"dfs({r},{c}) '{WORD[i]}'", 'good') for r, c, i in e['calls']]
        sw = e['sweep']
        cap, sub, hold = words(e, first, WORD, notes)
        sc.frame([GridView(cells(e, BOARD), outlines=rings, marks=marks, cell=70), wv], cap, sub, hold,
                 side=StackView(stack, 'Call stack', base=f'exist  start at {sw if sw else "-"}',
                                empty='(no path being explored)'),
                 counters={'matched': f'{depth}/{len(WORD)}'}, legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    sc1 = build(*HARD1, 'word = "AAB". The first start fails, and its marks must be undone for the second.',
                {('restore', (0, 1), 1): "Put the A back. Leave it marked and the start at (0,1) is blocked, and that's the only real path.",
                 ('mark', (0, 1), 0): "This start works only because (0,1) was restored after the first attempt.",
                 'done': "Forgetting to restore passes all three LeetCode samples, then answers false here."})
    sc2 = build(*HARD2, 'word = "SEND". Two E\'s touch the S, and only one of them leads on to N.',
                {('restore', (1, 0), 1): "The E below was a dead end. Backing up lets the search try the E to the right.",
                 'done': "Always stepping to the first matching neighbour passes all three samples, then answers false here."})
    return [(sc1, "Forgetting to put a letter back after a failed attempt passes all three LeetCode samples. Here the "
                  "first start leaves both A's marked, and the only real path is blocked."),
            (sc2, "Stepping to the first matching neighbour without ever backing up passes all three samples. Here "
                  "the E below the S is a dead end, and only backtracking finds the E to its right.")]


def main():
    args = cli()
    sc = build(BOARD, WORD, f'word = "{WORD}". Green # = square in the current path.')
    finish(sc, 79, "Watch (0,2) look back at the B it came from: the square is marked #, so the search "
                   "can't use it twice, and every mark is put back before the next start is tried.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
