#!/usr/bin/env python3
"""#875 Koko Eating Bananas: binary search over the SPEED, not the piles.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. The per-pile hour breakdown shown
under the piles is checked against the solution's own `hours` total.
"""
import math
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

PILES, H = [3, 6, 7, 11], 8          # LeetCode example 1


def trace(piles, h):
    events, tried = [], []
    st = {'lo': None, 'hi': None, 'mid': None, 'fits_from': max(piles), 'slow_upto': 0}

    def rec(kind, **kw):
        events.append(dict(kind=kind, tried=list(tried), **st, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    lo, hi = 1, max(piles)
    st.update(lo=lo, hi=hi)
    rec('start')
    while lo < hi:
        mid = lo + (hi - lo) // 2
        st['mid'] = mid
        rec('mid')
        hours = sum(math.ceil(p / mid) for p in piles)
        each = [math.ceil(p / mid) for p in piles]          # display only
        assert sum(each) == hours
        for i in range(len(piles)):
            rec('pile', i=i, each=each[:i + 1])
        if hours <= h:
            hi = mid
            st['fits_from'] = mid
            tried.append((mid, hours, True))
            st.update(lo=lo, hi=hi)
            rec('fits', hours=hours, each=each)
        else:
            lo = mid + 1
            st['slow_upto'] = mid
            tried.append((mid, hours, False))
            st.update(lo=lo, hi=hi)
            rec('slow', hours=hours, each=each)
    st['mid'] = None
    rec('done', answer=lo, each=[math.ceil(p / lo) for p in piles])   # display only
    return events


def words(e, first):
    k = e['kind']
    if k == 'start':
        return (f"Search the speeds 1 to {max(PILES)}, not the piles.",
                f"At speed {max(PILES)} every pile takes one hour, and h ≥ 4 piles, so {max(PILES)} always fits.", KEY)
    if k == 'mid':
        return (f"Range is {e['lo']}..{e['hi']}. Try the middle speed: {e['mid']} bananas an hour.",
                "Add up how many hours every pile would take at this speed.", STEP)
    if k == 'pile':
        i, m = e['i'], e['mid']
        p, hrs = PILES[i], e['each'][-1]
        if first.get('roundup') == id(e):
            what = (f"{p} bananas take less than an hour at speed {m}, but cost a whole hour."
                    if p < m else f"{p}/{m} isn't a whole number, so it rounds up to {hrs} hours.")
            return (f"Pile {p}: {what}",
                    "She waits out the rest of the hour instead of starting the next pile, so round UP.", KEY)
        return (f"Pile {p} at speed {m}: {hrs} hour{'s' if hrs > 1 else ''}.", "", QUICK)
    if k == 'fits':
        m = e['mid']
        if first.get('fits') == id(e):
            return (f"{e['hours']} hours ≤ {H}: speed {m} fits. Set hi = {m}, not {m - 1}.",
                    f"{m} might be the answer itself, and every faster speed fits too.", KEY)
        return (f"{e['hours']} hours ≤ {H}: speed {m} fits, so hi = {m}.",
                "Keep it in range: it might be the smallest one that works.", STEP * 1.4)
    if k == 'slow':
        m = e['mid']
        return (f"{e['hours']} hours > {H}: speed {m} is too slow, so lo = {m + 1}.",
                f"Every speed up to {m} is too slow as well, so they're all ruled out.", KEY)
    return (f"lo and hi meet at {e['answer']}. Answer: speed {e['answer']}.",
            f"{sum(e['each'])} hours, within the {H} allowed. Each guess halved the range: a billion speeds need only about 30.", END)


def speed_styles(e):
    out = {}
    for s in range(1, max(PILES) + 1):
        if s <= e['slow_upto']:
            out[s - 1] = 'bad'
        elif s >= e['fits_from']:
            out[s - 1] = 'good'
        else:
            out[s - 1] = 'window'
    if e['mid'] is not None and e['kind'] in ('mid', 'pile'):
        out[e['mid'] - 1] = 'active'
    return out


def main():
    args = cli()
    events = trace(PILES, H)
    first = {}
    for e in events:
        if e['kind'] == 'pile' and 'roundup' not in first and PILES[e['i']] % e['mid']:
            first['roundup'] = id(e)
        if e['kind'] == 'fits' and 'fits' not in first:
            first['fits'] = id(e)
    sc = Scene('#875 Koko Eating Bananas: binary search on speed',
               f'piles = {PILES}, h = {H}. Find the smallest speed that finishes in time.')
    legend = [(style('good')[1], 'fits'), (style('bad')[1], 'too slow'),
              (style('window')[1], 'not known yet'), (ACTIVE, 'speed being tried')]
    for e in events:
        speeds = ArrayView(list(range(1, max(PILES) + 1)), speed_styles(e),
                           pointers={'lo': e['lo'] - 1, 'hi': e['hi'] - 1}
                           if e['kind'] != 'done' else {'answer': e['answer'] - 1},
                           window=(e['lo'] - 1, e['hi'] - 1), title='speed', indices=False)
        each = e.get('each', [])
        pstyles = {}
        if e['kind'] == 'pile':
            pstyles = {j: 'gold' for j in range(e['i'])}
            pstyles[e['i']] = 'active'
        elif e['kind'] == 'done':
            pstyles = {j: 'good' for j in range(len(PILES))}
        elif e['kind'] in ('fits', 'slow'):
            pstyles = {j: 'good' if e['kind'] == 'fits' else 'bad' for j in range(len(PILES))}
        subs = {j: f'{v}h' for j, v in enumerate(each)}
        piles = ArrayView(PILES, pstyles, title='piles', subs=subs, indices=False, cell=62)
        rows = [(f'k = {m}', f'{hrs}h  {"fits" if ok else "too slow"}', 'good' if ok else 'bad')
                for m, hrs, ok in e['tried']]
        hours = sum(each) if each else '-'
        cap, sub, hold = words(e, first)
        sc.frame([speeds, piles], cap, sub, hold,
                 side=MapView(rows, 'Speeds tried', headers=('speed', 'hours, verdict'),
                              empty='(none yet)'),
                 counters={'hours': hours, 'h': H}, legend=legend)
    finish(sc, 875, "Watch speed 6 fit and hi drop to 6, not 5: the guess that works stays in range, "
                    "because it might be the answer.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
