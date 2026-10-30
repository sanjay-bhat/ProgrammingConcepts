#!/usr/bin/env python3
"""Build the interactive Motion walkthrough page for a notebook.

    python3 scripts/motion_build.py 200            # writes walkthroughs/0200.html
    python3 scripts/motion_build.py 200 3 42       # several
    python3 scripts/motion_build.py --all          # every scripts/animations/NNNN.py
    python3 scripts/motion_build.py 200 --link     # also link it from the notebook

It runs scripts/animations/NNNN.py exactly as written (the same trace that
makes the notebook's GIF), but instead of drawing pixels it records each
frame's views as data. scripts/motion_player.html turns that data into a page
you can play, pause, scrub and step through, animated with Motion.

A script also defines `hard()`, returning `(scene, blurb)`, or a list of one
or two of them, for harder inputs than LeetCode's sample. Each appears as
its own tab on the page. The GIF
stays on the standard example; the hard one lives only on the page, where the
reader can scrub through a long trace.
"""
import argparse
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import anim_lib  # noqa: E402

PAGES_URL = 'https://sanjay-bhat.github.io/ProgrammingConcepts/walkthroughs/{num:04d}.html'
LINK_MARK = 'Step through it yourself'


# ------------------------------------------------------------------ capture
def to_json(v):
    """Views and their parameters -> plain JSON. Tuple dict keys become 'a|b'."""
    if isinstance(v, anim_lib.View):
        d = {'type': type(v).__name__}
        for k, x in vars(v).items():
            if k != 'used':
                d[k] = to_json(x)
        return d
    if isinstance(v, dict):
        out = {}
        for k, x in v.items():
            key = '|'.join(map(str, k)) if isinstance(k, tuple) else str(k)
            out[key] = to_json(x)
        return out
    if isinstance(v, (list, tuple, set)):
        return [to_json(x) for x in v]
    if isinstance(v, (str, int, float, bool)) or v is None:
        return v
    return str(v)


class Capture:
    """Patches Scene.frame and anim_lib.finish while a script runs."""

    def __init__(self):
        self.scenes = []          # [(scene, blurb)]

    def __enter__(self):
        self._frame, self._finish = anim_lib.Scene.frame, anim_lib.finish
        cap = self

        def frame(scene, main, caption, sub='', hold=anim_lib.STEP, side=None,
                  counters=None, legend=None):
            mains = main if isinstance(main, (list, tuple)) else [main]
            scene.__dict__.setdefault('specs', []).append({
                'main': [to_json(m) for m in mains],
                'side': to_json(side) if side is not None else None,
                'caption': caption, 'sub': sub or '', 'hold': round(float(hold), 2),
                'counters': to_json(counters or {}),
                'legend': [[c, t] for c, t in (legend or [])],
            })

        def finish(scene, num, blurb, **_):
            cap.scenes.append((scene, blurb))

        anim_lib.Scene.frame, anim_lib.finish = frame, finish
        return self

    def __exit__(self, *exc):
        anim_lib.Scene.frame, anim_lib.finish = self._frame, self._finish


def load_script(num):
    path = os.path.join(HERE, 'animations', f'{num:04d}.py')
    spec = importlib.util.spec_from_file_location(f'anim_{num:04d}', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def capture(num):
    mod = load_script(num)
    with Capture() as cap:
        mod.finish = anim_lib.finish          # scripts bind finish at import ('from anim_lib import *')
        argv, sys.argv = sys.argv, [f'{num:04d}.py', '--no-embed']
        try:
            mod.main()
        finally:
            sys.argv = argv
        if not cap.scenes:
            raise SystemExit(f'#{num}: the script never called finish()')
        scenarios = [dict(name='LeetCode example', scene=cap.scenes[0][0], blurb=cap.scenes[0][1])]
        if hasattr(mod, 'hard'):
            extra = mod.hard()
            extra = [extra] if isinstance(extra, tuple) else list(extra)
            for k, (sc, blurb) in enumerate(extra, 1):
                name = 'Hard example' if len(extra) == 1 else f'Hard example {k}'
                scenarios.append(dict(name=name, scene=sc, blurb=blurb))
    return scenarios


# ------------------------------------------------------------------ theme
def _rgb(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))


def _hex(c):
    return '#%02x%02x%02x' % tuple(max(0, min(255, round(v))) for v in c)


def _mix(a, b, t):
    a, b = _rgb(a), _rgb(b)
    return _hex(tuple(x + (y - x) * t for x, y in zip(a, b)))


def style_tokens():
    """CSS custom properties for every anim_lib style, light and dark."""
    names = list(anim_lib.STYLES)
    light, dark = [], []
    for n in names:
        f, b, t = anim_lib.style(n)
        light.append(f'--{n}-f:{f};--{n}-b:{b};--{n}-t:{t};')
        dark.append(f'--{n}-f:{_mix(b, "#13232d", 0.74)};--{n}-b:{_mix(b, "#ffffff", 0.18)};--{n}-t:{f};')
    return ''.join(light), ''.join(dark)


# ------------------------------------------------------------------ page
def page_html(num, scenarios):
    tpl = open(os.path.join(HERE, 'motion_player.html')).read()
    first = scenarios[0]['scene']
    data = {
        'num': num,
        'title': first.title,
        'subtitle': first.subtitle,
        'scenarios': [dict(name=s['name'], blurb=s['blurb'], subtitle=s['scene'].subtitle,
                           frames=s['scene'].specs) for s in scenarios],
        'colors': {anim_lib.CURSOR: 'var(--cursor)', anim_lib.ACTIVE: 'var(--accent)',
                   anim_lib.REJECT: 'var(--reject)',
                   **{anim_lib.style(n)[1]: f'var(--{n}-b)' for n in anim_lib.STYLES}},
    }
    light, dark = style_tokens()
    title = re.sub(r'^#\d+\s*', '', first.title).split(':')[0].strip()
    html = (tpl.replace('__PAGE_TITLE__', f'#{num} {title} Walkthrough')
               .replace('__STYLE_LIGHT__', light).replace('__STYLE_DARK__', dark)
               .replace('__DATA__', json.dumps(data, separators=(',', ':'), ensure_ascii=False)))
    return html


def link_notebook(num):
    """Add (once) a link to the page under the GIF in the 'Watch It Run' cell."""
    import nbcells
    path = os.path.join(ROOT, 'leetcode', f'{num:04d}.ipynb')
    nb = nbcells.load(path)
    i = nbcells.find_animation(nb)
    if i is None:
        return False
    src = nbcells.text(nb['cells'][i])
    if LINK_MARK in src:
        return False
    src = (src.rstrip('\n') + f'\n\n**[{LINK_MARK}: play, pause, scrub and step through '
           f'this walkthrough, plus a harder example]({PAGES_URL.format(num=num)})**')
    nb['cells'][i]['source'] = src.splitlines(keepends=True)
    nbcells.save(nb, path)
    return True


def write_index(out_dir):
    """walkthroughs/index.html: every page, linked, in problem order."""
    rows = []
    for f in sorted(os.listdir(out_dir)):
        m = re.fullmatch(r'(\d{4})\.html', f)
        if not m:
            continue
        html = open(os.path.join(out_dir, f)).read(8192)
        t = re.search(r'<title>(.*?)</title>', html)
        name = re.sub(r'^#\d+\s*|\s*Walkthrough$', '', t.group(1)) if t else f
        rows.append(f'<li><a href="{f}"><b>#{int(m.group(1))}</b> {name}</a></li>')
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>LeetCode Walkthroughs</title>
<style>
:root{{--bg:#edf2f5;--card:#fff;--ink:#13212b;--muted:#566875;--line:#cfd9e1;--accent:#df5a12}}
@media (prefers-color-scheme:dark){{:root{{--bg:#0d1820;--card:#13232d;--ink:#e5edf2;--muted:#93a5b2;--line:#263d4b;--accent:#ff7b34;color-scheme:dark}}}}
body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 "IBM Plex Sans","Helvetica Neue",system-ui,sans-serif;
padding:32px max(16px,env(safe-area-inset-right,0px)) 48px max(16px,env(safe-area-inset-left,0px))}}
main{{max-width:900px;margin:0 auto}} h1{{font-size:32px;margin:0 0 6px}} p{{color:var(--muted);margin:0 0 22px}}
ul{{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:10px}}
a{{display:block;padding:12px 14px;background:var(--card);border:1px solid var(--line);border-radius:12px;color:inherit;text-decoration:none}}
a:hover,a:focus-visible{{border-color:var(--accent);outline:none}} b{{color:var(--accent);font-family:"JetBrains Mono",Menlo,monospace}}
</style></head><body><main><h1>LeetCode walkthroughs</h1>
<p>Interactive, step-through walkthroughs: play, pause, scrub, and try a harder example. {len(rows)} problems so far.</p>
<ul>{''.join(rows)}</ul></main></body></html>
"""
    with open(os.path.join(out_dir, 'index.html'), 'w') as f:
        f.write(page)


def build(num, out_dir, link):
    scenarios = capture(num)
    html = page_html(num, scenarios)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, f'{num:04d}.html')
    with open(path, 'w') as f:
        f.write(html)
    steps = '+'.join(str(len(s['scene'].specs)) for s in scenarios)
    linked = ' (notebook linked)' if link and link_notebook(num) else ''
    print(f'#{num}: {len(scenarios)} example(s), {steps} steps, {len(html) // 1024} KB -> {os.path.relpath(path, ROOT)}{linked}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('nums', nargs='*', type=int)
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--link', action='store_true', help='link the page from the notebook')
    ap.add_argument('--out', default=os.path.join(ROOT, 'walkthroughs'))
    a = ap.parse_args()
    nums = a.nums
    if a.all:
        nums = sorted(int(f[:4]) for f in os.listdir(os.path.join(HERE, 'animations'))
                      if re.fullmatch(r'\d{4}\.py', f))
    for n in nums:
        build(n, a.out, a.link)
    if nums:
        write_index(a.out)


if __name__ == '__main__':
    main()
