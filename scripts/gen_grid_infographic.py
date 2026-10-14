#!/usr/bin/env python3
"""Generate a YouTube-style grid infographic for Number of Islands (#200).
Each land cell is colored by island, connected cells are bridged with colored bars,
water cells are crossed out, and a running island counter is shown."""

# Island color palette (fill, border, text)
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

CELL = 46   # cell size px
GAP = 10    # gap between cells px (room for connector bars)
BRIDGE = 16  # connector bar thickness


def render_grid(grid, islands, title):
    """grid: 2D list of '1'/'0'. islands: 2D list of island-id (0 for water)."""
    rows = len(grid)
    cols = len(grid[0])
    W = cols * CELL + (cols - 1) * GAP
    H = rows * CELL + (rows - 1) * GAP

    parts = [f'<div class="grid-wrap" style="width:{W}px;height:{H}px;">']

    # Connector bars first (drawn under cells via z-index)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '1':
                continue
            iid = islands[r][c]
            fill, border, _ = PALETTE[(iid - 1) % len(PALETTE)]
            # horizontal connector to right neighbor
            if c + 1 < cols and grid[r][c + 1] == '1' and islands[r][c + 1] == iid:
                x = c * (CELL + GAP) + CELL
                y = r * (CELL + GAP) + (CELL - BRIDGE) // 2
                parts.append(
                    f'<div class="bridge" style="left:{x}px;top:{y}px;'
                    f'width:{GAP}px;height:{BRIDGE}px;background:{border};"></div>')
            # vertical connector to bottom neighbor
            if r + 1 < rows and grid[r + 1][c] == '1' and islands[r + 1][c] == iid:
                x = c * (CELL + GAP) + (CELL - BRIDGE) // 2
                y = r * (CELL + GAP) + CELL
                parts.append(
                    f'<div class="bridge" style="left:{x}px;top:{y}px;'
                    f'width:{BRIDGE}px;height:{GAP}px;background:{border};"></div>')

    # Cells
    for r in range(rows):
        for c in range(cols):
            x = c * (CELL + GAP)
            y = r * (CELL + GAP)
            if grid[r][c] == '1':
                iid = islands[r][c]
                fill, border, text = PALETTE[(iid - 1) % len(PALETTE)]
                parts.append(
                    f'<div class="cell land" style="left:{x}px;top:{y}px;'
                    f'background:{fill};border-color:{border};color:{text};">1</div>')
            else:
                parts.append(
                    f'<div class="cell water" style="left:{x}px;top:{y}px;">0</div>')

    parts.append('</div>')
    return '\n'.join(parts)


def counter_badge(n):
    """Running island counter like '1 → 2 → 3'."""
    if n == 1:
        seq = '<span class="count-final">1</span>'
    else:
        steps = ' <span class="count-arrow">→</span> '.join(
            [f'<span class="count-step">{i}</span>' for i in range(1, n)]
            + [f'<span class="count-final">{n}</span>'])
        seq = steps
    return f'<div class="counter">Islands found: {seq}</div>'


# ---- Example definitions ----

def make_examples():
    examples = []

    # 1. Common Case — single connected island
    g1 = [['1','1','1'],['0','1','0'],['1','1','1']]
    i1 = [[1,1,1],[0,1,0],[1,1,1]]
    examples.append(dict(
        title="1. Common Case — One Connected Island",
        subtitle="Every land cell links to the center column. A single DFS floods them all.",
        inp='grid = [["1","1","1"], ["0","1","0"], ["1","1","1"]]',
        grid=g1, islands=i1, count=1,
        note="One DFS starting at (0,0) reaches all 7 land cells through shared edges.",
        result=("success", "Output: 1 island"),
    ))

    # 2. Four corner islands
    g2 = [['1','0','0','1'],['0','0','0','0'],['0','0','0','0'],['1','0','0','1']]
    i2 = [[1,0,0,2],[0,0,0,0],[0,0,0,0],[3,0,0,4]]
    examples.append(dict(
        title="2. Slightly Complex — Four Corner Islands",
        subtitle="Each corner is isolated by water, so the scan triggers a fresh DFS four times.",
        inp='grid = [["1","0","0","1"], ["0","0","0","0"], ["0","0","0","0"], ["1","0","0","1"]]',
        grid=g2, islands=i2, count=4,
        note="No bridges exist — every land cell is its own island.",
        result=("success", "Output: 4 islands"),
    ))

    # 3. All land — one big island
    g3 = [['1']*5 for _ in range(4)]
    i3 = [[1]*5 for _ in range(4)]
    examples.append(dict(
        title="3. Edge Case: Time Factor — Entire Grid is Land",
        subtitle="Worst case for time: one DFS must visit all m×n cells, recursion depth = m×n.",
        inp='grid = 4×5 all "1"',
        grid=g3, islands=i3, count=1,
        note="⚠ At the 300×300 constraint this is 90,000 nested calls — naive recursive DFS risks stack overflow. Prefer BFS or an explicit stack.",
        result=("success", "Output: 1 island (20 cells, one flood)"),
    ))

    # 4. Checkerboard — max islands
    g4 = [['1' if (r+c)%2==0 else '0' for c in range(5)] for r in range(4)]
    i4 = [[0]*5 for _ in range(4)]
    k = 0
    for r in range(4):
        for c in range(5):
            if g4[r][c] == '1':
                k += 1
                i4[r][c] = k
    examples.append(dict(
        title="4. Edge Case: Space Factor — Checkerboard (Max Islands)",
        subtitle="Every land cell is diagonally isolated (diagonals don't connect), so each is its own island.",
        inp='grid = 4×5 checkerboard of "1"/"0"',
        grid=g4, islands=i4, count=k,
        note="No two land cells share an edge — the maximum possible island count for the grid size.",
        result=("info", f"Output: {k} islands (each a single cell)"),
    ))

    # 5. Spiral — one island, deep recursion
    g5 = [
        ['1','1','1','1','1'],
        ['0','0','0','0','1'],
        ['1','1','1','0','1'],
        ['1','0','0','0','1'],
        ['1','1','1','1','1'],
    ]
    i5 = [[1 if v=='1' else 0 for v in row] for row in g5]
    examples.append(dict(
        title="5. Almost-Impossible — Spiral Island (Deep Recursion)",
        subtitle="A single snaking path forces DFS to recurse cell-by-cell to maximum depth before unwinding.",
        inp='grid = 5×5 spiral path of "1"',
        grid=g5, islands=i5, count=1,
        note="⚠ The spiral has no shortcuts — depth grows with the full path length. At scale this is the classic stack-overflow trap for recursive DFS.",
        result=("success", "Output: 1 island (17 cells in one winding DFS)"),
    ))

    return examples


def build_html():
    examples = make_examples()
    cards = []
    for ex in examples:
        rtype, rtext = ex['result']
        card = f'''
  <div class="card">
    <div class="card-title">{ex['title']}</div>
    <div class="card-subtitle">{ex['subtitle']}</div>
    <div class="input-line">{ex['inp']}</div>
    <div class="grid-center">
      {render_grid(ex['grid'], ex['islands'], ex['title'])}
    </div>
    {counter_badge(ex['count'])}
    <div class="note">{ex['note']}</div>
    <div class="result-box result-{rtype}">&#10004; {rtext}</div>
  </div>'''
        cards.append(card)

    html = f'''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ background:#eef1f5; font-family:'Segoe UI',system-ui,-apple-system,sans-serif; padding:28px; }}
h1 {{ text-align:center; font-size:26px; color:#1f2430; margin-bottom:8px; font-weight:700; }}
.legend-top {{ text-align:center; font-size:13px; color:#666; margin-bottom:22px; }}
.card {{ background:#fff; border:2px solid #1f2430; border-radius:12px; padding:24px 28px;
  margin:0 auto 20px; width:968px; }}
.card-title {{ font-size:18px; font-weight:700; color:#1f2430; margin-bottom:6px; }}
.card-subtitle {{ font-size:13px; color:#666; margin-bottom:16px; font-style:italic; }}
.input-line {{ font-family:'Courier New',monospace; font-size:13px; background:#f4f5f7;
  padding:8px 12px; border-radius:6px; margin-bottom:20px; color:#333; }}
.grid-center {{ display:flex; justify-content:center; margin-bottom:18px; }}
.grid-wrap {{ position:relative; }}
.cell {{ position:absolute; width:{CELL}px; height:{CELL}px; display:flex; align-items:center;
  justify-content:center; font-family:'Courier New',monospace; font-size:17px; font-weight:700;
  border-radius:8px; border:2px solid transparent; z-index:2; }}
.cell.water {{ background:#f3f4f6; color:#c2c7d0; border-color:#e2e5ea;
  background-image:linear-gradient(to top right, transparent 44%, #6ea8d8 44%, #6ea8d8 56%, transparent 56%); }}
.bridge {{ position:absolute; border-radius:3px; z-index:1; }}
.counter {{ text-align:center; font-size:15px; color:#1f2430; font-weight:600; margin-bottom:12px; }}
.count-step {{ display:inline-block; min-width:26px; padding:2px 8px; border-radius:6px;
  background:#eef1f5; color:#888; font-family:'Courier New',monospace; }}
.count-final {{ display:inline-block; min-width:26px; padding:2px 10px; border-radius:6px;
  background:#2f9e58; color:#fff; font-family:'Courier New',monospace; font-weight:700; }}
.count-arrow {{ color:#aaa; font-weight:400; }}
.note {{ font-size:13px; color:#666; font-style:italic; margin-bottom:12px; text-align:center;
  max-width:820px; margin-left:auto; margin-right:auto; }}
.result-box {{ display:block; width:fit-content; margin:0 auto; padding:8px 20px; border-radius:8px;
  font-weight:700; font-size:15px; }}
.result-success {{ background:#d4edda; color:#155724; border:1px solid #c3e6cb; }}
.result-info {{ background:#d1ecf1; color:#0c5460; border:1px solid #bee5eb; }}
</style>
</head>
<body>
  <h1>LeetCode #200: Number of Islands — DFS Flood Fill</h1>
  <div class="legend-top">Colored cells = land grouped by island &nbsp;•&nbsp; colored bars = connected (shared edge) &nbsp;•&nbsp; blue-slashed cells = water</div>
  {''.join(cards)}
</body>
</html>'''
    return html


if __name__ == '__main__':
    with open('0200_infographic.html', 'w') as f:
        f.write(build_html())
    print("written 0200_infographic.html")
