# Notebook Batch Workflow

Step-by-step process for adding a batch of LeetCode notebooks and merging them to main.

---

## Standard mode: 2 parallel agents, 30 problems per round

This is the default operating mode. Each round completes ~30 notebooks in the time a single agent previously took for 15.

### Round structure

1. Pull `main`, identify the next 30 unsolved problems (see §1).
2. Split into two slices of 15 (A and B).
3. Create two git worktrees on separate branches (see §2).
4. Spawn two background agents simultaneously, one per worktree (see §3).
5. Log status to chat as each agent completes (see §4).
6. Each agent writes all notebooks then commits once per file, updates 6 list files, pushes, opens a PR.
7. Merge both PRs squash → main (see §5). If the second PR has list-file conflicts, rebase it (see §10).

---

## 1. Identify the next 30 problems

```bash
grep -n "^| [0-9]" leetcode/README.md | grep -v "📓" | head -35
```

Take the next 30 unsolved problems in README order. Skip SQL-only problems.
Split the list: problems 1–15 go to Agent A, problems 16–30 go to Agent B.

---

## 2. Create two worktrees

```bash
git checkout main && git pull origin main

BRANCH_A="feature/batch_a_$(date +%H%M)"
BRANCH_B="feature/batch_b_$(date +%H%M)"

git worktree add ../worktree-a -b "$BRANCH_A"
git worktree add ../worktree-b -b "$BRANCH_B"
```

Each agent operates in its own worktree directory (`../worktree-a`, `../worktree-b`) so they never touch the same working tree.

---

## 3. Spawn two background agents simultaneously

Use the Agent tool with `run_in_background: true`. Send both tool calls in the **same message** so they start in parallel. Each agent prompt must include:
- Its 15 problem numbers and titles
- The worktree path it should work in (`cd /path/to/worktree-X` at the start)
- The CLAUDE.md notebook structure (11 cells, C#/Python/Go/Rust, 5 examples)
- Git identity (see §6)
- List-file update instructions (all 6 files, `📓` links, `<span title="...">` hover tooltips)
- Single batch commit for all notebooks, then one commit for list files
- PR creation at the end

---

## 4. Status logging

Log each problem as it completes by watching agent output. When both agents finish, post a summary table to chat:

| # | Title | Agent | Status |
|---|-------|-------|--------|
| NNNN | Title | A | ✅ |
| ... | ... | B | ✅ |

---

## 5. Merge PRs

```bash
gh pr merge <N_A> --squash --admin
gh pr merge <N_B> --squash --admin
git checkout main && git pull origin main
```

Merge A first, then B. If B has list-file conflicts after A merges, rebase B (see §10) before merging.

---

## 6. Git identity (CRITICAL)

Every commit must use the noreply email or GitHub will reject the push (GH007):

```bash
GIT_AUTHOR_NAME="Sanjay Bhat" \
GIT_AUTHOR_EMAIL="12857923+sanjay-bhat@users.noreply.github.com" \
GIT_COMMITTER_NAME="Sanjay Bhat" \
GIT_COMMITTER_EMAIL="12857923+sanjay-bhat@users.noreply.github.com" \
git commit -m "Add #NNNN: <Title>"
```

**Never use** `sanjaybhat18492@gmail.com` for commits that will be pushed.

---

## 7. Hover tooltips

The Data Structure column in all 6 list files uses `<span title="...">` for native GitHub hover tooltips. The agent adds `<span>` wrapping as part of each notebook batch. If a new approach name is unmapped, add it to the `DESCRIPTIONS` dict in the tooltip script and re-run.

---

## 8. Infographic pipeline

For each notebook's cell 10:

1. Write `NNNN_infographic.html` to the scratchpad directory
2. Render with headless Chrome (`--force-device-scale-factor=2`, `--window-size=1024,<height>`)
3. Auto-crop with Pillow (`getbbox` + 112 px margin)
4. Base64-encode and embed in `cell[10].attachments.image.png.image/png`

---

## 9. List files to update per notebook

| File | Link format |
|------|-------------|
| `README.md` (root) | `[📓 Title](leetcode/NNNN.ipynb)` |
| `leetcode/README.md` | `[📓 Title](NNNN.ipynb)` |
| `lists/README.md` | `[📓 Title](../leetcode/NNNN.ipynb)` |
| `lists/all-problems.md` | `[📓 Title](../leetcode/NNNN.ipynb)` |
| `lists/by-difficulty.md` | `[📓 Title](../leetcode/NNNN.ipynb)` |
| `lists/by-complexity.md` | `[📓 Title](../leetcode/NNNN.ipynb)` |

---

## 10. Conflict resolution (rebase)

If a PR has merge conflicts (usually in list files after the first PR merges):

```bash
git fetch origin
git -C ../worktree-b rebase origin/main
# resolve conflicts: keep HEAD's 📓 rows, take new rows from feature branch
git -C ../worktree-b rebase --continue
git -C ../worktree-b push --force-with-lease origin <branch-b>
```

Force-push requires explicit user confirmation before running.

---

## 11. Worktree cleanup

After both PRs are merged:

```bash
git worktree remove ../worktree-a
git worktree remove ../worktree-b
git branch -d feature/batch_a_HHMM feature/batch_b_HHMM
```
