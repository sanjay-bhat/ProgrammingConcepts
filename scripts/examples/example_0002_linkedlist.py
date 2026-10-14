import sys
sys.path.insert(0, '/Users/sanjaybhat/Desktop/Projects/Leetcode/scripts')
from infographic_lib import *

cards = []

# 1. Common
body = (linked_list([2,4,3]) + '<div style="font-size:22px;align-self:center;">+</div>'
        + linked_list([5,6,4]) + '<div style="font-size:22px;align-self:center;">=</div>'
        + linked_list([7,0,8], highlight={0,1,2}))
cards.append(card(
    "1. Common Case — Equal Length, One Carry",
    "Digits stored in reverse. Add position by position, carrying when sum >= 10.",
    "l1 = [2,4,3] (342), l2 = [5,6,4] (465)",
    body,
    result=("success", "Output: [7,0,8] (807)"),
    note="2+5=7 | 4+6=10 → write 0 carry 1 | 3+4+1=8. 342 + 465 = 807."))

# 2. Different lengths
body = (linked_list([9,9]) + '<div style="font-size:22px;align-self:center;">+</div>'
        + linked_list([1]) + '<div style="font-size:22px;align-self:center;">=</div>'
        + linked_list([0,0,1], highlight={2}))
cards.append(card(
    "2. Slightly Complex — Unequal Lengths, Cascading Carry",
    "Shorter list is treated as 0 past its end; carry ripples into a brand-new node.",
    "l1 = [9,9] (99), l2 = [1] (1)",
    body,
    result=("success", "Output: [0,0,1] (100)"),
    note="9+1=10 → 0 carry 1 | 9+0+1=10 → 0 carry 1 | new node 1. 99 + 1 = 100."))

# 3. Time factor
body = (linked_list([5,5,5,5,5]) + '<div style="font-size:22px;align-self:center;">+</div>'
        + linked_list([5,5,5,5,5]) + '<div style="font-size:22px;align-self:center;">=</div>'
        + linked_list([0,1,1,1,1,1], highlight={5}))
cards.append(card(
    "3. Edge Case: Time Factor — Long Equal Lists",
    "Must traverse all max(m,n) nodes once; no shortcut. Time O(max(m,n)).",
    "l1 = [5,5,5,5,5], l2 = [5,5,5,5,5]",
    body,
    result=("success", "Output: [0,1,1,1,1,1]"),
    note="Every position sums to 10 → steady carry chain across all nodes."))

# 4. Space factor
body = (linked_list([9,9,9]) + '<div style="font-size:22px;align-self:center;">+</div>'
        + linked_list([1]) + '<div style="font-size:22px;align-self:center;">=</div>'
        + linked_list([0,0,0,1], highlight={3}))
cards.append(card(
    "4. Edge Case: Space Factor — Carry Creates Extra Node",
    "Final carry forces an output longer than both inputs — the extra allocation.",
    "l1 = [9,9,9] (999), l2 = [1] (1)",
    body,
    result=("success", "Output: [0,0,0,1] (1000)"),
    note="Output length = max(m,n)+1 in the worst case. 999 + 1 = 1000."))

# 5. Almost-impossible
body = (linked_list([0]) + '<div style="font-size:22px;align-self:center;">+</div>'
        + linked_list([0]) + '<div style="font-size:22px;align-self:center;">=</div>'
        + linked_list([0], highlight={0}))
cards.append(card(
    "5. Almost-Impossible but Plausible — Both Zero",
    "Degenerate single-node zeros; no carry, result is a single zero node.",
    "l1 = [0], l2 = [0]",
    body,
    result=("info", "Output: [0]"),
    note="Boundary case: 0 + 0 = 0 — must not emit an empty list."))

html = page_shell("LeetCode #2: Add Two Numbers — Digit-by-Digit with Carry", cards,
                  legend="Linked-list digits stored in reverse &nbsp;•&nbsp; green = result nodes &nbsp;•&nbsp; carry flows left to right")

with open('/private/tmp/claude-501/-Users-sanjaybhat-Desktop-Projects/6c42dc0e-9e99-4951-938c-0ccfae50a6e5/scratchpad/0002_infographic.html', 'w') as f:
    f.write(html)
print("written")
