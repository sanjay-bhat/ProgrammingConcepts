| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
|------------|---------------|----------------|---------------------------|-------|
| 1 | [📓 Two Sum](../leetcode/0001.ipynb) | <span title="Store key→value pairs for O(1) lookup; complement / seen-element checks in a single pass.">Hash Map</span> | Time: O(n), Space: O(n) | Easy |
| 2 | [📓 Add Two Numbers](../leetcode/0002.ipynb) | <span title="Singly-linked node chain; traverse with pointers and rewire next references in place.">Linked List</span> | Time: O(max(m, n)), Space: O(max(m, n)) | Medium |
| 3 | [📓 Longest Substring Without Repeating Characters](../leetcode/0003.ipynb) | <span title="Expand/shrink a window with a hash map tracking character frequencies.">Sliding Window, Hash Map</span> | Time: O(n), Space: O(min(n, m)) | Medium |
| 4 | [📓 Median of Two Sorted Arrays](../leetcode/0004.ipynb) | <span title="Sort the array first, then narrow the search window by half each step.">Array, Binary Search</span> | Time: O(log(min(m, n))), Space: O(1) | Hard |
| 5 | [📓 Longest Palindromic Substring](../leetcode/0005.ipynb) | <span title="Break the problem into overlapping subproblems; cache results to avoid recomputation.">Dynamic Programming</span> | Time: O(n^2), Space: O(n^2) | Medium |
| 6 | [📓 Zigzag Conversion](../leetcode/0006.ipynb) | <span title="Combined string and array manipulation — typically build/compare character frequency counts.">String, Array</span> | Time: O(n), Space: O(n) | Medium |
| 7 | [📓 Reverse Integer](../leetcode/0007.ipynb) | <span title="Operate directly on the integer bits or digits without converting to a string.">Integer</span> | Time: O(log x), Space: O(1) | Easy |
| 8 | [📓 String to Integer (atoi)](../leetcode/0008.ipynb) | <span title="Character-by-character scan or two-pointer technique on the raw string.">String</span> | Time: O(n), Space: O(1) | Easy |
| 9 | [📓 Palindrome Number](../leetcode/0009.ipynb) | <span title="Operate directly on the integer bits or digits without converting to a string.">Integer</span> | Time: O(log x), Space: O(1) | Easy |
| 10 | [📓 Regular Expression Matching](../leetcode/0010.ipynb) | <span title="Break the problem into overlapping subproblems; cache results to avoid recomputation.">Dynamic Programming</span> | Time: O(m * n), Space: O(m * n) | Hard |
| 11 | [📓 Container With Most Water](../leetcode/0011.ipynb) | <span title="Left and right pointers converge; move the pointer that makes progress toward the target.">Two Pointers</span> | Time: O(n), Space: O(1) | Medium |
| 12 | [📓 Integer to Roman](../leetcode/0012.ipynb) | <span title="Pure arithmetic or number-theory formula; no extra data structure needed.">Math</span> | Time: O(1), Space: O(1) | Medium |
| 13 | [📓 Roman to Integer](../leetcode/0013.ipynb) | <span title="Pure arithmetic or number-theory formula; no extra data structure needed.">Math</span> | Time: O(n), Space: O(1) | Easy |
| 14 | [📓 Longest Common Prefix](../leetcode/0014.ipynb) | <span title="Character-by-character scan or two-pointer technique on the raw string.">String</span> | Time: O(n * m), Space: O(1) | Easy |
| 15 | [📓 3Sum](../leetcode/0015.ipynb) | <span title="Sort first, then use two pointers to find pairs or triplets in a single sweep.">Sorting, Two Pointers</span> | Time: O(n^2), Space: O(1) | Medium |
| 16 | [📓 3Sum Closest](../leetcode/0016.ipynb) | <span title="Sort first, then use two pointers to find pairs or triplets in a single sweep.">Sorting, Two Pointers</span> | Time: O(n^2), Space: O(1) | Medium |
| 17 | [📓 Letter Combinations of a Phone Number](../leetcode/0017.ipynb) | <span title="Explore all candidates recursively; undo (backtrack) a choice when it leads to a dead end.">Backtracking</span> | Time: O(4^n), Space: O(n) | Medium |
| 18 | [📓 4Sum](../leetcode/0018.ipynb) | <span title="Sort first, then use two pointers from both ends to find pairs or triplets in a single sweep.">Sorting + Two Pointers</span> | Time: O(n^3), Space: O(1) | Medium |
| 19 | [📓 Remove Nth Node From End of List](../leetcode/0019.ipynb) | <span title="Single left-to-right scan with two pointers; no second pass needed.">One-Pass Two Pointers</span> | Time: O(n), Space: O(1) | Medium |
| 20 | [📓 Valid Parentheses](../leetcode/0020.ipynb) | <span title="LIFO structure; push on open events, pop and process on close events.">Stack</span> | Time: O(n), Space: O(n) | Easy |
| 21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Linked List | Time: O(m + n), Space: O(1) | Easy |
| 22 | [📓 Generate Parentheses](../leetcode/0022.ipynb) | <span title="Use open/close counters as constraints; only add ( when opens < n and ) when closes < opens.">Backtracking (DFS)</span> | Time: $O\!\left(\frac{4^n}{\sqrt{n}}\right)$, Space: $O(n)$ | Medium |
| 39 | [📓 Combination Sum](../leetcode/0039.ipynb) | <span title="DFS with explicit undo steps; prune branches early when constraints are already violated.">Backtracking (DFS)</span> | Time: $O(N^{T/M})$, Space: $O(T/M)$ | Medium |
| 40 | [📓 Combination Sum II](../leetcode/0040.ipynb) | <span title="DFS with explicit undo steps; prune branches early when constraints are already violated.">Backtracking (DFS)</span> | Time: $O(2^N)$, Space: $O(N)$ | Medium |
| 23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Heap, Divide and Conquer | Time: O(n log k), Space: O(k) | Hard |
| 24 | [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) | Linked List | Time: O(n), Space: O(1) | Medium |
| 25 | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | Linked List | Time: O(n), Space: O(1) | Hard |
| 26 | [📓 Remove Duplicates from Sorted Array](../leetcode/0026.ipynb) | <span title="Left and right pointers converge; move the pointer that makes progress toward the target.">Two Pointers</span> | Time: O(n), Space: O(1) | Easy |
| 27 | [📓 Remove Element](../leetcode/0027.ipynb) | <span title="Left and right pointers converge; move the pointer that makes progress toward the target.">Two Pointers</span> | Time: O(n), Space: O(1) | Easy |
| 28 | [Implement strStr()](https://leetcode.com/problems/implement-strstr/) | String | Time: O(n), Space: O(1) | Easy |
| 29 | [Divide Two Integers](https://leetcode.com/problems/divide-two-integers/) | Math | Time: O(log n), Space: O(1) | Medium |
| 30 | [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) | Hash Map, Sliding Window | Time: O(n * m), Space: O(n) | Hard |
| 31 | [📓 Next Permutation](../leetcode/0031.ipynb) | <span title="Find the rightmost descent, swap with the smallest successor to the right, then reverse the suffix.">Three-Step Reverse</span>| Time: O(n), Space: O(1) | Medium |
| 32 | [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/) | Stack, Dynamic Programming | Time: O(n), Space: O(n) | Hard |
| 33 | [📓 Search in Rotated Sorted Array](../leetcode/0033.ipynb) | <span title="One half is always sorted; check if target falls in the sorted half and narrow accordingly.">Binary Search with Pivot Detection</span> | Time: O(log n), Space: O(1) | Medium |
| 34 | [📓 Find First and Last Position of Element in Sorted Array](../leetcode/0034.ipynb) | <span title="Two separate binary searches: one for the leftmost index, one for the rightmost index.">Two Binary Searches</span> | Time: O(log n), Space: O(1) | Medium |
| 35 | [📓 Search Insert Position](../leetcode/0035.ipynb) | <span title="Halve the search space each step by comparing the midpoint to a monotone predicate.">Binary Search</span> | Time: $O(\log n)$, Space: $O(1)$ | Easy |
| 36 | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | Hash Set | Time: O(n^2), Space: O(n^2) | Medium |
| 37 | [📓 Sudoku Solver](../leetcode/0037.ipynb) | <span title="Try digits 1-9 in each empty cell; validate row, column, and 3×3 box; backtrack on failure.">Backtracking</span> | Time: $O(9^m)$, Space: $O(m)$ | Hard |
| 38 | [Count and Say](https://leetcode.com/problems/count-and-say/) | String | Time: O(n), Space: O(1) | Easy |
| 39 | [📓 Combination Sum](../leetcode/0039.ipynb) | <span title="DFS with explicit undo steps; prune branches early when constraints are already violated.">Backtracking (DFS)</span> | Time: $O(N^{T/M})$, Space: $O(T/M)$ | Medium |
| 40 | [📓 Combination Sum II](../leetcode/0040.ipynb) | <span title="DFS with explicit undo steps; prune branches early when constraints are already violated.">Backtracking (DFS)</span> | Time: $O(2^N)$, Space: $O(N)$ | Medium |
| 41 | [📓 First Missing Positive](../leetcode/0041.ipynb) | <span title="Negate nums[val-1] to stamp which values are present, then scan for the first positive slot.">In-place Index Negation</span>| Time: O(n), Space: O(1) | Hard |
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Two Pointers, Dynamic Programming | Time: O(n), Space: O(1) | Hard |
| 43 | [Multiply Strings](https://leetcode.com/problems/multiply-strings/) | String | Time: O(m * n), Space: O(m + n) | Medium |
| 44 | [Wildcard Matching](https://leetcode.com/problems/wildcard-matching/) | Dynamic Programming | Time: O(m * n), Space: O(m * n) | Hard |
| 45 | [Jump Game II](https://leetcode.com/problems/jump-game-ii/) | Greedy | Time: O(n), Space: O(1) | Hard |
| 46 | [📓 Permutations](../leetcode/0046.ipynb) | <span title="Swap each element to the current position, recurse on the suffix, then swap back to restore order.">Backtracking (Swap)</span> | Time: $O(n \times n!)$, Space: $O(n)$ | Medium |
| 47 | [📓 Permutations II](../leetcode/0047.ipynb) | <span title="Sort first, then skip duplicate elements at the same recursion depth to avoid repeated permutations.">Backtracking + Dedup</span> | Time: $O(n \times n!)$, Space: $O(n)$ | Medium |
| 48 | [📓 Rotate Image](../leetcode/0048.ipynb) | <span title="Transpose the matrix across the main diagonal, then reverse each row to achieve a 90 degree clockwise rotation.">Transpose + Row Reverse</span>| Time: O(n^2), Space: O(1) | Medium |
| 49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Hash Map | Time: O(n * k), Space: O(n * k) | Medium |
| 50 | [Pow(x, n)](https://leetcode.com/problems/powx-n/) | Math | Time: O(log n), Space: O(1) | Medium |
| 51 | [📓 N-Queens](../leetcode/0051.ipynb) | <span title="Recurse row by row with three bitmasks tracking attacked columns and diagonals; prune invalid states in O(1).">Backtracking (Bitmask)</span> | Time: $O(n!)$, Space: $O(n)$ | Hard |
| 52 | [📓 N-Queens II](../leetcode/0052.ipynb) | <span title="Count valid N-Queens placements using bitmask backtracking without reconstructing boards.">Backtracking (Bitmask)</span> | Time: $O(n!)$, Space: $O(n)$ | Hard |
| 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Dynamic Programming | Time: O(n), Space: O(1) | Easy |
| 54 | [📓 Spiral Matrix](../leetcode/0054.ipynb) | <span title="Shrink four boundary pointers inward after each directional pass to peel the matrix layer by layer.">Boundary Shrinking</span>| Time: O(m * n), Space: O(1) | Medium |
| 55 | [Jump Game](https://leetcode.com/problems/jump-game/) | Greedy | Time: O(n), Space: O(1) | Medium |
| 56 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Sorting | Time: O(n log n), Space: O(1) | Medium |
| 57 | [Insert Interval](https://leetcode.com/problems/insert-interval/) | Sorting | Time: O(n), Space: O(1) | Medium |
| 58 | [Length of Last Word](https://leetcode.com/problems/length-of-last-word/) | String | Time: O(n), Space: O(1) | Easy |
| 59 | [📓 Spiral Matrix II](../leetcode/0059.ipynb) | <span title="Fill numbers 1 to n-squared in spiral order using four boundary pointers that shrink inward after each directional pass.">Boundary Simulation</span>| Time: O(n^2), Space: O(1) | Medium |
| 60 | [📓 Permutation Sequence](../leetcode/0060.ipynb) | <span title="Decode k into the k-th permutation one digit at a time using factorial number system quotients.">Factorial Number System</span> | Time: $O(n^2)$, Space: $O(n)$ | Hard |
| 61 | [Rotate List](https://leetcode.com/problems/rotate-list/) | Linked List | Time: O(n), Space: O(1) | Medium |
| 62 | [Unique Paths](https://leetcode.com/problems/unique-paths/) | Dynamic Programming | Time: O(m * n), Space: O(m * n) | Medium |
| 63 | [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/) | Dynamic Programming | Time: O(m * n), Space: O(m * n) | Medium |
| 64 | [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) | Dynamic Programming | Time: O(m * n), Space: O(m * n) | Medium |
| 65 | [Valid Number](https://leetcode.com/problems/valid-number/) | Math, String | Time: O(n), Space: O(1) | Hard |
| 66 | [📓 Plus One](../leetcode/0066.ipynb) | <span title="Simulate digit-by-digit carry propagation (like hand addition) through linked list nodes.">Carry Simulation</span> | Time: O(n), Space: O(1) | Easy |
| 67 | [Add Binary](https://leetcode.com/problems/add-binary/) | String | Time: O(max(m, n)), Space: O(max(m, n)) | Easy |
| 68 | [Text Justification](https://leetcode.com/problems/text-justification/) | String | Time: O(n), Space: O(n) | Hard |
| 69 | [Sqrt(x)](https://leetcode.com/problems/sqrtx/) | Math | Time: O(log x), Space: O(1) | Easy |
| 70 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Dynamic Programming | Time: O(n), Space: O(1) | Easy |
| 71 | [Simplify Path](https://leetcode.com/problems/simplify-path/) | Stack | Time: O(n), Space: O(n) | Medium |
| 72 | [Edit Distance](https://leetcode.com/problems/edit-distance/) | Dynamic Programming | Time: O(m * n), Space: O(m * n) | Hard |
| 73 | [📓 Set Matrix Zeroes](../leetcode/0073.ipynb) | <span title="Use the first row and column as markers for which rows and cols to zero, saving their original state in two booleans.">First Row/Col as Flags</span>| Time: O(m * n), Space: O(1) | Medium |
| 74 | [📓 Search a 2D Matrix](../leetcode/0074.ipynb) | <span title="Treat the 2D matrix as a 1D array; map flat index → (row, col) with mid/cols and mid%cols.">Binary Search on Flattened Index</span> | Time: O(log(m * n)), Space: O(1) | Medium |
| 75 | [Sort Colors](https://leetcode.com/problems/sort-colors/) | Sorting, Two Pointers | Time: O(n), Space: O(1) | Medium |
| 76 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Hash Map, Sliding Window | Time: O(n), Space: O(n) | Hard |
| 77 | [📓 Combinations](../leetcode/0077.ipynb) | <span title="Fix a start index and recurse forward; prune branches where remaining elements cannot fill the combination.">Backtracking</span> | Time: $O\!\left(\binom{n}{k} \cdot k\right)$, Space: $O(k)$ | Medium |
| 78 | [📓 Subsets](../leetcode/0078.ipynb) | <span title="Record the running path at every step, then recurse from index+1 to generate all 2^n subsets.">Backtracking</span> | Time: $O(2^n \cdot n)$, Space: $O(n)$ | Medium |
| 79 | [📓 Word Search](../leetcode/0079.ipynb) | <span title="Mark each visited cell with a sentinel character in-place; restore it after the recursive call returns.">DFS + Backtracking</span> | Time: $O(m \cdot n \cdot 4^L)$, Space: $O(L)$ | Medium |
| 80 | [📓 Remove Duplicates from Sorted Array II](../leetcode/0080.ipynb) | <span title="Advance a write pointer, admitting each element only if it differs from the value two slots behind the write head.">Two Pointers</span>| Time: O(n), Space: O(1) | Medium |
| 81 | [📓 Search in Rotated Sorted Array II](../leetcode/0081.ipynb) | <span title="When arr[lo] == arr[mid], can't determine sorted half — increment lo to skip the duplicate.">Binary Search with Duplicate Handling</span> | Time: O(n) worst, O(log n) avg, Space: O(1) | Medium |
| 82 | [Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) | Linked List | Time: O(n), Space: O(1) | Medium |
| 83 | [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) | Linked List | Time: O(n), Space: O(1) | Easy |
| 84 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Stack | Time: O(n), Space: O(n) | Hard |
| 85 | [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/) | Dynamic Programming, Stack | Time: O(m * n), Space: O(n) | Hard |
| 86 | [Partition List](https://leetcode.com/problems/partition-list/) | Linked List | Time: O(n), Space: O(1) | Medium |
| 87 | [Scramble String](https://leetcode.com/problems/scramble-string/) | Dynamic Programming | Time: O(n^4), Space: O(n^4) | Hard |
| 88 | [📓 Merge Sorted Array](../leetcode/0088.ipynb) | <span title="Merge two sorted arrays in-place from the back using three index pointers.">Three Pointers (Merge from End)</span> | Time: O(m + n), Space: O(1) | Easy |
| 89 | [📓 Gray Code](../leetcode/0089.ipynb) | <span title="Generate each Gray code as i XOR (i >> 1) for all i in [0, 2^n) — O(1) per element.">Binary-Reflected XOR Formula</span> | Time: O(2^n), Space: O(2^n) | Medium |
| 90 | [📓 Subsets II](../leetcode/0090.ipynb) | <span title="Sort first, then skip duplicate elements at the same recursion depth to avoid repeated subsets.">Backtracking + Dedup</span> | Time: $O(2^n \cdot n)$, Space: $O(n)$ | Medium |
| 91 | [Decode Ways](https://leetcode.com/problems/decode-ways/) | Dynamic Programming | Time: O(n), Space: O(n) | Medium |
| 92 | [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/) | Linked List | Time: O(n), Space: O(1) | Medium |
| 93 | [📓 Restore IP Addresses](../leetcode/0093.ipynb) | <span title="Try 1-3 digit segments at each of 4 boundaries; prune segments outside 0-255 or with leading zeros.">Backtracking</span> | Time: $O(1)$, Space: $O(1)$ | Medium |
| 94 | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) | Tree, Stack | Time: O(n), Space: O(n) | Easy |
| 95 | [Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/) | Tree, Dynamic Programming | Time: O(4^n / sqrt(n)), Space: O(n) | Medium |
| 96 | [Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/) | Dynamic Programming | Time: O(n^2), Space: O(n) | Medium |
| 97 | [Interleaving String](https://leetcode.com/problems/interleaving-string/) | Dynamic Programming | Time: O(m * n), Space: O(m * n) | Hard |
| 98 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | Tree, DFS | Time: O(n), Space: O(n) | Medium |
| 99 | [Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/) | Tree, DFS | Time: O(n), Space: O(h) | Hard |
| 100 | [Same Tree](https://leetcode.com/problems/same-tree/) | Tree, DFS | Time: O(n), Space: O(n) | Easy |
| 101 | [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) | Tree, DFS | Time: O(n), Space: O(h) | Easy |
| 102 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Tree, BFS | Time: O(n), Space: O(n) | Medium |
| 103 | [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) | Tree, BFS | Time: O(n), Space: O(n) | Medium |
| 104 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Tree, DFS | Time: O(n), Space: O(h) | Easy |
| 105 | [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | Tree, Recursion | Time: O(n), Space: O(n) | Medium |
| 106 | [Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) | Tree, Recursion | Time: O(n), Space: O(n) | Medium |
| 107 | [Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/) | Tree, BFS | Time: O(n), Space: O(n) | Medium |
| 108 | [Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) | Tree, Recursion | Time: O(n), Space: O(log n) | Easy |
| 109 | [Convert Sorted List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/) | Linked List, Tree | Time: O(n), Space: O(log n) | Medium |
| 110 | [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | Tree, DFS | Time: O(n), Space: O(h) | Easy |
| 111 | [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/) | Tree, DFS | Time: O(n), Space: O(h) | Easy |
| 112 | [Path Sum](https://leetcode.com/problems/path-sum/) | Tree, DFS | Time: O(n), Space: O(h) | Easy |
| 113 | [Path Sum II](https://leetcode.com/problems/path-sum-ii/) | Tree, DFS | Time: O(n), Space: O(h) | Medium |
| 114 | [Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/) | Tree, DFS | Time: O(n), Space: O(h) | Medium |
| 115 | [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) | Dynamic Programming | Time: O(m * n), Space: O(m * n) | Hard |
| 116 | [Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/) | Tree, BFS | Time: O(n), Space: O(1) | Medium |
| 117 | [Populating Next Right Pointers in Each Node II](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/) | Tree, BFS | Time: O(n), Space: O(1) | Medium |
| 118 | [📓 Pascal's Triangle](../leetcode/0118.ipynb) | <span title="Process the matrix one row at a time, applying local rules to update state.">Row-by-Row Simulation</span> | Time: O(n^2), Space: O(n^2) | Easy |
| 119 | [📓 Pascal's Triangle II](../leetcode/0119.ipynb) | <span title="Reuse a fixed-size DP array row by row, reducing space from O(m·n) to O(n).">Rolling Array</span> | Time: O(k^2), Space: O(k) | Easy |
| 120 | [Triangle](https://leetcode.com/problems/triangle/) | Dynamic Programming | Time: O(n^2), Space: O(n^2) | Medium |
| 121 | [📓 Best Time to Buy and Sell Stock](../leetcode/0121.ipynb) | <span title="Make the locally optimal choice at each step; one left-to-right pass suffices.">Greedy (One Pass)</span> | Time: O(n), Space: O(1) | Easy |
| 122 | [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) | Greedy | Time: O(n), Space: O(1) | Medium |
| 123 | [Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) | Dynamic Programming | Time: O(n), Space: O(1) | Hard |
| 124 | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Tree, DFS | Time: O(n), Space: O(h) | Hard |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | String | Time: O(n), Space: O(1) | Easy |
| 126 | [Word Ladder II](https://leetcode.com/problems/word-ladder-ii/) | BFS, Graph | Time: O(n^2), Space: O(n) | Hard |
| 127 | [Word Ladder](https://leetcode.com/problems/word-ladder/) | BFS, Graph | Time: O(n^2), Space: O(n) | Medium |
| 128 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Hash Set | Time: O(n), Space: O(n) | Hard |
| 129 | [Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/) | Tree, DFS | Time: O(n), Space: O(h) | Medium |
| 130 | [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) | DFS, BFS | Time: O(m * n), Space: O(m * n) | Medium |
| 131 | [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) | Backtracking | Time: O(2^n), Space: O(n) | Medium |
| 132 | [Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/) | Dynamic Programming | Time: O(n^2), Space: O(n^2) | Hard |
| 133 | [Clone Graph](https://leetcode.com/problems/clone-graph/) | Graph, DFS | Time: O(V + E), Space: O(V) | Medium |
| 134 | [Gas Station](https://leetcode.com/problems/gas-station/) | Greedy | Time: O(n), Space: O(1) | Medium |
| 135 | [Candy](https://leetcode.com/problems/candy/) | Greedy | Time: O(n), Space: O(n) | Hard |
| 136 | [📓 Single Number](../leetcode/0136.ipynb) | <span title="XOR all elements; duplicate values cancel out (a ^ a = 0), leaving the unique value.">XOR</span> | Time: O(n), Space: O(1) | Easy |
| 137 | [📓 Single Number II](../leetcode/0137.ipynb) | <span title="For each bit position, sum counts across all numbers; mod 3 isolates the unique number's bits.">Bit-Count Mod 3</span> | Time: O(n), Space: O(1) | Medium |
| 138 | [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | Linked List | Time: O(n), Space: O(n) | Medium |
| 139 | [Word Break](https://leetcode.com/problems/word-break/) | Dynamic Programming, Hash Set | Time: O(n^2), Space: O(n) | Medium |
| 140 | [Word Break II](https://leetcode.com/problems/word-break-ii/) | Dynamic Programming, Backtracking | Time: O(n^3), Space: O(n) | Hard |
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Linked List | Time: O(n), Space: O(1) | Easy |
| 142 | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) | Linked List, Floyd's Cycle Detection | Time: O(n), Space: O(1) | Medium |
| 143 | [Reorder List](https://leetcode.com/problems/reorder-list/) | Linked List | Time: O(n), Space: O(1) | Medium |
| 144 | [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) | Tree, DFS | Time: O(n), Space: O(n) | Easy |
| 145 | [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/) | Tree, DFS | Time: O(n), Space: O(n) | Easy |
| 146 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | Hash Map, Doubly Linked List | Time: O(1), Space: O(capacity) | Hard |
| 147 | [Insertion Sort List](https://leetcode.com/problems/insertion-sort-list/) | Linked List | Time: O(n^2), Space: O(1) | Medium |
| 148 | [Sort List](https://leetcode.com/problems/sort-list/) | Linked List, Merge Sort | Time: O(n log n), Space: O(1) | Medium |
| 149 | [Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/) | Geometry, Hash Map | Time: O(n^2), Space: O(n) | Hard |
| 150 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Stack | Time: O(n), Space: O(n) | Medium |
| 151 | [Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/) | String | Time: O(n), Space: O(1) | Medium |
| 152 | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | Dynamic Programming | Time: O(n), Space: O(1) | Medium |
| 153 | [📓 Find Minimum in Rotated Sorted Array](../leetcode/0153.ipynb) | <span title="Compare arr[mid] to arr[hi] to determine which half contains the minimum.">Binary Search on Rotation Pivot</span> | Time: O(log n), Space: O(1) | Medium |
| 154 | [📓 Find Minimum in Rotated Sorted Array II](../leetcode/0154.ipynb) | <span title="When arr[mid] == arr[hi], can't determine which half has the min — decrement hi safely.">Binary Search with Duplicate Shrinking</span> | Time: O(n) worst, O(log n) avg, Space: O(1) | Medium |
| 155 | [Min Stack](https://leetcode.com/problems/min-stack/) | Stack | Time: O(1), Space: O(n) | Easy |
| 156 | [Binary Tree Upside Down](https://leetcode.com/problems/binary-tree-upside-down/) | Tree, Recursion | Time: O(n), Space: O(h) | Medium |
| 157 | [Read N Characters Given Read4](https://leetcode.com/problems/read-n-characters-given-read4/) | String | Time: O(n), Space: O(1) | Easy |
| 158 | [Read N Characters Given Read4 II - Call multiple times](https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/) | String | Time: O(n), Space: O(1) | Medium |
| 159 | [Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/) | Sliding Window | Time: O(n), Space: O(1) | Medium |
| 160 | [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/) | Linked List | Time: O(m + n), Space: O(1) | Easy |
| 161 | [One Edit Distance](https://leetcode.com/problems/one-edit-distance/) | String | Time: O(m * n), Space: O(1) | Medium |
| 162 | [📓 Find Peak Element](../leetcode/0162.ipynb) | <span title="Move toward the rising slope: if arr[mid] < arr[mid+1] the peak is to the right.">Binary Search on Gradient</span> | Time: O(log n), Space: O(1) | Medium |
| 163 | [Missing Ranges](https://leetcode.com/problems/missing-ranges/) | Array | Time: O(n), Space: O(1) | Medium |
| 164 | [Maximum Gap](https://leetcode.com/problems/maximum-gap/) | Sorting | Time: O(n log n), Space: O(n) | Hard |
| 165 | [Compare Version Numbers](https://leetcode.com/problems/compare-version-numbers/) | String | Time: O(n), Space: O(1) | Medium |
| 166 | [Fraction to Recurring Decimal](https://leetcode.com/problems/fraction-to-recurring-decimal/) | Math, String | Time: O(n), Space: O(n) | Medium |
| 167 | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Two Pointers | Time: O(n), Space: O(1) | Easy |
| 168 | [Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/) | Math | Time: O(log n), Space: O(1) | Easy |
| 169 | [Majority Element](https://leetcode.com/problems/majority-element/) | Hash Map, Sorting | Time: O(n), Space: O(n) | Easy |
| 170 | [Two Sum III - Data structure design](https://leetcode.com/problems/two-sum-iii-data-structure-design/) | Hash Map | Time: O(1), Space: O(n) | Easy |
| 171 | [Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/) | Math | Time: O(n), Space: O(1) | Easy |
| 172 | [Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/) | Math | Time: O(log n), Space: O(1) | Easy |
| 173 | [Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/) | Tree, Stack | Time: O(1), Space: O(h) | Medium |
| 174 | [Dungeon Game](https://leetcode.com/problems/dungeon-game/) | Dynamic Programming | Time: O(m * n), Space: O(m * n) | Hard |
| 175 | [Combine Two Tables](https://leetcode.com/problems/combine-two-tables/) | SQL | Time: O(1), Space: O(1) | Easy |
| 176 | [Second Highest Salary](https://leetcode.com/problems/second-highest-salary/) | SQL | Time: O(1), Space: O(1) | Easy |
| 177 | [Nth Highest Salary](https://leetcode.com/problems/nth-highest-salary/) | SQL | Time: O(1), Space: O(1) | Medium |
| 178 | [Rank Scores](https://leetcode.com/problems/rank-scores/) | SQL | Time: O(1), Space: O(1) | Medium |
| 179 | [Largest Number](https://leetcode.com/problems/largest-number/) | Sorting | Time: O(n log n), Space: O(n) | Medium |
| 180 | [Consecutive Numbers](https://leetcode.com/problems/consecutive-numbers/) | SQL | Time: O(1), Space: O(1) | Medium |
| 181 | [Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/) | SQL | Time: O(1), Space: O(1) | Easy |
| 182 | [Duplicate Emails](https://leetcode.com/problems/duplicate-emails/) | SQL | Time: O(1), Space: O(1) | Easy |
| 183 | [Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order/) | SQL | Time: O(1), Space: O(1) | Easy |
| 184 | [Department Highest Salary](https://leetcode.com/problems/department-highest-salary/) | SQL | Time: O(1), Space: O(1) | Easy |
| 185 | [Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries/) | SQL | Time: O(1), Space: O(1) | Hard |
| 186 | [Reverse Words in a String II](https://leetcode.com/problems/reverse-words-in-a-string-ii/) | String | Time: O(n), Space: O(1) | Medium |
| 187 | [Repeated DNA Sequences](https://leetcode.com/problems/repeated-dna-sequences/) | Hash Set | Time: O(n), Space: O(n) | Medium |
| 188 | [Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/) | Dynamic Programming | Time: O(k * n), Space: O(k * n) | Hard |
| 189 | [📓 Rotate Array](../leetcode/0189.ipynb) | <span title="Rotate an array by reversing the whole array, then each part separately.">Three Reversals</span> | Time: O(n), Space: O(1) | Medium |
| 190 | [📓 Reverse Bits](../leetcode/0190.ipynb) | <span title="Shift source bits one at a time into a result register, reversing their order.">Bit-by-bit Reversal</span> | Time: O(1), Space: O(1) | Easy |
| 191 | [📓 Number of 1 Bits](../leetcode/0191.ipynb) | <span title="Clear the lowest set bit with n &= (n-1) and count iterations to find the bit count in O(k).">Brian Kernighan's Algorithm</span> | Time: O(k), Space: O(1) | Easy |
| 192 | [Word Frequency](https://leetcode.com/problems/word-frequency/) | SQL | Time: O(1), Space: O(1) | Easy |
| 193 | [Valid Phone Numbers](https://leetcode.com/problems/valid-phone-numbers/) | Regex | Time: O(1), Space: O(1) | Easy |
| 194 | [Transpose File](https://leetcode.com/problems/transpose-file/) | File I/O | Time: O(1), Space: O(1) | Easy |
| 195 | [Tenth Line](https://leetcode.com/problems/tenth-line/) | File I/O | Time: O(1), Space: O(1) | Easy |
| 196 | [Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails/) | SQL | Time: O(1), Space: O(1) | Easy |
| 197 | [Rising Temperature](https://leetcode.com/problems/rising-temperature/) | SQL | Time: O(1), Space: O(1) | Easy |
| 198 | [House Robber](https://leetcode.com/problems/house-robber/) | Dynamic Programming | Time: O(n), Space: O(1) | Medium |
| 199 | [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | Tree, BFS | Time: O(n), Space: O(n) | Medium |
| 200 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | DFS, BFS | Time: O(m * n), Space: O(m * n) | Medium |
| 201 | [📓 Bitwise AND of Numbers Range](../leetcode/0201.ipynb) | <span title="Right-shift both endpoints until equal; the common prefix, shifted back, is the answer.">Common Prefix (Right Shift)</span> | Time: O(1), Space: O(1) | Medium |
| 202 | [Happy Number](https://leetcode.com/problems/happy-number/) | Hash Set, Cycle Detection | Time: O(log n), Space: O(log n) | Easy |
| 203 | [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/) | Linked List | Time: O(n), Space: O(1) | Easy |
| 204 | [Count Primes](https://leetcode.com/problems/count-primes/) | Sieve of Eratosthenes | Time: O(n log log n), Space: O(n) | Easy |
| 205 | [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/) | String, Hash Map | Time: O(n), Space: O(n) | Easy |
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Linked List | Time: O(n), Space: O(1) | Easy |
| 207 | [Course Schedule](https://leetcode.com/problems/course-schedule/) | Graph, Topological Sort | Time: O(V + E), Space: O(V + E) | Medium |
| 208 | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | Trie | Time: O(n), Space: O(n) | Medium |
| 209 | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | Sliding Window | Time: O(n), Space: O(1) | Medium |
| 210 | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | Graph, Topological Sort | Time: O(V + E), Space: O(V + E) | Medium |
| 211 | [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | Trie | Time: O(n), Space: O(n) | Medium |
| 212 | [Word Search II](https://leetcode.com/problems/word-search-ii/) | Trie, Backtracking | Time: O(m * n * 4^L), Space: O(m * n) | Hard |
| 213 | [House Robber II](https://leetcode.com/problems/house-robber-ii/) | Dynamic Programming | Time: O(n), Space: O(1) | Medium |
| 214 | [Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/) | String, KMP Algorithm | Time: O(n), Space: O(n) | Hard |
| 215 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Heap | Time: O(n log k), Space: O(k) | Medium |
| 216 | [Combination Sum III](https://leetcode.com/problems/combination-sum-iii/) | Backtracking | Time: O(2^n), Space: O(n) | Medium |
| 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Hash Set | Time: O(n), Space: O(n) | Easy |
| 218 | [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/) | Heap, Sweep Line | Time: O(n log n), Space: O(n) | Hard |
| 219 | [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) | Hash Set | Time: O(n), Space: O(n) | Easy |
| 220 | [Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/) | Bucket Sort | Time: O(n), Space: O(n) | Medium |
| 221 | [Maximal Square](https://leetcode.com/problems/maximal-square/) | Dynamic Programming | Time: O(m * n), Space: O(m * n) | Medium |
| 222 | [Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/) | Tree | Time: O(log^2 n), Space: O(log n) | Medium |
| 223 | [Rectangle Area](https://leetcode.com/problems/rectangle-area/) | Geometry | Time: O(1), Space: O(1) | Medium |
| 224 | [Basic Calculator](https://leetcode.com/problems/basic-calculator/) | Stack | Time: O(n), Space: O(n) | Hard |
| 225 | [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) | Queue, Stack | Time: O(1), Space: O(n) | Easy |
| 226 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Tree | Time: O(n), Space: O(h) | Easy |
| 227 | [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/) | Stack | Time: O(n), Space: O(n) | Medium |
| 228 | [📓 Summary Ranges](../leetcode/0228.ipynb) | <span title="Single left-to-right pass; update a running answer (min, max, count, etc.) at each step.">Linear Scan</span> | Time: O(n), Space: O(1) | Easy |
| 229 | [Majority Element II](https://leetcode.com/problems/majority-element-ii/) | Boyer-Moore Voting Algorithm | Time: O(n), Space: O(1) | Medium |
| 230 | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Tree, Inorder Traversal | Time: O(h + k), Space: O(h) | Medium |
| 231 | [Power of Two](https://leetcode.com/problems/power-of-two/) | Math | Time: O(1), Space: O(1) | Easy |
| 232 | [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) | Stack | Time: O(1), Space: O(n) | Easy |
| 233 | [Number of Digit One](https://leetcode.com/problems/number-of-digit-one/) | Math | Time: O(log n), Space: O(1) | Hard |
| 234 | [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) | Linked List, Stack | Time: O(n), Space: O(n) | Easy |
| 235 | [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | Tree, Binary Search | Time: O(h), Space: O(1) | Easy |
| 236 | [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | Tree, DFS | Time: O(n), Space: O(h) | Medium |
| 237 | [Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/) | Linked List | Time: O(1), Space: O(1) | Easy |
| 238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Array | Time: O(n), Space: O(1) | Medium |
| 239 | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Deque | Time: O(n), Space: O(k) | Hard |
| 240 | [📓 Search a 2D Matrix II](../leetcode/0240.ipynb) | <span title="Start at top-right corner of a sorted 2D matrix; eliminate a row or column each step.">Staircase Search</span> | Time: O(m + n), Space: O(1) | Medium |
| 241 | [Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/) | Recursion | Time: O(2^n), Space: O(n) | Medium |
| 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Hash Map | Time: O(n), Space: O(n) | Easy |
| 243 | [📓 Shortest Word Distance](../leetcode/0243.ipynb) | <span title="One traversal, accumulating the answer without backtracking.">One-Pass Linear Scan</span> | Time: O(n), Space: O(1) | Easy |
| 244 | [Shortest Word Distance II](https://leetcode.com/problems/shortest-word-distance-ii/) | Hash Map | Time: O(1), Space: O(n) | Medium |
| 245 | [Shortest Word Distance III](https://leetcode.com/problems/shortest-word-distance-iii/) | Array, Hash Map | Time: O(n), Space: O(1) | Medium |
| 246 | [Strobogrammatic Number](https://leetcode.com/problems/strobogrammatic-number/) | String | Time: O(n), Space: O(1) | Easy |
| 247 | [Strobogrammatic Number II](https://leetcode.com/problems/strobogrammatic-number-ii/) | String | Time: O(n), Space: O(1) | Medium |
| 248 | [Strobogrammatic Number III](https://leetcode.com/problems/strobogrammatic-number-iii/) | String | Time: O(n), Space: O(1) | Hard |
| 249 | [Group Shifted Strings](https://leetcode.com/problems/group-shifted-strings/) | Hash Map | Time: O(nk), Space: O(nk) | Medium |
| 250 | [Count Univalue Subtrees](https://leetcode.com/problems/count-univalue-subtrees/) | Tree, DFS | Time: O(n), Space: O(h) | Medium |
| 251 | [Flatten 2D Vector](https://leetcode.com/problems/flatten-2d-vector/) | Array, Iterator | Time: O(1), Space: O(1) | Medium |
| 252 | [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) | Greedy | Time: O(n log n), Space: O(1) | Easy |
| 253 | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) | Greedy, Heap | Time: O(n log n), Space: O(n) | Medium |
| 254 | [Factor Combinations](https://leetcode.com/problems/factor-combinations/) | Backtracking | Time: O(n log n), Space: O(n) | Medium |
| 255 | [Verify Preorder Serialization of a Binary Tree](https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/) | Stack | Time: O(n), Space: O(n) | Medium |
| 256 | [Paint House](https://leetcode.com/problems/paint-house/) | Dynamic Programming | Time: O(n), Space: O(1) | Medium |
| 257 | [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/) | Tree, DFS | Time: O(n), Space: O(h) | Easy |
| 258 | [Add Digits](https://leetcode.com/problems/add-digits/) | Math | Time: O(1), Space: O(1) | Easy |
| 259 | [3Sum Smaller](https://leetcode.com/problems/3sum-smaller/) | Sorting, Two Pointers | Time: O(n^2), Space: O(1) | Medium |
| 260 | [📓 Single Number III](../leetcode/0260.ipynb) | <span title="XOR all values to get x^y; split by the lowest differing bit into two groups; XOR each group.">XOR Partition by Lowest Differing Bit</span> | Time: O(n), Space: O(1) | Medium |
| 261 | [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) | Union Find, DFS | Time: O(n), Space: O(n) | Medium |
| 262 | [Trips and Users](https://leetcode.com/problems/trips-and-users/) | SQL | Time: O(1), Space: O(1) | Medium |
| 263 | [Ugly Number](https://leetcode.com/problems/ugly-number/) | Math | Time: O(log n), Space: O(1) | Easy |
| 264 | [Ugly Number II](https://leetcode.com/problems/ugly-number-ii/) | Dynamic Programming, Min-Heap | Time: O(n log n), Space: O(n) | Medium |
| 265 | [Paint House II](https://leetcode.com/problems/paint-house-ii/) | Dynamic Programming | Time: O(nk), Space: O(k) | Hard |
| 266 | [Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation/) | Hash Map | Time: O(n), Space: O(n) | Easy |
| 267 | [Palindrome Permutation II](https://leetcode.com/problems/palindrome-permutation-ii/) | Backtracking | Time: O(n!), Space: O(n) | Medium |
| 268 | [📓 Missing Number](../leetcode/0268.ipynb) | <span title="XOR all indices with all values; identical pairs cancel, leaving only the missing number.">XOR with Indices</span> | Time: O(n), Space: O(1) | Easy |
| 269 | [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) | Graph, Topological Sort | Time: O(V + E), Space: O(V + E) | Hard |
| 270 | [Closest Binary Search Tree Value](https://leetcode.com/problems/closest-binary-search-tree-value/) | Tree, Binary Search | Time: O(h), Space: O(1) | Easy |
| 271 | [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) | String | Time: O(n), Space: O(n) | Medium |
| 272 | [Closest Binary Search Tree Value II](https://leetcode.com/problems/closest-binary-search-tree-value-ii/) | Tree, BFS | Time: O(h + k), Space: O(h) | Hard |
| 273 | [Integer to English Words](https://leetcode.com/problems/integer-to-english-words/) | Math | Time: O(n), Space: O(1) | Hard |
| 274 | [H-Index](https://leetcode.com/problems/h-index/) | Sorting | Time: O(n log n), Space: O(1) | Medium |
| 275 | [📓 H-Index II](../leetcode/0275.ipynb) | <span title="Binary search directly on the answer value; use a feasibility check to halve the range.">Binary Search on Answer</span> | Time: O(log n), Space: O(1) | Medium |
| 276 | [Paint Fence](https://leetcode.com/problems/paint-fence/) | Dynamic Programming | Time: O(n), Space: O(1) | Medium |
| 277 | [Find the Celebrity](https://leetcode.com/problems/find-the-celebrity/) | Graph, Two Pointers | Time: O(n), Space: O(1) | Medium |
| 278 | [📓 First Bad Version](../leetcode/0278.ipynb) | <span title="Halve the search space each step by comparing the midpoint to a monotone predicate.">Binary Search</span> | Time: $O(\log n)$, Space: $O(1)$ | Easy |
| 279 | [Perfect Squares](https://leetcode.com/problems/perfect-squares/) | Dynamic Programming | Time: O(n√n), Space: O(n) | Medium |
| 280 | [Wiggle Sort](https://leetcode.com/problems/wiggle-sort/) | Sorting, Two Pointers | Time: O(n log n), Space: O(1) | Medium |
| 281 | [Zigzag Iterator](https://leetcode.com/problems/zigzag-iterator/) | Iterator | Time: O(1), Space: O(k) | Medium |
| 282 | [Expression Add Operators](https://leetcode.com/problems/expression-add-operators/) | Backtracking | Time: O(4^n), Space: O(n) | Hard |
| 283 | [📓 Move Zeroes](../leetcode/0283.ipynb) | <span title="Write pointer fills valid elements in-place; fill pointer finishes trailing padding.">Two Pointers (Write + Fill)</span> | Time: O(n), Space: O(1) | Easy |
| 284 | [Peeking Iterator](https://leetcode.com/problems/peeking-iterator/) | Iterator | Time: O(1), Space: O(1) | Medium |
| 285 | [Inorder Successor in BST](https://leetcode.com/problems/inorder-successor-in-bst/) | Tree | Time: O(h), Space: O(1) | Medium |
| 286 | [📓 Walls and Gates](../leetcode/0286.ipynb) | <span title="Breadth-first search with a queue; visit all neighbors level by level.">BFS (Queue)</span> | Time: $O(m \cdot n)$, Space: $O(m \cdot n)$ | Medium |
| 287 | [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) | Array, Floyd's Tortoise and Hare | Time: O(n), Space: O(1) | Medium |
| 288 | [Unique Word Abbreviation](https://leetcode.com/problems/unique-word-abbreviation/) | Hash Map | Time: O(n), Space: O(n) | Medium |
| 289 | [Game of Life](https://leetcode.com/problems/game-of-life/) | Array | Time: O(m * n), Space: O(1) | Medium |
| 290 | [Word Pattern](https://leetcode.com/problems/word-pattern/) | Hash Map | Time: O(n), Space: O(n) | Easy |
| 291 | [Word Pattern II](https://leetcode.com/problems/word-pattern-ii/) | Backtracking | Time: O(n!), Space: O(n) | Medium |
| 292 | [Nim Game](https://leetcode.com/problems/nim-game/) | Game Theory | Time: O(1), Space: O(1) | Easy |
| 293 | [📓 Flip Game](../leetcode/0293.ipynb) | <span title="One sweep through the data, typically updating a counter or maximum in place.">Single Scan</span> | Time: O(n²), Space: O(n) per result | Easy |
| 784 | [📓 Letter Case Permutation](../leetcode/0784.ipynb) | <span title="DFS with explicit undo steps; prune branches early when constraints are already violated.">Backtracking (DFS)</span> | Time: $O(n \cdot 2^n)$, Space: $O(n)$ | Medium |
| 22 | [📓 Generate Parentheses](../leetcode/0022.ipynb) | <span title="DFS with explicit undo steps; prune branches early when constraints are already violated.">Backtracking (DFS)</span> | Time: $O\left(\frac{4^n}{\sqrt{n}}\right)$, Space: $O(n)$ | Medium |
| 39 | [📓 Combination Sum](../leetcode/0039.ipynb) | <span title="DFS with explicit undo steps; prune branches early when constraints are already violated.">Backtracking (DFS)</span> | Time: $O(N^{T/M})$, Space: $O(T/M)$ | Medium |
| 40 | [📓 Combination Sum II](../leetcode/0040.ipynb) | <span title="DFS with explicit undo steps; prune branches early when constraints are already violated.">Backtracking (DFS)</span> | Time: $O(2^N)$, Space: $O(N)$ | Medium |
| 294 | [Flip Game II](https://leetcode.com/problems/flip-game-ii/) | Backtracking | Time: O(n), Space: O(n) | Medium |
| 295 | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Heap | Time: O(log n), Space: O(n) | Hard |
| 296 | [Best Meeting Point](https://leetcode.com/problems/best-meeting-point/) | Manhatten Distance | Time: O(m * n), Space: O(1) | Hard |
| 297 | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | Tree, DFS | Time: O(n), Space: O(n) | Hard |
| 298 | [Binary Tree Longest Consecutive Sequence](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/) | Tree, DFS | Time: O(n), Space: O(h) | Medium |
| 299 | [Bulls and Cows](https://leetcode.com/problems/bulls-and-cows/) | Hash Map | Time: O(n), Space: O(n) | Medium |
| 300 | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | Dynamic Programming | Time: O(n^2), Space: O(n) | Medium |
| 301 | [Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/) | BFS, Backtracking | Time: O(2^n), Space: O(n) | Hard |
| 302 | [Smallest Rectangle Enclosing Black Pixels](https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/) | Array | Time: O(m + n), Space: O(1) | Medium |
| 303 | [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) | Prefix Sum Array | Time: O(1), Space: O(n) | Easy |
| 304 | [📓 Range Sum Query 2D - Immutable](../leetcode/0304.ipynb) | <span title="Precompute rectangle sums so any submatrix query is answered in O(1) with inclusion-exclusion.">2D Prefix Sum</span> | Time: O(1) query, O(m·n) build, Space: O(m·n) | Medium |
| 305 | [Number of Islands II](https://leetcode.com/problems/number-of-islands-ii/) | Union Find | Time: O(n log n), Space: O(n) | Hard |
| 306 | [Additive Number](https://leetcode.com/problems/additive-number/) | String, Backtracking | Time: O(n^3), Space: O(1) | Medium |
| 307 | [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) | Segment Tree | Time: O(log n), Space: O(n) | Medium |
| 308 | [📓 Range Sum Query 2D - Mutable](../leetcode/0308.ipynb) | <span title="Fenwick tree extended to a 2D grid; update and query in O(log m · log n) per operation.">2D Binary Indexed Tree</span> | Time: O(log m · log n) update & query, Space: O(m·n) | Hard |
| 309 | [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | Dynamic Programming | Time: O(n), Space: O(n) | Medium |
| 310 | [Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/) | Graph, BFS | Time: O(n), Space: O(n) | Medium |
| 311 | [Sparse Matrix Multiplication](https://leetcode.com/problems/sparse-matrix-multiplication/) | Array | Time: O(m * n * k), Space: O(m * n) | Medium |
| 312 | [Burst Balloons](https://leetcode.com/problems/burst-balloons/) | Dynamic Programming | Time: O(n^3), Space: O(n^2) | Hard |
| 313 | [Super Ugly Number](https://leetcode.com/problems/super-ugly-number/) | Min-Heap | Time: O(k * log k), Space: O(k) | Medium |
| 314 | [Binary Tree Vertical Order Traversal](https://leetcode.com/problems/binary-tree-vertical-order-traversal/) | Tree, BFS | Time: O(n log n), Space: O(n) | Medium |
| 315 | [📓 Count of Smaller Numbers After Self](../leetcode/0315.ipynb) | <span title="Fenwick tree: update index i with i += i & -i; prefix-query with i -= i & -i. O(log n) per op.">Binary Indexed Tree</span> | Time: $O(n \log n)$, Space: $O(n)$ | Hard |
| 316 | [Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/) | Stack, Greedy | Time: O(n), Space: O(n) | Hard |
| 317 | [Shortest Distance from All Buildings](https://leetcode.com/problems/shortest-distance-from-all-buildings/) | BFS | Time: O(m * n), Space: O(m * n) | Hard |
| 318 | [📓 Maximum Product of Word Lengths](../leetcode/0318.ipynb) | <span title="Encode each word's letters as a 26-bit mask; zero AND means disjoint character sets.">Bitmask per Word</span> | Time: O(n^2), Space: O(n) | Medium |
| 319 | [Bulb Switcher](https://leetcode.com/problems/bulb-switcher/) | Math | Time: O(1), Space: O(1) | Medium |
| 320 | [Generalized Abbreviation](https://leetcode.com/problems/generalized-abbreviation/) | Backtracking | Time: O(2^n), Space: O(n) | Medium |
| 321 | [Create Maximum Number](https://leetcode.com/problems/create-maximum-number/) | Greedy, Stack | Time: O(n), Space: O(n) | Hard |
| 322 | [Coin Change](https://leetcode.com/problems/coin-change/) | Dynamic Programming | Time: O(n * amount), Space: O(amount) | Medium |
| 323 | [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | Graph, DFS/BFS | Time: O(V + E), Space: O(V) | Medium |
| 324 | [Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/) | Sorting, Two Pointers | Time: O(n log n), Space: O(n) | Medium |
| 325 | [Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/) | Hash Map | Time: O(n), Space: O(n) | Medium |
| 326 | [Power of Three](https://leetcode.com/problems/power-of-three/) | Math | Time: O(log n), Space: O(1) | Easy |
| 327 | [📓 Count of Range Sum](../leetcode/0327.ipynb) | <span title="Merge sort to count inversions or range sums; binary search for the split boundary.">Binary Search, Merge Sort</span> | Time: O(n log n), Space: O(n) | Hard |
| 328 | [Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/) | Linked List | Time: O(n), Space: O(1) | Medium |
| 329 | [Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | DFS, Topological Sort | Time: O(m * n), Space: O(m * n) | Hard |
| 330 | [Patching Array](https://leetcode.com/problems/patching-array/) | Greedy | Time: O(log n), Space: O(1) | Hard |
| 331 | [Verify Preorder Serialization of a Binary Tree](https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/) | Stack | Time: O(n), Space: O(n) | Medium |
| 332 | [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) | Graph, DFS | Time: O(E log E), Space: O(E) | Medium |
| 333 | [Largest BST Subtree](https://leetcode.com/problems/largest-bst-subtree/) | Tree, DFS | Time: O(n), Space: O(h) | Medium |
| 334 | [Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/) | Greedy, Dynamic Programming | Time: O(n), Space: O(1) | Medium |
| 335 | [Self Crossing](https://leetcode.com/problems/self-crossing/) | Geometry | Time: O(n), Space: O(1) | Hard |
| 336 | [Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/) | Trie, Hash Map | Time: O(n^2), Space: O(n) | Hard |
| 337 | [House Robber III](https://leetcode.com/problems/house-robber-iii/) | Tree, Dynamic Programming | Time: O(n), Space: O(h) | Medium |
| 338 | [Counting Bits](https://leetcode.com/problems/counting-bits/) | Dynamic Programming | Time: O(n), Space: O(n) | Medium |
| 339 | [Nested List Weight Sum](https://leetcode.com/problems/nested-list-weight-sum/) | DFS, Recursion | Time: O(n), Space: O(h) | Easy |
| 340 | [Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/) | Sliding Window | Time: O(n), Space: O(k) | Medium |
| 341 | [Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/) | Stack, Recursion | Time: O(n), Space: O(n) | Medium |
| 342 | [Power of Four](https://leetcode.com/problems/power-of-four/) | Math | Time: O(1), Space: O(1) | Easy |
| 343 | [Integer Break](https://leetcode.com/problems/integer-break/) | Dynamic Programming | Time: O(n), Space: O(n) | Medium |
| 344 | [Reverse String](https://leetcode.com/problems/reverse-string/) | Two Pointers | Time: O(n), Space: O(1) | Easy |
| 345 | [Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/) | Two Pointers | Time: O(n), Space: O(1) | Easy |
| 346 | [Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream/) | Queue | Time: O(1), Space: O(n) | Easy |
| 347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Heap, Hash Map | Time: O(n log k), Space: O(n) | Medium |
| 348 | [Design Tic-Tac-Toe](https://leetcode.com/problems/design-tic-tac-toe/) | Array | Time: O(1), Space: O(1) | Medium |
| 349 | [Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/) | Hash Set | Time: O(n), Space: O(n) | Easy |
| 350 | [Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/) | Hash Map | Time: O(n), Space: O(n) | Easy |
| 351 | [Android Unlock Patterns](https://leetcode.com/problems/android-unlock-patterns/) | Backtracking | Time: O(n), Space: O(1) | Medium |
| 352 | [Data Stream as Disjoint Intervals](https://leetcode.com/problems/data-stream-as-disjoint-intervals/) | TreeMap | Time: O(log n), Space: O(n) | Hard |
| 353 | [Design Snake Game](https://leetcode.com/problems/design-snake-game/) | Queue | Time: O(1), Space: O(n) | Medium |
| 354 | [Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/) | Sorting, Binary Search | Time: O(n log n), Space: O(n) | Hard |
| 355 | [Design Twitter](https://leetcode.com/problems/design-twitter/) | Hash Map, Linked List | Time: O(1), Space: O(n) | Medium |
| 356 | [Line Reflection](https://leetcode.com/problems/line-reflection/) | Hash Set | Time: O(n), Space: O(n) | Medium |
| 357 | [Count Numbers with Unique Digits](https://leetcode.com/problems/count-numbers-with-unique-digits/) | Math | Time: O(n), Space: O(1) | Medium |
| 358 | [Rearrange String k Distance Apart](https://leetcode.com/problems/rearrange-string-k-distance-apart/) | Greedy, Heap | Time: O(n log k), Space: O(n) | Hard |
| 359 | [Logger Rate Limiter](https://leetcode.com/problems/logger-rate-limiter/) | Hash Map | Time: O(1), Space: O(n) | Easy |
| 360 | [Sort Transformed Array](https://leetcode.com/problems/sort-transformed-array/) | Sorting | Time: O(n log n), Space: O(n) | Medium |
| 361 | [Bomb Enemy](https://leetcode.com/problems/bomb-enemy/) | Grid, DFS | Time: O(m * n), Space: O(m * n) | Medium |
| 362 | [📓 Design Hit Counter](../leetcode/1204.ipynb) | <span title="Fixed 300 slots indexed by timestamp % 300; overwrite stale slots on hit() and sum valid slots on getHits().">Circular Buffer</span>| Time: O(1), Space: O(n) | Medium |
| 363 | [Max Sum of Rectangle No Larger Than K](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/) | Segment Tree, Binary Search | Time: O(n^2 log n), Space: O(n) | Hard |
| 364 | [Nested List Weight Sum II](https://leetcode.com/problems/nested-list-weight-sum-ii/) | DFS, Recursion | Time: O(n), Space: O(h) | Medium |
| 365 | [Water and Jug Problem](https://leetcode.com/problems/water-and-jug-problem/) | Math, BFS | Time: O(max(a, b)), Space: O(max(a, b)) | Medium |
| 366 | [Find Leaves of Binary Tree](https://leetcode.com/problems/find-leaves-of-binary-tree/) | Tree, DFS | Time: O(n), Space: O(h) | Medium |
| 367 | [📓 Valid Perfect Square](../leetcode/0367.ipynb) | <span title="Halve the search space each step by comparing the midpoint to a monotone predicate.">Binary Search</span> | Time: $O(\log n)$, Space: $O(1)$ | Easy |
| 368 | [Largest Divisible Subset](https://leetcode.com/problems/largest-divisible-subset/) | Dynamic Programming | Time: O(n^2), Space: O(n) | Medium |
| 369 | [Plus One Linked List](https://leetcode.com/problems/plus-one-linked-list/) | Linked List | Time: O(n), Space: O(1) | Medium |
| 370 | [Range Addition](https://leetcode.com/problems/range-addition/) | Difference Array | Time: O(n), Space: O(n) | Medium |
| 371 | [📓 Sum of Two Integers](../leetcode/0371.ipynb) | <span title="Simulate addition with XOR for the sum bits and AND+shift for the carry; repeat until carry is zero.">Bit Manipulation (carry simulation)</span> | Time: O(1), Space: O(1) | Easy |
| 372 | [Super Pow](https://leetcode.com/problems/super-pow/) | Divide and Conquer | Time: O(log k), Space: O(1) | Medium |
| 373 | [Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) | Min-Heap | Time: O(k log k), Space: O(k) | Medium |
| 374 | [📓 Guess Number Higher or Lower](../leetcode/0374.ipynb) | <span title="Halve the search space each step by comparing the midpoint to a monotone predicate.">Binary Search</span> | Time: $O(\log n)$, Space: $O(1)$ | Easy |
| 375 | [Guess Number Higher or Lower II](https://leetcode.com/problems/guess-number-higher-or-lower-ii/) | Dynamic Programming | Time: O(n^2), Space: O(n^2) | Medium |
| 376 | [Wiggle Subsequence](https://leetcode.com/problems/wiggle-subsequence/) | Dynamic Programming | Time: O(n), Space: O(n) | Medium |
| 377 | [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/) | Dynamic Programming | Time: O(n * target), Space: O(target) | Medium |
| 378 | [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | Heap | Time: O(k log n), Space: O(n) | Medium |
| 379 | [Design Phone Directory](https://leetcode.com/problems/design-phone-directory/) | Linked List | Time: O(1), Space: O(n) | Medium |
| 380 | [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) | Hash Map, Array | Time: O(1), Space: O(n) | Medium |
| 381 | [Insert Delete GetRandom O(1) - Duplicates allowed](https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/) | Hash Map, Array | Time: O(1), Space: O(n) | Hard |
| 382 | [Linked List Random Node](https://leetcode.com/problems/linked-list-random-node/) | Reservoir Sampling | Time: O(n), Space: O(1) | Medium |
| 383 | [Ransom Note](https://leetcode.com/problems/ransom-note/) | Hash Map | Time: O(n), Space: O(n) | Easy |
| 384 | [Shuffle an Array](https://leetcode.com/problems/shuffle-an-array/) | Random, Array | Time: O(n), Space: O(n) | Medium |
| 385 | [Mini Parser](https://leetcode.com/problems/mini-parser/) | Stack | Time: O(n), Space: O(n) | Medium |
| 386 | [Lexicographical Numbers](https://leetcode.com/problems/lexicographical-numbers/) | DFS | Time: O(n), Space: O(1) | Medium |
| 387 | [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) | Hash Map | Time: O(n), Space: O(n) | Easy |
| 388 | [Longest Absolute File Path](https://leetcode.com/problems/longest-absolute-file-path/) | Stack | Time: O(n), Space: O(n) | Medium |
| 389 | [Find the Difference](https://leetcode.com/problems/find-the-difference/) | Hash Map | Time: O(n), Space: O(n) | Easy |
| 390 | [Elimination Game](https://leetcode.com/problems/elimination-game/) | Math | Time: O(n), Space: O(1) | Medium |
| 391 | [Perfect Rectangle](https://leetcode.com/problems/perfect-rectangle/) | Sweep Line | Time: O(n log n), Space: O(n) | Hard |
| 392 | [Is Subsequence](https://leetcode.com/problems/is-subsequence/) | Two Pointers | Time: O(n), Space: O(1) | Easy |
| 393 | [📓 UTF-8 Validation](../leetcode/0393.ipynb) | <span title="Use bitmasks (0x80, 0xC0, 0xE0, 0xF0, 0xF8) to classify each byte; track expected continuations.">Bit-Masking In-Place</span> | Time: O(n), Space: O(1) | Medium |
| 394 | [Decode String](https://leetcode.com/problems/decode-string/) | Stack | Time: O(n), Space: O(n) | Medium |
| 395 | [Longest Substring with At Least K Repeating Characters](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/) | Divide and Conquer | Time: O(n log n), Space: O(n) | Medium |
| 396 | [Rotate Function](https://leetcode.com/problems/rotate-function/) | Math | Time: O(n), Space: O(1) | Medium |
| 397 | [Integer Replacement](https://leetcode.com/problems/integer-replacement/) | Greedy | Time: O(log n), Space: O(1) | Medium |
| 398 | [Random Pick Index](https://leetcode.com/problems/random-pick-index/) | Reservoir Sampling | Time: O(1), Space: O(n) | Medium |
| 399 | [Evaluate Division](https://leetcode.com/problems/evaluate-division/) | Graph, DFS | Time: O(E), Space: O(V) | Medium |
| 400 | [Nth Digit](https://leetcode.com/problems/nth-digit/) | Math | Time: O(log n), Space: O(1) | Easy |
| 401 | [📓 Binary Watch](../leetcode/0401.ipynb) | <span title="Enumerate all 720 valid watch times; filter by total set bits equaling the given number.">Bit Manipulation (enumerate all times)</span> | Time: O(1), Space: O(1) | Easy |
| 402 | [Remove K Digits](https://leetcode.com/problems/remove-k-digits/) | Stack | Time: O(n), Space: O(n) | Medium |
| 403 | [Frog Jump](https://leetcode.com/problems/frog-jump/) | Dynamic Programming | Time: O(n^2), Space: O(n) | Hard |
| 404 | [Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves/) | Tree | Time: O(n), Space: O(h) | Easy |
| 405 | [Convert a Number to Hexadecimal](https://leetcode.com/problems/convert-a-number-to-hexadecimal/) | Math | Time: O(1), Space: O(1) | Easy |
| 406 | [Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/) | Greedy | Time: O(n^2), Space: O(n) | Medium |
| 407 | [Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/) | Min-Heap, BFS | Time: O(n * m * log(n * m)), Space: O(n * m) | Hard |
| 408 | [Valid Word Abbreviation](https://leetcode.com/problems/valid-word-abbreviation/) | String | Time: O(n), Space: O(1) | Easy |
| 409 | [Longest Palindrome](https://leetcode.com/problems/longest-palindrome/) | Hash Map | Time: O(n), Space: O(n) | Easy |
| 410 | [📓 Split Array Largest Sum](../leetcode/0410.ipynb) | <span title="Binary search for the insert position within a DP transition (e.g., patience sorting for LIS).">Binary Search, Dynamic Programming</span> | Time: O(n log m), Space: O(n) | Hard |
| 411 | [Minimum Unique Word Abbreviation](https://leetcode.com/problems/minimum-unique-word-abbreviation/) | Greedy | Time: O(n^2), Space: O(n) | Hard |
| 412 | [Fizz Buzz](https://leetcode.com/problems/fizz-buzz/) | Math | Time: O(n), Space: O(1) | Easy |
| 413 | [Arithmetic Slices](https://leetcode.com/problems/arithmetic-slices/) | Dynamic Programming | Time: O(n), Space: O(1) | Medium |
| 414 | [Third Maximum Number](https://leetcode.com/problems/third-maximum-number/) | Sorting | Time: O(n log n), Space: O(1) | Easy |
| 415 | [Add Strings](https://leetcode.com/problems/add-strings/) | String | Time: O(n), Space: O(1) | Easy |
| 416 | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | Dynamic Programming | Time: O(n * sum), Space: O(sum) | Medium |
| 417 | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | DFS | Time: O(m * n), Space: O(m * n) | Medium |
| 418 | [Sentence Screen Fitting](https://leetcode.com/problems/sentence-screen-fitting/) | Dynamic Programming | Time: O(n * m), Space: O(1) | Hard |
| 419 | [Battleships in a Board](https://leetcode.com/problems/battleships-in-a-board/) | Array | Time: O(m * n), Space: O(1) | Medium |
| 420 | [Strong Password Checker](https://leetcode.com/problems/strong-password-checker/) | Greedy | Time: O(n), Space: O(1) | Hard |
| 421 | [Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) | Trie | Time: O(n), Space: O(n) | Medium |
| 422 | [Valid Word Square](https://leetcode.com/problems/valid-word-square/) | Matrix | Time: O(n^2), Space: O(1) | Easy |
| 423 | [Reconstruct Original Digits from English](https://leetcode.com/problems/reconstruct-original-digits-from-english/) | Hash Map | Time: O(n), Space: O(1) | Medium |
| 424 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Sliding Window | Time: O(n), Space: O(1) | Medium |
| 425 | [Word Squares](https://leetcode.com/problems/word-squares/) | Backtracking | Time: O(n^4), Space: O(n^2) | Hard |
| 426 | [Convert Binary Search Tree to Sorted Doubly Linked List](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/) | Tree, In-order Traversal | Time: O(n), Space: O(h) | Medium |
| 427 | [Construct Quad Tree](https://leetcode.com/problems/construct-quad-tree/) | Divide and Conquer, Recursion | Time: O(n), Space: O(n) | Medium |
| 428 | [Serialize and Deserialize N-ary Tree](https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/) | Tree, BFS/DFS | Time: O(n), Space: O(n) | Medium |
| 429 | [📓 N-ary Tree Level Order Traversal](../leetcode/0429.ipynb) | <span title="Breadth-first search with a queue; visit all neighbors level by level.">BFS (Queue)</span> | Time: $O(n)$, Space: $O(n)$ | Easy |
| 430 | [Flatten a Multilevel Doubly Linked List](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/) | Linked List | Time: O(n), Space: O(1) | Medium |
| 431 | [Encode N-ary Tree to Binary Tree](https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/) | Tree | Time: O(n), Space: O(n) | Medium |
| 432 | [All O`one Data Structure](https://leetcode.com/problems/all-oone-data-structure/) | Doubly Linked List, Hash Map | Time: O(1), Space: O(n) | Hard |
| 433 | [📓 Minimum Genetic Mutation](../leetcode/0433.ipynb) | <span title="Breadth-first search with a queue; visit all neighbors level by level.">BFS (Queue)</span> | Time: $O(N^2 \cdot L)$, Space: $O(N)$ | Medium |
| 434 | [Number of Segments in a String](https://leetcode.com/problems/number-of-segments-in-a-string/) | String | Time: O(n), Space: O(1) | Easy |
| 435 | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | Greedy | Time: O(n log n), Space: O(1) | Medium |
| 436 | [📓 Find Right Interval](../leetcode/0436.ipynb) | <span title="Sort interval start points; for each query end, binary search for the smallest start ≥ end.">Binary Search on Sorted Starts</span> | Time: O(n log n), Space: O(n) | Medium |
| 437 | [Path Sum III](https://leetcode.com/problems/path-sum-iii/) | Tree, DFS | Time: O(n), Space: O(h) | Medium |
| 438 | [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | Sliding Window | Time: O(n), Space: O(1) | Medium |
| 439 | [Ternary Expression Parser](https://leetcode.com/problems/ternary-expression-parser/) | Stack | Time: O(n), Space: O(n) | Medium |
| 440 | [K-th Smallest in Lexicographical Order](https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/) | Backtracking | Time: O(n), Space: O(1) | Hard |
| 441 | [📓 Arranging Coins](../leetcode/0441.ipynb) | <span title="Halve the search space each step by comparing the midpoint to a monotone predicate.">Binary Search</span> | Time: $O(\log n)$, Space: $O(1)$ | Easy |
| 442 | [Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/) | Array, Hash Set | Time: O(n), Space: O(n) | Medium |
| 443 | [String Compression](https://leetcode.com/problems/string-compression/) | Array | Time: O(n), Space: O(1) | Medium |
| 444 | [Sequence Reconstruction](https://leetcode.com/problems/sequence-reconstruction/) | Topological Sort | Time: O(n), Space: O(n) | Medium |
| 445 | [Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/) | Linked List, Stack | Time: O(max(m, n)), Space: O(max(m, n)) | Medium |
| 446 | [Arithmetic Slices II - Subsequence](https://leetcode.com/problems/arithmetic-slices-ii-subsequence/) | Dynamic Programming | Time: O(n^2), Space: O(n^2) | Hard |
| 447 | [Number of Boomerangs](https://leetcode.com/problems/number-of-boomerangs/) | Hash Map | Time: O(n^2), Space: O(n) | Easy |
| 448 | [📓 Find All Numbers Disappeared in an Array](../leetcode/0448.ipynb) | <span title="Negate arr[|val|-1] to mark |val| as seen; positive indices signal missing values.">In-place Negation</span> | Time: O(n), Space: O(1) | Easy |
| 449 | [Serialize and Deserialize BST](https://leetcode.com/problems/serialize-and-deserialize-bst/) | Tree, BFS/DFS | Time: O(n), Space: O(n) | Medium |
| 450 | [Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/) | Tree | Time: O(h), Space: O(h) | Medium |
| 451 | [Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/) | Hash Map, Heap | Time: O(n log n), Space: O(n) | Medium |
| 452 | [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | Greedy, Sorting | Time: O(n log n), Space: O(1) | Medium |
| 453 | [Minimum Moves to Equal Array Elements](https://leetcode.com/problems/minimum-moves-to-equal-array-elements/) | Math | Time: O(n), Space: O(1) | Easy |
| 454 | [4Sum II](https://leetcode.com/problems/4sum-ii/) | Hash Map | Time: O(n^2), Space: O(n^2) | Medium |
| 455 | [Assign Cookies](https://leetcode.com/problems/assign-cookies/) | Greedy | Time: O(n log n), Space: O(1) | Easy |
| 456 | [132 Pattern](https://leetcode.com/problems/132-pattern/) | Stack | Time: O(n), Space: O(n) | Medium |
| 457 | [Circular Array Loop](https://leetcode.com/problems/circular-array-loop/) | Floyd's Cycle Detection | Time: O(n), Space: O(1) | Medium |
| 458 | [Poor Pigs](https://leetcode.com/problems/poor-pigs/) | Math | Time: O(1), Space: O(1) | Hard |
| 459 | [Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/) | String | Time: O(n), Space: O(1) | Easy |
| 460 | [LFU Cache](https://leetcode.com/problems/lfu-cache/) | Hash Map, Double Linked List | Time: O(1), Space: O(n) | Hard |
| 461 | [📓 Hamming Distance](../leetcode/0461.ipynb) | <span title="XOR two numbers to isolate differing bits, then count set bits (popcount) for Hamming distance.">XOR + Popcount</span> | Time: O(1), Space: O(1) | Easy |
| 462 | [Minimum Moves to Equal Array Elements II](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/) | Math | Time: O(n), Space: O(1) | Medium |
| 463 | [📓 Island Perimeter](../leetcode/0463.ipynb) | <span title="Count each edge once (shared between adjacent cells) in a single grid scan.">Single Pass (Count + Shared Edges)</span> | Time: O(m·n), Space: O(1) | Easy |
| 464 | [Can I Win](https://leetcode.com/problems/can-i-win/) | Dynamic Programming | Time: O(2^n), Space: O(2^n) | Medium |
| 465 | [Optimal Account Balancing](https://leetcode.com/problems/optimal-account-balancing/) | DFS, Backtracking | Time: O(2^n), Space: O(n) | Hard |
| 466 | [Count The Repetitions](https://leetcode.com/problems/count-the-repetitions/) | Dynamic Programming | Time: O(n^2), Space: O(n) | Hard |
| 467 | [Unique Substrings in Wraparound String](https://leetcode.com/problems/unique-substrings-in-wraparound-string/) | String, Dynamic Programming | Time: O(n), Space: O(1) | Medium |
| 468 | [Validate IP Address](https://leetcode.com/problems/validate-ip-address/) | String | Time: O(1), Space: O(1) | Medium |
| 469 | [Convex Polygon](https://leetcode.com/problems/convex-polygon/) | Geometry | Time: O(n), Space: O(1) | Medium |
| 470 | [Implement Rand10() Using Rand7()](https://leetcode.com/problems/implement-rand10-using-rand7/) | Random, Math | Time: O(1), Space: O(1) | Medium |
| 471 | [Encode String with Shortest Length](https://leetcode.com/problems/encode-string-with-shortest-length/) | Dynamic Programming | Time: O(n^3), Space: O(n^2) | Hard |
| 472 | [Concatenated Words](https://leetcode.com/problems/concatenated-words/) | Trie, Hash Set | Time: O(n * m^2), Space: O(n * m) | Hard |
| 473 | [Matchsticks to Square](https://leetcode.com/problems/matchsticks-to-square/) | Backtracking, Dynamic Programming | Time: O(4^n), Space: O(n) | Medium |
| 474 | [Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/) | Dynamic Programming | Time: O(m * n * max), Space: O(m * n * max) | Medium |
| 475 | [📓 Heaters](../leetcode/0475.ipynb) | <span title="Halve the search space each step by comparing the midpoint to a monotone predicate.">Binary Search</span> | Time: $O(n \log n)$, Space: $O(1)$ | Easy |
| 476 | [📓 Number Complement](../leetcode/0476.ipynb) | <span title="Build a mask of all 1s up to the highest set bit, then XOR with it to flip those bits.">Bit Mask Flip</span> | Time: O(log n), Space: O(1) | Easy |
| 477 | [📓 Total Hamming Distance](../leetcode/0477.ipynb) | <span title="For each bit, count 1-bits (k); contribution is k*(n-k) since 1s pair with 0s across all numbers.">Per-Bit Population Count</span> | Time: O(n), Space: O(1) | Medium |
| 478 | [Generate Random Point in a Circle](https://leetcode.com/problems/generate-random-point-in-a-circle/) | Geometry, Math | Time: O(1), Space: O(1) | Medium |
| 479 | [Largest Palindrome Product](https://leetcode.com/problems/largest-palindrome-product/) | Math | Time: O(n^2), Space: O(1) | Hard |
| 480 | [Sliding Window Median](https://leetcode.com/problems/sliding-window-median/) | Heap | Time: O(n log k), Space: O(k) | Hard |
| 481 | [Magical String](https://leetcode.com/problems/magical-string/) | Math | Time: O(n), Space: O(n) | Easy |
| 482 | [License Key Formatting](https://leetcode.com/problems/license-key-formatting/) | String | Time: O(n), Space: O(1) | Easy |
| 483 | [Smallest Good Base](https://leetcode.com/problems/smallest-good-base/) | Math | Time: O(log n), Space: O(1) | Hard |
| 484 | [Find Permutation](https://leetcode.com/problems/find-permutation/) | Greedy | Time: O(n), Space: O(1) | Medium |
| 485 | [📓 Max Consecutive Ones](../leetcode/0485.ipynb) | <span title="Process each element exactly once; maintain running state to build the result.">Single Pass</span> | Time: O(n), Space: O(1) | Easy |
| 486 | [Predict the Winner](https://leetcode.com/problems/predict-the-winner/) | Dynamic Programming | Time: O(n^2), Space: O(n^2) | Medium |
| 487 | [Max Consecutive Ones II](https://leetcode.com/problems/max-consecutive-ones-ii/) | Sliding Window | Time: O(n), Space: O(1) | Medium |
| 488 | [Zuma Game](https://leetcode.com/problems/zuma-game/) | Backtracking | Time: O(n!), Space: O(n) | Hard |
| 489 | [Robot Room Cleaner](https://leetcode.com/problems/robot-room-cleaner/) | Backtracking | Time: O(4^n), Space: O(n) | Hard |
| 490 | [The Maze](https://leetcode.com/problems/the-maze/) | BFS, DFS | Time: O(m * n), Space: O(m * n) | Medium |
| 491 | [Increasing Subsequences](https://leetcode.com/problems/increasing-subsequences/) | Backtracking | Time: O(2^n), Space: O(n) | Medium |
| 492 | [Construct the Rectangle](https://leetcode.com/problems/construct-the-rectangle/) | Math | Time: O(sqrt(n)), Space: O(1) | Easy |
| 493 | [📓 Reverse Pairs](../leetcode/0493.ipynb) | <span title="Fenwick tree: update index i with i += i & -i; prefix-query with i -= i & -i. O(log n) per op.">Binary Indexed Tree</span> | Time: $O(n \log n)$, Space: $O(n)$ | Hard |
| 494 | [Target Sum](https://leetcode.com/problems/target-sum/) | Dynamic Programming | Time: O(n * sum), Space: O(n * sum) | Medium |
| 495 | [Teemo Attacking](https://leetcode.com/problems/teemo-attacking/) | Sliding Window | Time: O(n), Space: O(1) | Easy |
| 496 | [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) | Stack | Time: O(n), Space: O(n) | Easy |
| 497 | [Random Point in Non-overlapping Rectangles](https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/) | Random | Time: O(1), Space: O(n) | Medium |
| 498 | [Diagonal Traverse](https://leetcode.com/problems/diagonal-traverse/) | Array | Time: O(m * n), Space: O(1) | Medium |
| 499 | [The Maze III](https://leetcode.com/problems/the-maze-iii/) | BFS | Time: O(m * n), Space: O(m * n) | Hard |
| 500 | [Keyboard Row](https://leetcode.com/problems/keyboard-row/) | String | Time: O(n), Space: O(1) | Easy |
| 501 |[Find Mode in Binary Search Tree](https://leetcode.com/problems/find-mode-in-binary-search-tree/)|Tree,Depth-First Search|O(N) Time,O(H) Space|Easy|
| 502 |[IPO](https://leetcode.com/problems/ipo/)|Heap,Greedy|O(N log N) Time|Hard|
| 503 |[Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/)|Stack|O(N) Time, O(N) Space|Medium|
| 504 |[Base 7](https://leetcode.com/problems/base-7/)|Math|O(log N) Time|Easy|
| 505 |[The Maze II](https://leetcode.com/problems/the-maze-ii/)|Breadth-First Search|O(MN) Time, O(MN) Space|Medium|
| 506 |[Relative Ranks](https://leetcode.com/problems/relative-ranks/)|Sorting|O(N log N) Time|Easy|
| 507 |[Perfect Number](https://leetcode.com/problems/perfect-number/)|Math|O(√N) Time|Easy|
| 508 |[Most Frequent Subtree Sum](https://leetcode.com/problems/most-frequent-subtree-sum/)|Tree,HashMap|O(N) Time, O(N) Space|Medium|
| 509 |[Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)|Recursion,Dynamic Programming|O(N) Time, O(1) Space|Easy|
| 510 | [📓 Inorder Successor in BST II](../leetcode/0510.ipynb) | <span title="Use BST ordering property to search, insert, or traverse in O(h) time.">Binary Search Tree (BST)</span> | Time: O(h), Space: O(1) | Medium |
| 511 | [Game Play Analysis I](https://leetcode.com/problems/game-play-analysis-i/) | Hash Map| Time: O(n), Space: O(n) | Easy |
| 512 | [Game Play Analysis II](https://leetcode.com/problems/game-play-analysis-ii/) | Hash Map| Time: O(n), Space: O(n) | Easy |
| 513 | [📓 Find Bottom Left Tree Value](../leetcode/0513.ipynb) | <span title="Queue-based BFS; collect all nodes at each depth before advancing to the next level.">BFS Level Order</span> | Time: O(n), Space: O(n) | Medium |
| 514 | [Freedom Trail](https://leetcode.com/problems/freedom-trail/)| Dynamic Programming, Binary Search | Time: O(m * n), Space: O(m * n) | Hard |
| 515 | [📓 Find Largest Value in Each Tree Row](../leetcode/0515.ipynb) | <span title="Queue-based BFS; collect all nodes at each depth before advancing to the next level.">BFS Level Order</span> | Time: O(n), Space: O(n) | Medium |
| 516 | [Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/) | Dynamic Programming | Time: O(n^2), Space: O(n^2) | Medium |
| 517 | [Super Washing Machines](https://leetcode.com/problems/super-washing-machines/) | Dynamic Programming | Time: O(n^2), Space: O(n) | Hard |
| 518 | [Coin Change 2](https://leetcode.com/problems/coin-change-2/)| Dynamic Programming | Time: O(n * amount), Space: O(n * amount) | Medium |
| 519 | [📓 Random Flip Matrix](../leetcode/0519.ipynb) | <span title="Use BST ordering property to search, insert, or traverse in O(h) time.">Binary Search Tree (BST)</span> | Time: O(log n), Space: O(n) | Medium |
| 520 | [Detect Capital](https://leetcode.com/problems/detect-capital/)| String| Time: O(n), Space: O(1) | Easy |
| 521 | [Longest Uncommon Subsequence I](https://leetcode.com/problems/longest-uncommon-subsequence-i/) | String| Time: O(n), Space: O(1) | Easy |
| 522 | [Longest Uncommon Subsequence II](https://leetcode.com/problems/longest-uncommon-subsequence-ii/) | String| Time: O(n^2), Space: O(n^2) | Medium |
| 523 | [Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/) | Array, Hash Map | Time: O(n), Space: O(n) | Medium |
| 524 | [Longest Word in Dictionary through Deleting](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/) | Dynamic Programming | Time: O(n * m), Space: O(n * m) | Medium |
| 525 | [Contiguous Array](https://leetcode.com/problems/contiguous-array/) | Hash Map| Time: O(n), Space: O(n) | Medium |
| 526 | [Beautiful Arrangement](https://leetcode.com/problems/beautiful-arrangement/) | Backtracking, Dynamic Programming| Time: O(n!), Space: O(n) | Medium |
| 527 | [Word Abbreviation](https://leetcode.com/problems/word-abbreviation/) | String| Time: O(n), Space: O(n) | Hard |
| 528 | [📓 Random Pick with Weight](../leetcode/0528.ipynb) | <span title="Use BST ordering property to search, insert, or traverse in O(h) time.">Binary Search Tree (BST)</span> | Time: O(log n), Space: O(n) | Medium |
| 529 | [Minesweeper](https://leetcode.com/problems/minesweeper/)| Array, Depth-First Search (DFS)| Time: O(n), Space: O(n) | Medium |
| 530 | [📓 Minimum Absolute Difference in BST](../leetcode/0530.ipynb) | <span title="Use BST ordering property to search, insert, or traverse in O(h) time.">Binary Search Tree (BST)</span> | Time: O(n), Space: O(h) | Medium |
| 531 | [Lonely Pixel I](https://leetcode.com/problems/lonely-pixel-i/)| Array, Hash Map | Time: O(m * n), Space: O(m + n) | Medium |
| 532 | [K-diff Pairs in an Array](https://leetcode.com/problems/k-diff-pairs-in-an-array/) | Array, Hash Map | Time: O(n), Space: O(n) | Medium |
| 533 | [Lonely Pixel II](https://leetcode.com/problems/lonely-pixel-ii/)| Array, Hash Map | Time: O(m * n), Space: O(m + n) | Medium |
| 534 | [Game Play Analysis III](https://leetcode.com/problems/game-play-analysis-iii/) | Hash Map| Time: O(n), Space: O(n) | Easy |
| 535 | [Encode and Decode TinyURL](https://leetcode.com/problems/encode-and-decode-tinyurl/) | Hash Map| Time: O(1), Space: O(n) | Medium |
| 536 | [📓 Construct Binary Tree from String](../leetcode/0536.ipynb) | <span title="Recursively parse a string into a tree by tracking an index through the input character by character.">Recursive Parsing</span> | Time: O(n), Space: O(n) | Medium |
| 537 | [Complex Number Multiplication](https://leetcode.com/problems/complex-number-multiplication/) | String| Time: O(1), Space: O(1) | Medium |
| 538 | [📓 Convert BST to Greater Tree](../leetcode/0538.ipynb) | <span title="Use BST ordering property to search, insert, or traverse in O(h) time.">Binary Search Tree (BST)</span> | Time: O(n), Space: O(h) | Easy |
| 539 | [Minimum Time Difference](https://leetcode.com/problems/minimum-time-difference/) | Array, Hash Map | Time: O(n), Space: O(n) | Medium |
| 540 | [📓 Single Element in a Sorted Array](../leetcode/0540.ipynb) | <span title="Before the lone element, each pair starts at an even index; use that parity invariant to binary search.">Binary Search on Parity</span> | Time: O(log n), Space: O(1) | Medium |
| 541 | [Reverse String II](https://leetcode.com/problems/reverse-string-ii/) | String| Time: O(n), Space: O(n) | Easy |
| 542 | [01 Matrix](https://leetcode.com/problems/01-matrix/)| Dynamic Programming, BFS| Time: O(m * n), Space: O(m * n) | Medium |
| 543 | [📓 Diameter of Binary Tree](../leetcode/0543.ipynb) | <span title="Recursive DFS over a binary tree; return values up the call stack to accumulate the answer.">Binary Tree</span> | Time: O(n), Space: O(h) | Easy |
| 544 | [Output Contest Matches](https://leetcode.com/problems/output-contest-matches/) | String| Time: O(n log n), Space: O(n) | Medium |
| 545 | [📓 Boundary of Binary Tree](../leetcode/0545.ipynb) | <span title="Three separate DFS passes: left boundary top-down, all leaves, right boundary bottom-up.">DFS Three-pass Boundary</span> | Time: O(n), Space: O(h) | Medium |
| 546 | [Remove Boxes](https://leetcode.com/problems/remove-boxes/)| Dynamic Programming | Time: O(n^3), Space: O(n^3) | Hard |
| 547 | [Friend Circles](https://leetcode.com/problems/friend-circles/)| Depth-First Search (DFS), Union-Find | Time: O(n^2), Space: O(n) | Medium |
| 548 | [Split Array with Equal Sum](https://leetcode.com/problems/split-array-with-equal-sum/) | Dynamic Programming, Prefix Sum| Time: O(n^2), Space: O(n) | Hard |
| 549 | [📓 Binary Tree Longest Consecutive Sequence II](../leetcode/0549.ipynb) | <span title="Visit left, right, then root; aggregate subtree results on the way back up.">DFS Post-order</span> | Time: O(n), Space: O(h) | Medium |
| 550 | [Game Play Analysis IV](https://leetcode.com/problems/game-play-analysis-iv/) | Hash Map| Time: O(n), Space: O(n) | Easy |
| 551 | [Student Attendance Record I](https://leetcode.com/problems/student-attendance-record-i/) | String| Time: O(n), Space: O(1) | Easy |
| 552 | [Student Attendance Record II](https://leetcode.com/problems/student-attendance-record-ii/) | Dynamic Programming | Time: O(n), Space: O(n) | Hard |
| 553 | [Optimal Division](https://leetcode.com/problems/optimal-division/) | Math| Time: O(n), Space: O(n) | Medium |
| 554 | [Brick Wall](https://leetcode.com/problems/brick-wall/)| Hash Map| Time: O(n), Space: O(n) | Medium |
| 555 | [Split Concatenated Strings](https://leetcode.com/problems/split-concatenated-strings/) | String| Time: O(n), Space: O(n) | Hard |
| 556 | [Next Greater Element III](https://leetcode.com/problems/next-greater-element-iii/) | Array | Time: O(n), Space: O(n) | Medium |
| 557 | [Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/) | String| Time: O(n), Space: O(n) | Easy |
| 558 | [Quadrangle Area](https://leetcode.com/problems/quadrangle-area/) | Math| Time: O(1), Space: O(1) | Medium |
| 559 | [Maximum Depth of N-ary Tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/) | Tree (DFS)| Time: O(n), Space: O(n) | Easy |
| 560 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | Array, Hash Map | Time: O(n), Space: O(n) | Medium |
| 561 | [Array Partition I](https://leetcode.com/problems/array-partition-i/) | Array | Time: O(n log n), Space: O(1) | Easy |
| 562 | [Longest Line of Consecutive One in Matrix](https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/) | Matrix| Time: O(m * n), Space: O(1) | Medium |
| 563 | [📓 Binary Tree Tilt](../leetcode/0563.ipynb) | <span title="Pre/in/post-order recursive traversal; propagate depth, sums, or lengths up from leaves.">Binary Tree (DFS)</span> | Time: O(n), Space: O(h) | Easy |
| 564 | [Find the Closest Palindrome](https://leetcode.com/problems/find-the-closest-palindrome/) | Math| Time: O(n), Space: O(1) | Hard |
| 565 | [Array Nesting](https://leetcode.com/problems/array-nesting/)| Array | Time: O(n), Space: O(n) | Medium |
| 566 | [Reshape the Matrix](https://leetcode.com/problems/reshape-the-matrix/) | Matrix| Time: O(m * n), Space: O(m * n) | Easy |
| 567 | [Permutation in String](https://leetcode.com/problems/permutation-in-string/) | Array, Hash Map | Time: O(n), Space: O(n) | Medium |
| 568 | [Maximum Vacation Days](https://leetcode.com/problems/maximum-vacation-days/) | Dynamic Programming | Time: O(n^2), Space: O(n^2) | Hard |
| 569 | [Median Employee Salary](https://leetcode.com/problems/median-employee-salary/) | Array, Heap | Time: O(n log n), Space: O(n) | Medium |
| 570 | [Managers with at Least 5 Direct Reports](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/) | SQL | Time: O(n), Space: O(1) | Easy |
| 571 | [Find Median Given Frequency of Numbers](https://leetcode.com/problems/find-median-given-frequency-of-numbers/) | Heap, Sorting | Time: O(n log n), Space: O(n) | Medium |
| 572 | [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) | Tree, DFS| Time: O(n), Space: O(h) | Easy |
| 573 | [Squirrel Simulation](https://leetcode.com/problems/squirrel-simulation/) | Array, Dynamic Programming | Time: O(n), Space: O(n) | Hard |
| 574 | [Winning Candidate](https://leetcode.com/problems/winning-candidate/) | Hash Map| Time: O(n), Space: O(n) | Easy |
| 575 | [Distribute Candies](https://leetcode.com/problems/distribute-candies/) | Hash Set| Time: O(n), Space: O(n) | Easy |
| 576 | [Out of Boundary Paths](https://leetcode.com/problems/out-of-boundary-paths/) | Dynamic Programming, DFS| Time: O(m * n * maxMove), Space: O(m * n) | Medium |
| 577 | [Employee Bonus](https://leetcode.com/problems/employee-bonus/)| SQL | Time: O(n), Space: O(1) | Easy |
| 578 | [Get Highest Answer Rate Question](https://leetcode.com/problems/get-highest-answer-rate-question/) | SQL | Time: O(n), Space: O(1) | Easy |
| 579 | [Find Cumulative Salary of an Employee](https://leetcode.com/problems/find-cumulative-salary-of-an-employee/) | SQL | Time: O(n), Space: O(1) | Medium |
| 580 | [Game Winner](https://leetcode.com/problems/game-winner/)| Game Theory, Array| Time: O(n), Space: O(n) | Easy |
| 581 | [Shortest Unsorted Continuous Subarray](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/) | Array | Time: O(n), Space: O(1) | Medium |
| 582 | [Kill Process](https://leetcode.com/problems/kill-process/)| Tree, DFS, BFS| Time: O(n), Space: O(n) | Medium |
| 583 | [Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/) | Dynamic Programming | Time: O(m * n), Space: O(m * n) | Medium |
| 584 | [Find Customer Referee](https://leetcode.com/problems/find-customer-referee/) | SQL | Time: O(n), Space: O(1) | Medium |
| 585 | [Investments in 2016](https://leetcode.com/problems/investments-in-2016/) | SQL | Time: O(n), Space: O(1) | Easy |
| 586 | [Customer Placing the Largest Number of Orders](https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/) | SQL | Time: O(n), Space: O(1) | Medium |
| 587 | [Erect the Fence](https://leetcode.com/problems/erect-the-fence/) | Geometry| Time: O(n log n), Space: O(n) | Hard |
| 588 | [Design In-Memory File System](https://leetcode.com/problems/design-in-memory-file-system/) | Hash Map| Time: O(n), Space: O(n) | Hard |
| 589 | [N-ary Tree Preorder Traversal](https://leetcode.com/problems/n-ary-tree-preorder-traversal/) | Tree (Preorder) | Time: O(n), Space: O(n) | Easy |
| 590 | [N-ary Tree Postorder Traversal](https://leetcode.com/problems/n-ary-tree-postorder-traversal/) | Tree (Postorder)| Time: O(n), Space: O(n) | Easy |
| 591 | [Tag Validator](https://leetcode.com/problems/tag-validator/)| Stack | Time: O(n), Space: O(n) | Hard |
| 592 | [Fraction Addition and Subtraction](https://leetcode.com/problems/fraction-addition-and-subtraction/) | Math, String| Time: O(n), Space: O(1) | Medium |
| 593 | [Valid Square](https://leetcode.com/problems/valid-square/)| Geometry| Time: O(1), Space: O(1) | Medium |
| 594 | [Longest Harmonious Subsequence](https://leetcode.com/problems/longest-harmonious-subsequence/) | Hash Map| Time: O(n), Space: O(n) | Easy |
| 595 | [Big Countries](https://leetcode.com/problems/big-countries/)| SQL | Time: O(n), Space: O(1) | Easy |
| 596 | [Classes More Than 5 Students](https://leetcode.com/problems/classes-more-than-5-students/) | SQL | Time: O(n), Space: O(1) | Easy |
| 597 | [Friend Requests I: Overall Acceptance Rate](https://leetcode.com/problems/friend-requests-i-overall-acceptance-rate/) | SQL | Time: O(n), Space: O(1) | Easy |
| 598 | [Range Addition II](https://leetcode.com/problems/range-addition-ii/) | Array | Time: O(1), Space: O(1) | Easy |
| 599 | [Minimum Index of a Repeated Element](https://leetcode.com/problems/minimum-index-of-a-repeated-element/) | Hash Map| Time: O(n), Space: O(n) | Medium |
| 600 | [Non-negative Integers without Consecutive Ones](https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/) | Dynamic Programming | Time: O(log n), Space: O(log n) | Medium |
| 601 | [Human Traffic of Stadium](https://leetcode.com/problems/human-traffic-of-stadium/) | Interval, Prefix Sum| Time: O(n), Space: O(1) | Medium |
| 602 | [Friend Requests II: The Final Count](https://leetcode.com/problems/friend-requests-ii-the-final-count/) | Union-Find, Hash Map| Time: O(n), Space: O(n) | Medium |
| 603 | [Consecutive Available Seats](https://leetcode.com/problems/consecutive-available-seats/) | Array | Time: O(n), Space: O(1) | Easy |
| 604 | [Design Compressed String Iterator](https://leetcode.com/problems/design-compressed-string-iterator/) | String, Iterator| Time: O(1), Space: O(1) | Easy |
| 605 | [Can Place Flowers](https://leetcode.com/problems/can-place-flowers/) | Array | Time: O(n), Space: O(1) | Easy |
| 606 | [📓 Construct String from Binary Tree](../leetcode/0606.ipynb) | <span title="Visit root first, then recurse into children, adding parentheses around non-empty subtrees.">DFS Pre-order with Parentheses</span> | Time: O(n), Space: O(n) | Easy |
| 607 | [Sales Person](https://leetcode.com/problems/sales-person/) | SQL | Time: O(n), Space: O(1) | Medium |
| 608 | [Tree Node](https://leetcode.com/problems/tree-node/) | Tree, Hash Map| Time: O(n), Space: O(n) | Easy |
| 609 | [Find Duplicate File in System](https://leetcode.com/problems/find-duplicate-file-in-system/) | Hash Map, String| Time: O(n), Space: O(n) | Medium |
| 610 | [Combination Sum III](https://leetcode.com/problems/combination-sum-iii/) | Backtracking| Time: O(n!), Space: O(n) | Medium |
| 611 | [Valid Triangle Number](https://leetcode.com/problems/valid-triangle-number/) | Sorting, Two Pointer| Time: O(n^2), Space: O(1) | Medium |
| 612 | [Student Attendance Record III](https://leetcode.com/problems/student-attendance-record-iii/) | Dynamic Programming | Time: O(n), Space: O(n) | Hard |
| 1091 | [📓 Shortest Path in Binary Matrix](../leetcode/1091.ipynb) | <span title="Breadth-first search with a queue; visit all neighbors level by level.">BFS (Queue)</span> | Time: $O(n^2)$, Space: $O(n^2)$ | Medium |
| 614 | [Binary Tree Longest Consecutive Sequence III](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-iii/) | Tree, DFS | Time: O(n), Space: O(h) | Medium |
| 615 | [Average Salary: Excluding the Minimum and Maximum Salary](https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/) | Array | Time: O(n), Space: O(1) | Easy |
| 616 | [Add Bold Tag in String](https://leetcode.com/problems/add-bold-tag-in-string/) | String, Dynamic Programming | Time: O(n), Space: O(n) | Medium |
| 617 | [📓 Merge Two Binary Trees](../leetcode/0617.ipynb) | <span title="Recursive DFS over a binary tree; return values up the call stack to accumulate the answer.">Binary Tree</span> | Time: O(n), Space: O(h) | Easy |
| 618 | [Students Reporting Results](https://leetcode.com/problems/students-reporting-results/) | SQL | Time: O(n), Space: O(1) | Easy |
| 619 | [Binary Tree Longest Consecutive Sequence IV](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-iv/) | Tree, DFS | Time: O(n), Space: O(h) | Medium |
| 620 | [Not Boring Movies](https://leetcode.com/problems/not-boring-movies/) | SQL | Time: O(n), Space: O(1) | Easy |
| 621 | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | Greedy, Heap, Hash Map| Time: O(n log n), Space: O(n) | Medium |
| 622 | [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) | Array, Queue| Time: O(1), Space: O(k) | Medium |
| 623 | [📓 Add One Row to Tree](../leetcode/0623.ipynb) | <span title="Recursive DFS over a binary tree; return values up the call stack to accumulate the answer.">Binary Tree</span> | Time: O(n), Space: O(h) | Medium |
| 624 | [Maximum Distance in Arrays](https://leetcode.com/problems/maximum-distance-in-arrays/) | Array | Time: O(n), Space: O(1) | Medium |
| 625 | [Minimum Factorization](https://leetcode.com/problems/minimum-factorization/) | Math | Time: O(sqrt(n)), Space: O(1) | Medium |
| 626 | [Exchange Seats](https://leetcode.com/problems/exchange-seats/) | SQL | Time: O(n), Space: O(1) | Easy |
| 627 | [Swap Salary](https://leetcode.com/problems/swap-salary/) | SQL | Time: O(1), Space: O(1) | Easy |
| 628 | [Maximum Product of Three Numbers](https://leetcode.com/problems/maximum-product-of-three-numbers/) | Array | Time: O(n log n), Space: O(1) | Easy |
| 629 | [K Inverse Pairs Array](https://leetcode.com/problems/k-inverse-pairs-array/) | Dynamic Programming | Time: O(n * k), Space: O(n * k) | Hard |
| 630 | [Course Schedule III](https://leetcode.com/problems/course-schedule-iii/) | Greedy, Heap| Time: O(n log n), Space: O(n) | Hard |
| 631 | [Design Excel Sum Formula](https://leetcode.com/problems/design-excel-sum-formula/) | SQL | Time: O(n), Space: O(1) | Medium |
| 632 | [Smallest Range Covering Elements from K Lists](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/) | Heap, Merge | Time: O(n log k), Space: O(k) | Hard |
| 633 | [Sum of Square Numbers](https://leetcode.com/problems/sum-of-square-numbers/) | Math, Two Pointer | Time: O(sqrt(n)), Space: O(1) | Easy |
| 634 | [Find the Derangement of an Array](https://leetcode.com/problems/find-the-derangement-of-an-array/) | Dynamic Programming | Time: O(n), Space: O(1) | Medium |
| 635 | [Design Log Storage System](https://leetcode.com/problems/design-log-storage-system/) | Hash Map | Time: O(1), Space: O(n) | Medium |
| 636 | [Exclusive Time of Functions](https://leetcode.com/problems/exclusive-time-of-functions/) | Stack | Time: O(n), Space: O(n) | Medium |
| 637 | [📓 Average of Levels in Binary Tree](../leetcode/0637.ipynb) | <span title="Level-order traversal with a queue; process all nodes at each depth before moving deeper.">Binary Tree (BFS)</span> | Time: O(n), Space: O(n) | Easy |
| 638 | [Shopping Offers](https://leetcode.com/problems/shopping-offers/) | Dynamic Programming | Time: O(n * m), Space: O(n * m) | Medium |
| 639 | [Decode Ways II](https://leetcode.com/problems/decode-ways-ii/) | Dynamic Programming | Time: O(n), Space: O(1) | Hard |
| 640 | [Solve the Equation](https://leetcode.com/problems/solve-the-equation/) | Math | Time: O(n), Space: O(1) | Medium |
| 641 | [Design Circular Deque](https://leetcode.com/problems/design-circular-deque/) | Array, Deque| Time: O(1), Space: O(k) | Medium |
| 642 | [Design Search Autocomplete System](https://leetcode.com/problems/design-search-autocomplete-system/) | Trie, String, Heap| Time: O(k), Space: O(k) | Hard |
| 643 | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | Array | Time: O(n), Space: O(1) | Easy |
| 644 | [Maximum Average Subarray II](https://leetcode.com/problems/maximum-average-subarray-ii/) | Dynamic Programming | Time: O(n log n), Space: O(1) | Hard |
| 645 | [Set Mismatch](https://leetcode.com/problems/set-mismatch/) | Array, Hash Set | Time: O(n), Space: O(n) | Easy |
| 646 | [Maximum Length of Pair Chain](https://leetcode.com/problems/maximum-length-of-pair-chain/) | Greedy, Sorting | Time: O(n log n), Space: O(1) | Medium |
| 647 | [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | Dynamic Programming | Time: O(n^2), Space: O(n^2) | Medium |
| 648 | [Replace Words](https://leetcode.com/problems/replace-words/) | Trie, String| Time: O(n), Space: O(n) | Medium |
| 649 | [Dota2 Senate](https://leetcode.com/problems/dota2-senate/) | Queue, String | Time: O(n), Space: O(n) | Medium |
| 650 | [2 Keys Keyboard](https://leetcode.com/problems/2-keys-keyboard/) | Dynamic Programming | Time: O(n), Space: O(n) | Medium |
| 651 | [4 Keys Keyboard](https://leetcode.com/problems/4-keys-keyboard/) | Dynamic Programming | Time: O(n^2), Space: O(n) | Medium |
| 652 | [Find Duplicate Subtrees](https://leetcode.com/problems/find-duplicate-subtrees/) | Tree, Hash Map| Time: O(n), Space: O(n) | Medium |
| 653 | [Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/) | Tree, Hash Set| Time: O(n), Space: O(n) | Easy |
| 654 | [Maximum Binary Tree](https://leetcode.com/problems/maximum-binary-tree/) | Tree | Time: O(n), Space: O(n) | Medium |
| 655 | [Print Binary Tree](https://leetcode.com/problems/print-binary-tree/) | Tree | Time: O(n), Space: O(n) | Medium |
| 656 | [Coin Path](https://leetcode.com/problems/coin-path/) | Dynamic Programming | Time: O(n^2), Space: O(n) | Hard |
| 657 | [Judge Route Circle](https://leetcode.com/problems/judge-route-circle/) | String | Time: O(n), Space: O(1) | Easy |
| 658 | [Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/) | Two Pointer, Binary Search| Time: O(log n + k), Space: O(k) | Medium |
| 659 | [Split Array into Consecutive Subsequences](https://leetcode.com/problems/split-array-into-consecutive-subsequences/) | Greedy, Hash Map | Time: O(n), Space: O(n) | Hard |
| 660 | [Remove 9](https://leetcode.com/problems/remove-9/) | Math | Time: O(log n), Space: O(1) | Hard |
| 661 | [Image Smoothening](https://leetcode.com/problems/image-smoothening/) | Array | Time: O(mn), Space: O(1) | Easy |
| 662 | [Maximum Width of Binary Tree](https://leetcode.com/problems/maximum-width-of-binary-tree/) | Tree, BFS | Time: O(n), Space: O(n) | Medium |
| 663 | [Equal Tree Partition](https://leetcode.com/problems/equal-tree-partition/) | Tree | Time: O(n), Space: O(n) | Medium |
| 664 | [Strange Printer](https://leetcode.com/problems/strange-printer/) | Dynamic Programming | Time: O(n^3), Space: O(n^2) | Hard |
| 665 | [Non-decreasing Array](https://leetcode.com/problems/non-decreasing-array/) | Array | Time: O(n), Space: O(1) | Medium |
| 666 | [Path Sum IV](https://leetcode.com/problems/path-sum-iv/) | Tree | Time: O(n), Space: O(n) | Medium |
| 667 | [Beautiful Arrangement II](https://leetcode.com/problems/beautiful-arrangement-ii/) | Greedy, Array | Time: O(n), Space: O(1) | Medium |
| 668 | [📓 Kth Smallest Number in Multiplication Table](../leetcode/0668.ipynb) | <span title="Halve the search space each step by comparing the midpoint to a monotone predicate.">Binary Search</span> | Time: O(n log m), Space: O(1) | Hard |
| 669 | [Trim a Binary Search Tree](https://leetcode.com/problems/trim-a-binary-search-tree/) | Tree | Time: O(n), Space: O(h) | Medium |
| 670 | [Maximum Swap](https://leetcode.com/problems/maximum-swap/) | Array, Greedy | Time: O(n), Space: O(n) | Medium |
| 671 | [Second Minimum Node In a Binary Tree](https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/) | Tree | Time: O(n), Space: O(n) | Medium |
| 672 | [Bulb Switcher II](https://leetcode.com/problems/bulb-switcher-ii/) | Math | Time: O(1), Space: O(1) | Medium |
| 673 | [Number of Longest Increasing Subsequence](https://leetcode.com/problems/number-of-longest-increasing-subsequence/) | DP, Segment Tree| Time: O(n^2), Space: O(n) | Medium |
| 674 | [Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/) | Array | Time: O(n), Space: O(1) | Easy |
| 675 | [Cut Off Trees for Golf Event](https://leetcode.com/problems/cut-off-trees-for-golf-event/) | BFS, Graph, Priority Queue| Time: O(n log n), Space: O(n) | Hard |
| 676 | [Implement Magic Dictionary](https://leetcode.com/problems/implement-magic-dictionary/) | Trie, Hash Map| Time: O(n), Space: O(n) | Medium |
| 677 | [Map Sum Pairs](https://leetcode.com/problems/map-sum-pairs/) | Trie | Time: O(1), Space: O(n) | Medium |
| 678 | [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) | Stack, String | Time: O(n), Space: O(n) | Medium |
| 679 | [24 Game](https://leetcode.com/problems/24-game/) | Backtracking| Time: O(n!), Space: O(1) | Hard |
| 680 | [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) | String | Time: O(n), Space: O(1) | Easy |
| 681 | [Next Closest Time](https://leetcode.com/problems/next-closest-time/)   | Math | Time: O(1), Space: O(1) | Medium |
| 682 | [Baseball Game](https://leetcode.com/problems/baseball-game/)   | Stack| Time: O(n), Space: O(n) | Easy |
| 683 | [K Empty Slots](https://leetcode.com/problems/k-empty-slots/)   | Array, Sliding Window| Time: O(n), Space: O(1) | Hard |
| 684 | [Redundant Connection](https://leetcode.com/problems/redundant-connection/)   | Union-Find   | Time: O(n), Space: O(n) | Medium |
| 685 | [Redundant Connection II](https://leetcode.com/problems/redundant-connection-ii/) | Union-Find   | Time: O(n), Space: O(n) | Hard |
| 686 | [Repeated String Match](https://leetcode.com/problems/repeated-string-match/) | String | Time: O(n), Space: O(1) | Easy |
| 687 | [Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/) | Tree | Time: O(n), Space: O(h) | Medium |
| 688 | [Knight Probability in Chessboard](https://leetcode.com/problems/knight-probability-in-chessboard/) | DP, Chessboard| Time: O(n^2 * k), Space: O(n^2) | Medium |
| 689 | [Maximum Sum of 3 Non-Overlapping Subarrays](https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/) | DP  | Time: O(n), Space: O(n) | Hard |
| 690 | [Employee Importance](https://leetcode.com/problems/employee-importance/) | Tree, Hash Map| Time: O(n), Space: O(n) | Easy |
| 691 | [Sticker to Spell Word](https://leetcode.com/problems/sticker-to-spell-word/) | DP, Hash Map| Time: O(n * m * k), Space: O(n) | Hard |
| 692 | [Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)   | Hash Map, Heap| Time: O(n log k), Space: O(n) | Medium |
| 693 | [Binary Number with Alternating Bits](https://leetcode.com/problems/binary-number-with-alternating-bits/) | Math | Time: O(1), Space: O(1) | Easy |
| 694 | [Number of Distinct Islands](https://leetcode.com/problems/number-of-distinct-islands/) | DFS, Hash Set | Time: O(n), Space: O(n) | Medium |
| 695 | [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | DFS | Time: O(n), Space: O(n) | Medium |
| 696 | [Count Binary Substrings](https://leetcode.com/problems/count-binary-substrings/) | String, Counting  | Time: O(n), Space: O(1) | Medium |
| 697 | [Degree of an Array](https://leetcode.com/problems/degree-of-an-array/) | Hash Map| Time: O(n), Space: O(n) | Easy |
| 698 | [Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) | Backtracking, DP  | Time: O(2^n), Space: O(n) | Hard |
| 699 | [Falling Squares](https://leetcode.com/problems/falling-squares/) | Segment Tree | Time: O(n log n), Space: O(n) | Hard |
| 700 | [📓 Search in a Binary Search Tree](../leetcode/0700.ipynb) | <span title="Iterative BST traversal using the ordering property: go left if val < node, else right.">Iterative (BST property)</span> | Time: $O(h)$, Space: $O(1)$ | Easy |
| 701 | [📓 Insert into a Binary Search Tree](../leetcode/0701.ipynb) | <span title="Exploit BST ordering: go left when target < node, right when target > node.">Binary Search Tree</span> | Time: O(h), Space: O(1) | Easy |
| 702 | [📓 Search in a Sorted Array of Unknown Size](../leetcode/0702.ipynb) | <span title="Double the window (1,2,4,8…) until the target is within range, then binary search inside.">Exponential Search + Binary Search</span> | Time: O(log n), Space: O(1) | Medium |
| 703 | [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | Heap | Time: O(log k), Space: O(k) | Easy |
| 704 | [📓 Binary Search](../leetcode/0704.ipynb) | <span title="Halve the search space each step by comparing the midpoint to a monotone predicate.">Binary Search</span> | Time: $O(\log n)$, Space: $O(1)$ | Easy |
| 705 | [Design HashSet](https://leetcode.com/problems/design-hashset/) | Hash Set | Time: O(1), Space: O(n) | Easy |
| 706 | [Design HashMap](https://leetcode.com/problems/design-hashmap/) | Hash Map| Time: O(1), Space: O(n) | Easy |
| 707 | [Design Linked List](https://leetcode.com/problems/design-linked-list/) | Linked List | Time: O(1), Space: O(n) | Easy |
| 708 | [Insert into a Sorted Circular Linked List](https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/) | Linked List | Time: O(n), Space: O(1) | Medium |
| 709 | [To Lower Case](https://leetcode.com/problems/to-lower-case/)   | String | Time: O(n), Space: O(1) | Easy |
| 710 | [Random Pick with Blacklist](https://leetcode.com/problems/random-pick-with-blacklist/) | Array, Hash Map   | Time: O(1), Space: O(n) | Hard |
| 711 | [Number of Distinct Islands II](https://leetcode.com/problems/number-of-distinct-islands-ii/) | DFS, Union-Find   | Time: O(n), Space: O(n) | Hard |
| 712 | [Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/) | Dynamic Programming| Time: O(m * n), Space: O(m * n) | Medium |
| 713 | [Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/) | Two Pointer, Sliding Window| Time: O(n), Space: O(1) | Medium |
| 714 | [Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) | Dynamic Programming| Time: O(n), Space: O(1) | Medium |
| 715 | [Range Module](https://leetcode.com/problems/range-module/) | Interval | Time: O(n), Space: O(n) | Hard |
| 716 | [Max Stack](https://leetcode.com/problems/max-stack/) | Stack| Time: O(1), Space: O(n) | Hard |
| 717 | [1-bit and 2-bit Characters](https://leetcode.com/problems/1-bit-and-2-bit-characters/) | Array | Time: O(n), Space: O(1) | Easy |
| 718 | [Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/) | Dynamic Programming| Time: O(m * n), Space: O(m * n) | Medium |
| 719 | [📓 Find K-th Smallest Pair Distance](../leetcode/0719.ipynb) | <span title="Sort first; binary search for the right boundary; sliding window counts pairs in O(n).">Binary Search, Two Pointer</span> | Time: O(n log n), Space: O(1) | Hard |
| 720 | [Longest Word in Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/) | Trie | Time: O(n), Space: O(n) | Easy |
| 721 | [Accounts Merge](https://leetcode.com/problems/accounts-merge/) | Graph, DFS  | Time: O(n), Space: O(n) | Medium |
| 722 | [Remove Comments](https://leetcode.com/problems/remove-comments/) | String | Time: O(n), Space: O(1) | Medium |
| 723 | [📓 Candy Crush](../leetcode/0723.ipynb) | <span title="Mark visited elements by negating or cycling their values; no extra space needed.">In-place Marking</span> | Time: O(n * m), Space: O(1) | Medium |
| 724 | [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) | Array | Time: O(n), Space: O(1) | Easy |
| 725 | [Split Linked List in Parts](https://leetcode.com/problems/split-linked-list-in-parts/) | Linked List | Time: O(n), Space: O(1) | Medium |
| 726 | [Number of Atoms](https://leetcode.com/problems/number-of-atoms/) | Hash Map, Stack   | Time: O(n), Space: O(n) | Hard |
| 727 | [Minimum Window Subsequence](https://leetcode.com/problems/minimum-window-subsequence/) | Sliding Window, Two Pointer| Time: O(n), Space: O(1) | Hard |
| 728 | [Self Dividing Numbers](https://leetcode.com/problems/self-dividing-numbers/) | Math | Time: O(n), Space: O(1) | Easy |
| 729 | [📓 My Calendar I](../leetcode/0729.ipynb) | <span title="Exploit BST ordering: go left when target < node, right when target > node.">Binary Search Tree</span> | Time: O(log n), Space: O(n) | Medium |
| 730 | [Count Different Palindromes](https://leetcode.com/problems/count-different-palindromes/) | DP   | Time: O(n^2), Space: O(n^2) | Hard |
| 731 | [📓 My Calendar II](../leetcode/0731.ipynb) | <span title="Exploit BST ordering: go left when target < node, right when target > node.">Binary Search Tree</span> | Time: O(log n), Space: O(n) | Medium |
| 732 | [My Calendar III](https://leetcode.com/problems/my-calendar-iii/) | Segment Tree | Time: O(log n), Space: O(n) | Hard |
| 733 | [Flood Fill](https://leetcode.com/problems/flood-fill/)   | DFS, BFS| Time: O(n), Space: O(n) | Easy |
| 734 | [Sentence Similarity](https://leetcode.com/problems/sentence-similarity/) | Graph, Hash Map   | Time: O(n), Space: O(n) | Easy |
| 735 | [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/) | Stack| Time: O(n), Space: O(n) | Medium |
| 736 | [Parse Lisp Expression](https://leetcode.com/problems/parse-lisp-expression/) | Stack| Time: O(n), Space: O(n) | Hard |
| 737 | [Sentence Similarity II](https://leetcode.com/problems/sentence-similarity-ii/) | Graph, Union-Find | Time: O(n), Space: O(n) | Medium |
| 738 | [Monotone Increasing Digits](https://leetcode.com/problems/monotone-increasing-digits/) | Math | Time: O(n), Space: O(1) | Medium |
| 739 | [Daily Temperature](https://leetcode.com/problems/daily-temperature/)   | Stack| Time: O(n), Space: O(n) | Medium |
| 740 | [Delete and Earn](https://leetcode.com/problems/delete-and-earn/) | Dynamic Programming| Time: O(n), Space: O(n) | Medium |
| 741 | [Cherry Pickup](https://leetcode.com/problems/cherry-pickup/)   | Dynamic Programming, DP Table| Time: O(n^2), Space: O(n^2) | Hard |
| 742 | [Closest Leaf in a Binary Tree](https://leetcode.com/problems/closest-leaf-in-a-binary-tree/) | Tree, BFS, DFS | Time: O(n), Space: O(n) | Medium |
| 743 | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Graph, Dijkstra   | Time: O(E log V), Space: O(V) | Medium |
| 744 | [📓 Find Smallest Letter Greater Than Target](../leetcode/0744.ipynb) | <span title="Halve the search space each step by comparing the midpoint to a monotone predicate.">Binary Search</span> | Time: $O(\log n)$, Space: $O(1)$ | Easy |
| 745 | [Prefix and Suffix Search](https://leetcode.com/problems/prefix-and-suffix-search/) | Trie | Time: O(n), Space: O(n) | Hard |
| 746 | [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | DP  | Time: O(n), Space: O(n) | Easy |
| 747 | [Largest Number At Least Twice of Others](https://leetcode.com/problems/largest-number-at-least-twice-of-others/) | Array | Time: O(n), Space: O(1) | Easy |
| 748 | [Shortest Completing Word](https://leetcode.com/problems/shortest-completing-word/) | String, Hash Map  | Time: O(n), Space: O(n) | Medium |
| 749 | [Contain Virus](https://leetcode.com/problems/contain-virus/)   | Graph, BFS   | Time: O(n^2), Space: O(n^2) | Hard |
| 750 | [Number of Corner Rectangles](https://leetcode.com/problems/number-of-corner-rectangles/) | Hash Map| Time: O(n^2), Space: O(n) | Medium |
| 751 | [IP to CIDR](https://leetcode.com/problems/ip-to-cidr/)   | Math | Time: O(1), Space: O(1) | Easy |
| 752 | [📓 Open the Lock](../leetcode/0752.ipynb) | <span title="Breadth-first search with a queue; visit all neighbors level by level.">BFS (Queue)</span> | Time: $O(10^4 + D)$, Space: $O(10^4 + D)$ | Medium |
| 753 | [Cracking the Safe](https://leetcode.com/problems/cracking-the-safe/)   | Graph, BFS  | Time: O(n^2), Space: O(n) | Hard |
| 754 | [Reach a Number](https://leetcode.com/problems/reach-a-number/) | Math | Time: O(sqrt(n)), Space: O(1) | Medium |
| 755 | [Pour Water](https://leetcode.com/problems/pour-water/)   | Simulation   | Time: O(n^2), Space: O(1) | Medium |
| 756 | [Pyramid Transition Matrix](https://leetcode.com/problems/pyramid-transition-matrix/) | DP  | Time: O(n^3), Space: O(n^2) | Hard |
| 757 | [Set Intersection Size At Least Two](https://leetcode.com/problems/set-intersection-size-at-least-two/) | Greedy, Sorting   | Time: O(n log n), Space: O(n) | Hard |
| 758 | [Bold Words in String](https://leetcode.com/problems/bold-words-in-string/)   | String, Hash Set  | Time: O(n), Space: O(n) | Medium |
| 759 | [Employee Free Time](https://leetcode.com/problems/employee-free-time/) | Interval, Priority Queue   | Time: O(n log n), Space: O(n) | Hard |
| 760 | [Find Anagram Mappings](https://leetcode.com/problems/find-anagram-mappings/) | Hash Map| Time: O(n), Space: O(n) | Easy |
| 761 | [Special Binary String](https://leetcode.com/problems/special-binary-string/) | String, Recursion | Time: O(n), Space: O(n) | Medium |
| 762 | [📓 Prime Number of Set Bits in Binary Representation](../leetcode/0762.ipynb) | <span title="Count set bits (popcount); check if the count is prime using a precomputed bitmask of primes ≤ 20.">Bit Manipulation + Prime Mask</span> | Time: O(n), Space: O(1) | Easy |
| 763 | [Partition Labels](https://leetcode.com/problems/partition-labels/) | Greedy, Hash Map  | Time: O(n), Space: O(n) | Medium |
| 764 | [Largest Plus Sign](https://leetcode.com/problems/largest-plus-sign/)   | DP, 2D Array| Time: O(n^2), Space: O(n^2) | Medium |
| 765 | [Couples Holding Hands](https://leetcode.com/problems/couples-holding-hands/) | Greedy, Union-Find| Time: O(n log n), Space: O(n) | Hard |
| 766 | [Toeplitz Matrix](https://leetcode.com/problems/toeplitz-matrix/) | Array | Time: O(m * n), Space: O(1) | Easy |
| 767 | [Reorganize String](https://leetcode.com/problems/reorganize-string/)   | Greedy, Priority Queue| Time: O(n log n), Space: O(n) | Medium |
| 768 | [Max Chunks To Make Sorted II](https://leetcode.com/problems/max-chunks-to-make-sorted-ii/) | Greedy, Stack | Time: O(n), Space: O(n) | Hard |
| 769 | [Max Chunks To Make Sorted](https://leetcode.com/problems/max-chunks-to-make-sorted/) | Greedy| Time: O(n), Space: O(1) | Medium |
| 770 | [Basic Calculator IV](https://leetcode.com/problems/basic-calculator-iv/) | Stack, Recursion  | Time: O(n), Space: O(n) | Hard |
| 771 | [Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/)   | Hash Map| Time: O(n), Space: O(n) | Easy |
| 772 | [Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/)   | Stack, Recursion  | Time: O(n), Space: O(n) | Hard |
| 773 | [Sliding Puzzle](https://leetcode.com/problems/sliding-puzzle/) | BFS | Time: O(n^2), Space: O(n^2) | Hard |
| 774 | [📓 Minimize Max Distance to Gas Station](../leetcode/0774.ipynb) | <span title="Halve the search space each step by comparing the midpoint to a monotone predicate.">Binary Search</span> | Time: O(n log m), Space: O(1) | Hard |
| 775 | [Global and Local Inversions](https://leetcode.com/problems/global-and-local-inversions/) | Array, Sorting| Time: O(n log n), Space: O(n) | Medium |
| 776 | [Split BST](https://leetcode.com/problems/split-bst/) | Tree | Time: O(h), Space: O(h) | Medium |
| 777 | [Swap Adjacent in LR String](https://leetcode.com/problems/swap-adjacent-in-lr-string/) | Two Pointer | Time: O(n), Space: O(1) | Medium |
| 778 | [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/)   | BFS, Priority Queue | Time: O(n log n), Space: O(n) | Hard |
| 779 | [K-th Symbol in Grammar](https://leetcode.com/problems/k-th-symbol-in-grammar/) | Recursion| Time: O(log n), Space: O(1) | Medium |
| 780 | [Reaching Points](https://leetcode.com/problems/reaching-points/) | Math | Time: O(log n), Space: O(1) | Hard |
| 781 | [Rabbits in Forest](https://leetcode.com/problems/rabbits-in-forest/)   | Hash Map| Time: O(n), Space: O(n) | Medium |
| 782 | [Transform to Chessboard](https://leetcode.com/problems/transform-to-chessboard/) | Array | Time: O(n^2), Space: O(1) | Hard |
| 783 | [Minimum Distance Between BST Nodes](https://leetcode.com/problems/minimum-distance-between-bst-nodes/) | Tree | Time: O(n), Space: O(n) | Medium |
| 784 | [Letter Case Permutation](https://leetcode.com/problems/letter-case-permutation/) | Backtracking| Time: O(2^n), Space: O(1) | Easy |
| 785 | [Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/) | Graph, BFS/DFS| Time: O(n + e), Space: O(n) | Medium |
| 786 | [K-th Smallest Prime Fraction](https://leetcode.com/problems/k-th-smallest-prime-fraction/) | Heap, Binary Search | Time: O(n log n), Space: O(n) | Hard |
| 787 | [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | Dijkstra, Graph   | Time: O(E log V), Space: O(V) | Medium |
| 788 | [Rotated Digits](https://leetcode.com/problems/rotated-digits/) | Math | Time: O(n), Space: O(1) | Easy |
| 789 | [Escape The Ghosts](https://leetcode.com/problems/escape-the-ghosts/)| Math | Time: O(1), Space: O(1) | Easy |
| 790 | [Domino and Tromino Tiling](https://leetcode.com/problems/domino-and-tromino-tiling/) | Dynamic Programming| Time: O(n), Space: O(n) | Medium |
| 791 | [Custom Sort String](https://leetcode.com/problems/custom-sort-string/) | Sorting, Hash Map | Time: O(n log n), Space: O(n) | Medium |
| 792 | [Number of Matching Subsequences](https://leetcode.com/problems/number-of-matching-subsequences/) | Hash Map| Time: O(n), Space: O(n) | Medium |
| 793 | [📓 Preimage Size of Factorial Zeroes Function](../leetcode/0793.ipynb) | <span title="Halve the search space each step by comparing the midpoint to a monotone predicate.">Binary Search</span> | Time: O(log n), Space: O(1) | Hard |
| 794 | [Valid Tic-Tac-Toe State](https://leetcode.com/problems/valid-tic-tac-toe-state/) | Simulation   | Time: O(1), Space: O(1) | Medium |
| 795 | [Number of Subarrays with Bounded Maximum](https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/) | Sliding Window, Two Pointers| Time: O(n), Space: O(1) | Medium |
| 796 | [Rotate String](https://leetcode.com/problems/rotate-string/)   | String, Array | Time: O(n), Space: O(1) | Easy |
| 797 | [All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/) | DFS, Backtracking  | Time: O(n * 2^n), Space: O(n) | Medium |
| 798 | [Smallest Rotation with Highest Score](https://leetcode.com/problems/smallest-rotation-with-highest-score/) | Sliding Window, Greedy| Time: O(n), Space: O(n) | Hard |
| 799 | [Champagne Tower](https://leetcode.com/problems/champagne-tower/) | Simulation, DP| Time: O(n^2), Space: O(n^2) | Medium |
| 800 | [Similar RGB Color](https://leetcode.com/problems/similar-rgb-color/)   | String, Math| Time: O(1), Space: O(1) | Easy |
| 801 | [Minimum Swaps To Make Sequences Increasing](https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/) | Dynamic Programming, DP Table| Time: O(n^2), Space: O(n) | Hard |
| 802 | [Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/) | Graph, DFS | Time: O(V + E), Space: O(V) | Medium |
| 803 | [Bricks Falling When Hit](https://leetcode.com/problems/bricks-falling-when-hit/) | Union-Find, Graph | Time: O(n * m), Space: O(n * m) | Hard |
| 804 | [Unique Morse Code Words](https://leetcode.com/problems/unique-morse-code-words/) | Hash Set, String  | Time: O(n), Space: O(1) | Easy |
| 805 | [Split Array With Same Average](https://leetcode.com/problems/split-array-with-same-average/) | Dynamic Programming| Time: O(2^n), Space: O(n) | Hard |
| 806 | [Number of Lines To Write String](https://leetcode.com/problems/number-of-lines-to-write-string/) | Math, Array | Time: O(n), Space: O(1) | Easy |
| 807 | [Max Increase to Keep City Skyline](https://leetcode.com/problems/max-increase-to-keep-city-skyline/) | Array, Simulation | Time: O(n^2), Space: O(n) | Medium |
| 808 | [Soup Servings](https://leetcode.com/problems/soup-servings/)   | Dynamic Programming, DP Table| Time: O(n), Space: O(n) | Hard |
| 809 | [Expressive Words](https://leetcode.com/problems/expressive-words/) | String, Trie| Time: O(n), Space: O(n) | Medium |
| 810 | [Chalkboard XOR Game](https://leetcode.com/problems/chalkboard-xor-game/) | Game Theory | Time: O(n), Space: O(1) | Hard |
| 811 | [Subdomain Visit Count](https://leetcode.com/problems/subdomain-visit-count/) | Hash Map| Time: O(n), Space: O(n) | Easy |
| 812 | [Largest Triangle Area](https://leetcode.com/problems/largest-triangle-area/) | Geometry, Math| Time: O(1), Space: O(1) | Easy |
| 813 | [Largest Sum of Averages](https://leetcode.com/problems/largest-sum-of-averages/) | Dynamic Programming, DP Table| Time: O(n^2), Space: O(n^2) | Medium |
| 814 | [Binary Tree Pruning](https://leetcode.com/problems/binary-tree-pruning/) | Tree, DFS   | Time: O(n), Space: O(h) | Medium |
| 815 | [Bus Routes](https://leetcode.com/problems/bus-routes/)   | Graph, BFS  | Time: O(n * m), Space: O(n * m) | Hard |
| 816 | [Ambiguous Coordinates](https://leetcode.com/problems/ambiguous-coordinates/) | String | Time: O(n^3), Space: O(n^3) | Medium |
| 817 | [Linked List Components](https://leetcode.com/problems/linked-list-components/) | Linked List, Hash Set | Time: O(n), Space: O(n) | Medium |
| 818 | [Race Car](https://leetcode.com/problems/race-car/) | Dynamic Programming| Time: O(n), Space: O(n) | Hard |
| 819 | [Most Common Word](https://leetcode.com/problems/most-common-word/) | String, Hash Map  | Time: O(n), Space: O(n) | Easy |
| 820 | [Short Encoding of Words](https://leetcode.com/problems/short-encoding-of-words/) | Trie | Time: O(n), Space: O(n) | Medium |
| 821 | [Shortest Distance to a Character](https://leetcode.com/problems/shortest-distance-to-a-character/) | Array, Two Pointers| Time: O(n), Space: O(1) | Easy |
| 822 | [Card Flipping Game](https://leetcode.com/problems/card-flipping-game/) | Hash Map, Set | Time: O(n), Space: O(n) | Medium |
| 823 | [Binary Trees With Factors](https://leetcode.com/problems/binary-trees-with-factors/) | Dynamic Programming, DP Table| Time: O(n^2), Space: O(n) | Hard |
| 824 | [Goat Latin](https://leetcode.com/problems/goat-latin/)   | String | Time: O(n), Space: O(1) | Easy |
| 825 | [Friends Of Appropriate Ages](https://leetcode.com/problems/friends-of-appropriate-ages/) | Array, Sorting| Time: O(n log n), Space: O(1) | Medium |
| 826 | [Most Profit Assigning Work](https://leetcode.com/problems/most-profit-assigning-work/) | Greedy, Sorting   | Time: O(n log n), Space: O(n) | Medium |
| 827 | [Making A Large Island](https://leetcode.com/problems/making-a-large-island/) | Union-Find, DFS   | Time: O(n^2), Space: O(n^2) | Hard |
| 828 | [Count Unique Characters of All Substrings of a Given String](https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/) | Math, Sliding Window| Time: O(n^2), Space: O(1) | Hard |
| 829 | [Consecutive Numbers Sum](https://leetcode.com/problems/consecutive-numbers-sum/) | Math | Time: O(sqrt(n)), Space: O(1) | Medium |
| 830 | [Positions of Large Groups](https://leetcode.com/problems/positions-of-large-groups/) | String, Array | Time: O(n), Space: O(1) | Easy |
| 831 | [Masking Personal Information](https://leetcode.com/problems/masking-personal-information/) | String | Time: O(n), Space: O(1) | Medium |
| 832 | [Flipping an Image](https://leetcode.com/problems/flipping-an-image/)   | Array | Time: O(n), Space: O(1) | Easy |
| 833 | [Find And Replace in String](https://leetcode.com/problems/find-and-replace-in-string/) | String, Hash Map  | Time: O(n), Space: O(n) | Medium |
| 834 | [Sum of Distances in Tree](https://leetcode.com/problems/sum-of-distances-in-tree/) | Tree, DFS   | Time: O(n), Space: O(n) | Hard |
| 835 | [Image Overlap](https://leetcode.com/problems/image-overlap/)   | Array | Time: O(n^2), Space: O(1) | Medium |
| 836 | [Rectangle Overlap](https://leetcode.com/problems/rectangle-overlap/)   | Geometry, Math| Time: O(1), Space: O(1) | Easy |
| 837 | [New 21 Game](https://leetcode.com/problems/new-21-game/) | Dynamic Programming| Time: O(n), Space: O(n) | Medium |
| 838 | [Push Dominoes](https://leetcode.com/problems/push-dominoes/)   | Array, Simulation | Time: O(n), Space: O(n) | Medium |
| 839 | [Similar String Groups](https://leetcode.com/problems/similar-string-groups/) | Union-Find   | Time: O(n^2), Space: O(n) | Hard |
| 840 | [Magic Squares In Grid](https://leetcode.com/problems/magic-squares-in-grid/) | Array | Time: O(n), Space: O(1) | Medium |
| 841 | [Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/) | Graph, DFS  | Time: O(n), Space: O(n) | Medium |
| 842 | [Split Array into Fibonacci Sequence](https://leetcode.com/problems/split-array-into-fibonacci-sequence/) | Backtracking, Recursion| Time: O(n), Space: O(n) | Medium |
| 843 | [Guess the Word](https://leetcode.com/problems/guess-the-word/) | String, Game Theory | Time: O(n^2), Space: O(1) | Hard |
| 844 | [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/) | Stack, String | Time: O(n), Space: O(n) | Easy |
| 845 | [Longest Mountain in Array](https://leetcode.com/problems/longest-mountain-in-array/) | Array, Two Pointers | Time: O(n), Space: O(1) | Medium |
| 846 | [Hand of Straights](https://leetcode.com/problems/hand-of-straights/)   | Hash Map, Sorting | Time: O(n log n), Space: O(n) | Medium |
| 847 | [Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) | Graph, BFS  | Time: O(n^2), Space: O(n^2) | Hard |
| 848 | [Shifting Letters](https://leetcode.com/problems/shifting-letters/) | Array | Time: O(n), Space: O(1) | Medium |
| 849 | [Maximize Distance to Closest Person](https://leetcode.com/problems/maximize-distance-to-closest-person/) | Array, Simulation | Time: O(n), Space: O(1) | Easy |
| 850 | [Rectangle Area II](https://leetcode.com/problems/rectangle-area-ii/)   | Segment Tree, Geometry | Time: O(n log n), Space: O(n) | Hard |
| 851 | [Loud and Rich](https://leetcode.com/problems/loud-and-rich/)   | Graph, Topological Sort| Time: O(n + m), Space: O(n + m) | Medium |
| 852 | [📓 Peak Index in a Mountain Array](../leetcode/0852.ipynb) | <span title="Halve the search space each step by comparing the midpoint to a monotone predicate.">Binary Search</span> | Time: $O(\log n)$, Space: $O(1)$ | Medium |
| 853 | [Car Fleet](https://leetcode.com/problems/car-fleet/) | Sorting, Stack| Time: O(n log n), Space: O(n) | Medium |
| 854 | [K-Similar Strings](https://leetcode.com/problems/k-similar-strings/)   | BFS | Time: O(n * n!), Space: O(n!) | Hard |
| 855 | [Exam Room](https://leetcode.com/problems/exam-room/) | Priority Queue, Heap | Time: O(log n), Space: O(n) | Medium |
| 856 | [Score of Parentheses](https://leetcode.com/problems/score-of-parentheses/)   | Stack | Time: O(n), Space: O(n) | Medium |
| 857 | [Minimum Cost to Hire K Workers](https://leetcode.com/problems/minimum-cost-to-hire-k-workers/) | Sorting, Greedy   | Time: O(n log n), Space: O(n) | Hard |
| 858 | [Mirror Reflection](https://leetcode.com/problems/mirror-reflection/)   | Math | Time: O(1), Space: O(1) | Medium |
| 859 | [Buddy Strings](https://leetcode.com/problems/buddy-strings/)   | String, Hash Set  | Time: O(n), Space: O(n) | Easy |
| 860 | [Lemonade Change](https://leetcode.com/problems/lemonade-change/) | Greedy | Time: O(n), Space: O(1) | Easy |
| 861 | [Score After Flipping Matrix](https://leetcode.com/problems/score-after-flipping-matrix/) | Array | Time: O(n * m), Space: O(1) | Medium |
| 862 | [Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/) | Deque, Sliding Window| Time: O(n), Space: O(n) | Hard |
| 863 | [All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) | Tree, DFS   | Time: O(n), Space: O(n) | Medium |
| 864 | [Shortest Path to Get All Keys](https://leetcode.com/problems/shortest-path-to-get-all-keys/) | BFS, Bitmask| Time: O(n * m), Space: O(n * m) | Hard |
| 865 | [Smallest Subtree with all the Deepest Nodes](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/) | Tree, DFS   | Time: O(n), Space: O(n) | Medium |
| 866 | [Prime Palindrome](https://leetcode.com/problems/prime-palindrome/) | Math, Prime | Time: O(n), Space: O(1) | Medium |
| 867 | [Transpose Matrix](https://leetcode.com/problems/transpose-matrix/) | Array | Time: O(n * m), Space: O(1) | Easy |
| 868 | [Binary Gap](https://leetcode.com/problems/binary-gap/)   | Math, Bit Manipulation | Time: O(1), Space: O(1) | Easy |
| 869 | [Reordered Power of 2](https://leetcode.com/problems/reordered-power-of-2/)   | Math | Time: O(n), Space: O(1) | Medium |
| 870 | [Advantage Shuffle](https://leetcode.com/problems/advantage-shuffle/)   | Sorting, Two Pointers| Time: O(n log n), Space: O(n) | Hard |
| 871 | [Minimum Number of Refueling Stops](https://leetcode.com/problems/minimum-number-of-refueling-stops/) | DP, Greedy, Heap  | Time: O(n^2), Space: O(n) | Hard |
| 872 | [Leaf-Similar Trees](https://leetcode.com/problems/leaf-similar-trees/) | Tree, DFS, BFS| Time: O(n), Space: O(n) | Easy |
| 873 | [Length of Longest Fibonacci Subsequence](https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/) | DP, Hash Map| Time: O(n^2), Space: O(n) | Medium |
| 874 | [Walking Robot Simulation](https://leetcode.com/problems/walking-robot-simulation/) | Simulation, Set   | Time: O(n), Space: O(n) | Easy |
| 875 | [📓 Koko Eating Bananas](../leetcode/0875.ipynb) | <span title="Binary search on Koko's eating rate; count hours needed at each rate to find the minimum.">Binary Search on Eating Speed</span> | Time: O(n log m), Space: O(1) | Medium |
| 876 | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | Linked List, Two Pointers  | Time: O(n), Space: O(1) | Easy |
| 877 | [Stone Game](https://leetcode.com/problems/stone-game/)   | Dynamic Programming, DP Table| Time: O(n^2), Space: O(n^2) | Medium |
| 878 | [Nth Magical Number](https://leetcode.com/problems/nth-magical-number/) | Math, Binary Search | Time: O(log n), Space: O(1) | Hard |
| 879 | [Profitable Schemes](https://leetcode.com/problems/profitable-schemes/) | Dynamic Programming, DP Table| Time: O(n * m), Space: O(n * m) | Hard |
| 880 | [Decoded String at Index](https://leetcode.com/problems/decoded-string-at-index/) | String, Simulation | Time: O(n), Space: O(1) | Medium |
| 881 | [Boats to Save People](https://leetcode.com/problems/boats-to-save-people/)   | Greedy, Two Pointers | Time: O(n log n), Space: O(1) | Medium |
| 882 | [Reachable Nodes In Subdivided Graph](https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/) | Graph, DFS, BFS  | Time: O(n^2), Space: O(n) | Hard |
| 883 | [Projection Area of 3D Shapes](https://leetcode.com/problems/projection-area-of-3d-shapes/) | Math, Simulation   | Time: O(n^2), Space: O(1) | Easy |
| 884 | [Uncommon Words from Two Sentences](https://leetcode.com/problems/uncommon-words-from-two-sentences/) | Hash Map, String  | Time: O(n), Space: O(n) | Easy |
| 885 | [Spiral Matrix III](https://leetcode.com/problems/spiral-matrix-iii/)   | Simulation   | Time: O(n * m), Space: O(1) | Medium |
| 886 | [Possible Bipartition](https://leetcode.com/problems/possible-bipartition/)   | Graph, DFS   | Time: O(n + m), Space: O(n) | Medium |
| 887 | [Super Egg Drop](https://leetcode.com/problems/super-egg-drop/) | Dynamic Programming, DP Table| Time: O(K * log N), Space: O(K) | Hard |
| 888 | [Fair Candy Swap](https://leetcode.com/problems/fair-candy-swap/) | Hash Set, Array   | Time: O(n), Space: O(n) | Easy |
| 889 | [Construct Binary Tree from Preorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/) | Tree, Recursion | Time: O(n), Space: O(n) | Medium |
| 890 | [Find and Replace Pattern](https://leetcode.com/problems/find-and-replace-pattern/) | Hash Map, String | Time: O(n), Space: O(n) | Medium |
| 891 | [Sum of Subsequence Widths](https://leetcode.com/problems/sum-of-subsequence-widths/) | Sorting, Math| Time: O(n log n), Space: O(n) | Hard |
| 892 | [Surface Area of 3D Shapes](https://leetcode.com/problems/surface-area-of-3d-shapes/) | Math, Geometry | Time: O(n^2), Space: O(1) | Easy |
| 893 | [Groups of Special-Equivalent Strings](https://leetcode.com/problems/groups-of-special-equivalent-strings/) | String, Hash Set  | Time: O(n), Space: O(n) | Medium |
| 894 | [All Possible Full Binary Trees](https://leetcode.com/problems/all-possible-full-binary-trees/) | Tree, DP | Time: O(2^n), Space: O(2^n) | Hard |
| 895 | [Maximum Frequency Stack](https://leetcode.com/problems/maximum-frequency-stack/) | Stack, Hash Map   | Time: O(1), Space: O(n) | Hard |
| 896 | [Monotonic Array](https://leetcode.com/problems/monotonic-array/) | Array | Time: O(n), Space: O(1) | Easy |
| 897 | [Increasing Order Search Tree](https://leetcode.com/problems/increasing-order-search-tree/) | Tree, Recursion | Time: O(n), Space: O(n) | Easy |
| 898 | [Bitwise ORs of Subarrays](https://leetcode.com/problems/bitwise-ors-of-subarrays/) | Set, Bit Manipulation | Time: O(n), Space: O(n) | Hard |
| 899 | [Orderly Queue](https://leetcode.com/problems/orderly-queue/)   | String, Sorting   | Time: O(n log n), Space: O(n) | Hard |
| 900 | [RLE Iterator](https://leetcode.com/problems/rle-iterator/) | Array, Iterator   | Time: O(1), Space: O(n) | Medium |
| 901 | [Online Stock Span](https://leetcode.com/problems/online-stock-span/)   | Stack | Time: O(1), Space: O(n) | Medium |
| 902 | [Numbers At Most N Given Digit Set](https://leetcode.com/problems/numbers-at-most-n-given-digit-set/) | Backtracking, DFS | Time: O(n), Space: O(1) | Hard |
| 903 | [Valid Permutations for DI Sequence](https://leetcode.com/problems/valid-permutations-for-di-sequence/) | DP, Backtracking   | Time: O(n^2), Space: O(n) | Hard |
| 904 | [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) | Sliding Window, Two Pointers| Time: O(n), Space: O(1) | Medium |
| 905 | [Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/)   | Array | Time: O(n), Space: O(1) | Easy |
| 906 | [Super Palindromes](https://leetcode.com/problems/super-palindromes/)   | Math | Time: O(sqrt(n)), Space: O(1) | Hard |
| 907 | [Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/) | Stack, DP   | Time: O(n), Space: O(n) | Medium |
| 908 | [Smallest Range I](https://leetcode.com/problems/smallest-range-i/) | Math | Time: O(n), Space: O(1) | Easy |
| 909 | [Snakes and Ladders](https://leetcode.com/problems/snakes-and-ladders/) | BFS | Time: O(n^2), Space: O(n) | Medium |
| 910 | [Smallest Range II](https://leetcode.com/problems/smallest-range-ii/)   | Math | Time: O(n log n), Space: O(1) | Medium |
| 911 | [Online Election](https://leetcode.com/problems/online-election/) | Array, Hash Map   | Time: O(1), Space: O(n) | Medium |
| 912 | [Sort an Array](https://leetcode.com/problems/sort-an-array/)   | Sorting, Quick Sort | Time: O(n log n), Space: O(1) | Medium |
| 913 | [Cat and Mouse](https://leetcode.com/problems/cat-and-mouse/)   | Dynamic Programming| Time: O(n^3), Space: O(n^2) | Hard |
| 914 | [X of a Kind in a Deck of Cards](https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/) | Hash Map, Math| Time: O(n), Space: O(n) | Easy |
| 915 | [Partition Array into Disjoint Intervals](https://leetcode.com/problems/partition-array-into-disjoint-intervals/) | Array, Dynamic Programming | Time: O(n), Space: O(n) | Medium |
| 916 | [Word Subsets](https://leetcode.com/problems/word-subsets/) | Hash Map, String  | Time: O(n * m), Space: O(n) | Medium |
| 917 | [Reverse Only Letters](https://leetcode.com/problems/reverse-only-letters/)   | String, Two Pointers| Time: O(n), Space: O(1) | Easy |
| 918 | [Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/) | Kadane's Algorithm, DP| Time: O(n), Space: O(1) | Medium |
| 919 | [Complete Binary Tree Inserter](https://leetcode.com/problems/complete-binary-tree-inserter/) | Tree, BST   | Time: O(1), Space: O(n) | Medium |
| 920 | [Number of Music Playlists](https://leetcode.com/problems/number-of-music-playlists/) | Dynamic Programming, DP Table| Time: O(n * k), Space: O(n * k) | Hard |
| 921 | [Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/) | Stack, String | Time: O(n), Space: O(1) | Easy |
| 922 | [Sort Array By Parity II](https://leetcode.com/problems/sort-array-by-parity-ii/) | Array | Time: O(n), Space: O(1) | Easy |
| 923 | [3Sum With Multiplicity](https://leetcode.com/problems/3sum-with-multiplicity/) | Array, Hash Map   | Time: O(n^2), Space: O(n) | Medium |
| 924 | [Minimize Malware Spread](https://leetcode.com/problems/minimize-malware-spread/) | Graph, DFS  | Time: O(n^2), Space: O(n) | Hard |
| 925 | [Long Pressed Name](https://leetcode.com/problems/long-pressed-name/)   | String | Time: O(n), Space: O(1) | Easy |
| 926 | [Flip String to Monotone Increasing](https://leetcode.com/problems/flip-string-to-monotone-increasing/) | Dynamic Programming| Time: O(n), Space: O(1) | Medium |
| 927 | [Three Equal Parts](https://leetcode.com/problems/three-equal-parts/)   | Array, Simulation | Time: O(n), Space: O(1) | Hard |
| 928 | [Minimize Malware Spread II](https://leetcode.com/problems/minimize-malware-spread-ii/) | Graph, DFS, Simulation| Time: O(n^2), Space: O(n) | Hard |
| 929 | [Unique Email Addresses](https://leetcode.com/problems/unique-email-addresses/) | String, Hash Set  | Time: O(n), Space: O(n) | Easy |
| 930 | [Binary Subarrays With Sum](https://leetcode.com/problems/binary-subarrays-with-sum/) | DP, Sliding Window| Time: O(n), Space: O(n) | Medium |
| 931 | [Minimum Falling Path Sum](https://leetcode.com/problems/minimum-falling-path-sum/) | DP, Matrix   | Time: O(n^2), Space: O(n^2) | Medium |
| 932 | [Beautiful Array](https://leetcode.com/problems/beautiful-array/) | Divide and Conquer | Time: O(n log n), Space: O(n) | Medium |
| 933 | [Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/) | Queue | Time: O(1), Space: O(n) | Easy |
| 934 | [Shortest Bridge](https://leetcode.com/problems/shortest-bridge/) | BFS, DFS | Time: O(n^2), Space: O(n) | Medium |
| 935 | [Knight Dialer](https://leetcode.com/problems/knight-dialer/)   | Dynamic Programming| Time: O(n), Space: O(1) | Medium |
| 936 | [Stamping the Sequence](https://leetcode.com/problems/stamping-the-sequence/) | DFS | Time: O(n^2), Space: O(n) | Hard |
| 937 | [Reorder Data in Log Files](https://leetcode.com/problems/reorder-data-in-log-files/) | Sorting, String   | Time: O(n log n), Space: O(1) | Medium |
| 938 | [Range Sum of BST](https://leetcode.com/problems/range-sum-of-bst/) | Tree, DFS, BST | Time: O(n), Space: O(n) | Easy |
| 939 | [Minimum Area Rectangle](https://leetcode.com/problems/minimum-area-rectangle/) | Hash Set, Geometry | Time: O(n^2), Space: O(n) | Medium |
| 940 | [Distinct Subsequences II](https://leetcode.com/problems/distinct-subsequences-ii/) | DP, String   | Time: O(n^2), Space: O(n) | Hard |
| 941 | [Valid Mountain Array](https://leetcode.com/problems/valid-mountain-array/)   | Array | Time: O(n), Space: O(1) | Easy |
| 942 | [DI String Match](https://leetcode.com/problems/di-string-match/) | Array | Time: O(n), Space: O(1) | Easy |
| 943 | [Shortest Distance to a Character](https://leetcode.com/problems/shortest-distance-to-a-character/) | String, Array | Time: O(n), Space: O(1) | Easy |
| 944 | [Delete Column to Make Sorted](https://leetcode.com/problems/delete-column-to-make-sorted/) | Array | Time: O(n * m), Space: O(1) | Easy |
| 945 | [Minimum Increment to Make Array Unique](https://leetcode.com/problems/minimum-increment-to-make-array-unique/) | Array, Hash Set   | Time: O(n log n), Space: O(n) | Medium |
| 946 | [Validate Stack Sequences](https://leetcode.com/problems/validate-stack-sequences/) | Stack | Time: O(n), Space: O(n) | Medium |
| 947 | [Most Stones Removed with Same Row or Column](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/) | Graph, DFS  | Time: O(n), Space: O(n) | Medium |
| 948 | [Bag of Tokens](https://leetcode.com/problems/bag-of-tokens/)   | Greedy | Time: O(n log n), Space: O(1) | Medium |
| 949 | [Largest Time for Given Digits](https://leetcode.com/problems/largest-time-for-given-digits/) | Math | Time: O(1), Space: O(1) | Medium |
| 950 | [Reveal Cards In Increasing Order](https://leetcode.com/problems/reveal-cards-in-increasing-order/) | Queue | Time: O(n log n), Space: O(n) | Medium |
| 951 | [Flip Equivalent Binary Trees](https://leetcode.com/problems/flip-equivalent-binary-trees/) | Tree, Recursion| Time: O(n), Space: O(n) | Medium |
| 952 | [Largest Component Size by Common Factor](https://leetcode.com/problems/largest-component-size-by-common-factor/) | Union Find   | Time: O(n log n), Space: O(n) | Hard |
| 953 | [Verifying an Alien Dictionary](https://leetcode.com/problems/verifying-an-alien-dictionary/) | String | Time: O(n), Space: O(1) | Easy |
| 954 | [Array of Doubled Pairs](https://leetcode.com/problems/array-of-doubled-pairs/) | Hash Map, Sorting | Time: O(n log n), Space: O(n) | Medium |
| 955 | [Delete Columns to Make Sorted II](https://leetcode.com/problems/delete-columns-to-make-sorted-ii/) | Array, Sorting| Time: O(n log n), Space: O(1) | Medium |
| 956 | [Tallest Billboard](https://leetcode.com/problems/tallest-billboard/)   | DP, Bitmask  | Time: O(n * sum), Space: O(sum) | Hard |
| 957 | [Prison Cells After N Days](https://leetcode.com/problems/prison-cells-after-n-days/) | Array, Simulation | Time: O(n), Space: O(1) | Medium |
| 958 | [Check Completeness of a Binary Tree](https://leetcode.com/problems/check-completeness-of-a-binary-tree/) | Tree, BFS| Time: O(n), Space: O(n) | Medium |
| 959 | [Regions Cut By Slashes](https://leetcode.com/problems/regions-cut-by-slashes/) | DFS | Time: O(n^2), Space: O(n^2) | Hard |
| 960 | [Delete Columns to Make Sorted III](https://leetcode.com/problems/delete-columns-to-make-sorted-iii/) | Array, Sorting| Time: O(n log n), Space: O(1) | Medium |
| 961 | [N-Repeated Element in Size 2N Array](https://leetcode.com/problems/n-repeated-element-in-size-2n-array/) | Array, Hash Set   | Time: O(n), Space: O(n) | Easy |
| 962 | [Maximum Width Ramp](https://leetcode.com/problems/maximum-width-ramp/) | Stack | Time: O(n), Space: O(n) | Medium |
| 963 | [Minimum Area Rectangle II](https://leetcode.com/problems/minimum-area-rectangle-ii/) | DP, Geometry, Sort| Time: O(n log n), Space: O(n) | Hard |
| 964 | [Least Operators to Express Number](https://leetcode.com/problems/least-operators-to-express-number/) | Math | Time: O(log n), Space: O(1) | Medium |
| 965 | [Univalued Binary Tree](https://leetcode.com/problems/univalued-binary-tree/) | Tree, DFS   | Time: O(n), Space: O(n) | Easy |
| 966 | [Vowel Spellchecker](https://leetcode.com/problems/vowel-spellchecker/) | String, Hash Set  | Time: O(n), Space: O(n) | Medium |
| 967 | [Numbers With Same Consecutive Differences](https://leetcode.com/problems/numbers-with-same-consecutive-differences/) | DP, Backtracking  | Time: O(2^n), Space: O(1) | Hard |
| 968 | [Binary Tree Cameras](https://leetcode.com/problems/binary-tree-cameras/) | Tree, DP| Time: O(n), Space: O(n) | Hard |
| 969 | [Pancake Sorting](https://leetcode.com/problems/pancake-sorting/) | Sorting, Stack| Time: O(n^2), Space: O(n) | Medium |
| 970 | [Powerful Integers](https://leetcode.com/problems/powerful-integers/)   | Math | Time: O(log N), Space: O(1) | Medium |
| 971 | [Flip Binary Tree To Match Preorder Traversal](https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/) | Tree, Recursion| Time: O(n), Space: O(n) | Hard |
| 972 | [Equal Rational Numbers](https://leetcode.com/problems/equal-rational-numbers/) | Math | Time: O(1), Space: O(1) | Hard |
| 973 | [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | Heap, Sorting | Time: O(n log k), Space: O(k) | Medium |
| 974 | [Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/) | Hash Map, Array   | Time: O(n), Space: O(n) | Medium |
| 975 | [Odd Even Jump](https://leetcode.com/problems/odd-even-jump/)   | DP, Stack| Time: O(n log n), Space: O(n) | Hard |
| 976 | [Largest Perimeter Triangle](https://leetcode.com/problems/largest-perimeter-triangle/) | Array, Sorting| Time: O(n log n), Space: O(1) | Easy |
| 977 | [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) | Two Pointers, Array| Time: O(n), Space: O(1) | Easy |
| 978 | [Longest Turbulent Subarray](https://leetcode.com/problems/longest-turbulent-subarray/) | Two Pointers, Sliding Window| Time: O(n), Space: O(1) | Medium |
| 979 | [Distribute Coins in Binary Tree](https://leetcode.com/problems/distribute-coins-in-binary-tree/) | Tree, DFS| Time: O(n), Space: O(n) | Medium |
| 980 | [Unique Paths III](https://leetcode.com/problems/unique-paths-iii/) | Backtracking, DFS  | Time: O(n^2), Space: O(n^2) | Hard |
| 981 | [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) | Hash Map, BST| Time: O(1), Space: O(n) | Medium |
| 982 | [Triples with Sum Less Than Target](https://leetcode.com/problems/triples-with-sum-less-than-target/) | Sorting, Two Pointers| Time: O(n^2), Space: O(1) | Medium |
| 983 | [Minimum Cost For Tickets](https://leetcode.com/problems/minimum-cost-for-tickets/) | DP, Array| Time: O(n), Space: O(n) | Medium |
| 984 | [String Without AAA or BBB](https://leetcode.com/problems/string-without-aaa-or-bbb/) | String | Time: O(n), Space: O(1) | Medium |
| 985 | [Sum of Even Numbers After Queries](https://leetcode.com/problems/sum-of-even-numbers-after-queries/) | Array | Time: O(n), Space: O(1) | Easy |
| 986 | [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/) | Two Pointers, Sorting | Time: O(n), Space: O(1) | Medium |
| 987 | [Vertical Order Traversal of a Binary Tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/) | Tree, BFS   | Time: O(n log n), Space: O(n) | Hard |
| 988 | [Smallest String Starting From Leaf](https://leetcode.com/problems/smallest-string-starting-from-leaf/) | Tree, DFS   | Time: O(n), Space: O(n) | Medium |
| 989 | [Add to Array-Form of Integer](https://leetcode.com/problems/add-to-array-form-of-integer/) | Array | Time: O(n), Space: O(1) | Easy |
| 990 | [Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/) | Union Find, Graph  | Time: O(n), Space: O(n) | Medium |
| 991 | [Broken Calculator](https://leetcode.com/problems/broken-calculator/)   | Math | Time: O(log n), Space: O(1) | Medium |
| 992 | [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/) | Sliding Window, Hash Map  | Time: O(n), Space: O(k) | Hard |
| 993 | [Cousins in Binary Tree](https://leetcode.com/problems/cousins-in-binary-tree/) | Tree, BFS, DFS| Time: O(n), Space: O(n) | Easy |
| 994 | [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | BFS, Queue   | Time: O(n^2), Space: O(n) | Medium |
| 995 | [Minimum Number of K Consecutive Bit Flips](https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/) | Greedy, Sliding Window| Time: O(n), Space: O(1) | Hard |
| 996 | [Number of Squareful Arrays](https://leetcode.com/problems/number-of-squareful-arrays/) | Backtracking | Time: O(n!), Space: O(n) | Hard |
| 997 | [Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/) | Graph, DFS, In-degree | Time: O(n), Space: O(n) | Easy |
| 998 | [Maximum Binary Tree II](https://leetcode.com/problems/maximum-binary-tree-ii/) | Tree | Time: O(n), Space: O(n) | Medium |
| 999 | [Available Captures for Rook](https://leetcode.com/problems/available-captures-for-rook/) | Math | Time: O(1), Space: O(1) | Easy |
| 1000 | [📓 Minimum Cost to Merge Stones](../leetcode/1000.ipynb) | <span title="Split intervals at every k-1 step and use prefix sums to accumulate merge costs in a bottom-up DP table.">Interval DP</span> | O(n^3/k) Time, O(n^2) Space | Hard |
| 1001 | [Grid Illuminated](https://leetcode.com/problems/grid-illuminated/) | Graph, DFS   | Time: O(n), Space: O(n) | Hard |
| 1002 | [Find Common Characters](https://leetcode.com/problems/find-common-characters/) | String | Time: O(n), Space: O(1) | Easy |
| 1003 | [Check If Word Is Valid After Substitutions](https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/) | Stack | Time: O(n), Space: O(n) | Medium |
| 1004 | [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) | Sliding Window, Array| Time: O(n), Space: O(1) | Medium |
| 1005 | [Maximize Sum of Array After K Negations](https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/) | Greedy | Time: O(n log n), Space: O(1) | Medium |
| 1006 | [Clumsy Factorial](https://leetcode.com/problems/clumsy-factorial/) | Math | Time: O(log n), Space: O(1) | Medium |
| 1007 | [Minimum Domino Rotations For Equal Row](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/) | Greedy, Sorting   | Time: O(n), Space: O(1) | Medium |
| 1008 | [Construct Binary Search Tree from Preorder Traversal](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/) | Tree, BST| Time: O(n), Space: O(n) | Medium |
| 1009 | [Complement of Base 10 Integer](https://leetcode.com/problems/complement-of-base-10-integer/) | Math | Time: O(log n), Space: O(1) | Easy |
| 1010 | [Pairs of Songs With Total Durations Divisible by 60](https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/) | Hash Map| Time: O(n), Space: O(n) | Medium |
| 1011 | [📓 Capacity To Ship Packages Within D Days](../leetcode/1011.ipynb) | <span title="Greedily simulate a feasibility check (e.g., days or capacity) inside a binary-search loop.">Binary Search, Greedy</span> | Time: O(n log m), Space: O(1) | Medium |
| 1012 | [Numbers With Repeated Digits](https://leetcode.com/problems/numbers-with-repeated-digits/) | Math | Time: O(log n), Space: O(1) | Hard |
| 1013 | [📓 Partition Array Into Three Parts With Equal Sum](../leetcode/1013.ipynb) | <span title="Compute total sum divided by 3, then scan left-to-right counting how many times the running sum hits each target multiple.">Array, Prefix Sum</span> | Time: O(n), Space: O(1) | Medium |
| 1014 | [Best Sightseeing Pair](https://leetcode.com/problems/best-sightseeing-pair/)  | Sliding Window, Two Pointers | Time: O(n), Space: O(1) | Medium |
| 1015 | [📓 Swim in Rising Water](../leetcode/1015.ipynb) | <span title="Use a min-heap to greedily expand the lowest-elevation unvisited cell; track the running max elevation to reach (n-1,n-1).">Dijkstra (Min-Heap)</span> | Time: O(n^2 log n), Space: O(n^2) | Hard |
| 1016 | [📓 Subarray Sums Divisible by K](../leetcode/1016.ipynb) | <span title="Track prefix-sum remainders mod k; a repeated remainder means the subarray between those indices sums to a multiple of k.">Prefix Sum + Hash Map</span> | O(n) Time, O(k) Space | Medium |
| 1017 | [Convert to Base -2](https://leetcode.com/problems/convert-to-base-2/)   | Math | Time: O(log n), Space: O(1) | Medium |
| 1018 | [Binary Prefix Divisible By 5](https://leetcode.com/problems/binary-prefix-divisible-by-5/) | String | Time: O(n), Space: O(1) | Medium |
| 1019 | [Next Greater Node In Linked List](https://leetcode.com/problems/next-greater-node-in-linked-list/) | Stack | Time: O(n), Space: O(n) | Medium |
| 1020 | [📓 Number of Enclaves](../leetcode/1020.ipynb) | <span title="Flood-fill from border land cells to mark escapable regions; count remaining unvisited land cells as enclaves.">DFS, Flood-Fill</span> | Time: O(mn), Space: O(mn) | Medium |
| 1021 | [Remove Outermost Parentheses](https://leetcode.com/problems/remove-outermost-parentheses/) | String | Time: O(n), Space: O(1) | Easy |
| 1022 | [Sum of Root To Leaf Binary Numbers](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/) | Tree, DFS   | Time: O(n), Space: O(n) | Easy |
| 1023 | [Camelcase Matching](https://leetcode.com/problems/camelcase-matching/) | String, Array| Time: O(n), Space: O(1) | Medium |
| 1024 | [📓 Video Stitching](../leetcode/1024.ipynb) | <span title="Sort clips by start time; greedily pick the clip extending coverage farthest at each step, counting selections.">Greedy Interval Cover</span> | O(n log n) Time, O(1) Space | Medium |
| 1025 | [Divisor Game](https://leetcode.com/problems/divisor-game/) | Math | Time: O(log n), Space: O(1) | Easy |
| 1026 | [Tree Sister](https://leetcode.com/problems/tree-sister/) | Tree, DFS | Time: O(n), Space: O(n) | Easy |
| 1027 | [📓 Longest Arithmetic Subsequence](../leetcode/1027.ipynb) | <span title="dp[i] maps each arithmetic difference to the longest subsequence length ending at index i; extend for each (j,i) pair">DP with HashMap</span> | Time: O(n), Space: O(n) | Easy |
| 1028 | [Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves/) | Tree, DFS   | Time: O(n), Space: O(n) | Easy |
| 1029 | [📓 Two City Scheduling](../leetcode/1029.ipynb) | <span title="Sort people by cost difference (A minus B); send the cheapest-A half to city A and the rest to city B.">Greedy Sort</span> | O(n log n) Time, O(1) Space | Medium |
| 1030 | [📓 Matrix Cells in Distance Order](../leetcode/1030.ipynb) | <span title="BFS from the center cell naturally yields cells in non-decreasing Manhattan-distance order with no sorting needed.">BFS</span> | O(R*C) Time, O(R*C) Space | Easy |
| 1031 | [📓 Maximum Sum of Two Non-Overlapping Subarrays](../leetcode/1031.ipynb) | <span title="Slide the second window forward while tracking the max first-window sum seen before it; try both orderings.">Prefix Sum + Rolling Max</span> | O(n) Time, O(n) Space | Medium |
| 1032 | [📓 Stream of Characters](../leetcode/1032.ipynb) | <span title="Insert reversed words into a Trie; on each query advance all active suffix-match states one step, returning true if any reaches a terminal node.">Reverse Trie</span> | O(W*L + Q*L) Time, O(W*L) Space | Hard |
| 1033 | [📓 Matrix Block Sum](../leetcode/1033.ipynb) | <span title="Precompute rectangle sums so any submatrix query is answered in O(1) with inclusion-exclusion.">2D Prefix Sum</span> | Time: O(m * n), Space: O(m * n)  | Medium |
| 1034 | [Edge List to Adj List Conversion](https://leetcode.com/problems/edge-list-to-adj-list-conversion/) | Graph, Adjacency List| Time: O(E), Space: O(V)| Medium |
| 1035 | [📓 Uncrossed Lines](../leetcode/1035.ipynb) | <span title="Non-crossing lines correspond to matching value pairs in order — equivalent to LCS of the two arrays">LCS DP</span> | Time: O(m * n), Space: O(m * n)  | Medium |
| 1036 | [Escape a Large Maze](https://leetcode.com/problems/escape-a-large-maze/) | Graph, BFS | Time: O(n), Space: O(n)| Medium |
| 1037 | [Valid Boomerang](https://leetcode.com/problems/valid-boomerang/) | Math, Geometry | Time: O(1), Space: O(1)| Easy |
| 1038 | [Binary Search Tree to Greater Sum Tree](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/) | Tree, DFS| Time: O(n), Space: O(n)| Medium |
| 1039 | [📓 Minimum Score Triangulation of Polygon](../leetcode/1039.ipynb) | <span title="dp[i][j] is the min cost to triangulate vertices i..j; try every interior vertex k as the apex of the spanning triangle.">Interval DP</span> | O(n^3) Time, O(n^2) Space | Medium |
| 1040 | [Moving Stones Until Consecutive](https://leetcode.com/problems/moving-stones-until-consecutive/)  | Simulation, Sorting   | Time: O(1), Space: O(1)| Easy |
| 1041 | [Robot Bounded In Circle](https://leetcode.com/problems/robot-bounded-in-circle/)| Simulation | Time: O(1), Space: O(1)| Medium |
| 1042 | [Friendship Requests I: Individual Contributions](https://leetcode.com/problems/friendship-requests-i-individual-contributions/) | Graph, Union Find| Time: O(n * log n), Space: O(n)  | Medium |
| 1043 | [📓 Partition Array for Maximum Sum](../leetcode/1043.ipynb) | <span title="Slide a window of up to k elements backward from each position, filling it with its maximum, and carry the best prefix total forward.">1-D DP</span> | O(n*k) Time, O(n) Space | Medium |
| 1044 | [Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/)| String, Binary Search, Hashing| Time: O(n log n), Space: O(n)| Hard |
| 1045 | [Customer Orders Availability System](https://leetcode.com/problems/customer-orders-availability-system/) | Graph, Adjacency List | Time: O(n^2), Space: O(n)  | Medium |
| 1046 | [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)   | Heap, Priority Queue | Time: O(n log n), Space: O(n)| Easy |
| 1047 | [Remove All Adjacent Duplicates In String II](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/) | Stack | Time: O(n), Space: O(n)| Medium |
| 1048 | [📓 Longest String Chain](../leetcode/1048.ipynb) | <span title="Sort words by length; for each word try all single-deletion predecessors in a hash map to extend the longest chain.">DP + Sort + Hash Map</span> | O(n*L^2) Time, O(n*L) Space | Medium |
| 1049 | [📓 Last Stone Weight II](../leetcode/1049.ipynb) | <span title="Reduce to partition problem: maximize subset sum up to total/2 with a boolean knapsack; answer is total minus twice that max.">0/1 Knapsack DP</span> | O(n*S) Time, O(S) Space | Medium |
| 1050 | [Animals in a Zoo](https://leetcode.com/problems/animals-in-a-zoo/) | Simulation | Time: O(1), Space: O(1)| Easy |
| 1051 | [Height Checker](https://leetcode.com/problems/height-checker/)| Sorting| Time: O(n log n), Space: O(1)| Easy |
| 1052 | [Grumpy Bookstore Owner](https://leetcode.com/problems/grumpy-bookstore-owner/) | Sliding Window, Greedy | Time: O(n), Space: O(1)| Medium |
| 1053 | [📓 Previous Permutation With One Swap](../leetcode/1053.ipynb) | <span title="Scan from the right for the first descent, then swap with the leftmost occurrence of the largest valid smaller element.">Array, Sorting</span>| Time: O(n), Space: O(1)| Medium |
| 1054 | [Distant Barcodes](https://leetcode.com/problems/distant-barcodes/) | Greedy, Sorting| Time: O(n log n), Space: O(n)| Medium |
| 1055 | [📓 Shortest Way to Form String](../leetcode/1055.ipynb) | <span title="Precompute nxt[i][c] = next position of char c at or after i in source; jump to it in O(1) per target character">Next-Char Index Table</span> | Time: O(n * m), Space: O(n * m)  | Hard |
| 1056 | [Confusing Number](https://leetcode.com/problems/confusing-number/)| Math, Simulation | Time: O(1), Space: O(1)| Easy |
| 1057 | [Campus Bikes](https://leetcode.com/problems/campus-bikes/)| Greedy | Time: O(n log n), Space: O(1)| Medium |
| 1058 | [Minimize Rounding Errors](https://leetcode.com/problems/minimize-rounding-errors/)  | Math, Simulation | Time: O(n), Space: O(1)| Medium |
| 1059 | [The K Weakest Rows in a Matrix](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/)| Sorting| Time: O(m log m), Space: O(1)| Easy |
| 1060 | [📓 Missing Element in Sorted Array](../leetcode/1060.ipynb) | <span title="Count how many numbers are missing up to index i; binary search for the boundary.">Binary Search on Missing Count</span> | Time: O(log n), Space: O(1) | Medium |
| 1061 | [Lexicographically Smallest Equivalent String](https://leetcode.com/problems/lexicographically-smallest-equivalent-string/) | Union Find   | Time: O(n), Space: O(n)| Medium |
| 1062 | [📓 Longest Repeating Substring](../leetcode/1062.ipynb) | <span title="Binary search on length; use rolling hash or suffix array to detect duplicate substrings.">Binary Search, String</span> | Time: O(n log n), Space: O(n)| Hard |
| 1063 | [📓 Valid Triangles](../leetcode/1063.ipynb) | <span title="Sort the array, then fix the largest side and use two pointers to count pairs whose sum exceeds it.">Array, Math</span>| Time: O(n^3), Space: O(1)  | Medium |
| 1064 | [📓 Fixed Point](../leetcode/1064.ipynb) | <span title="arr[i]-i is strictly increasing; binary search on this monotone function to find the smallest fixed-point index">Binary Search</span> | Time: O(n), Space: O(n)| Medium |
| 1065 | [Train System](https://leetcode.com/problems/train-system/)| Graph, BFS | Time: O(n^2), Space: O(n)  | Medium |
| 1066 | [📓 Campus Bikes II](../leetcode/1066.ipynb) | <span title="Represent assigned bikes as a bitmask; the set-bit count determines the next worker, so each state transitions to m new states in one pass.">Bitmask DP</span> | O(2^m * m) Time, O(2^m) Space | Hard |
| 1067 | [📓 Digit Count in Range](../leetcode/1067.ipynb) | <span title="Count digit d in [0..n] using place-value decomposition; apply prefix subtraction f(high)-f(low-1).">Digit DP</span> | Time: O(log n), Space: O(1) | Hard |
| 1068 | [Largest Palindromic Substring](https://leetcode.com/problems/largest-palindromic-substring/) | DP, String | Time: O(n^2), Space: O(n^2)| Medium |
| 1069 | [Minimum Swap to Make Strings Equal](https://leetcode.com/problems/minimum-swap-to-make-strings-equal/) | Greedy| Time: O(n), Space: O(1)| Medium |
| 1070 | [Largest BST Subtree](https://leetcode.com/problems/largest-bst-subtree/)| Tree, DFS| Time: O(n), Space: O(n)| Medium |
| 1071 | [Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/) | Math, String   | Time: O(n), Space: O(1)| Easy |
| 1072 | [Flip Columns For Maximum Number of Equal Rows](https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/) | Greedy, Hash Map| Time: O(m * n), Space: O(m)| Medium |
| 1073 | [Adding Two Negabinary Numbers](https://leetcode.com/problems/adding-two-negabinary-numbers/) | Math, Array| Time: O(n), Space: O(n)| Medium |
| 1074 | [📓 Number of Submatrices That Sum to Target](../leetcode/1074.ipynb) | <span title="2D prefix sums for rectangle totals combined with a hash map to count target-sum submatrices.">2D Prefix Sum + Hash Map</span> | Time: O(n^3), Space: O(n^2)| Hard |
| 1075 | [Project Employees](https://leetcode.com/problems/project-employees/)   | Simulation, Hash Map | Time: O(n), Space: O(n)| Medium |
| 1076 | [📓 Project Employees II](../leetcode/1076.ipynb) | <span title="Group employees by project, find the maximum count, then return all projects tied at that count.">Aggregation JOIN</span> | Time: $O(n \log n)$, Space: $O(n)$ | Easy |
| 1077 | [Project Management](https://leetcode.com/problems/project-management/) | DP, Graph| Time: O(n), Space: O(n)| Hard |
| 1078 | [Smallest Subtree with all the Deepest Nodes](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/) | Tree, DFS| Time: O(n), Space: O(n)| Medium |
| 1079 | [Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/) | Graph, DFS, In-degree| Time: O(n), Space: O(n)| Easy |
| 1080 | [📓 Insufficient Nodes in Root to Leaf Paths](../leetcode/1080.ipynb) | <span title="Subtract each node's value from the limit as DFS descends, then prune leaves and childless internals that can never satisfy the threshold.">DFS Post-Order Pruning</span> | O(n) Time, O(h) Space | Medium |
| 1081 | [Smallest Subtree with all the Deepest Nodes](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/) | Tree, DFS| Time: O(n), Space: O(n)| Medium |
| 1082 | [Special Array With X Elements Greater Than or Equal X](https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/) | Sorting, Binary Search | Time: O(n log n), Space: O(1)| Easy |
| 1083 | [Ancient Chinese Remainder](https://leetcode.com/problems/ancient-chinese-remainder/) | Math, Simulation | Time: O(1), Space: O(1)| Medium |
| 1084 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/)   | Hash Map, String | Time: O(n * k log k), Space: O(n) | Medium |
| 1085 | [Sum of Digits in the Minimum Number](https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/) | Math, String| Time: O(1), Space: O(1)| Easy |
| 1086 | [📓 High Five](../leetcode/1086.ipynb) | <span title="Sort by (id asc, score desc), then take the first 5 scores per student in one linear pass">Sort + Group</span> | Time: O(n^2), Space: O(n^2)| Hard |
| 1087 | [📓 Design Tic-Tac-Toe](../leetcode/1087.ipynb) | <span title="Use per-row, per-column, and diagonal integer counters to detect wins in O(1) per move.">Array, Simulation</span>| Time: O(1), Space: O(1)| Easy |
| 1088 | [Validate IP Address](https://leetcode.com/problems/validate-ip-address/) | String | Time: O(1), Space: O(1)| Medium |
| 1089 | [📓 Duplicate Zeros](../leetcode/1089.ipynb) | <span title="Count zeros first, then fill backwards from right using a virtual extended index to duplicate each zero in-place.">Two-Pass In-Place</span>| Time: O(n), Space: O(1)| Easy |
| 1090 | [📓 Largest Element in an Array](../leetcode/1090.ipynb) | <span title="Scan the array once tracking the running maximum, updating whenever a larger element is found.">Single Pass</span>| Time: O(n), Space: O(1)| Easy |
| 1091 | [Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | BFS, Graph | Time: O(n^2), Space: O(n^2)| Medium |
| 1092 | [📓 Shortest Common Supersequence](../leetcode/1092.ipynb) | <span title="Build LCS DP table then traceback to merge both strings around LCS characters into the shortest supersequence.">DP (LCS)</span> | Time: $O(m \cdot n)$, Space: $O(m \cdot n)$ | Hard |
| 1093 | [Car Pooling](https://leetcode.com/problems/car-pooling/) | Greedy, Simulation| Time: O(n), Space: O(1)| Medium |
| 1094 | [📓 Car Pooling](../leetcode/1094.ipynb) | <span title="Apply passenger deltas at trip endpoints in a difference array; prefix-sum scan detects capacity violations.">Difference Array</span> | Time: $O(n)$, Space: $O(1)$ | Medium |
| 1095 | [📓 Find in Mountain Array](../leetcode/1095.ipynb) | <span title="Find mountain peak, then binary search the ascending half, then the descending half.">Three Binary Searches</span> | Time: O(log n), Space: O(1) | Medium |
| 1096 | [Brace Expansion II](https://leetcode.com/problems/brace-expansion-ii/) | String | Time: O(n!), Space: O(n)| Hard |
| 1097 | [Game of Life](https://leetcode.com/problems/game-of-life/) | Simulation | Time: O(n * m), Space: O(1)| Medium |
| 1098 | [📓 Sort the Matrix Diagonally](../leetcode/1098.ipynb) | <span title="Group cells by diagonal key (row minus col), sort each group, then scatter values back in traversal order.">Diagonal Grouping</span>| Time: O(n^2 log n), Space: O(n^2)| Medium |
| 1099 | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Two Pointers| Time: O(n), Space: O(1)| Easy |
| 1100 | [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | Sliding Window, Hash Map | Time: O(n), Space: O(1)| Medium |
| 1101 | [Path Crossing](https://leetcode.com/problems/path-crossing/) | Simulation, Graph| Time: O(n), Space: O(n)| Medium |
| 1102 | [Path Sum IV](https://leetcode.com/problems/path-sum-iv/) | Tree, DFS| Time: O(n), Space: O(n)| Easy |
| 1103 | [Distribute Candies to People](https://leetcode.com/problems/distribute-candies-to-people/)   | Math, Simulation | Time: O(n), Space: O(1)| Easy |
| 1104 | [Path In Zigzag Labelled Binary Tree](https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/) | Tree, BFS| Time: O(log n), Space: O(log n)  | Medium |
| 1105 | [📓 Filling Bookcase Shelves](../leetcode/1105.ipynb) | <span title="dp[i] = min shelf height for first i books; scan backwards adding books to the current shelf until width is exceeded.">1-D DP</span> | O(n^2) Time, O(n) Space | Medium |
| 1106 | [Parsing A Boolean Expression](https://leetcode.com/problems/parsing-a-boolean-expression/)   | Stack, String  | Time: O(n), Space: O(n)| Medium |
| 1107 | [Gift Card Purchase](https://leetcode.com/problems/gift-card-purchase/) | DP, Knapsack   | Time: O(n^2), Space: O(n)  | Medium |
| 1108 | [📓 IP Address to CIDR](../leetcode/1108.ipynb) | <span title="Greedily take the largest power-of-two-aligned CIDR block fitting the current IP and count.">Greedy Largest Aligned Block</span> | Time: O(1), Space: O(1)| Medium |
| 1109 | [📓 Corporate Flight Bookings](../leetcode/1109.ipynb) | <span title="Mark +seats at booking start and -seats one past the end; a single prefix-sum pass yields per-flight counts.">Difference Array</span> | Time: $O(n + m)$, Space: $O(1)$ | Medium |
| 1110 | [Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/) | Tree, BST| Time: O(log n), Space: O(1)| Medium |
| 1111 | [Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/) | Tree, BST  | Time: O(log n), Space: O(1)| Medium |
| 1112 | [Smallest Subtree with all the Deepest Nodes](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/) | Tree, DFS  | Time: O(n), Space: O(n)| Medium |
| 1113 | [📓 Intersection of Three Sorted Arrays](../leetcode/1113.ipynb) | <span title="Advance the pointer pointing at the smallest value; record and advance all three when they agree.">Three Pointers</span> | Time: $O(n)$, Space: $O(1)$ | Easy |
| 1114 | [Print in Order](https://leetcode.com/problems/print-in-order/) | DFS, Multi-threading | Time: O(1), Space: O(1)| Easy |
| 1115 | [Print Foo Bar Alternately](https://leetcode.com/problems/print-foo-bar-alternately/) | DFS, Multi-threading | Time: O(1), Space: O(1)| Medium |
| 1116 | [Print Zero Even Odd](https://leetcode.com/problems/print-zero-even-odd/)   | Multi-threading | Time: O(1), Space: O(1)| Medium |
| 1117 | [Building H2O](https://leetcode.com/problems/building-h2o/)   | Multi-threading | Time: O(1), Space: O(1)| Medium |
| 1118 | [Number of Days in a Month](https://leetcode.com/problems/number-of-days-in-a-month/) | Math, Array | Time: O(1), Space: O(1)| Easy |
| 1119 | [Remove Vowels from a String](https://leetcode.com/problems/remove-vowels-from-a-string/) | String| Time: O(n), Space: O(1)| Easy |
| 1120 | [Path Sum III](https://leetcode.com/problems/path-sum-iii/)   | Tree, DFS   | Time: O(n), Space: O(n)| Medium |
| 1121 | [Divide Array in Sets of K Consecutive Numbers](https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/) | Greedy, Hash Map| Time: O(n), Space: O(n)| Medium |
| 1122 | [Relative Sort Array](https://leetcode.com/problems/relative-sort-array/)   | Sorting, Hash Map   | Time: O(n log n), Space: O(n)| Easy |
| 1123 | [Lowest Common Ancestor of Deepest Leaves](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/) | Tree, DFS   | Time: O(n), Space: O(n)| Medium |
| 1124 | [Longest Well-Performing Interval](https://leetcode.com/problems/longest-well-performing-interval/) | Hash Map, Array | Time: O(n), Space: O(n)| Medium |
| 1125 | [📓 Smallest Sufficient Team](../leetcode/1125.ipynb) | <span title="Bitmask each skill set; dp[mask] tracks the smallest team covering exactly the skills in mask.">Bitmask DP over Skill Sets</span> | Time: O(n), Space: O(n)| Hard |
| 1126 | [Active Businesses](https://leetcode.com/problems/active-businesses/) | Simulation, Array   | Time: O(n), Space: O(n)| Medium |
| 1127 | [Mosaic Style Display](https://leetcode.com/problems/mosaic-style-display/) | DP, Matrix | Time: O(n^2), Space: O(n^2)| Medium |
| 1128 | [Number of Equivalent Domino Pairs](https://leetcode.com/problems/number-of-equivalent-domino-pairs/)   | Hash Map   | Time: O(n), Space: O(n)| Easy |
| 1129 | [📓 Shortest Path with Alternating Colors](../leetcode/1129.ipynb) | <span title="BFS over (node, last-color) states to find the shortest alternating-color path from node 0.">BFS (Color State)</span> | Time: $O(n + e)$, Space: $O(n + e)$ | Medium |
| 1130 | [📓 Minimum Cost Tree From Leaf Values](../leetcode/1130.ipynb) | <span title="Keep a decreasing stack; pair each local-minimum leaf with its smaller neighbour to minimise the parent node cost">Monotonic Stack</span> | Time: O(n^2), Space: O(n^2)| Hard |
| 1131 | [Maximum of Absolute Value Expression](https://leetcode.com/problems/maximum-of-absolute-value-expression/) | Math, Array| Time: O(n), Space: O(1)| Medium |
| 1132 | [Brothers From Different Roots](https://leetcode.com/problems/brothers-from-different-roots/) | Tree, DFS   | Time: O(n), Space: O(n)| Medium |
| 1133 | [📓 Largest Unique Number](../leetcode/1133.ipynb) | <span title="Count occurrences in a hash map in one pass, then return the largest key with exactly one occurrence.">Frequency Count</span>| Time: O(n), Space: O(n)| Easy |
| 1134 | [Armstrong Number](https://leetcode.com/problems/armstrong-number/)   | Math  | Time: O(n), Space: O(1)| Easy |
| 1135 | [📓 Connecting Cities With Minimum Cost](../leetcode/1135.ipynb) | <span title="Sort edges by cost and greedily union components; stop as soon as n-1 edges span all cities or declare disconnected.">Kruskal's MST (Union-Find)</span> | O(E log E) Time, O(V) Space | Medium |
| 1136 | [Parallel Courses](https://leetcode.com/problems/parallel-courses/)   | Graph, Topological Sort   | Time: O(n), Space: O(n)| Hard |
| 1137 | [📓 N-th Tribonacci Number](../leetcode/1137.ipynb) | <span title="Keep only the three most recent Tribonacci values and slide them forward each step, discarding the oldest.">Iterative Rolling Variables</span> | O(n) Time, O(1) Space | Easy |
| 1138 | [Alphabet Board Path](https://leetcode.com/problems/alphabet-board-path/)   | Simulation, String   | Time: O(n), Space: O(1)| Medium |
| 1139 | [📓 Largest 1-Bordered Square](../leetcode/1139.ipynb) | <span title="Precompute horizontal and vertical consecutive-1 arrays; check all four borders of each candidate square in O(1)">Prefix Sum DP</span> | Time: O(n^2), Space: O(n^2)| Medium |
| 1140 | [📓 Stone Game II](../leetcode/1140.ipynb) | <span title="Precompute suffix sums so any range total is O(1); dp[i][m] encodes the minimax gain as the max-of-remainder after the opponent plays optimally.">DP with Suffix Sums</span> | O(n^2) Time, O(n^2) Space | Medium |
| 1141 | [User Activity for the Past 30 Days I](https://leetcode.com/problems/user-activity-for-the-past-30-days-i/) | SQL  | Time: O(n), Space: O(n)| Easy |
| 1142 | [User Activity for the Past 30 Days II](https://leetcode.com/problems/user-activity-for-the-past-30-days-ii/) | SQL  | Time: O(n), Space: O(n)| Medium |
| 1143 | [📓 Longest Common Subsequence](../leetcode/1143.ipynb) | <span title="Fill a table where matching characters extend the diagonal and mismatches propagate the best of skipping one character from either string.">2-D DP Table</span> | O(m*n) Time, O(m*n) Space | Medium |
| 1144 | [📓 Decrease Elements To Make Array Zigzag](../leetcode/1144.ipynb) | <span title="For each of two valley-parity choices, sum the minimum decrements needed to push each valley strictly below both neighbors.">Greedy Per-Parity</span> | O(n) Time, O(1) Space | Medium |
| 1145 | [📓 Binary Tree Coloring Game](../leetcode/1145.ipynb) | <span title="One DFS counts left and right subtree sizes of x; the parent component is n minus those two minus one; player 2 wins if any component exceeds n/2.">DFS Subtree Count</span> | O(n) Time, O(h) Space | Medium |
| 1146 | [📓 Snapshot Array](../leetcode/1146.ipynb) | <span title="Store (snap_id, value) pairs per index; binary-search for the floor entry to answer get() in O(log s).">Binary Search on Snapshots</span>| Time: O(1), Space: O(n)| Medium |
| 1147 | [Longest Chunked Palindrome Decomposition](https://leetcode.com/problems/longest-chunked-palindrome-decomposition/) | Greedy, String   | Time: O(n^2), Space: O(n^2)| Hard |
| 1148 | [Article Views I](https://leetcode.com/problems/article-views-i/) | SQL  | Time: O(n), Space: O(n)| Easy |
| 1149 | [Article Views II](https://leetcode.com/problems/article-views-ii/)   | SQL  | Time: O(n), Space: O(n)| Medium |
| 1150 | [Split Array into Consecutive Subsequences](https://leetcode.com/problems/split-array-into-consecutive-subsequences/) | Greedy, Heap | Time: O(n log n), Space: O(n)| Hard |
| 1151 | [Minimum Swaps to Arrange a Binary String](https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-string/) | Greedy, Array| Time: O(n), Space: O(1)| Medium |
| 1152 | [Analyzing User Website Visit Pattern](https://leetcode.com/problems/analyzing-user-website-visit-pattern/) | SQL  | Time: O(n), Space: O(n)| Medium |
| 1153 | [A Fancy String](https://leetcode.com/problems/a-fancy-string/) | String| Time: O(n), Space: O(1)| Medium |
| 1154 | [Day of the Year](https://leetcode.com/problems/day-of-the-year/) | Integer, Array | O(1) Time, O(1) Space | Easy |
| 1155 | [📓 Number of Dice Rolls With Target Sum](../leetcode/1155.ipynb) | <span title="dp[s] = ways to reach sum s; roll one die at a time, distributing counts across k face additions">DP Rolling Array</span> | O(n * target) Time, O(n * target) Space | Medium |
| 1156 | [Swap For Longest Repeated Character Substring](https://leetcode.com/problems/swap-for-longest-repeated-character-substring/) | String, HashMap| O(n) Time, O(n) Space | Medium |
| 1157 | [Online Majority Element In Subarray](https://leetcode.com/problems/online-majority-element-in-subarray/) | HashMap, Queue | O(1) Time, O(n) Space | Hard |
| 1158 | [Market Analysis I](https://leetcode.com/problems/market-analysis-i/)   | HashMap, Array | O(n) Time, O(n) Space | Medium |
| 1159 | [Market Analysis II](https://leetcode.com/problems/market-analysis-ii/)  | HashMap, Array | O(n) Time, O(n) Space | Hard |
| 1160 | [Find Words That Can Be Formed by Characters](https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/) | HashMap, Set   | O(n) Time, O(n) Space | Easy |
| 1161 | [📓 Maximum Level Sum of a Binary Tree](../leetcode/1161.ipynb) | <span title="Queue-based BFS; collect all nodes at each depth before advancing to the next level.">BFS Level Order</span> | Time: O(n), Space: O(n) | Medium |
| 1162 | [As Far from Land as Possible](https://leetcode.com/problems/as-far-from-land-as-possible/) | Matrix, BFS| O(n * m) Time, O(n * m) Space | Medium |
| 1163 | [Last Substring in Lexicographical Order](https://leetcode.com/problems/last-substring-in-lexicographical-order/) | String, Stack  | O(n) Time, O(1) Space | Hard |
| 1164 | [Product Price at a Given Date](https://leetcode.com/problems/product-price-at-a-given-date/) | HashMap, Array | O(log n) Time, O(n) Space | Medium |
| 1165 | [Single-Row Keyboard](https://leetcode.com/problems/single-row-keyboard/) | String, HashMap| O(n) Time, O(1) Space | Easy |
| 1166 | [Design File System](https://leetcode.com/problems/design-file-system/) | Trie, HashMap  | O(n) Time, O(n) Space | Medium |
| 1167 | [Minimum Cost to Connect Sticks](https://leetcode.com/problems/minimum-cost-to-connect-sticks/) | Priority Queue, Array   | O(n log n) Time, O(n) Space | Medium |
| 1168 | [Optimize Water Distribution in a Village](https://leetcode.com/problems/optimize-water-distribution-in-a-village/) | Union-Find, Graph | O(n log n) Time, O(n) Space | Hard |
| 1169 | [Invalid Transactions](https://leetcode.com/problems/invalid-transactions/)   | HashMap, Set   | O(n) Time, O(n) Space | Medium |
| 1170 | [Compare Strings by Frequency of the Smallest Character](https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/) | String, HashMap| O(n) Time, O(n) Space | Easy |
| 1171 | [Remove Zero Sum Consecutive Nodes from Linked List](https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/) | Linked List, HashMap| O(n) Time, O(n) Space | Medium |
| 1172 | [Dinner Plate Stacks](https://leetcode.com/problems/dinner-plate-stacks/) | Stack, Priority Queue   | O(log n) Time, O(n) Space | Hard |
| 1173 | [Immediate Food Delivery I](https://leetcode.com/problems/immediate-food-delivery-i/) | HashMap, Array | O(n) Time, O(n) Space | Easy |
| 1174 | [Immediate Food Delivery II](https://leetcode.com/problems/immediate-food-delivery-ii/) | HashMap, Array | O(n) Time, O(n) Space | Medium |
| 1175 | [Prime Arrangements](https://leetcode.com/problems/prime-arrangements/) | Math, Factorization | O(n) Time, O(1) Space | Easy |
| 1176 | [📓 Diet Plan Performance](../leetcode/1176.ipynb) | <span title="Compute the first k-day window sum once, then slide by adding the incoming day and subtracting the outgoing day.">Sliding Window</span>| O(n) Time, O(n) Space | Easy |
| 1177 | [Can Make Palindrome from Substring](https://leetcode.com/problems/can-make-palindrome-from-substring/) | String, HashMap| O(n) Time, O(n) Space | Medium |
| 1178 | [Number of Valid Words for Each Puzzle](https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/) | Trie, Bitmasking| O(n) Time, O(n) Space | Hard |
| 1179 | [Reformat Department Table](https://leetcode.com/problems/reformat-department-table/) | SQL| O(n) Time, O(n) Space | Easy |
| 1180 | [Count Substrings with Only One Distinct Letter](https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/) | String, HashMap| O(n) Time, O(n) Space | Easy |
| 1181 | [Before and After Puzzle](https://leetcode.com/problems/before-and-after-puzzle/) | String, HashMap| O(n) Time, O(n) Space | Medium |
| 1182 | [📓 Shortest Distance to Target Color](../leetcode/1182.ipynb) | <span title="Left-to-right and right-to-left sweeps per color precompute distances so each query answers in O(1).">Two-Pass Precomputation</span>| O(n) Time, O(n) Space | Medium |
| 1183 | [📓 Maximum Number of Ones](../leetcode/1183.ipynb) | <span title="Count positions by tile-type (row mod sideLength, col mod sideLength), then greedily fill the most-common types first.">Array, HashMap</span>  | O(n) Time, O(n) Space | Hard |
| 1184 | [📓 Distance Between Bus Stops](../leetcode/1184.ipynb) | <span title="Sum the clockwise arc from source to destination and return the minimum of that and the total-minus-clockwise distance.">Array, Math</span> | O(n) Time, O(1) Space | Easy |
| 1185 | [Day of the Week](https://leetcode.com/problems/day-of-the-week/) | Integer | O(1) Time, O(1) Space | Easy |
| 1186 | [Maximum Subarray Sum with One Deletion](https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/) | Dynamic Programming, Array| O(n) Time, O(n) Space | Medium |
| 1187 | [📓 Make Two Arrays Equal by Reversing Subarrays](../leetcode/1187.ipynb) | <span title="Sort both arrays; any permutation is reachable via reversals, so equality of sorted forms implies transformability.">Array, Sorting</span> | O(n log n) Time, O(n) Space | Easy |
| 1188 | [Design a Stack With Increment Operation](https://leetcode.com/problems/design-a-stack-with-increment-operation/) | Stack, Array   | O(1) Time, O(n) Space | Medium |
| 1189 | [Maximum Number of Words Found in Sentences](https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/) | String, Array  | O(n) Time, O(1) Space | Easy |
| 1190 | [Reverse Substrings Between Each Pair of Parentheses](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/) | Stack, String  | O(n) Time, O(n) Space | Medium |
| 1191 | [📓 K Concatenation Maximum Sum](../leetcode/1191.ipynb) | <span title="Run Kadane on the double copy for cross-boundary subarrays, then add (k-2) times total sum when positive.">Kadane + Math</span>| O(n) Time, O(1) Space | Medium |
| 1192 | [Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/) | Graph, DFS, Union-Find | O(n + m) Time, O(n) Space | Hard |
| 1193 | [Maximum Profit of Operating a Centennial Wheel](https://leetcode.com/problems/maximum-profit-of-operating-a-centennial-wheel/) | Dynamic Programming, Array| O(n) Time, O(n) Space | Medium |
| 1194 | [Target Sum](https://leetcode.com/problems/target-sum/)   | Dynamic Programming, Array| O(n * sum) Time, O(n * sum) Space | Medium |
| 1195 | [Frog Jump](https://leetcode.com/problems/frog-jump/) | Dynamic Programming, Array| O(n^2) Time, O(n) Space   | Hard |
| 1196 | [How Many Apples Can You Put into the Basket](https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/) | Sliding Window, Array   | O(n) Time, O(1) Space | Medium |
| 1197 | [📓 Minimum Knight Moves](../leetcode/1197.ipynb) | <span title="BFS from origin in the symmetry-reduced first quadrant; shortest path = minimum knight moves.">BFS, Queue</span> | Time: O(|x|*|y|), Space: O(|x|*|y|) | Medium |
| 1198 | [Find Smallest Common Element in All Rows](https://leetcode.com/problems/find-smallest-common-element-in-all-rows/) | HashSet, Array  | O(n * m) Time, O(n) Space | Medium |
| 1199 | [Minimum Time to Build Blocks](https://leetcode.com/problems/minimum-time-to-build-blocks/) | Dynamic Programming, Array| O(n) Time, O(n) Space | Medium |
| 1200 | [Minimum Absolute Difference](https://leetcode.com/problems/minimum-absolute-difference/) | Sorting, Array  | O(n log n) Time, O(1) Space | Medium |
| #   | Problem Title   | Data Structure(s) | Time and Space Complexity | Difficulty |
| 1201 | [Ugly Number III](https://leetcode.com/problems/ugly-number-iii/) | Math, Priority Queue   | O(log N) Time, O(1) Space | Medium |
| 1202 | [Smallest String With Swaps](https://leetcode.com/problems/smallest-string-with-swaps/) | Union-Find, Graph | O(n log n) Time, O(n) Space | Medium |
| 1203 | [Sort Items by Groups Respecting Dependencies](https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/) | Graph, Topological Sort| O(n + m) Time, O(n + m) Space | Hard |
| 1204 | [📓 Design Hit Counter](../leetcode/1204.ipynb) | <span title="Fixed 300 slots indexed by timestamp % 300; overwrite stale slots on hit() and sum valid slots on getHits().">Circular Buffer</span>| O(1) Time, O(k) Space | Medium |
| 1205 | [📓 Google Question](../leetcode/1205.ipynb)| <span title="Sort meeting start and end times independently, then greedily reuse rooms with a two-pointer sweep.">Array, Sorting</span> | O(n log n) Time, O(1) Space | Medium |
| 1206 | [Design Linked List](https://leetcode.com/problems/design-linked-list/)| Linked List| O(1) Time, O(1) Space | Easy |
| 1207 | [Unique Number of Occurrences](https://leetcode.com/problems/unique-number-of-occurrences/) | HashMap, Set   | O(n) Time, O(n) Space | Easy |
| 1208 | [Get Equal Substrings Within Budget](https://leetcode.com/problems/get-equal-substrings-within-budget/) | Sliding Window, String | O(n) Time, O(1) Space | Medium |
| 1209 | [Remove All Adjacent Duplicates in String II](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/) | Stack, String  | O(n) Time, O(n) Space | Medium |
| 1210 | [📓 Minimum Moves to Reach Target with Rotations](../leetcode/1210.ipynb) | <span title="BFS on (tail_row, tail_col, orientation) state space; first hit guarantees minimum moves.">BFS, Queue</span> | Time: O(n^2), Space: O(n^2) | Hard |
| 1211 | [📓 Divide Chocolate](../leetcode/1211.ipynb) | <span title="Binary search on the minimum sweetness; greedily cut when the running sum hits the threshold.">Binary Search</span> | Time: O(n log(sum)), Space: O(1) | Hard |
| 1212 | [Matrix Block Sum](https://leetcode.com/problems/matrix-block-sum/)| Matrix, Prefix Sum | O(m * n) Time, O(m * n) Space | Medium |
| 1213 | [Split a String into Balanced Strings](https://leetcode.com/problems/split-a-string-into-balanced-strings/) | String, Count  | O(n) Time, O(1) Space | Easy |
| 1214 | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Two-pointer, Array | O(n) Time, O(1) Space | Easy |
| 1215 | [Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/) | Dynamic Programming, Array| O(n^2) Time, O(n^2) Space | Hard |
| 1216 | [📓 Valid Palindrome III](../leetcode/1216.ipynb) | <span title="Deletions needed to make s a palindrome equals n minus the LCS length of s and its reverse">LCS-based DP</span> | O(n^2) Time, O(n^2) Space | Hard |
| 1217 | [Play with Chips](https://leetcode.com/problems/play-with-chips/) | Math | O(n) Time, O(1) Space | Easy |
| 1218 | [📓 Longest Arithmetic Subsequence of Given Difference](../leetcode/1218.ipynb) | <span title="dp[v] = longest arithmetic subsequence with given difference ending at value v; extend in O(1) per element">DP with HashMap</span> | O(n) Time, O(n) Space | Medium |
| 1219 | [📓 Path with Maximum Gold](../leetcode/1219.ipynb) | <span title="Mark visited cells as 0 during DFS and restore them after backtracking, trying every non-zero starting cell to find the maximum gold path.">DFS Backtracking</span> | O(m*n*4^k) Time, O(m*n) Space | Medium |
| 1220 | [Count Vowels Permutation](https://leetcode.com/problems/count-vowels-permutation/) | Dynamic Programming, Array| O(n) Time, O(1) Space | Hard |
| 1221 | [Split a String in Balanced Strings](https://leetcode.com/problems/split-a-string-in-balanced-strings/) | String   | O(n) Time, O(1) Space | Easy |
| 1222 | [📓 Queens That Can Attack the King](../leetcode/1222.ipynb) | <span title="Store queens in a HashSet, then walk outward in all 8 directions from the king, stopping at the first queen found.">Array, Matrix</span>  | O(1) Time, O(1) Space | Medium |
| 1223 | [📓 Dice Roll Simulation](../leetcode/1223.ipynb) | <span title="dp[f][c] = ways for last face f with streak c; extend by subtracting sequences that would exceed rollMax[f]">DP with Subtraction</span> | O(n) Time, O(n) Space | Medium |
| 1224 | [Maximum Equal Frequency](https://leetcode.com/problems/maximum-equal-frequency/) | HashMap, Array | O(n) Time, O(n) Space | Hard |
| 1225 | [Reports to the Boss](https://leetcode.com/problems/reports-to-the-boss/)| Tree, Graph| O(n) Time, O(n) Space | Medium |
| 1226 | [📓 The Employee That Worked on the Longest Task](../leetcode/1226.ipynb) | <span title="Track the previous end-time; update the best employee whenever the current task duration strictly exceeds the running maximum.">Array, HashMap</span> | O(n) Time, O(n) Space | Medium |
| 1227 | [Airplane Seat Assignment Probability](https://leetcode.com/problems/airplane-seat-assignment-probability/) | Probability, Simulation | O(1) Time, O(1) Space | Medium |
| 1228 | [Missing Number in Arithmetic Progression](https://leetcode.com/problems/missing-number-in-arithmetic-progression/) | Math | O(n) Time, O(1) Space | Medium |
| 1229 | [Meeting Scheduler](https://leetcode.com/problems/meeting-scheduler/)  | Interval, Sorting | O(n log n) Time, O(1) Space | Medium |
| 1230 | [Toss Strange Coins](https://leetcode.com/problems/toss-strange-coins/)| Dynamic Programming, Probability | O(n) Time, O(1) Space | Hard |
| 1231 | [📓 Divide Chocolate](../leetcode/1231.ipynb)| <span title="Binary search for the insert position within a DP transition (e.g., patience sorting for LIS).">Binary Search, Dynamic Programming</span> | O(n log n) Time, O(1) Space | Medium |
| 1232 | [Check If It Is a Straight Line](https://leetcode.com/problems/check-if-it-is-a-straight-line/) | Geometry, Math | O(n) Time, O(1) Space | Easy |
| 1233 | [📓 Remove Sub-Folders from the Filesystem](../leetcode/1233.ipynb) | <span title="Sort the array then binary search; or sort + two-pointer sweep after the search.">Binary Search, Array</span> | O(n log n) Time, O(n) Space | Medium |
| 1234 | [Replace the Substring for Balanced String](https://leetcode.com/problems/replace-the-substring-for-balanced-string/) | Sliding Window, String  | O(n) Time, O(1) Space | Medium |
| 1235 | [Job Scheduler](https://leetcode.com/problems/job-scheduler/)  | Dynamic Programming, Array| O(n^2) Time, O(n^2) Space | Hard |
| 1236 | [String Compression II](https://leetcode.com/problems/string-compression-ii/) | String, Dynamic Programming| O(n) Time, O(n) Space | Hard |
| 1237 | [Rotate Function](https://leetcode.com/problems/rotate-function/)| Math, Array| O(n) Time, O(n) Space | Medium |
| 1238 | [📓 Circular Permutation in Binary Representation](../leetcode/1238.ipynb) | <span title="XOR each Gray code i^(i>>1) with the start offset to rebase the circular permutation.">Gray Code with Start XOR</span> | O(n) Time, O(1) Space | Medium |
| 1239 | [LongestSubstringWithoutRepeatingCharacters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Sliding Window, HashSet | O(n) Time, O(n) Space | Medium |
| 1240 | [Tiling a Rectangle with the Fewest Squares](https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/) | Dynamic Programming, Array| O(m * n) Time, O(m * n) Space | Hard |
| 1241 | [A Number After a Double Reversal](https://leetcode.com/problems/a-number-after-a-double-reversal/) | Math| O(1) Time, O(1) Space | Easy |
| 1242 | [Maximum Sum of Two Non-Overlapping Subarrays](https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/) | Sliding Window, Dynamic Programming | O(n) Time, O(1) Space | Medium |
| 1243 | [📓 Array Transformation](../leetcode/1243.ipynb)   | <span title="Apply local-min-up/local-max-down each round, stopping as soon as a full pass produces no changes.">Simulation</span>| O(n) Time, O(1) Space | Medium |
| 1244 | [📓 Design A Leaderboard](../leetcode/1244.ipynb) | <span title="HashMap for O(1) score mutations; sort values descending on query to sum top-k entries.">HashMap</span> | Time: O(n log n), Space: O(n) | Medium |
| 1245 | [Tree Diameter](https://leetcode.com/problems/tree-diameter/)  | Tree, DFS| O(n) Time, O(n) Space | Medium |
| 1246 | [Palindrome Removal](https://leetcode.com/problems/palindrome-removal/)| Dynamic Programming, String   | O(n^2) Time, O(n^2) Space | Medium |
| 1247 | [Minimum Number of Steps to Make Two Strings Anagram](https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/) | HashMap, String| O(n) Time, O(n) Space | Medium |
| 1248 | [Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/) | Sliding Window, Array   | O(n) Time, O(1) Space | Medium |
| 1249 | [Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/) | Stack, String  | O(n) Time, O(n) Space | Medium |
| 1250 | [Check If It Is a Good Array](https://leetcode.com/problems/check-if-it-is-a-good-array/) | Math, GCD | O(n) Time, O(1) Space | Medium |
| 1251 | [Average Selling Price](https://leetcode.com/problems/average-selling-price/) | Math, Array| O(n) Time, O(1) Space | Medium |
| 1252 | [Cells with Odd Values in a Matrix](https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/) | Matrix, Array  | O(n * m) Time, O(1) Space | Easy |
| 1253 | [Reconstruct a 2-Row Binary Matrix](https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/) | Matrix   | O(n * m) Time, O(1) Space | Medium |
| 1254 | [📓 Number of Closed Islands](../leetcode/1254.ipynb) | <span title="Drown all border-connected land first, then count remaining enclosed land components in a single sweep.">DFS Flood Fill</span> | O(m*n) Time, O(m*n) Space | Medium |
| 1255 | [Maximum Score Words Formed by Letters](https://leetcode.com/problems/maximum-score-words-formed-by-letters/) | Dynamic Programming, HashMap  | O(n * m) Time, O(n) Space | Medium |
| 1256 | [📓 Encode Number](../leetcode/1256.ipynb) | <span title="n+1 in binary with the leading 1 stripped equals the encoded string">Bit Manipulation</span> | O(n) Time, O(n) Space | Medium |
| 1257 | [Smallest Common Region](https://leetcode.com/problems/smallest-common-region/) | Graph, Tree| O(n) Time, O(n) Space | Medium |
| 1258 | [Synonym, Sort](https://leetcode.com/problems/synonym-sort/)| String, Sorting| O(n log n) Time, O(n) Space | Medium |
| 1259 | [📓 Handshakes That Don't Cross](../leetcode/1259.ipynb) | <span title="Non-crossing handshakes among 2n people equal the nth Catalan number; fill via C[n]=sum C[k]*C[n-1-k]">Catalan DP</span> | O(n) Time, O(n) Space | Hard |
| 1260 | [Shift 2D Grid](https://leetcode.com/problems/shift-2d-grid/)   | Matrix, Array  | O(n * m) Time, O(n * m) Space | Easy |
| 1261 | [Find Elements in a Contaminated Binary Tree](https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/) | Tree, BFS, HashSet | O(n) Time, O(n) Space | Medium |
| 1262 | [Greatest Sum Divisible by Three](https://leetcode.com/problems/greatest-sum-divisible-by-three/) | Dynamic Programming, Array| O(n) Time, O(1) Space | Medium |
| 1263 | [📓 Minimum Moves to Move a Box to Their Target Location](../leetcode/1263.ipynb) | <span title="BFS on (box_pos, player_pos) state; inner BFS checks player reachability for each potential push direction.">BFS, Deque</span> | Time: O(m^2*n^2), Space: O(m^2*n^2) | Hard |
| 1264 | [Page Completion](https://leetcode.com/problems/page-completion/)| Binary Search  | O(log n) Time, O(1) Space | Medium |
| 1265 | [Print Immutable Linked List in Reverse](https://leetcode.com/problems/print-immutable-linked-list-in-reverse/) | Stack, Linked List | O(n) Time, O(n) Space | Medium |
| 1266 | [Number of Ways to Stay in the Same Place After Some Moves](https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-moves/) | Dynamic Programming, Math | O(n) Time, O(n) Space | Medium |
| 1267 | [Count Servers that Communicate](https://leetcode.com/problems/count-servers-that-communicate/) | Matrix, HashMap| O(n * m) Time, O(n * m) Space | Medium |
| 1268 | [Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/) | Trie, Array| O(n * m) Time, O(n * m) Space | Medium |
| 1269 | [📓 Number of Ways to Stay in the Same Place After Some Steps](../leetcode/1269.ipynb) | <span title="dp[i] = ways to be at index i; roll over steps, capping reachable positions at min(steps/2+1, arrLen)">DP Rolling Array</span> | O(n) Time, O(n) Space | Medium |
| 1270 | [All Paths from Source Lead to Destination](https://leetcode.com/problems/all-paths-from-source-lead-to-destination/) | DFS, Graph | O(n * m) Time, O(n * m) Space | Medium |
| 1271 | [Hexspeak](https://leetcode.com/problems/hexspeak/) | Math, String   | O(n) Time, O(1) Space | Easy |
| 1272 | [Delete Tree Nodes](https://leetcode.com/problems/delete-tree-nodes/)  | Tree, DFS| O(n) Time, O(n) Space | Medium |
| 1273 | [Delete Nodes And Return Forest](https://leetcode.com/problems/delete-nodes-and-return-forest/) | Tree, DFS| O(n) Time, O(n) Space | Medium |
| 1274 | [📓 Prime Number of Set Bits in Binary Representation](../leetcode/1274.ipynb) | <span title="Precompute a prime bitmask for counts 0-20; use popcount + single bit-shift lookup per number.">Bit Manipulation</span> | Time: O((R-L)*log R), Space: O(1) | Easy |
| 1275 | [Find Winner on a Tic Tac Toe Game](https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/) | Matrix, Array  | O(1) Time, O(1) Space | Easy |
| 1276 | [Number of Burgers with No Waste of Ingredients](https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/) | Math | O(1) Time, O(1) Space | Medium |
| 1277 | [📓 Count Square Submatrices with All Ones](../leetcode/1277.ipynb) | <span title="dp[i][j] = side of largest all-ones square with bottom-right at (i,j); sum all dp values to count every valid square">DP</span> | O(n * m) Time, O(n * m) Space | Medium |
| 1278 | [Palindrome Partitioning III](https://leetcode.com/problems/palindrome-partitioning-iii/) | Dynamic Programming, String   | O(n^2) Time, O(n^2) Space | Hard |
| 1279 | [Frog Jump II](https://leetcode.com/problems/frog-jump-ii/)| DP, Array| O(n) Time, O(n) Space | Medium |
| 1280 | [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/) | Two-pointer, Array | O(n + m) Time, O(n + m) Space | Medium |
| 1281 | [Subtract the Product and Sum of Digits of an Integer](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/) | Math | O(1) Time, O(1) Space | Easy |
| 1282 | [Group People Given the Group Size They Belong To](https://leetcode.com/problems/group-people-given-the-group-size-they-belong-to/) | HashMap, Array | O(n) Time, O(n) Space | Medium |
| 1283 | [📓 Find the Smallest Divisor Given a Threshold](../leetcode/1283.ipynb) | <span title="Combine binary search with a mathematical formula to evaluate the feasibility predicate.">Binary Search, Math</span> | O(n log m) Time, O(1) Space | Medium |
| 1284 | [📓 Minimum Number of Flips to Convert Binary Matrix to Zero Matrix](../leetcode/1284.ipynb) | <span title="Encode the matrix as a bitmask and BFS; the first time zero state is reached is the minimum flips.">BFS (Bitmask State)</span> | Time: $O(2^{nm} \cdot nm)$, Space: $O(2^{nm})$ | Hard |
| 1285 | [📓 Find the Right Interval](../leetcode/1285.ipynb) | <span title="Sort interval starts with original indices; binary search each end point for smallest start >= end.">Binary Search</span> | Time: O(n log n), Space: O(n) | Medium |
| 1286 | [📓 Iterator for Combination](../leetcode/1286.ipynb) | <span title="Advance a k-size index array like a mixed-radix counter to yield combinations on demand in O(k) per call.">Index Array (On-Demand)</span> | Time: $O(k)$ per call, Space: $O(k)$ | Medium |
| 1287 | [📓 Element Appearing More Than 25% in Sorted Array](../leetcode/1287.ipynb) | <span title="Check arr[i] == arr[i + n/4] for each i; the dominant element must bridge any quarter-length gap.">Quarter-Jump Check</span>| O(n) Time, O(1) Space | Easy |
| 1288 | [Remove Covered Intervals](https://leetcode.com/problems/remove-covered-intervals/) | Sorting, Array | O(n log n) Time, O(n) Space | Medium |
| 1289 | [Minimum Falling Path Sum II](https://leetcode.com/problems/minimum-falling-path-sum-ii/) | Dynamic Programming, Matrix  | O(n * m) Time, O(n * m) Space | Medium |
| 1290 | [Convert Binary Number in a Linked List to Integer](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/) | Linked List, Math| O(n) Time, O(1) Space | Easy |
| 1291 | [Sequential Digits](https://leetcode.com/problems/sequential-digits/)| Math, String   | O(n) Time, O(1) Space | Medium |
| 1292 | [Maximum Side Length of a Square with Sum Less than or Equal to Threshold](https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/) | Matrix, Sliding Window | O(n * m) Time, O(1) Space | Medium |
| 1| 293 | [📓 Flip Game](../leetcode/0293.ipynb) | <span title="One sweep through the data, typically updating a counter or maximum in place.">Single Scan</span> | Time: O(n²), Space: O(n) per result | Easy |
| 1294 | [📓 Weather Type in Each Country](../leetcode/1294.ipynb) | <span title="Join Countries with November Day rows, average weather_state per country, then classify by threshold.">Aggregation JOIN</span> | Time: $O(n + m)$, Space: $O(n)$ | Easy |
| 1295 | [Find Numbers with Even Number of Digits](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/) | Math, Array   | O(n) Time, O(1) Space | Easy |
| 1296 | [Divide Array in Sets of K Consecutive Numbers](https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/) | HashMap, Sorting | O(n log n) Time, O(n) Space | Hard |
| 1297 | [Maximum Number of Occurrences of a Substring](https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/) | HashMap, Sliding Window| O(n) Time, O(n) Space | Medium |
| 1298 | [Maximum Sum of 3 Non-Overlapping Subarrays](https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/) | Dynamic Programming, Sliding Window | O(n) Time, O(n) Space | Hard |
| 1299 | [📓 Replace Elements with Greatest Element on Right Side](../leetcode/1299.ipynb) | <span title="Scan right-to-left maintaining a running maximum; write it into each position before extending it with the original value.">Array, Iteration</span> | O(n) Time, O(1) Space | Easy |
| 1300 | [📓 Sum of Mutated Array Closest to Target](../leetcode/1300.ipynb) | <span title="Sort the array then binary search; or sort + two-pointer sweep after the search.">Binary Search, Array</span> | O(n log n) Time, O(1) Space | Medium |
| 1301 | [Number of Paths with Max Score](https://leetcode.com/problems/number-of-paths-with-max-score/) | Dynamic Programming, Graph  | O(n * m) Time, O(n * m) Space | Hard |
| 1302 | [Deepest Leaves Sum](https://leetcode.com/problems/deepest-leaves-sum/) | Tree, BFS | O(n) Time, O(n) Space | Medium |
| 1303 | [📓 Find the Team Size](../leetcode/1303.ipynb) | <span title="Build a frequency map of team sizes in one pass, then look up each employee's team count directly.">Array, Sorting</span>| O(n log n) Time, O(n) Space | Medium |
| 1304 | [📓 Find N Unique Integers Sum up to Zero](../leetcode/1304.ipynb) | <span title="Fill slots with 1 through n-1, then set the last element to their negated sum to guarantee a total of zero.">Direct Construction</span> | O(n) Time, O(n) Space | Easy |
| 1305 | [All Elements in Two Binary Search Trees](https://leetcode.com/problems/all-elements-in-two-binary-search-trees/) | Tree, Sorting, Merge  | O(n + m) Time, O(n + m) Space | Medium |
| 1306 | [📓 Jump Game III](../leetcode/1306.ipynb) | <span title="BFS from start index trying both jump directions; first reach of a zero-valued index is the answer.">BFS (Visited Set)</span> | Time: $O(n)$, Space: $O(n)$ | Medium |
| 1307 | [📓 Verbal Arithmetic Puzzle](../leetcode/1307.ipynb) | <span title="Assign digits to letters with backtracking using net coefficient sums to prune invalid partial assignments.">Backtracking</span> | Time: $O(10!)$, Space: $O(10)$ | Hard |
| 1308 | [📓 Run-Length Encoding II](../leetcode/1308.ipynb) | <span title="Process encoded runs directly without decoding, splitting the targeted run and merging adjacent same-character runs.">Array, String</span> | O(n) Time, O(n) Space | Medium |
| 1309 | [📓 Decompress Run-Length Encoded List](../leetcode/1309.ipynb) | <span title="Iterate through [freq, val] pairs and append val exactly freq times to reconstruct each run.">Single Pass Expansion</span> | O(n) Time, O(n) Space | Easy |
| 1310 | [Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/) | Stack, Array  | O(n) Time, O(n) Space | Medium |
| 1311 | [Get Watched Videos by Your Friends](https://leetcode.com/problems/get-watched-videos-by-your-friends/) | Graph, HashMap| O(n + m) Time, O(n + m) Space | Medium |
| 1312 | [Minimum Insertion Steps to Make a String Palindrome](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/) | Dynamic Programming, String  | O(n^2) Time, O(n^2) Space | Hard |
| 1313 | [📓 Decompress Array](../leetcode/1313.ipynb) | <span title="Pre-compute total output size once, then expand each [val, freq] pair into a contiguous run in the result buffer.">Single Pass Expansion</span> | O(n) Time, O(n) Space | Easy |
| 1314 | [Matrix Block Sum](https://leetcode.com/problems/matrix-block-sum/) | Matrix, Prefix Sum| O(n * m) Time, O(n * m) Space | Medium |
| 1315 | [Sum of Nodes with Even-Valued Grandparent](https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/) | Tree, DFS | O(n) Time, O(n) Space | Easy |
| 1316 | [Distinguishable Palindrome](https://leetcode.com/problems/distinguishable-palindrome/) | String, Backtracking  | O(n!) Time, O(n) Space| Hard |
| 1317 | [Convert Integer to the Sum of Two No-Zero Integers](https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/) | Math| O(n) Time, O(1) Space | Easy |
| 1318 | [Maximum Product of Two Elements in an Array](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/) | Sorting, Array| O(n log n) Time, O(1) Space | Medium |
| 1319 | [Number of Operations to Make Network Connected](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) | Graph, Union-Find | O(n + m) Time, O(n) Space | Medium |
| 1320 | [Minimum Moves to Equal Array Elements II](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/) | Sorting, Array| O(n log n) Time, O(1) Space | Medium |
| 1321 | [Restaurant Profit](https://leetcode.com/problems/restaurant-profit/)   | Math| O(1) Time, O(1) Space | Medium |
| 1322 | [Longest Arithmetic Subsequence](https://leetcode.com/problems/longest-arithmetic-subsequence/) | Dynamic Programming, Array   | O(n^2) Time, O(n) Space   | Medium |
| 1323 | [Maximum 69 Number](https://leetcode.com/problems/maximum-69-number/) | Math| O(n) Time, O(1) Space | Easy |
| 1324 | [Print Words Vertically](https://leetcode.com/problems/print-words-vertically/) | String   | O(n) Time, O(n) Space | Medium |
| 1325 | [Delete Leaves with a Given Value](https://leetcode.com/problems/delete-leaves-with-a-given-value/) | Tree, DFS | O(n) Time, O(n) Space | Medium |
| 1326 | [Minimum Cost to Move Chips to the Same Position](https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/) | Math, Array   | O(n) Time, O(1) Space | Easy |
| 1327 | [📓 Sort Array by Parity](../leetcode/1327.ipynb) | <span title="Advance left past evens and right past odds; swap when left holds an odd and right holds an even.">Two Pointers</span> | Time: $O(n)$, Space: $O(1)$ | Medium |
| 1328 | [Break a Palindrome](https://leetcode.com/problems/break-a-palindrome/)| String   | O(n) Time, O(n) Space | Medium |
| 1329 | [Sort Matrix Diagonally](https://leetcode.com/problems/sort-matrix-diagonally/) | Matrix, Sorting | O(n * m log n) Time, O(n * m) Space | Medium |
| 1330 | [Super Egg Drop](https://leetcode.com/problems/super-egg-drop/)| Dynamic Programming| O(k * log n) Time, O(k * log n) Space | Hard |
| 1331 | [Rank Transform of an Array](https://leetcode.com/problems/rank-transform-of-an-array/) | Sorting, HashMap| O(n log n) Time, O(n) Space | Easy |
| 1332 | [Remove Palindromic Subsequences](https://leetcode.com/problems/remove-palindromic-subsequences/) | String   | O(n) Time, O(1) Space | Medium |
| 1333 | [📓 Filter Restaurants by Vegan-Friendly, Price and Distance](../leetcode/1333.ipynb) | <span title="Filter by constraints first, then sort survivors by rating descending and id descending.">Array, Sorting</span>| O(n log n) Time, O(n) Space | Medium |
| 1334 | [Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) | Graph, Dijkstra | O(n^3) Time, O(n^2) Space | Medium |
| 1335 | [Minimum Difficulty of a Job Schedule](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/) | Dynamic Programming| O(n^2) Time, O(n) Space   | Hard |
| 1336 | [The K Weakest Rows in a Matrix](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/) | Sorting, Array| O(n log n) Time, O(n) Space | Medium |
| 1337 | [The K Weakest Rows in a Matrix](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/) | Sorting, Array| O(n log n) Time, O(n) Space | Medium |
| 1338 | [Reduce Array Size to The Half](https://leetcode.com/problems/reduce-array-size-to-the-half/) | HashMap, Sorting| O(n log n) Time, O(n) Space | Medium |
| 1339 | [Maximum Product of Splitted Binary Tree](https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/) | Tree, DFS | O(n) Time, O(n) Space | Hard |
| 1340 | [Jump Game V](https://leetcode.com/problems/jump-game-v/)| Dynamic Programming, Array   | O(n) Time, O(n) Space | Hard |
| 1341 | [Matrix Block Sum](https://leetcode.com/problems/matrix-block-sum/) | Matrix, Prefix Sum| O(n * m) Time, O(n * m) Space | Medium |
| 1342 | [Number of Steps to Reduce a Number to Zero](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/) | Math| O(log n) Time, O(1) Space | Easy |
| 1343 | [Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/) | Sliding Window, Array  | O(n) Time, O(1) Space | Medium |
| 1344 | [Angle Between Hands of a Clock](https://leetcode.com/problems/angle-between-hands-of-a-clock/) | Math| O(1) Time, O(1) Space | Medium |
| 1345 | [📓 Jump Game IV](../leetcode/1345.ipynb) | <span title="BFS with same-value group pruning; clear each group after visiting to guarantee O(n) total work.">BFS, Queue</span> | Time: O(n), Space: O(n) | Hard |
| 1346 | [Check If N and Its Double Exist](https://leetcode.com/problems/check-if-n-and-its-double-exist/) | HashMap, Array| O(n) Time, O(n) Space | Easy |
| 1347 | [Minimum Cost to Move Chips to the Same Position](https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/) | Math| O(n) Time, O(1) Space | Easy |
| 1348 | [Tweet Counts Per Frequency](https://leetcode.com/problems/tweet-counts-per-frequency/) | HashMap, Queue| O(n) Time, O(n) Space | Medium |
| 1349 | [📓 Maximum Students Taking Exam](../leetcode/1349.ipynb) | <span title="Encode each row as a seat-availability bitmask; DP transitions ensure no adjacent or diagonal cheating between rows.">Bitmask DP</span> | O(m*4^n) Time, O(2^n) Space | Hard |
| 1350 | [📓 Product of the Last K Numbers](../leetcode/1350.ipynb) | <span title="Maintain a prefix-product list; reset on zero and answer queries in O(1) via prefix division.">Array, Sliding Window</span> | O(1) Time, O(n) Space | Medium |
| 1351 | [Count Negative Numbers in a Sorted Matrix](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/) | Matrix, Binary Search | O(n + m) Time, O(1) Space | Easy |
| 1352 | [📓 Product of Array Except Self](../leetcode/1352.ipynb) | <span title="Accumulate prefix products left-to-right, then fold in suffix products right-to-left using a single scalar.">Array, Sliding Window</span> | O(1) Time, O(n) Space | Medium |
| 1353 | [Maximum Number of Events That Can Be Attended](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/) | Greedy, Sorting| O(n log n) Time, O(n) Space | Medium |
| 1354 | [Construct Target Array With Multiple Sums](https://leetcode.com/problems/construct-target-array-with-multiple-sums/) | Priority Queue, Greedy| O(n log n) Time, O(n) Space | Hard |
| 1355 | [Count Words Obtained After Adding a Letter](https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/) | Trie, HashMap | O(n) Time, O(n) Space | Medium |
| 1356 | [📓 Sort Integers by The Number of 1 Bits](../leetcode/1356.ipynb) | <span title="Precompute popcount for each element once, then sort by (popcount, value) as a composite key.">Precomputed Popcount + Stable Sort</span> | O(n log n) Time, O(n) Space | Medium |
| 1357 | [Apply Discount Every n Orders](https://leetcode.com/problems/apply-discount-every-n-orders/) | Queue, Array | O(1) Time, O(n) Space | Medium |
| 1358 | [Number of Substrings Containing All Three Characters](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/) | Sliding Window, HashMap| O(n) Time, O(1) Space | Medium |
| 1359 | [Count All Valid Pickup and Delivery Options](https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/) | Math, Dynamic Programming   | O(n^2) Time, O(n) Space   | Hard |
| 1360 | [Number of Days Between Two Dates](https://leetcode.com/problems/number-of-days-between-two-dates/) | Math| O(1) Time, O(1) Space | Easy |
| 1361 | [Validate Binary Tree Nodes](https://leetcode.com/problems/validate-binary-tree-nodes/) | Union-Find, Graph | O(n) Time, O(n) Space | Medium |
| 1362 | [Closest Divisors](https://leetcode.com/problems/closest-divisors/)| Math| O(sqrt(n)) Time, O(1) Space | Medium |
| 1363 | [Largest Multiple of Three](https://leetcode.com/problems/largest-multiple-of-three/) | Sorting, Array| O(n log n) Time, O(n) Space | Medium |
| 1364 | [Jetpack](https://leetcode.com/problems/jetpack/)  | Graph, Priority Queue | O(n log n) Time, O(n) Space | Medium |
| 1365 | [How Many Numbers Are Smaller Than the Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/) | Sorting, Array| O(n log n) Time, O(n) Space | Easy |
| 1366 | [Rank Teams by Votes](https://leetcode.com/problems/rank-teams-by-votes/)| Sorting, HashMap| O(n log n) Time, O(n) Space | Medium |
| 1367 | [Linked List in Binary Tree](https://leetcode.com/problems/linked-list-in-binary-tree/) | Tree, Linked List | O(n) Time, O(n) Space | Medium |
| 1368 | [Minimum Cost to Make at Least One Valid Path in a Grid](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/) | Graph, Dijkstra, BFS  | O(n * m) Time, O(n * m) Space | Hard |
| 1369 | [📓 Get Maximum in Generated Array](../leetcode/1369.ipynb) | <span title="Build the generated array bottom-up using two filling rules, then scan for the maximum value.">Dynamic Programming</span> | O(n) Time, O(1) Space | Easy |
| 1370 | [Increasing Decreasing String](https://leetcode.com/problems/increasing-decreasing-string/) | Sorting, String | O(n log n) Time, O(n) Space | Easy |
| 1371 | [📓 Find the Longest Substring Containing Vowels in Even Counts](../leetcode/1371.ipynb) | <span title="Track vowel parity as a 5-bit XOR state; when state recurs, the gap has all even vowel counts.">Bitmask Prefix XOR + HashMap</span> | O(n) Time, O(1) Space | Medium |
| 1372 | [Longest ZigZag Path in a Binary Tree](https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/) | Tree, DFS | O(n) Time, O(n) Space | Medium |
| 1373 | [Maximum Sum of Digits in a String](https://leetcode.com/problems/maximum-sum-of-digits-in-a-string/) | Math| O(n) Time, O(1) Space | Easy |
| 1374 | [Generate a String With Characters That Have Odd Counts](https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/) | String, Math | O(n) Time, O(n) Space | Easy |
| 1375 | [📓 Bulb Switcher III](../leetcode/1375.ipynb)   | <span title="Count turned-on bulbs and track the rightmost position; a moment is all-blue when the max position equals the count.">Array, Prefix Sum</span> | O(n) Time, O(n) Space | Medium |
| 1376 | [Time Needed to Inform All Employees](https://leetcode.com/problems/time-needed-to-inform-all-employees/) | Tree, BFS, DFS| O(n) Time, O(n) Space | Medium |
| 1377 | [Frog Position After T Seconds](https://leetcode.com/problems/frog-position-after-t-seconds/) | Graph, BFS| O(n) Time, O(n) Space | Hard |
| 1378 | [Replace Employee ID in a Table](https://leetcode.com/problems/replace-employee-id-in-a-table/) | SQL | O(1) Time, O(1) Space | Easy |
| 1379 | [Find a Corresponding Node of a Binary Tree in a Clone of That Tree](https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/) | Tree, DFS | O(n) Time, O(n) Space | Medium |
| 1380 | [Lucky Numbers in a Matrix](https://leetcode.com/problems/lucky-numbers-in-a-matrix/) | Matrix, HashSet | O(n * m) Time, O(n) Space | Medium |
| 1381 | [Design a Stack With Increment Operation](https://leetcode.com/problems/design-a-stack-with-increment-operation/) | Stack, Array  | O(1) Time, O(n) Space | Medium |
| 1382 | [Balance a Binary Search Tree](https://leetcode.com/problems/balance-a-binary-search-tree/) | Tree, DFS | O(n) Time, O(n) Space | Medium |
| 1383 | [Maximum Performance of a Team](https://leetcode.com/problems/maximum-performance-of-a-team/) | Greedy, Heap  | O(n log n) Time, O(n) Space | Hard |
| 1384 | [📓 Movie Rating](../leetcode/1384.ipynb) | <span title="Aggregate user rating counts and Feb-2020 movie sums in one pass, then pick the top entries from each map.">Dual Hash Map</span>| O(n) Time, O(n) Space | Easy |
| 1385 | [Find the Distance Value Between Two Arrays](https://leetcode.com/problems/find-the-distance-value-between-two-arrays/) | Sorting, Binary Search| O(n log n) Time, O(1) Space | Easy |
| 1386 | [📓 Cinema Seat Allocation](../leetcode/1386.ipynb) | <span title="Represent reserved seats per row as a 10-bit integer, then test three column-block masks to count valid groups.">Bitmask</span>| O(n * m) Time, O(n * m) Space | Medium |
| 1387 | [Sort Integers by The Number of 1 Bits](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/) | Sorting, Bit Manipulation   | O(n log n) Time, O(n) Space | Medium |
| 1388 | [Pizza With 3n Slices](https://leetcode.com/problems/pizza-with-3n-slices/)  | Dynamic Programming, Array   | O(n^2) Time, O(n) Space   | Hard |
| 1389 | [📓 Create Target Array in the Given Order](../leetcode/1389.ipynb) | <span title="Use a resizable list's built-in insert to place each element at its specified index, shifting the tail right.">Array, Insertion</span>| O(n) Time, O(n) Space | Easy |
| 1390 | [Four Divisors](https://leetcode.com/problems/four-divisors/)  | Math| O(n sqrt(n)) Time, O(1) Space | Medium |
| 1391 | [Check if There is a Valid Path in a Grid](https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/) | Graph, BFS, DFS | O(n * m) Time, O(n * m) Space | Medium |
| 1392 | [Longest Happy Prefix](https://leetcode.com/problems/longest-happy-prefix/)   | String, KMP   | O(n) Time, O(n) Space | Hard |
| 1393 | [Capital Gain](https://leetcode.com/problems/capital-gain/)| Math| O(n) Time, O(1) Space | Easy |
| 1394 | [Find Lucky Integer in an Array](https://leetcode.com/problems/find-lucky-integer-in-an-array/) | HashMap, Array| O(n) Time, O(n) Space | Easy |
| 1395 | [📓 Count Number of Teams](../leetcode/1395.ipynb) | <span title="Fix each element as the middle soldier and count smaller/larger elements on each side to multiply valid triplet counts.">Array, Sorting</span>| O(n^2) Time, O(n) Space   | Medium |
| 1396 | [Design Underground System](https://leetcode.com/problems/design-underground-system/) | HashMap, Queue| O(1) Time, O(n) Space | Medium |
| 1397 | [Find All Good Strings](https://leetcode.com/problems/find-all-good-strings/) | Dynamic Programming, DFS | O(n) Time, O(1) Space | Hard |
| 1398 | [📓 Company Finder](../leetcode/1398.ipynb)| <span title="Load the first array into a HashSet, then collect elements from the second array that hit the set in O(1).">Array, HashSet</span>| O(n) Time, O(n) Space | Easy |
| 1399 | [Count Largest Group](https://leetcode.com/problems/count-largest-group/)| HashMap, Array| O(n) Time, O(n) Space | Easy |
| 1400 | [Find Good Days to Rob the Bank](https://leetcode.com/problems/find-good-days-to-rob-the-bank/) | Dynamic Programming, Array  | O(n) Time, O(n) Space | Medium |
| 1401 | [Circle and Rectangle Overlapping](https://leetcode.com/problems/circle-and-rectangle-overlapping/) | Geometry, Math| O(1) Time, O(1) Space | Medium |
| 1402 | [Redundant Connection II](https://leetcode.com/problems/redundant-connection-ii/) | Graph, Union-Find | O(n) Time, O(n) Space | Hard |
| 1403 | [Minimum Subsequence in Non-Increasing Order](https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/) | Sorting, Array| O(n log n) Time, O(n) Space | Easy |
| 1404 | [📓 Number of Steps to Reduce a Number in Binary Representation to One](../leetcode/1404.ipynb) | <span title="Scan bits right-to-left with a carry variable; odd bits cost 2 steps, even bits cost 1.">Linear Scan with Carry</span> | O(log n) Time, O(1) Space | Easy |
| 1405 | [Longest Happy String](https://leetcode.com/problems/longest-happy-string/)   | Greedy, String| O(n) Time, O(1) Space | Medium |
| 1406 | [Stone Game III](https://leetcode.com/problems/stone-game-iii/)  | Dynamic Programming, DP| O(n) Time, O(n) Space | Hard |
| 1407 | [Rank Teams by Votes](https://leetcode.com/problems/rank-teams-by-votes/)| Sorting, HashMap| O(n log n) Time, O(n) Space | Medium |
| 1408 | [String Matching in an Array](https://leetcode.com/problems/string-matching-in-an-array/) | Trie, Array   | O(n) Time, O(n) Space | Easy |
| 1409 | [📓 Queries on a Permutation With Key](../leetcode/1409.ipynb) | <span title="Maintain the permutation in a list; for each query, find the element's position, record it, and move it to the front.">Array, Map</span>| O(1) Time, O(n) Space | Medium |
| 1410 | [HTML Entity Parser](https://leetcode.com/problems/html-entity-parser/) | String, Stack | O(n) Time, O(n) Space | Easy |
| 1411 | [📓 Number of Ways to Paint N × 3 Grid](../leetcode/1411.ipynb) | <span title="Track only two pattern types per row (ABA and ABC); apply fixed transition counts each row for O(n) time and O(1) space.">Row-Pattern DP</span> | O(n) Time, O(1) Space | Hard |
| 1412 | [📓 Shortest Distance to Target String in a Circular Array](../leetcode/1412.ipynb) | <span title="For each occurrence of the target, compute min(clockwise, counterclockwise) distance and track the running minimum.">Circular Array</span>| O(n) Time, O(n) Space | Medium |
| 1413 | [Minimum Value to Get Positive Step by Step Sum](https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/) | Math, Greedy  | O(n) Time, O(1) Space | Easy |
| 1414 | [📓 Find the Minimum of an Integer Array](../leetcode/1414.ipynb) | <span title="Scan the array once tracking the running minimum, updating whenever a smaller element is found.">Single Pass</span> | O(n) Time, O(1) Space | Easy |
| 1415 | [📓 The k-th Lexicographical String of All Happy Strings of Length n](../leetcode/1415.ipynb) | <span title="Skip subtrees of size 2^(n-1-pos) to locate the k-th happy string character by character in O(n).">DFS (Mathematical Skip)</span> | Time: $O(n)$, Space: $O(n)$ | Medium |
| 1416 | [Restore The Array](https://leetcode.com/problems/restore-the-array/)| Dynamic Programming| O(n) Time, O(n) Space | Medium |
| 1417 | [Rearrange the Array to Maximize Prefix Score](https://leetcode.com/problems/rearrange-the-array-to-maximize-prefix-score/) | Sorting, Greedy | O(n log n) Time, O(n) Space | Medium |
| 1418 | [Display Table of Food Orders in a Restaurant](https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/) | HashMap, Sorting| O(n log n) Time, O(n) Space | Medium |
| 1419 | [📓 Minimum Number of Frogs Croaking](../leetcode/1419.ipynb) | <span title="Halve the search space each step by comparing the midpoint to a monotone predicate.">Binary Search</span> | O(n log n) Time, O(1) Space | Hard |
| 1420 | [Find Good Days to Rob the Bank](https://leetcode.com/problems/find-good-days-to-rob-the-bank/) | Dynamic Programming, Array  | O(n) Time, O(n) Space | Medium |
| 1421 | [📓 Finding the Users Active Minutes](../leetcode/1421.ipynb) | <span title="Map each user to a set of unique active minutes for automatic deduplication, then tally set sizes.">Hash Map of Sets</span> | Time: $O(n)$, Space: $O(n)$ | Medium |
| 1422 | [Maximum Score After Splitting a String](https://leetcode.com/problems/maximum-score-after-splitting-a-string/) | String, Greedy| O(n) Time, O(1) Space | Easy |
| 1423 | [Maximum Points You Can Obtain from Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/) | Sliding Window, Array | O(n) Time, O(n) Space | Medium |
| 1424 | [📓 Diagonal Traverse II](../leetcode/1424.ipynb)   | <span title="Group elements by diagonal key (row + col) into buckets, then emit each bucket in reverse-row order.">Array, Priority Queue</span> | O(n log n) Time, O(n) Space | Medium |
| 1425 | [Constrained Subset Sum](https://leetcode.com/problems/constrained-subset-sum/) | Dynamic Programming, Queue   | O(n log n) Time, O(n) Space | Hard |
| 1426 | [📓 Counting Elements](../leetcode/1426.ipynb)   | <span title="Build a HashSet of all values, then count each element x whose successor x+1 is also in the set.">Array, HashSet</span>| O(n) Time, O(n) Space | Easy |
| 1427 | [Clockwise Rotation](https://leetcode.com/problems/clockwise-rotation/)  | Matrix  | O(n^2) Time, O(1) Space   | Easy |
| 1428 | [Leftmost Column with at Least a One](https://leetcode.com/problems/leftmost-column-with-at-least-a-one/) | Matrix, Binary Search | O(m log n) Time, O(1) Space | Medium |
| 1429 | [First Unique Number](https://leetcode.com/problems/first-unique-number/)| Queue, HashMap| O(n) Time, O(n) Space | Easy |
| 1430 | [Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree](https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/) | Tree, DFS, String | O(n) Time, O(n) Space | Medium |
| 1431 | [📓 Kids With the Greatest Number of Candies](../leetcode/1431.ipynb) | <span title="Find the global maximum first, then check if each kid's total with extra candies meets or exceeds it.">Single Pass</span> | O(n) Time, O(1) Space | Easy |
| 1432 | [Max Difference You Can Get From Changing an Integer](https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/) | Math, Greedy  | O(n) Time, O(1) Space | Medium |
| 1433 | [Check If a String Can Break Another String](https://leetcode.com/problems/check-if-a-string-can-break-another-string/) | Sorting, String | O(n log n) Time, O(n) Space | Medium |
| 1434 | [Number of Ways to Wear Different Hats to Each Other](https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/) | HashMap, Array| O(n * m) Time, O(n * m) Space | Hard |
| 1435 | [Check if a string contains a valid palindrome](https://leetcode.com/problems/check-if-a-string-contains-a-valid-palindrome/) | String, Dynamic Programming  | O(n^2) Time, O(n) Space   | Medium |
| 1436 | [Destination City](https://leetcode.com/problems/destination-city/)| Graph, HashMap| O(n) Time, O(n) Space | Easy |
| 1437 | [📓 Check If All 1's Are at Least Length K Places Away](../leetcode/1437.ipynb) | <span title="Track the index of the last seen 1 and reject any pair whose gap falls below k.">Array, Sliding Window</span> | O(n) Time, O(1) Space | Medium |
| 1438 | [Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) | Sliding Window, Queue | O(n) Time, O(n) Space | Medium |
| 1439 | [Find the Kth Smallest Sum of a Matrix with Sorted Rows](https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/) | Heap, Matrix  | O(k log n) Time, O(n) Space | Hard |
| 1440 | [Evaluate Boolean Expression](https://leetcode.com/problems/evaluate-boolean-expression/) | Stack, Recursion| O(n) Time, O(n) Space | Medium |
| 1441 | [Build an Array With Stack Operations](https://leetcode.com/problems/build-an-array-with-stack-operations/) | Stack, Array  | O(n) Time, O(n) Space | Easy |
| 1442 | [📓 Count Triplets That Can Form Two Arrays of Equal XOR](../leetcode/1442.ipynb) | <span title="Use prefix XOR; when prefix[i]==prefix[k+1] the subarray XOR is zero, giving k-i valid triplets.">Prefix XOR</span> | O(n^2) Time, O(n) Space | Hard |
| 1443 | [Minimum Time to Collect All Apples in a Tree](https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/) | Tree, DFS | O(n) Time, O(n) Space | Medium |
| 1444 | [📓 Count Subarrays With Fixed Bounds](../leetcode/1444.ipynb) | <span title="Slide a window tracking the last out-of-range index and last positions of minK and maxK to count valid subarrays in O(1).">Array, Sliding Window</span> | O(n) Time, O(1) Space | Hard |
| 1445 | [Add Two Integers in Linked List Representation](https://leetcode.com/problems/add-two-integers-in-linked-list-representation/) | Linked List, Math | O(n) Time, O(1) Space | Medium |
| 1446 | [Count Distinct Integers After Reverse Operations](https://leetcode.com/problems/count-distinct-integers-after-reverse-operations/) | Set, Math | O(n log n) Time, O(n) Space | Medium |
| 1447 | [Simplified Fractions](https://leetcode.com/problems/simplified-fractions/)| Math, HashSet | O(n^2) Time, O(n) Space | Medium |
| 1448 | [Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | Tree, DFS | O(n) Time, O(n) Space | Medium |
| 1449 | [📓 Form Largest Integer With Digits That Add up to Target](../leetcode/1449.ipynb) | <span title="Maximize digit count at each cost with unbounded knapsack; reconstruct greedily from largest digit downward.">Unbounded Knapsack DP</span> | O(9*target) Time, O(target) Space | Hard |
| 1450 | [📓 Number of Students Doing Homework at a Given Time](../leetcode/1450.ipynb) | <span title="Count students whose [startTime, endTime] interval contains queryTime using one linear pass.">Single Pass</span> | O(n) Time, O(1) Space | Easy |
| 1451 | [Rearrange Words in a Sentence](https://leetcode.com/problems/rearrange-words-in-a-sentence/) | String, Sorting | O(n log n) Time, O(n) Space | Medium |
| 1452 | [People Whose List of Favorite Companies Is Not a Subset of Another List](https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/) | HashSet, Array| O(n^2) Time, O(n^2) Space   | Medium |
| 1453 | [📓 Maximum Number of Darts Inside of a Circular Dartboard](../leetcode/1453.ipynb) | <span title="For each pair of darts, compute two circle centers of radius r; count darts inside each candidate center.">Geometry</span> | Time: O(n^2*n), Space: O(n) | Hard |
| 1454 | [📓 Active Students](../leetcode/1454.ipynb)| <span title="Seed an active set from the first session and intersect with each subsequent session to retain only universal attendees.">Array, Set</span>| O(n) Time, O(n) Space | Easy |
| 1455 | [Check If a Word Occurs As a Prefix of Any Word in a Sentence](https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/) | String, Array | O(n) Time, O(1) Space | Easy |
| 1456 | [Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) | Sliding Window, String| O(n) Time, O(1) Space | Medium |
| 1457 | [Pseudoclassical Pairs](https://leetcode.com/problems/pseudoclassical-pairs/)  | Math, HashSet | O(n^2) Time, O(n) Space | Hard |
| 1458 | [📓 Max Dot Product of Two Subsequences](../leetcode/1458.ipynb) | <span title="dp[i][j] = max dot product of non-empty subsequences of nums1[0..i] and nums2[0..j]; pair current elements or skip one.">2-D DP</span> | O(m*n) Time, O(m*n) Space | Hard |
| 1459 | [Find the Start and End of the Range](https://leetcode.com/problems/find-the-start-and-end-of-the-range/) | Binary Search, Array  | O(log n) Time, O(1) Space   | Medium |
| 1460 | [Make Two Arrays Equal by Reversing Subarrays](https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/) | Sorting, Array| O(n log n) Time, O(n) Space | Easy |
| 1461 | [Check If a String Contains All Binary Codes of Size K](https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/) | HashSet, Sliding Window | O(n) Time, O(2^k) Space| Medium |
| 1462 | [Course Schedule IV](https://leetcode.com/problems/course-schedule-iv/)   | Graph, Topological Sort | O(n^2) Time, O(n) Space | Hard |
| 1463 | [Cherry Pickup II](https://leetcode.com/problems/cherry-pickup-ii/)| Dynamic Programming, DP| O(n^2) Time, O(n^2) Space   | Hard |
| 1464 | [Max Product of Two Elements in an Array](https://leetcode.com/problems/max-product-of-two-elements-in-an-array/) | Sorting, Array| O(n log n) Time, O(1) Space | Easy |
| 1465 | [Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts](https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/) | Sorting, Math | O(n log n) Time, O(1) Space | Medium |
| 1466 | [Reorder Routes to Make All Paths Lead to the City Zero](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/) | Graph, DFS, BFS | O(n) Time, O(n) Space | Medium |
| 1467 | [Probability of a Two Boxes Having the Same Label](https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-label/) | Math, Simulation| O(n) Time, O(1) Space | Hard |
| 1468 | [📓 Find All Numbers Disappeared in an Array](../leetcode/1468.ipynb) | <span title="Insert all values into a HashSet, then collect every number in [1, n] that is absent from the set.">Array, HashSet</span>| O(n) Time, O(n) Space | Easy |
| 1469 | [📓 Find All Numbers that Disappeared](../leetcode/1469.ipynb) | <span title="Insert all values into a HashSet, then collect every number in [1, n] that is absent from the set.">Array, HashSet</span>| O(n) Time, O(n) Space | Medium |
| 1470 | [📓 Shuffle the Array](../leetcode/1470.ipynb)| <span title="Write first-half elements at even positions and second-half elements at odd positions in a single output pass.">Index Interleaving</span> | O(n) Time, O(n) Space | Easy |
| 1471 | [The k-th Factor of n](https://leetcode.com/problems/the-k-th-factor-of-n/)   | Math, Array   | O(n) Time, O(1) Space | Medium |
| 1472 | [Design Browser History](https://leetcode.com/problems/design-browser-history/) | Stack, Linked List| O(1) Time, O(n) Space | Medium |
| 1473 | [Paint House III](https://leetcode.com/problems/paint-house-iii/)| Dynamic Programming, DP| O(n^2) Time, O(n) Space | Hard |
| 1474 | [Delete N Nodes After M Nodes of a Linked List](https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/) | Linked List, Simulation| O(n) Time, O(1) Space | Medium |
| 1475 | [Final Price with a Special Discount in a Shop](https://leetcode.com/problems/final-price-with-a-special-discount-in-a-shop/) | Stack, Array  | O(n) Time, O(n) Space | Easy |
| 1476 | [Subrectangle Query](https://leetcode.com/problems/subrectangle-query/)  | Matrix, Array | O(1) Time, O(m*n) Space | Medium |
| 1477 | [Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/)| Graph, Array  | O(n) Time, O(n) Space | Easy |
| 1478 | [📓 Allocate Mailboxes](../leetcode/1478.ipynb) | <span title="Precompute median-based single-mailbox costs for each segment; dp[i][m] = min cost for first i houses with m mailboxes.">DP + Median Cost</span> | O(n^2*k) Time, O(n^2) Space | Hard |
| 1479 | [Maximize Palindrome Length From Subsequences](https://leetcode.com/problems/maximize-palindrome-length-from-subsequences/) | Greedy, DP| O(n) Time, O(n) Space | Medium |
| 1480 | [📓 Running Sum of 1d Array](../leetcode/1480.ipynb) | <span title="Add each element's left neighbor cumulatively in one forward pass, turning the array into its own prefix sum.">Prefix Sum In-Place</span> | O(n) Time, O(n) Space | Easy |
| 1481 | [Least Number of Unique Integers after K Removals](https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/) | HashMap, Min-Heap | O(n log n) Time, O(n) Space | Medium |
| 1482 | [📓 Minimum Number of Days to Make m Bouquets](../leetcode/1482.ipynb) | <span title="Halve the search space each step by comparing the midpoint to a monotone predicate.">Binary Search</span> | O(n log n) Time, O(1) Space | Medium |
| 1483 | [Kth Ancestor of a Tree Node](https://leetcode.com/problems/kth-ancestor-of-a-tree-node/) | Tree, Binary Lifting  | O(log n) Time, O(n) Space   | Hard |
| 1484 | [Group Strings](https://leetcode.com/problems/group-strings/)| Graph, Union-Find | O(n log n) Time, O(n) Space | Medium |
| 1| 485 | [📓 Max Consecutive Ones](../leetcode/0485.ipynb) | <span title="Process each element exactly once; maintain running state to build the result.">Single Pass</span> | Time: O(n), Space: O(1) | Easy |
| 1486 | [📓 XOR Operation in an Array](../leetcode/1486.ipynb) | <span title="Compute start+2*i on the fly and XOR into a running accumulator without building the array.">XOR Scan</span> | Time: $O(n)$, Space: $O(1)$ | Easy |
| 1487 | [Making File Names Unique](https://leetcode.com/problems/making-file-names-unique/) | HashMap, Set  | O(n) Time, O(n) Space | Medium |
| 1488 | [Avoid Flood in The City](https://leetcode.com/problems/avoid-flood-in-the-city/) | Heap, HashMap | O(n log n) Time, O(n) Space | Hard |
| 1489 | [Find the Most Competitive Subsequence](https://leetcode.com/problems/find-the-most-competitive-subsequence/) | Stack, Greedy | O(n) Time, O(n) Space | Medium |
| 1490 | [Clone N-ary Tree](https://leetcode.com/problems/clone-n-ary-tree/)| Tree, DFS | O(n) Time, O(n) Space | Medium |
| 1491 | [📓 Average Salary Excluding the Minimum and Maximum Salary](../leetcode/1491.ipynb) | <span title="Find min and max in one pass, subtract both from the total sum, then divide by count minus two.">Array, Sorting</span>| O(n log n) Time, O(1) Space | Easy |
| 1492 | [The kth Factor of n](https://leetcode.com/problems/the-k-th-factor-of-n/)| Math, Array   | O(n) Time, O(1) Space | Medium |
| 1493 | [📓 Longest Subarray of 1's After Deleting One Element](../leetcode/1493.ipynb) | <span title="Expand a window allowing at most one zero; shrink from the left when a second zero appears, answer is window size minus one.">Array, Sliding Window</span> | O(n) Time, O(1) Space | Medium |
| 1494 | [Parallel Courses II](https://leetcode.com/problems/parallel-courses-ii/)| Graph, Topological Sort | O(n^2) Time, O(n) Space | Hard |
| 1495 | [Least Number of Unique Integers After K Removals](https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/) | HashMap, Min-Heap | O(n log n) Time, O(n) Space | Medium |
| 1496 | [Path Crossing](https://leetcode.com/problems/path-crossing/)   | Set, Array| O(n) Time, O(n) Space | Medium |
| 1497 | [Check If Array Pairs Are Divisible by K](https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/) | HashMap, Array| O(n) Time, O(n) Space | Medium |
| 1498 | [📓 Number of Subsequences That Satisfy the Given Sum Condition](../leetcode/1498.ipynb) | <span title="Sort first, then binary search for target positions or boundaries.">Binary Search, Sorting</span> | O(n log n) Time, O(n) Space | Medium |
| 1499 | [Max Value of Equation](https://leetcode.com/problems/max-value-of-equation/) | Stack, Sliding Window | O(n) Time, O(n) Space | Medium |
| 1500 | [Find the Median of a Data Stream](https://leetcode.com/problems/find-the-median-of-a-data-stream/) | Heap, Priority Queue  | O(log n) Time, O(n) Space   | Hard |