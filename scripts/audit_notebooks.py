#!/usr/bin/env python3
"""Collection-wide health check — the single source of truth for what's left.

Run it instead of keeping a hand-written backlog; a list in a doc goes stale,
this cannot.

    python3 scripts/audit_notebooks.py              # summary
    python3 scripts/audit_notebooks.py --list       # summary + the numbers
    python3 scripts/audit_notebooks.py --list empty_infographic

Checks, and why each exists:

  empty_infographic  The `image.png` attachment is present but its payload is
                     an empty string, so the notebook renders a broken image.
                     165 notebooks shipped this way and were reported complete
                     for weeks, because the old check only asked whether the
                     key existed. Never check a key's presence as a proxy for
                     its content.
  no_infographic     No infographic cell at all.
  clipped_infographic  Real content runs into the image's bottom edge — the
                     signature of a render whose window was too short. Chrome
                     truncates silently; #206 lost scenario 5 this way.
                     Verified against all 81 hits: every one ends inside an
                     unclosed white card (71 cut through content, 10 cut only
                     the card's bottom padding), so no false positives.
  fail_box_check     Contains a red failure box, which every image rendered
                     before the card() fix labels with a green "✔". Fixing the
                     library only helps new renders; these need regenerating.
  no_examples        No '## Example Scenarios' cell.
  wrong_scenarios    Not exactly 5 '### ' scenario headings.
  scenario_labels    The 5 headings don't follow the slot order (Common Case,
                     Slightly Complex, Edge Case: Time Factor, Edge Case:
                     Space Factor, Almost-Impossible). A relabelled slot
                     usually means the Time/Space worst case was never written.
  no_interview       Missing '## Talking It Through in an Interview'.
  few_code_cells     Fewer than 4 code cells (C#, Python, Go, Rust).
  aside              Prose contains an unresolved mid-edit aside ("wait,
                     actually..."). ~10 notebooks shipped with these.
"""
import argparse
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nbcells  # noqa: E402
import infographic_lib  # noqa: E402

FAIL_BG = (248, 215, 218)   # .result-fail background, #f8d7da

# "wait" only counts as an aside when used as an interjection — adjacent to a
# dash, ellipsis or question mark. Concurrency notebooks legitimately contain
# "Busy-Wait Spin" and "circular-wait deadlock", which must not trip this.
ASIDE = re.compile(
    r"(?:[—–…?]|\.\.\.|,)\s*wait\b"      # "... wait", "? Wait", "— wait"
    r"|\bwait\s*[—–]"                      # "wait —"
    r"|\bactually[,.]"                      # "Actually, ..."
    r"|\blet me (?:re)?calculate"
    r"|\bno[,:]? (?:wait|that's wrong)",
    re.I)

# Each scenario heading must open with its slot's label (an optional "3." is fine).
SLOT_LABELS = [re.compile(r'(?:\d+[.)]\s*)?' + label, re.I) for label in
               ('Common Case', 'Slightly Complex', 'Edge Case: Time',
                'Edge Case: Space', 'Almost')]

CHECKS = ['empty_infographic', 'no_infographic', 'clipped_infographic', 'fail_box_check', 'no_examples', 'wrong_scenarios',
          'scenario_labels', 'no_interview', 'few_code_cells', 'aside']


def has_fail_box(png, min_px=400, tol=4):
    """True if the image contains a red failure-result box."""
    import io
    from PIL import Image
    im = Image.open(io.BytesIO(png)).convert('RGB')
    w, h = im.size
    px = im.load()
    hits = 0
    for y in range(0, h, 3):
        for x in range(0, w, 3):
            r, g, b = px[x, y]
            if (abs(r - FAIL_BG[0]) <= tol and abs(g - FAIL_BG[1]) <= tol
                    and abs(b - FAIL_BG[2]) <= tol):
                hits += 1
                if hits >= min_px:
                    return True
    return False


def inspect(path):
    """Return the set of failed check names for one notebook."""
    bad = set()
    nb = nbcells.load(path)
    cells = nb['cells']

    ig = nbcells.find_infographic(nb)
    if ig is None:
        bad.add('no_infographic')
    else:
        png = nbcells.get_infographic(nb)
        if png is None:
            # cell and key exist, payload does not
            bad.add('empty_infographic')
        else:
            if infographic_lib.is_clipped(png):
                bad.add('clipped_infographic')
            if has_fail_box(png):
                bad.add('fail_box_check')

    ex = nbcells.find_examples(nb)
    if ex is None:
        bad.add('no_examples')
    else:
        heads = re.findall(r'^### (.*)$', nbcells.text(cells[ex]), re.M)
        if len(heads) != 5:
            bad.add('wrong_scenarios')
        elif not all(r.match(h) for r, h in zip(SLOT_LABELS, heads)):
            bad.add('scenario_labels')

    if nbcells.find_interview(nb) is None:
        bad.add('no_interview')

    if len(nbcells.code_cells(nb)) < 4:
        bad.add('few_code_cells')

    for c in cells:
        if c.get('cell_type') == 'markdown' and ASIDE.search(nbcells.text(c)):
            bad.add('aside')
            break
    return bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--list', nargs='?', const='all', default=None,
                    help='print the failing notebook numbers (optionally for one check)')
    ap.add_argument('--root', default=os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'leetcode'))
    args = ap.parse_args()

    failures = {k: [] for k in CHECKS}
    total = 0
    for path in sorted(glob.glob(os.path.join(args.root, '????.ipynb'))):
        num = int(os.path.basename(path)[:4])
        total += 1
        try:
            for k in inspect(path):
                failures[k].append(num)
        except Exception as e:                      # noqa: BLE001
            failures.setdefault('unreadable', []).append((num, str(e)[:50]))

    print(f'notebooks scanned: {total}\n')
    width = max(len(k) for k in failures)
    for k in failures:
        n = len(failures[k])
        flag = '' if n == 0 else '  <-- backlog'
        print(f'  {k:<{width}}  {n:>4}{flag}')

    clean = total - len({n for v in failures.values() for n in
                         (x[0] if isinstance(x, tuple) else x for x in v)})
    print(f'\nfully clean: {clean} / {total}')

    if args.list:
        for k, v in failures.items():
            if v and (args.list == 'all' or args.list == k):
                print(f'\n{k} ({len(v)}):\n{v}')


if __name__ == '__main__':
    main()
