#!/usr/bin/env python3
"""Shared infographic building blocks for LeetCode notebook visualizations.

Each generator returns an HTML snippet (a <div class="card">...</div>) given
structured data, so per-problem scripts supply data instead of hand-writing
large HTML/SVG (which tends to stall agents). Compose cards with page_shell().

Visualization families:
  - card()          : wrapper for one example (title, subtitle, input, body, result)
  - array_row()     : 1D array of colored cells with optional pointer labels
  - trace_table()   : step-by-step table
  - linked_list()   : horizontal node chain with -> pointer arrows
  - binary_tree()   : SVG binary tree from a level-order list
  - decision_tree() : SVG backtracking/decision tree from nested nodes
  - stack_view()    : vertical stack with push/pop annotations
  - dp_table()      : 2D DP grid with row/col headers and highlighted cells
  - bar_chart()     : vertical bars (heights), e.g. container-with-most-water
  - grid()          : 2D grid with region colors + connection bars + crossouts
"""

# ---- shared palette (fill, border, text) ----
PALETTE = [
    ("#d4f5d4", "#2f9e58", "#1a6b35"),  # green
    ("#d4e8f5", "#2f7e9e", "#1a4f6b"),  # blue
    ("#f5d4e8", "#9e2f7e", "#6b1a4f"),  # pink
    ("#f5eed4", "#9e8e2f", "#6b5f1a"),  # gold
    ("#e8d4f5", "#7e2f9e", "#4f1a6b"),  # purple
    ("#d4f5ef", "#2f9e8e", "#1a6b5f"),  # teal
    ("#f5ddd4", "#9e5a2f", "#6b3a1a"),  # orange
    ("#ddf5d4", "#5a9e2f", "#3a6b1a"),  # lime
    ("#f5d4d4", "#9e2f2f", "#6b1a1a"),  # red
    ("#d4ddf5", "#2f5a9e", "#1a3a6b"),  # indigo
]
GREEN = PALETTE[0]
BLUE = PALETTE[1]


def color(i):
    return PALETTE[i % len(PALETTE)]


# ---------------------------------------------------------------- page shell
def page_shell(title, cards, legend=None):
    legend_html = f'<div class="legend-top">{legend}</div>' if legend else ''
    return f'''<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ background:#eef1f5; font-family:'Segoe UI',system-ui,-apple-system,sans-serif; padding:28px; }}
h1 {{ text-align:center; font-size:26px; color:#1f2430; margin-bottom:8px; font-weight:700; }}
.legend-top {{ text-align:center; font-size:13px; color:#666; margin-bottom:22px; }}
.card {{ background:#fff; border:2px solid #1f2430; border-radius:12px; padding:24px 28px; margin:0 auto 20px; width:968px; }}
.card-title {{ font-size:18px; font-weight:700; color:#1f2430; margin-bottom:6px; }}
.card-subtitle {{ font-size:13px; color:#666; margin-bottom:16px; font-style:italic; }}
.input-line {{ font-family:'Courier New',monospace; font-size:13px; background:#f4f5f7; padding:8px 12px; border-radius:6px; margin-bottom:20px; color:#333; }}
.body-center {{ display:flex; justify-content:center; margin-bottom:18px; flex-wrap:wrap; gap:24px; }}
.note {{ font-size:13px; color:#666; font-style:italic; margin-bottom:12px; text-align:center; max-width:820px; margin:0 auto 12px; }}
.result-box {{ display:block; width:fit-content; margin:0 auto; padding:8px 20px; border-radius:8px; font-weight:700; font-size:15px; }}
.result-success {{ background:#d4edda; color:#155724; border:1px solid #c3e6cb; }}
.result-fail {{ background:#f8d7da; color:#721c24; border:1px solid #f5c6cb; }}
.result-info {{ background:#d1ecf1; color:#0c5460; border:1px solid #bee5eb; }}
/* array */
.arr {{ display:inline-grid; gap:4px; }}
.acell {{ width:46px; height:46px; display:flex; align-items:center; justify-content:center; font-family:'Courier New',monospace; font-size:15px; font-weight:700; border-radius:8px; border:2px solid #b0b8c8; background:#e8edf3; color:#1f2430; position:relative; }}
.aidx {{ position:absolute; bottom:-16px; left:50%; transform:translateX(-50%); font-size:9px; color:#999; }}
.aptr {{ position:absolute; top:-18px; left:50%; transform:translateX(-50%); font-size:11px; font-weight:700; }}
/* trace table */
table.trace {{ border-collapse:collapse; font-size:13px; margin:0 auto; }}
table.trace th {{ background:#1f2430; color:#fff; padding:7px 14px; text-align:left; font-weight:600; }}
table.trace td {{ padding:6px 14px; border-bottom:1px solid #eee; font-family:'Courier New',monospace; }}
table.trace tr:nth-child(even) td {{ background:#fafbfc; }}
.hit {{ color:#2f9e58; font-weight:700; }}
.miss {{ color:#999; }}
/* linked list */
.ll {{ display:flex; align-items:center; gap:0; flex-wrap:wrap; justify-content:center; }}
.llnode {{ display:flex; align-items:center; }}
.llbox {{ min-width:46px; height:46px; padding:0 12px; display:flex; align-items:center; justify-content:center; font-family:'Courier New',monospace; font-size:16px; font-weight:700; border-radius:8px; border:2px solid #2f7e9e; background:#d4e8f5; color:#1a4f6b; }}
.llarrow {{ color:#1f2430; font-size:22px; margin:0 8px; }}
.llnull {{ color:#999; font-family:'Courier New',monospace; font-size:14px; margin-left:8px; }}
/* stack */
.stack {{ display:inline-flex; flex-direction:column-reverse; border:2px solid #1f2430; border-top:none; border-radius:0 0 8px 8px; min-width:80px; }}
.stackcell {{ height:40px; display:flex; align-items:center; justify-content:center; font-family:'Courier New',monospace; font-weight:700; border-top:1px solid #ccc; background:#d4e8f5; color:#1a4f6b; }}
.stacklabel {{ text-align:center; font-size:12px; color:#666; margin-top:6px; }}
/* bars */
.bars {{ display:flex; align-items:flex-end; gap:6px; height:200px; }}
.bar {{ width:36px; background:#d4e8f5; border:2px solid #2f7e9e; border-radius:4px 4px 0 0; display:flex; align-items:flex-start; justify-content:center; font-family:'Courier New',monospace; font-size:12px; font-weight:700; color:#1a4f6b; padding-top:4px; position:relative; }}
.bar.active {{ background:#d4f5d4; border-color:#2f9e58; color:#1a6b35; }}
.bar .bidx {{ position:absolute; bottom:-18px; left:50%; transform:translateX(-50%); font-size:10px; color:#999; }}
/* dp table */
table.dp {{ border-collapse:collapse; margin:0 auto; font-family:'Courier New',monospace; font-size:14px; }}
table.dp th {{ background:#1f2430; color:#fff; padding:6px 10px; font-weight:600; }}
table.dp td {{ width:40px; height:40px; text-align:center; border:1px solid #ccc; background:#fff; }}
table.dp td.fill {{ background:#d4f5d4; color:#1a6b35; font-weight:700; }}
table.dp td.base {{ background:#f5eed4; color:#6b5f1a; }}
/* counter */
.counter {{ text-align:center; font-size:15px; color:#1f2430; font-weight:600; margin-bottom:12px; }}
.count-step {{ display:inline-block; min-width:26px; padding:2px 8px; border-radius:6px; background:#eef1f5; color:#888; font-family:'Courier New',monospace; }}
.count-final {{ display:inline-block; min-width:26px; padding:2px 10px; border-radius:6px; background:#2f9e58; color:#fff; font-family:'Courier New',monospace; font-weight:700; }}
.count-arrow {{ color:#aaa; }}
/* grid */
.grid-wrap {{ position:relative; }}
.gcell {{ position:absolute; width:46px; height:46px; display:flex; align-items:center; justify-content:center; font-family:'Courier New',monospace; font-size:17px; font-weight:700; border-radius:8px; border:2px solid transparent; z-index:2; }}
.gcell.water {{ background:#f3f4f6; color:#c2c7d0; border-color:#e2e5ea; background-image:linear-gradient(to top right, transparent 44%, #6ea8d8 44%, #6ea8d8 56%, transparent 56%); }}
.bridge {{ position:absolute; border-radius:3px; z-index:1; }}
</style></head><body>
<h1>{title}</h1>
{legend_html}
{''.join(cards)}
</body></html>'''


def card(title, subtitle, input_line, body, result=None, note=None):
    rtype, rtext = result if result else ("info", "")
    note_html = f'<div class="note">{note}</div>' if note else ''
    res_html = f'<div class="result-box result-{rtype}">&#10004; {rtext}</div>' if result else ''
    return f'''<div class="card">
<div class="card-title">{title}</div>
<div class="card-subtitle">{subtitle}</div>
<div class="input-line">{input_line}</div>
<div class="body-center">{body}</div>
{note_html}{res_html}
</div>'''


# ---------------------------------------------------------------- array
def array_row(values, colors=None, pointers=None, show_index=True):
    """values: list. colors: optional list of PALETTE indices or None per cell.
    pointers: optional dict {index: 'label'} drawn above a cell."""
    cells = []
    for i, v in enumerate(values):
        style = ''
        if colors and colors[i] is not None:
            f, b, t = color(colors[i])
            style = f'background:{f};border-color:{b};color:{t};'
        ptr = ''
        if pointers and i in pointers:
            f, b, t = GREEN
            ptr = f'<span class="aptr" style="color:{b};">{pointers[i]}</span>'
        idx = f'<span class="aidx">{i}</span>' if show_index else ''
        cells.append(f'<div class="acell" style="{style}">{ptr}{v}{idx}</div>')
    cols = len(values)
    return f'<div class="arr" style="grid-template-columns:repeat({cols},46px);">{"".join(cells)}</div>'


def trace_table(headers, rows):
    """headers: list of column names. rows: list of lists (cells may contain HTML)."""
    head = ''.join(f'<th>{h}</th>' for h in headers)
    body = ''
    for r in rows:
        body += '<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>'
    return f'<table class="trace"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'


# ---------------------------------------------------------------- linked list
def linked_list(values, color_idx=1, highlight=None):
    """values: list of node values. highlight: set of indices to color green."""
    highlight = highlight or set()
    parts = ['<div class="ll">']
    for i, v in enumerate(values):
        f, b, t = GREEN if i in highlight else color(color_idx)
        parts.append(f'<div class="llnode"><div class="llbox" style="background:{f};border-color:{b};color:{t};">{v}</div>')
        if i < len(values) - 1:
            parts.append('<span class="llarrow">&rarr;</span>')
        parts.append('</div>')
    parts.append('<span class="llnull">&rarr; null</span>')
    parts.append('</div>')
    return ''.join(parts)


# ---------------------------------------------------------------- stack
def stack_view(items, label='stack'):
    """items: bottom-to-top list of values currently on the stack."""
    cells = ''.join(f'<div class="stackcell">{v}</div>' for v in items)
    if not items:
        cells = '<div class="stackcell" style="color:#bbb;background:#f8f9fa;">(empty)</div>'
    return f'<div><div class="stack">{cells}</div><div class="stacklabel">{label}</div></div>'


# ---------------------------------------------------------------- bars
def bar_chart(heights, active=None, scale=None):
    """heights: list of ints. active: set of indices to color green."""
    active = active or set()
    mx = scale or max(heights) or 1
    bars = []
    for i, h in enumerate(heights):
        px = int(h / mx * 180) + 20
        cls = 'bar active' if i in active else 'bar'
        bars.append(f'<div class="{cls}" style="height:{px}px;">{h}<span class="bidx">{i}</span></div>')
    return f'<div class="bars">{"".join(bars)}</div>'


# ---------------------------------------------------------------- dp table
def dp_table(matrix, col_headers=None, row_headers=None, fills=None, bases=None):
    """matrix: 2D list. fills/bases: sets of (r,c) to style."""
    fills = fills or set()
    bases = bases or set()
    html = '<table class="dp">'
    if col_headers is not None:
        html += '<tr><th></th>' + ''.join(f'<th>{h}</th>' for h in col_headers) + '</tr>'
    for r, row in enumerate(matrix):
        html += '<tr>'
        if row_headers is not None:
            html += f'<th>{row_headers[r]}</th>'
        for c, v in enumerate(row):
            cls = 'fill' if (r, c) in fills else ('base' if (r, c) in bases else '')
            html += f'<td class="{cls}">{v}</td>'
        html += '</tr>'
    html += '</table>'
    return html


# ---------------------------------------------------------------- counter
def counter(n, label='Count'):
    if n <= 1:
        seq = f'<span class="count-final">{n}</span>'
    else:
        seq = ' <span class="count-arrow">&rarr;</span> '.join(
            [f'<span class="count-step">{i}</span>' for i in range(1, n)]
            + [f'<span class="count-final">{n}</span>'])
    return f'<div class="counter">{label}: {seq}</div>'
