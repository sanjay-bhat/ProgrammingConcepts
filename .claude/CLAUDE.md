# LeetCode Notebook Standards

## Notebook Structure

Each problem lives in `leetcode/NNNN.ipynb` (zero-padded to 4 digits), numbered to match the order in `markdown/All Problems List - Leetcode.md`.

Kernel: `.NET (C#)` — all notebooks use the .NET Interactive C# kernel.

### Cell Layout

| Order | Type     | Content                            |
|-------|----------|------------------------------------|
| 1     | markdown | Title, URL, complexity table, methodology |
| 2     | markdown | `## Explain Like I'm a Newbie` *(only where it earns its place — see below)* |
| 3     | markdown | `## Talking It Through in an Interview` |
| 4     | markdown | `## Solutions` header + `### C#`   |
| 5     | code     | C# solution                        |
| 6     | markdown | `### Python`                       |
| 7     | code     | Python solution                    |
| 8     | markdown | `### Go`                           |
| 9     | code     | Go solution                        |
| 10    | markdown | `### Rust`                         |
| 11    | code     | Rust solution                      |
| 12    | markdown | `## Example Scenarios` (5 examples) |
| 13    | markdown | Infographic image attachment       |

### Check the collection with the audit, not by eye ★

```bash
python3 scripts/audit_notebooks.py            # summary of what's outstanding
python3 scripts/audit_notebooks.py --list     # with the notebook numbers
```

This is the source of truth for remaining work — don't keep a hand-written
backlog, it goes stale.

It exists because of a real failure: for weeks the retrofit was reported
"555 of 569 complete" while **165 notebooks rendered a broken image**. Their
`image.png` attachment was present but its payload was an empty string, and
the verification only asked whether the key existed. **Never check a key's
presence as a proxy for its content.**

### Never address cells by index ★

The newbie section is optional, so a notebook is **12 or 13 cells** and the
examples/infographic sit at different indices in each. Code that hardcodes
"cell 9" and "cell 10" silently edits the wrong cell.

Use `scripts/nbcells.py`, which finds cells by content:

```python
import sys; sys.path.insert(0, 'scripts')
import nbcells

nb = nbcells.load('leetcode/0200.ipynb')
nbcells.set_examples(nb, markdown)          # finds '## Example Scenarios'
nbcells.set_infographic(nb, png_bytes)      # finds the image cell, embeds base64
nbcells.upsert_newbie(nb, markdown)         # inserts/replaces before '## Solutions'
nbcells.upsert_interview(nb, markdown)      # same, for the interview section
nbcells.save(nb, 'leetcode/0200.ipynb')     # indent=1 + trailing newline

nbcells.audit(nb)   # {'cells', 'examples_at', 'infographic_at', 'newbie_at', ...}
```

---

## House style: plain language everywhere ★

These notebooks exist to be understood on the fly. A notebook the reader can't
follow has failed, however correct it is. So the plain-language treatment is
not one optional section — it applies to the whole file:

| Part | Scope |
| :--- | :--- |
| Header | **every** notebook — never leave a term unexplained |
| `Explain Like I'm a Newbie` | only where there's a genuine "aha" |
| `Talking It Through in an Interview` | **every** notebook |
| Code comments | **every** notebook |
| Example scenarios | **every** notebook |

Unpack jargon rather than assuming it. Don't leave $O(m \times n)$ bare — say
it means "the work grows with the number of squares", and that a 300×300 grid
is about 90,000 steps. Don't leave $\alpha$ sitting in a table — say it is
under 5 for any input you could physically store. Introduce a technique's name
*after* its idea, as a label for something already explained.

Only the dedicated newbie section is selective. Everything else is just
writing clearly, which costs little and always helps.

---

## Cell 0 — Header

```
# LeetCode #N: <Title>

https://leetcode.com/problems/<slug>/

## Comparison of Approaches

| Approach | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **Brute Force** | ... | ... |
| **<Other Optimal Name>** | ... | ... |
| **<Best Optimal Name>** | ... | ... |

---

## Understanding the Methods

### Brute Force
<1-3 sentences. Explain what it does and why it's slow.>

### <Other Optimal Name>
<1-3 sentences. Explain the approach and note its limitation vs the best.>

### Optimal: <Best Name> ★
<1-3 sentences. Explain the core idea.>

**Why this is better than <Other>:** <1-2 sentences comparing them directly.>

**Constraints:**
* <from the problem>
```

### Multiple Optimal Approaches

When a problem has more than one optimal-class solution (same or similar Big-O):

- **List all** of them in the complexity table, ordered worst → best (brute force first, best optimal last).
- **Describe each** under "Understanding the Methods" with 1-3 sentences.
- **Mark the best one** with a ★ after the heading (`### Optimal: <Name> ★`).
- **Explain why** the chosen one is better — even if the Big-O is identical, call out the practical difference (e.g., one-pass vs two-pass, stack overhead, short-circuit behavior).
- **Only code the best optimal** in all four languages. Other approaches are described in prose only.

If there is genuinely only one optimal approach, skip the comparison — just list brute force and the optimal.

Keep descriptions concise — an entry-level developer should understand them without extra context.

---

## Cells 1–8 — Solutions (C#, Python, Go, Rust)

- Only implement the **optimal** approach (brute force is explained in prose, not coded).
- All four languages use the **same comment structure** so the logic can be followed across languages.
- Comments explain the *why*, not the *what* — e.g., "Calculate the complement needed to hit the target" not "subtract nums[i] from target".
- Use each language's idiomatic naming conventions (PascalCase for C#, snake_case for Python/Rust, camelCase for Go).

### Comment for a reader who doesn't know the technique

Comment the handful of places where the logic turns, and say what breaks
otherwise — not every line. For #200 that's three: why any `1` the sweep finds
must be a new island, why the square is marked **before** recursing (recurse
first and two neighbours call each other forever), and what the guard covers.
Label mechanical things inline where it's free (`// down`, `// up`).

Add a one-line note under a `### Language` heading only where the *language*
is the confusing part, not the algorithm — Python's nested closure, Go's
forward-declared `var dfs func`, Rust's `i32` coordinates (`usize` would
underflow at −1). Skip it when there's nothing language-specific to say. A
missing note is a deliberate decision, not a gap to fill. Don't add "Python
uses a dict here" to make the four sections look symmetrical.

**Never change behaviour while commenting.** Re-run the Python cell against a
reference implementation afterwards; adding comments to working code is an
easy way to introduce a typo.

---

## "Explain Like I'm a Newbie" (optional section)

A plain-English bridge between the header and the code, for a reader who does
not yet know the technique. It goes **before** `## Solutions` — that is where
the gap is, since the header jumps straight from the title to a complexity
table full of unexplained terms.

**Only add it where it earns its place.** The test is not "is this problem
hard?" but **"is there an idea here that the header states without making it
click?"** Two Sum passes (the complement flip, and why you check before you
record). XOR Operation in an Array does not. Padding easy problems trains the
reader to skip the section everywhere.

To make that call concretely, ask: **is there a wrong implementation that
passes the sample input?** If yes, there's a trap a newbie will fall into and
the section has a job (Binary Search: `while lo < hi` passes both samples,
then returns -1 for `nums = [5], target = 5`). If the only way to get it wrong
is to misread the question, skip the section.

Structure, in this order — skip any part that has nothing to say:

1. **What the question is actually asking** — restate it concretely, with a
   tiny worked picture. No jargon.
2. **The one idea you need** — name the real difficulty, then the insight that
   dissolves it. An everyday analogy if an honest one exists (flood fill is the
   paint-bucket tool), never a forced one.
3. **What that means in code** — only here introduce the technique's name, and
   call out any ordering that must be right (mark *before* you recurse).
4. **Mistakes people make the first time** — a short numbered list of the
   specific bugs this problem produces.
5. **Things worth knowing** — honest caveats (mutating the input, recursion
   depth, overflow).

Rules:
- Length follows the difficulty band in the table below. Check it with
  `python3 scripts/wordcount.py N`; never let an Easy run longer than a Medium.
- **Data-structure primer allowance.** When the problem rests on a structure
  the reader may never have built (the doubly linked list inside LRU Cache, a
  trie, a monotonic deque), open with a short `### Primer: <structure>` of up
  to 150 words. It sits outside the band, and the counter allows for it
  automatically.
- Don't re-trace what the infographic already shows — the picture does step
  tables better. The unique value here is framing and mistakes.
- **No rhetorical self-corrections** ("you need a 4… no, you need 2"). They are
  indistinguishable from the unresolved mid-edit asides that have shipped in
  this repo by accident, and undermine trust in the prose.
- Write it so someone who has never seen the technique can follow it, without
  ever talking down to them.

---

## "Talking It Through in an Interview" (every notebook)

Sits between the newbie section and `## Solutions`. It is **written from the
interviewer's chair** — not as advice to the candidate. The difference is the
whole point of the section:

> ✗ *"Ask a clarifying question that shows you read the problem."*
> ✓ *"That question is the one I'm listening for. It changes the answer, and it
>    tells me you looked at the actual problem instead of pattern-matching."*

Write it as a running dialogue from the moment the problem is handed over to
the finished whiteboard. The reader's lines appear as block quotes; the
interviewer's reasoning sits between them, in first person.

**The arc** (skip any beat the problem doesn't support):

1. **The 30-second pitch** up front — the destination, what they should end up
   able to say out loud. End it pointing at the solution's own weakness.
2. **I slide the problem across** — reading time is fine; the restatement; the
   one or two clarifiers that genuinely change something, *with the
   interviewer's answers written in*.
3. **Name the hard part before naming a technique.** The highest-signal moment
   in the interview. Opening with "I'll use DFS" teaches the interviewer
   nothing; "a 2×2 block would get counted four times" proves understanding.
   The technique must fall out of the difficulty, not precede it.
4. **The shape of the code, and the cost derived rather than announced.**
   Anyone can say O(n); the section must show the reasoning that survives the
   follow-up.
5. **Whiteboard it in order**, with the one sentence worth saying at each line
   that could have gone wrong — and state the question the interviewer will ask
   if that sentence is missing.
6. **Dry-run it** on a concrete input before handing the pen back, tying an
   edge case back to the clarifier asked at the start.
7. **Volunteer the breaking point** before being asked. When the solution
   is already optimal and nothing breaks, this beat doesn't disappear; it
   becomes one of these, whichever is true:
   - **The assumption it leans on**: "this relies on the list being sorted;
     unsorted, binary search returns garbage, not an error."
   - **The contract cost**: "I'm mutating your grid; if you need it back
     that's an extra O(m×n)."
   - **How it generalises**: "if 'k' were 3 instead of 2, the same trick
     needs a hash map instead of two pointers."
8. **What would worry me** — the anti-patterns, briefly.

**Design problems** (LRU Cache, Min Stack, Trie, iterators): whiteboard the
**structures before the methods**. Draw the fields and how they point at each
other, say why each one is there ("the map gives me O(1) lookup, the list gives
me O(1) eviction order"), and only then write `get`/`put`. Methods written
before the structure is agreed get rewritten.

**Rules:**
- Every quote must be specific to this problem. Generic lines ("can the input
  be null?") appear only as examples of what *not* to say.
- Include the interviewer's replies, so it reads as a conversation.
- Be honest about where the posted solution breaks. If it has no real
  weakness, say that instead of inventing one.
- No pacing tables, no numbered "tips". If it reads like a listicle, rewrite it.
- Use contractions. An interviewer says "I'd", "you're", "that's".

### Length bands ★

The pilot ran Two Sum (Easy) longer than Number of Islands (Medium), the wrong
way round. The bands below are word counts of prose: code fences don't count.
Check with `python3 scripts/wordcount.py N` (difficulty comes from
`tracker.html`). The bands in that script must match this table.

| Difficulty | Newbie   | Interview  |
|------------|----------|------------|
| Easy       | 300–450  | 800–1100   |
| Medium     | 350–500  | 1000–1500  |
| Hard       | 450–650  | 1200–1800  |

`#200` (Medium, ~1450) is the reference. Overrunning a band means something
is being said twice. Find it and cut it; don't trim sentences evenly.

---

## Cell 9 — Example Scenarios

Exactly **5 examples**, each with `**Input:**` and a short walkthrough:

1. **Common Case** — straightforward, happy-path input
2. **Slightly Complex** — needs a bit more thought (negatives, longer arrays, etc.)
3. **Edge Case: Time Factor** — worst case for time (e.g., match at the very end, forcing full scan)
4. **Edge Case: Space Factor** — worst case for space (e.g., no match found, dictionary fills completely)
5. **Almost-Impossible but Plausible** — extreme boundary values, overflow-adjacent, near-miss decoys

Each walkthrough should be 1-2 sentences. Use LaTeX for math notation (`$O(n)$`, `$\approx$`, `$\pm$`).

Keep the slot label at the start of each heading and put the specifics after
it: `### 3. Edge Case: Time Factor — Single Row`, not `### 3. Edge Case: Single
Row`. The audit's `scenario_labels` check enforces this. A slot relabelled to
describe its input is usually one whose input isn't actually the worst case
for time or space. Fix the input, not just the label.

---

## Cell 10 — Infographic Image

An embedded PNG (`image.png` attachment) rendered from an HTML template via headless Chrome.

### Match the Visualization to the Data Structure ★

**The most important rule: draw the problem's actual data structure, not a flattened array.**
A 1D array of cells + a trace table is only right for genuinely 1D problems (two-pointer, sliding
window, prefix sums). For anything with spatial or relational structure, show that structure
directly — the way a good YouTube walkthrough sketches it on a whiteboard:

| Problem shape | Visualization |
| :--- | :--- |
| **Grid / matrix** (islands, flood fill, DP on grid) | A real 2D grid. Color each region/component distinctly, draw **connection bars** between adjacent cells that belong together, **cross out** inactive/water cells (diagonal slash), and show a **running counter** when something is being tallied. See the `#200` generator in `scripts/`. |
| **Tree** (BST, binary tree, traversal) | An SVG node-and-edge tree. Highlight the visited path / target nodes; number nodes in traversal order. |
| **Graph** (topological sort, union-find, shortest path) | An SVG node-edge diagram with colored traversal order or component grouping — not an adjacency array. |
| **Linked list** | A horizontal chain of node boxes with `→` pointer arrows; show before/after for pointer surgery. |
| **Intervals** | A horizontal timeline with overlapping bars. |
| **1D array / string** | Flat colored cells + trace table (the original default). |

Show **input → after** side by side where it clarifies the transformation (e.g. grid before vs.
after flood fill). Each example should make the *mechanism* visible at a glance, not just the answer.

A reusable grid generator lives at `scripts/gen_grid_infographic.py` — feed it a grid and an
island/region assignment and it auto-places cells, connection bars, crossouts, and the counter.
Prefer extending a generator like this over hand-writing hundreds of cell `<div>`s (hand-writing
large grids by hand tends to stall the agent).

### Image Generation Steps

1. **Create the HTML file** in the scratchpad directory with all 5 examples laid out as cards. Pick
   the visualization that matches the data structure (see the table above). Each card contains:
   - Example title and input line (monospace)
   - The structure visualization (2D grid / tree / graph / chain / timeline / array as appropriate)
   - A step indicator where it helps (trace table, running counter, or numbered traversal order)
   - Result box: pass `result=('success'|'fail'|'info', text)` to
     `infographic_lib.card()`. It adds the ✔ / ✘ / → itself, so don't put a
     glyph in the text. Before this was enforced, 119 images shipped with a
     green ✔ on a red failure box.
   - Optional note for non-obvious behavior

2. **Preview in browser** to verify layout — use `preview_start` with a local HTTP server, check for overlaps, truncated text, or misaligned elements.

3. **Render to PNG** with `infographic_lib.render_png(html_path, png_path)`.
   **Never call Chrome with a guessed `--window-size`.** Chrome silently drops
   everything below the window, and 81 images shipped cut off that way.
   `render_png` renders into an oversized window, grows until the content
   stops short of the bottom, and crops to the content plus a margin.
   Afterwards `infographic_lib.is_clipped(png_bytes)` must be False.

4. **Embed into notebook** by base64-encoding the PNG and writing it into the last cell's `attachments.image.png.image/png` field in the notebook JSON.

### Image Design Rules

- Card width: 968px inside a 1024px viewport
- Background: `#eef1f5`, card: `#ffffff` with `#1f2430` border, rounded corners
- Array / grid cells: 46×46px default, 42×42px for 6+ per row, 72×42px for wide values (e.g., `-1e9`)
- **Grid cells** sit in a `position:relative` wrapper with ~10px gaps; connection bars are absolutely
  positioned in those gaps (thickness ~16px) colored to match the region
- **Region palette**: cycle 10 distinct (fill, border, text) triples so adjacent components never
  share a color. Green `#d4f5d4`/`#2f9e58`, blue `#d4e8f5`/`#2f7e9e`, pink, gold, purple, teal, etc.
  (full list in `scripts/gen_grid_infographic.py`)
- **Water / inactive cells**: grey fill with a blue diagonal slash via `linear-gradient`
- Matched elements highlighted with green border/background (`#2f9e58` / `#e4f7ea`)
- Trace table uses monospace font, green for matches, grey for misses
- Result boxes: green for success (`#d4edda`/`#155724`), red for failure (`#f8d7da`/`#721c24`), blue info (`#d1ecf1`/`#0c5460`)
- Notes in italic, kept to 1-2 lines

---

## Editing Notebooks Programmatically

Notebooks are JSON files. Use Python with a **heredoc** (`<< 'PYEOF'`) to avoid backslash escaping issues — Python string literals will eat `\a`, `\t`, `\p` etc. which breaks LaTeX (`\approx`, `\times`, `\pm`).

```bash
python3 << 'PYEOF'
import json
with open('NNNN.ipynb') as f:
    nb = json.load(f)
# ... modify nb['cells'] ...
with open('NNNN.ipynb', 'w') as f:
    json.dump(nb, f, indent=1)
    f.write('\n')
PYEOF
```

Always verify LaTeX escapes survived by checking the written file for `\\approx`, `\\times`, `\\pm` etc.
