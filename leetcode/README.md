## 2D Array
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
| 1074 | [📓 Number of Submatrices That Sum to Target](1074.ipynb) | <span title="2D prefix sums for rectangle totals combined with a hash map to count target-sum submatrices.">2D Prefix Sum + Hash Map</span> | Time: O(n^3), Space: O(n^2)| Hard|
| 1033 | [📓 Matrix Block Sum](1033.ipynb) | <span title="Precompute rectangle sums so any submatrix query is answered in O(1) with inclusion-exclusion.">2D Prefix Sum</span> | Time: O(m * n), Space: O(m * n)| Medium|
|723 | [📓 Candy Crush](0723.ipynb) | <span title="Mark visited elements by negating or cycling their values; no extra space needed.">In-place Marking</span> | Time: O(n * m), Space: O(1)| Medium|

## 2D Prefix Sum
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
| 304 | [📓 Range Sum Query 2D - Immutable](0304.ipynb) | <span title="Precompute rectangle sums so any submatrix query is answered in O(1) with inclusion-exclusion.">2D Prefix Sum</span> | Time: O(1) query, O(m·n) build, Space: O(m·n) | Medium |

## 2D Segment Tree
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
| 308 | [📓 Range Sum Query 2D - Mutable](0308.ipynb) | <span title="Fenwick tree extended to a 2D grid; update and query in O(log m · log n) per operation.">2D Binary Indexed Tree</span> | Time: O(log m · log n) update & query, Space: O(m·n) | Hard |

## Array
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
| 26 | [📓 Remove Duplicates from Sorted Array](0026.ipynb) | <span title="Left and right pointers converge; move the pointer that makes progress toward the target.">Two Pointers</span> | Time: O(n), Space: O(1)| Easy|
| 27 | [📓 Remove Element](0027.ipynb) | <span title="Left and right pointers converge; move the pointer that makes progress toward the target.">Two Pointers</span> | Time: O(n), Space: O(1)| Easy|
| 66 | [📓 Plus One](0066.ipynb) | <span title="Simulate digit-by-digit carry propagation (like hand addition) through linked list nodes.">Carry Simulation</span> | Time: O(n), Space: O(1)| Easy|
| 88 | [📓 Merge Sorted Array](0088.ipynb) | <span title="Merge two sorted arrays in-place from the back using three index pointers.">Three Pointers (Merge from End)</span> | Time: O(m + n), Space: O(1)| Easy|
| 118 | [📓 Pascal's Triangle](0118.ipynb) | <span title="Process the matrix one row at a time, applying local rules to update state.">Row-by-Row Simulation</span> | Time: O(n^2), Space: O(n^2) | Easy |
| 119 | [📓 Pascal's Triangle II](0119.ipynb) | <span title="Reuse a fixed-size DP array row by row, reducing space from O(m·n) to O(n).">Rolling Array</span> | Time: O(k^2), Space: O(k) | Easy |
| 121 | [📓 Best Time to Buy and Sell Stock](0121.ipynb) | <span title="Make the locally optimal choice at each step; one left-to-right pass suffices.">Greedy (One Pass)</span> | Time: O(n), Space: O(1) | Easy |
| 189 | [📓 Rotate Array](0189.ipynb) | <span title="Rotate an array by reversing the whole array, then each part separately.">Three Reversals</span> | Time: O(n), Space: O(1) | Medium |
| 228 | [📓 Summary Ranges](0228.ipynb) | <span title="Single left-to-right pass; update a running answer (min, max, count, etc.) at each step.">Linear Scan</span> | Time: O(n), Space: O(1) | Easy |
| 243 | [📓 Shortest Word Distance](0243.ipynb) | <span title="One traversal, accumulating the answer without backtracking.">One-Pass Linear Scan</span> | Time: O(n), Space: O(1) | Easy |
| 283 | [📓 Move Zeroes](0283.ipynb) | <span title="Write pointer fills valid elements in-place; fill pointer finishes trailing padding.">Two Pointers (Write + Fill)</span> | Time: O(n), Space: O(1) | Easy |
| 448 | [📓 Find All Numbers Disappeared in an Array](0448.ipynb) | <span title="Negate arr[|val|-1] to mark |val| as seen; positive indices signal missing values.">In-place Negation</span> | Time: O(n), Space: O(1) | Easy |
| 463 | [📓 Island Perimeter](0463.ipynb) | <span title="Count each edge once (shared between adjacent cells) in a single grid scan.">Single Pass (Count + Shared Edges)</span> | Time: O(m·n), Space: O(1) | Easy |
| 485 | [📓 Max Consecutive Ones](0485.ipynb) | <span title="Process each element exactly once; maintain running state to build the result.">Single Pass</span> | Time: O(n), Space: O(1) | Easy |
|561 | [Array Partition I](https://leetcode.com/problems/array-partition-i/) | Array| Time: O(n log n), Space: O(1)| Easy|
|598 | [Range Addition II](https://leetcode.com/problems/range-addition-ii/) | Array| Time: O(1), Space: O(1)| Easy|
|603 | [Consecutive Available Seats](https://leetcode.com/problems/consecutive-available-seats/) | Array| Time: O(n), Space: O(1)| Easy|
|605 | [Can Place Flowers](https://leetcode.com/problems/can-place-flowers/) | Array| Time: O(n), Space: O(1)| Easy|
|615 | [Average Salary: Excluding the Minimum and Maximum Salary](https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/)| Array| Time: O(n), Space: O(1)| Easy|
|628 | [Maximum Product of Three Numbers](https://leetcode.com/problems/maximum-product-of-three-numbers/) | Array| Time: O(n log n), Space: O(1)| Easy|
|643 | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | Array| Time: O(n), Space: O(1)| Easy|
|661 | [Image Smoothening](https://leetcode.com/problems/image-smoothening/) | Array| Time: O(mn), Space: O(1) | Easy|
|674 | [Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/) | Array| Time: O(n), Space: O(1)| Easy|
|717 | [1-bit and 2-bit Characters](https://leetcode.com/problems/1-bit-and-2-bit-characters/) | Array| Time: O(n), Space: O(1)| Easy|
|724 | [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) | Array| Time: O(n), Space: O(1)| Easy|
|747 | [Largest Number At Least Twice of Others](https://leetcode.com/problems/largest-number-at-least-twice-of-others/) | Array| Time: O(n), Space: O(1)| Easy|
|766 | [Toeplitz Matrix](https://leetcode.com/problems/toeplitz-matrix/) | Array| Time: O(m * n), Space: O(1)| Easy|
|832 | [Flipping an Image](https://leetcode.com/problems/flipping-an-image/) | Array| Time: O(n), Space: O(1)| Easy|
|867 | [Transpose Matrix](https://leetcode.com/problems/transpose-matrix/) | Array| Time: O(n * m), Space: O(1)| Easy|
|896 | [Monotonic Array](https://leetcode.com/problems/monotonic-array/) | Array| Time: O(n), Space: O(1)| Easy|
|905 | [Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/) | Array| Time: O(n), Space: O(1)| Easy|
|922 | [Sort Array By Parity II](https://leetcode.com/problems/sort-array-by-parity-ii/) | Array| Time: O(n), Space: O(1)| Easy|
|941 | [Valid Mountain Array](https://leetcode.com/problems/valid-mountain-array/) | Array| Time: O(n), Space: O(1)| Easy|
|942 | [DI String Match](https://leetcode.com/problems/di-string-match/) | Array| Time: O(n), Space: O(1)| Easy|
|944 | [Delete Column to Make Sorted](https://leetcode.com/problems/delete-column-to-make-sorted/) | Array| Time: O(n * m), Space: O(1)| Easy|
|985 | [Sum of Even Numbers After Queries](https://leetcode.com/problems/sum-of-even-numbers-after-queries/) | Array| Time: O(n), Space: O(1)| Easy|
|989 | [Add to Array-Form of Integer](https://leetcode.com/problems/add-to-array-form-of-integer/) | Array| Time: O(n), Space: O(1)| Easy|
| 1089 | [📓 Duplicate Zeros](1089.ipynb) | <span title="Count zeros first, then fill backwards from right using a virtual extended index to duplicate each zero in-place.">Two-Pass In-Place</span>| Time: O(n), Space: O(1)| Easy|
| 1090 | [📓 Largest Element in an Array](1090.ipynb) | <span title="Scan the array once tracking the running maximum, updating whenever a larger element is found.">Single Pass</span>| Time: O(n), Space: O(1)| Easy|
| 1304 | [📓 Find N Unique Integers Sum up to Zero](1304.ipynb) | <span title="Fill slots with 1 through n-1, then set the last element to their negated sum to guarantee a total of zero.">Direct Construction</span>| O(n) Time, O(n) Space| Easy|
| 1309 | [📓 Decompress Run-Length Encoded List](1309.ipynb) | <span title="Iterate through [freq, val] pairs and append val exactly freq times to reconstruct each run.">Single Pass Expansion</span>| O(n) Time, O(n) Space| Easy|
| 1313 | [📓 Decompress Array](1313.ipynb) | <span title="Pre-compute total output size once, then expand each [val, freq] pair into a contiguous run in the result buffer.">Single Pass Expansion</span>| O(n) Time, O(n) Space| Easy|
| 1369 | [📓 Get Maximum in Generated Array](1369.ipynb) | <span title="Build the generated array bottom-up using two filling rules, then scan for the maximum value.">Dynamic Programming</span>| O(n) Time, O(1) Space| Easy|
| 1414 | [📓 Find the Minimum of an Integer Array](1414.ipynb) | <span title="Scan the array once tracking the running minimum, updating whenever a smaller element is found.">Single Pass</span>| O(n) Time, O(1) Space| Easy|
| 1431 | [📓 Kids With the Greatest Number of Candies](1431.ipynb) | <span title="Find the global maximum first, then check if each kid's total with extra candies meets or exceeds it.">Single Pass</span>| O(n) Time, O(1) Space| Easy|
| 1450 | [📓 Number of Students Doing Homework at a Given Time](1450.ipynb) | <span title="Count students whose [startTime, endTime] interval contains queryTime using one linear pass.">Single Pass</span>| O(n) Time, O(1) Space| Easy|
| 1470 | [📓 Shuffle the Array](1470.ipynb) | <span title="Write first-half elements at even positions and second-half elements at odd positions in a single output pass.">Index Interleaving</span>| O(n) Time, O(n) Space| Easy|
| 1480 | [📓 Running Sum of 1d Array](1480.ipynb) | <span title="Add each element's left neighbor cumulatively in one forward pass, turning the array into its own prefix sum.">Prefix Sum In-Place</span>| O(n) Time, O(n) Space| Easy|
| 31 | [📓 Next Permutation](0031.ipynb) | <span title="Find the rightmost descent, swap with the smallest successor to the right, then reverse the suffix.">Three-Step Reverse</span>| Time: O(n), Space: O(1)| Medium|
| 48 | [📓 Rotate Image](0048.ipynb) | <span title="Transpose the matrix across the main diagonal, then reverse each row to achieve a 90 degree clockwise rotation.">Transpose + Row Reverse</span>| Time: O(n^2), Space: O(1)| Medium|
| 54 | [📓 Spiral Matrix](0054.ipynb) | <span title="Shrink four boundary pointers inward after each directional pass to peel the matrix layer by layer.">Boundary Shrinking</span>| Time: O(m * n), Space: O(1)| Medium|
| 59 | [📓 Spiral Matrix II](0059.ipynb) | <span title="Fill numbers 1 to n-squared in spiral order using four boundary pointers that shrink inward after each directional pass.">Boundary Simulation</span>| Time: O(n^2), Space: O(1)| Medium|
| 73 | [📓 Set Matrix Zeroes](0073.ipynb) | <span title="Use the first row and column as markers for which rows and cols to zero, saving their original state in two booleans.">First Row/Col as Flags</span>| Time: O(m * n), Space: O(1)| Medium|
| 80 | [📓 Remove Duplicates from Sorted Array II](0080.ipynb) | <span title="Advance a write pointer, admitting each element only if it differs from the value two slots behind the write head.">Two Pointers</span>| Time: O(n), Space: O(1)| Medium|
|163 | [Missing Ranges](https://leetcode.com/problems/missing-ranges/) | Array| Time: O(n), Space: O(1)| Medium|
|238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Array| Time: O(n), Space: O(1)| Medium|
|289 | [Game of Life](https://leetcode.com/problems/game-of-life/) | Array| Time: O(m * n), Space: O(1)| Medium|
|302 | [Smallest Rectangle Enclosing Black Pixels](https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/) | Array| Time: O(m + n), Space: O(1)| Medium|
|311 | [Sparse Matrix Multiplication](https://leetcode.com/problems/sparse-matrix-multiplication/) | Array| Time: O(m * n * k), Space: O(m * n)| Medium|
|348 | [Design Tic-Tac-Toe](https://leetcode.com/problems/design-tic-tac-toe/) | Array| Time: O(1), Space: O(1)| Medium|
|419 | [Battleships in a Board](https://leetcode.com/problems/battleships-in-a-board/) | Array| Time: O(m * n), Space: O(1)| Medium|
|443 | [String Compression](https://leetcode.com/problems/string-compression/) | Array| Time: O(n), Space: O(1)| Medium|
|498 | [Diagonal Traverse](https://leetcode.com/problems/diagonal-traverse/) | Array| Time: O(m * n), Space: O(1)| Medium|
|556 | [Next Greater Element III](https://leetcode.com/problems/next-greater-element-iii/) | Array| Time: O(n), Space: O(n)| Medium|
|565 | [Array Nesting](https://leetcode.com/problems/array-nesting/) | Array| Time: O(n), Space: O(n)| Medium|
|581 | [Shortest Unsorted Continuous Subarray](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/) | Array| Time: O(n), Space: O(1)| Medium|
|624 | [Maximum Distance in Arrays](https://leetcode.com/problems/maximum-distance-in-arrays/) | Array| Time: O(n), Space: O(1)| Medium|
|665 | [Non-decreasing Array](https://leetcode.com/problems/non-decreasing-array/) | Array| Time: O(n), Space: O(1)| Medium|
|835 | [Image Overlap](https://leetcode.com/problems/image-overlap/) | Array| Time: O(n^2), Space: O(1)| Medium|
|840 | [Magic Squares In Grid](https://leetcode.com/problems/magic-squares-in-grid/) | Array| Time: O(n), Space: O(1)| Medium|
|848 | [Shifting Letters](https://leetcode.com/problems/shifting-letters/) | Array| Time: O(n), Space: O(1)| Medium|
|861 | [Score After Flipping Matrix](https://leetcode.com/problems/score-after-flipping-matrix/) | Array| Time: O(n * m), Space: O(1)| Medium|
| 1098 | [📓 Sort the Matrix Diagonally](1098.ipynb) | <span title="Group cells by diagonal key (row minus col), sort each group, then scatter values back in traversal order.">Diagonal Grouping</span>| Time: O(n^2 log n), Space: O(n^2)| Medium|
| 1243 | [📓 Array Transformation](1243.ipynb) | <span title="Apply local-min-up/local-max-down each round, stopping as soon as a full pass produces no changes.">Simulation</span>| O(n) Time, O(1) Space| Medium|
| 41 | [📓 First Missing Positive](0041.ipynb) | <span title="Negate nums[val-1] to stamp which values are present, then scan for the first positive slot.">In-place Index Negation</span>| Time: O(n), Space: O(1)| Hard|
|782 | [Transform to Chessboard](https://leetcode.com/problems/transform-to-chessboard/) | Array| Time: O(n^2), Space: O(1)| Hard|
|4 | [📓 Median of Two Sorted Arrays](0004.ipynb) | <span title="Sort the array first, then narrow the search window by half each step.">Array, Binary Search</span> | Time: O(log(min(m, n))), Space: O(1) | Hard|
|268 | [📓 Missing Number](0268.ipynb) | <span title="XOR all indices with all values; identical pairs cancel, leaving only the missing number.">XOR with Indices</span> | Time: O(n), Space: O(1)| Easy|
| 1412 | [📓 Shortest Distance to Target String in a Circular Array](1412.ipynb) | <span title="For each occurrence of the target, compute min(clockwise, counterclockwise) distance and track the running minimum.">Circular Array</span>| O(n) Time, O(n) Space| Medium|
|529 | [Minesweeper](https://leetcode.com/problems/minesweeper/) | Array, Depth-First Search (DFS)| Time: O(n), Space: O(n)| Medium|
|641 | [Design Circular Deque](https://leetcode.com/problems/design-circular-deque/) | Array, Deque | Time: O(1), Space: O(k)| Medium|
|915 | [Partition Array into Disjoint Intervals](https://leetcode.com/problems/partition-array-into-disjoint-intervals/) | Array, Dynamic Programming | Time: O(n), Space: O(n)| Medium|
| 1191 | [📓 K Concatenation Maximum Sum](1191.ipynb) | <span title="Run Kadane on the double copy for cross-boundary subarrays, then add (k-2) times total sum when positive.">Kadane + Math</span>| O(n) Time, O(1) Space| Medium|
|573 | [Squirrel Simulation](https://leetcode.com/problems/squirrel-simulation/) | Array, Dynamic Programming | Time: O(n), Space: O(n)| Hard|
|287 | [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) | Array, Floyd's Tortoise and Hare | Time: O(n), Space: O(1)| Medium|
|670 | [Maximum Swap](https://leetcode.com/problems/maximum-swap/) | Array, Greedy| Time: O(n), Space: O(n)| Medium|
| 1386 | [📓 Cinema Seat Allocation](1386.ipynb) | <span title="Represent reserved seats per row as a 10-bit integer, then test three column-block masks to count valid groups.">Bitmask</span>| O(n * m) Time, O(n * m) Space| Medium|
| 1133 | [📓 Largest Unique Number](1133.ipynb) | <span title="Count occurrences in a hash map in one pass, then return the largest key with exactly one occurrence.">Frequency Count</span>| Time: O(n), Space: O(n)| Easy|
|245 | [Shortest Word Distance III](https://leetcode.com/problems/shortest-word-distance-iii/) | Array, Hash Map| Time: O(n), Space: O(1)| Medium|
|523 | [Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/) | Array, Hash Map| Time: O(n), Space: O(n)| Medium|
|531 | [Lonely Pixel I](https://leetcode.com/problems/lonely-pixel-i/) | Array, Hash Map| Time: O(m * n), Space: O(m + n)| Medium|
|532 | [K-diff Pairs in an Array](https://leetcode.com/problems/k-diff-pairs-in-an-array/) | Array, Hash Map| Time: O(n), Space: O(n)| Medium|
|533 | [Lonely Pixel II](https://leetcode.com/problems/lonely-pixel-ii/) | Array, Hash Map| Time: O(m * n), Space: O(m + n)| Medium|
|539 | [Minimum Time Difference](https://leetcode.com/problems/minimum-time-difference/) | Array, Hash Map| Time: O(n), Space: O(n)| Medium|
|560 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | Array, Hash Map| Time: O(n), Space: O(n)| Medium|
|567 | [Permutation in String](https://leetcode.com/problems/permutation-in-string/) | Array, Hash Map| Time: O(n), Space: O(n)| Medium|
|911 | [Online Election](https://leetcode.com/problems/online-election/) | Array, Hash Map| Time: O(1), Space: O(n)| Medium|
|923 | [3Sum With Multiplicity](https://leetcode.com/problems/3sum-with-multiplicity/) | Array, Hash Map| Time: O(n^2), Space: O(n)| Medium|
| 1146 | [📓 Snapshot Array](1146.ipynb) | <span title="Store (snap_id, value) pairs per index; binary-search for the floor entry to answer get() in O(log s).">Binary Search on Snapshots</span>| Time: O(1), Space: O(n)| Medium|
|710 | [Random Pick with Blacklist](https://leetcode.com/problems/random-pick-with-blacklist/) | Array, Hash Map| Time: O(1), Space: O(n)| Hard|
|645 | [Set Mismatch](https://leetcode.com/problems/set-mismatch/) | Array, Hash Set| Time: O(n), Space: O(n)| Easy|
|961 | [N-Repeated Element in Size 2N Array](https://leetcode.com/problems/n-repeated-element-in-size-2n-array/) | Array, Hash Set| Time: O(n), Space: O(n)| Easy|
|442 | [Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/) | Array, Hash Set| Time: O(n), Space: O(n)| Medium|
|945 | [Minimum Increment to Make Array Unique](https://leetcode.com/problems/minimum-increment-to-make-array-unique/) | Array, Hash Set| Time: O(n log n), Space: O(n)| Medium|
| 1176 | [📓 Diet Plan Performance](1176.ipynb) | <span title="Compute the first k-day window sum once, then slide by adding the incoming day and subtracting the outgoing day.">Sliding Window</span>| O(n) Time, O(n) Space| Easy|
| 1287 | [📓 Element Appearing More Than 25% in Sorted Array](1287.ipynb)| <span title="Check arr[i] == arr[i + n/4] for each i; the dominant element must bridge any quarter-length gap.">Quarter-Jump Check</span>| O(n) Time, O(1) Space| Easy|
| 1384 | [📓 Movie Rating](1384.ipynb) | <span title="Aggregate user rating counts and Feb-2020 movie sums in one pass, then pick the top entries from each map.">Dual Hash Map</span>| O(n) Time, O(n) Space| Easy|
| 1182 | [📓 Shortest Distance to Target Color](1182.ipynb) | <span title="Left-to-right and right-to-left sweeps per color precompute distances so each query answers in O(1).">Two-Pass Precomputation</span>| O(n) Time, O(n) Space| Medium|
| 1204 | [📓 Design Hit Counter](1204.ipynb) | <span title="Fixed 300 slots indexed by timestamp % 300; overwrite stale slots on hit() and sum valid slots on getHits().">Circular Buffer</span>| O(1) Time, O(k) Space| Medium|
| 1226 | [📓 The Employee That Worked on the Longest Task](1226.ipynb) | <span title="Track the previous end-time; update the best employee whenever the current task duration strictly exceeds the running maximum.">Array, HashMap</span> | O(n) Time, O(n) Space| Medium|
| 1183 | [📓 Maximum Number of Ones](1183.ipynb) | <span title="Count positions by tile-type (row mod sideLength, col mod sideLength), then greedily fill the most-common types first.">Array, HashMap</span> | O(n) Time, O(n) Space| Hard|
| 1398 | [📓 Company Finder](1398.ipynb) | <span title="Load the first array into a HashSet, then collect elements from the second array that hit the set in O(1).">Array, HashSet</span> | O(n) Time, O(n) Space| Easy|
| 1426 | [📓 Counting Elements](1426.ipynb) | <span title="Build a HashSet of all values, then count each element x whose successor x+1 is also in the set.">Array, HashSet</span> | O(n) Time, O(n) Space| Easy|
| 1468 | [📓 Find All Numbers Disappeared in an Array](1468.ipynb) | <span title="Insert all values into a HashSet, then collect every number in [1, n] that is absent from the set.">Array, HashSet</span> | O(n) Time, O(n) Space| Easy|
| 1469 | [📓 Find All Numbers that Disappeared](1469.ipynb) | <span title="Insert all values into a HashSet, then collect every number in [1, n] that is absent from the set.">Array, HashSet</span> | O(n) Time, O(n) Space| Medium|
|569 | [Median Employee Salary](https://leetcode.com/problems/median-employee-salary/) | Array, Heap| Time: O(n log n), Space: O(n)| Medium|
| 1389 | [📓 Create Target Array in the Given Order](1389.ipynb) | <span title="Use a resizable list's built-in insert to place each element at its specified index, shifting the tail right.">Array, Insertion</span> | O(n) Time, O(n) Space| Easy|
| 1299 | [📓 Replace Elements with Greatest Element on Right Side](1299.ipynb) | <span title="Scan right-to-left maintaining a running maximum; write it into each position before extending it with the original value.">Array, Iteration</span> | O(n) Time, O(1) Space| Easy|
|251 | [Flatten 2D Vector](https://leetcode.com/problems/flatten-2d-vector/) | Array, Iterator| Time: O(1), Space: O(1)| Medium|
|900 | [RLE Iterator](https://leetcode.com/problems/rle-iterator/) | Array, Iterator| Time: O(1), Space: O(n)| Medium|
| 1409 | [📓 Queries on a Permutation With Key](1409.ipynb) | <span title="Maintain the permutation in a list; for each query, find the element's position, record it, and move it to the front.">Array, Map</span> | O(1) Time, O(n) Space| Medium|
| 1184 | [📓 Distance Between Bus Stops](1184.ipynb) | <span title="Sum the clockwise arc from source to destination and return the minimum of that and the total-minus-clockwise distance.">Array, Math</span>| O(n) Time, O(1) Space| Easy|
| 1063 | [📓 Valid Triangles](1063.ipynb) | <span title="Sort the array, then fix the largest side and use two pointers to count pairs whose sum exceeds it.">Array, Math</span>| Time: O(n^3), Space: O(1)| Medium|
| 1222 | [📓 Queens That Can Attack the King](1222.ipynb) | <span title="Store queens in a HashSet, then walk outward in all 8 directions from the king, stopping at the first queen found.">Array, Matrix</span>| O(1) Time, O(1) Space| Medium|
| 1013 | [📓 Partition Array Into Three Parts With Equal Sum](1013.ipynb) | <span title="Compute total sum divided by 3, then scan left-to-right counting how many times the running sum hits each target multiple.">Array, Prefix Sum</span>| Time: O(n), Space: O(1)| Medium|
| 1375 | [📓 Bulb Switcher III](1375.ipynb) | <span title="Count turned-on bulbs and track the rightmost position; a moment is all-blue when the max position equals the count.">Array, Prefix Sum</span>| O(n) Time, O(n) Space| Medium|
| 1424 | [📓 Diagonal Traverse II](1424.ipynb) | <span title="Group elements by diagonal key (row + col) into buckets, then emit each bucket in reverse-row order.">Array, Priority Queue</span>| O(n log n) Time, O(n) Space| Medium|
|622 | [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) | Array, Queue | Time: O(1), Space: O(k)| Medium|
| 1454 | [📓 Active Students](1454.ipynb) | <span title="Seed an active set from the first session and intersect with each subsequent session to retain only universal attendees.">Array, Set</span> | O(n) Time, O(n) Space| Easy|
|849 | [Maximize Distance to Closest Person](https://leetcode.com/problems/maximize-distance-to-closest-person/) | Array, Simulation| Time: O(n), Space: O(1)| Easy|
| 1087 | [📓 Design Tic-Tac-Toe](1087.ipynb) | <span title="Use per-row, per-column, and diagonal integer counters to detect wins in O(1) per move.">Array, Simulation</span>| Time: O(1), Space: O(1)| Easy|
|807 | [Max Increase to Keep City Skyline](https://leetcode.com/problems/max-increase-to-keep-city-skyline/) | Array, Simulation| Time: O(n^2), Space: O(n)| Medium|
|838 | [Push Dominoes](https://leetcode.com/problems/push-dominoes/) | Array, Simulation| Time: O(n), Space: O(n)| Medium|
|957 | [Prison Cells After N Days](https://leetcode.com/problems/prison-cells-after-n-days/) | Array, Simulation| Time: O(n), Space: O(1)| Medium|
|927 | [Three Equal Parts](https://leetcode.com/problems/three-equal-parts/) | Array, Simulation| Time: O(n), Space: O(1)| Hard|
| 1350 | [📓 Product of the Last K Numbers](1350.ipynb) | <span title="Maintain a prefix-product list; reset on zero and answer queries in O(1) via prefix division.">Array, Sliding Window</span>| O(1) Time, O(n) Space| Medium|
| 1352 | [📓 Product of Array Except Self](1352.ipynb) | <span title="Accumulate prefix products left-to-right, then fold in suffix products right-to-left using a single scalar.">Array, Sliding Window</span>| O(1) Time, O(n) Space| Medium|
| 1437 | [📓 Check If All 1's Are at Least Length K Places Away](1437.ipynb)| <span title="Track the index of the last seen 1 and reject any pair whose gap falls below k.">Array, Sliding Window</span>| O(n) Time, O(1) Space| Medium|
| 1493 | [📓 Longest Subarray of 1's After Deleting One Element](1493.ipynb)| <span title="Expand a window allowing at most one zero; shrink from the left when a second zero appears, answer is window size minus one.">Array, Sliding Window</span>| O(n) Time, O(1) Space| Medium|
|683 | [K Empty Slots](https://leetcode.com/problems/k-empty-slots/) | Array, Sliding Window| Time: O(n), Space: O(1)| Hard|
| 1444 | [📓 Count Subarrays With Fixed Bounds](1444.ipynb) | <span title="Slide a window tracking the last out-of-range index and last positions of minK and maxK to count valid subarrays in O(1).">Array, Sliding Window</span>| O(n) Time, O(1) Space| Hard|
|976 | [Largest Perimeter Triangle](https://leetcode.com/problems/largest-perimeter-triangle/) | Array, Sorting | Time: O(n log n), Space: O(1)| Easy|
| 1187 | [📓 Make Two Arrays Equal by Reversing Subarrays](1187.ipynb) | <span title="Sort both arrays; any permutation is reachable via reversals, so equality of sorted forms implies transformability.">Array, Sorting</span> | O(n log n) Time, O(n) Space| Easy|
| 1491 | [📓 Average Salary Excluding the Minimum and Maximum Salary](1491.ipynb) | <span title="Find min and max in one pass, subtract both from the total sum, then divide by count minus two.">Array, Sorting</span> | O(n log n) Time, O(1) Space| Easy|
|775 | [Global and Local Inversions](https://leetcode.com/problems/global-and-local-inversions/) | Array, Sorting | Time: O(n log n), Space: O(n)| Medium|
|825 | [Friends Of Appropriate Ages](https://leetcode.com/problems/friends-of-appropriate-ages/) | Array, Sorting | Time: O(n log n), Space: O(1)| Medium|
|955 | [Delete Columns to Make Sorted II](https://leetcode.com/problems/delete-columns-to-make-sorted-ii/) | Array, Sorting | Time: O(n log n), Space: O(1)| Medium|
|960 | [Delete Columns to Make Sorted III](https://leetcode.com/problems/delete-columns-to-make-sorted-iii/) | Array, Sorting | Time: O(n log n), Space: O(1)| Medium|
| 1053 | [📓 Previous Permutation With One Swap](1053.ipynb) | <span title="Scan from the right for the first descent, then swap with the leftmost occurrence of the largest valid smaller element.">Array, Sorting</span> | Time: O(n), Space: O(1)| Medium|
| 1205 | [📓 Google Question](1205.ipynb) | <span title="Sort meeting start and end times independently, then greedily reuse rooms with a two-pointer sweep.">Array, Sorting</span> | O(n log n) Time, O(1) Space| Medium|
| 1303 | [📓 Find the Team Size](1303.ipynb) | <span title="Build a frequency map of team sizes in one pass, then look up each employee's team count directly.">Array, Sorting</span> | O(n log n) Time, O(n) Space| Medium|
| 1333 | [📓 Filter Restaurants by Vegan-Friendly, Price and Distance](1333.ipynb)| <span title="Filter by constraints first, then sort survivors by rating descending and id descending.">Array, Sorting</span> | O(n log n) Time, O(n) Space| Medium|
| 1395 | [📓 Count Number of Teams](1395.ipynb) | <span title="Fix each element as the middle soldier and count smaller/larger elements on each side to multiply valid triplet counts.">Array, Sorting</span> | O(n^2) Time, O(n) Space| Medium|
| 1308 | [📓 Run-Length Encoding II](1308.ipynb) | <span title="Process encoded runs directly without decoding, splitting the targeted run and merging adjacent same-character runs.">Array, String</span>| O(n) Time, O(n) Space| Medium|
|821 | [Shortest Distance to a Character](https://leetcode.com/problems/shortest-distance-to-a-character/) | Array, Two Pointers| Time: O(n), Space: O(1)| Easy|
| 1113 | [📓 Intersection of Three Sorted Arrays](1113.ipynb) | <span title="Advance the pointer pointing at the smallest value; record and advance all three when they agree.">Three Pointers</span> | Time: $O(n)$, Space: $O(1)$ | Easy |
|845 | [Longest Mountain in Array](https://leetcode.com/problems/longest-mountain-in-array/) | Array, Two Pointers| Time: O(n), Space: O(1)| Medium|
| 1327 | [📓 Sort Array by Parity](1327.ipynb) | <span title="Advance left past evens and right past odds; swap when left holds an odd and right holds an even.">Two Pointers</span> | Time: $O(n)$, Space: $O(1)$ | Medium |
| 1486 | [📓 XOR Operation in an Array](1486.ipynb) | <span title="Compute start+2*i on the fly and XOR into a running accumulator without building the array.">XOR Scan</span> | Time: $O(n)$, Space: $O(1)$ | Easy |

## Backtracking
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
| 293 | [📓 Flip Game](0293.ipynb) | <span title="One sweep through the data, typically updating a counter or maximum in place.">Single Scan</span> | Time: O(n²), Space: O(n) per result | Easy |
| 784 | [📓 Letter Case Permutation](0784.ipynb) | <span title="DFS with explicit undo steps; prune branches early when constraints are already violated.">Backtracking (DFS)</span> | Time: $O(n \cdot 2^n)$, Space: $O(n)$ | Medium |
| 22 | [📓 Generate Parentheses](0022.ipynb) | <span title="DFS with explicit undo steps; prune branches early when constraints are already violated.">Backtracking (DFS)</span> | Time: $O\left(\frac{4^n}{\sqrt{n}}\right)$, Space: $O(n)$ | Medium |
| 39 | [📓 Combination Sum](0039.ipynb) | <span title="DFS with explicit undo steps; prune branches early when constraints are already violated.">Backtracking (DFS)</span> | Time: $O(N^{T/M})$, Space: $O(T/M)$ | Medium |
| 40 | [📓 Combination Sum II](0040.ipynb) | <span title="DFS with explicit undo steps; prune branches early when constraints are already violated.">Backtracking (DFS)</span> | Time: $O(2^N)$, Space: $O(N)$ | Medium |
|784 | [Letter Case Permutation](https://leetcode.com/problems/letter-case-permutation/) | Backtracking | Time: O(2^n), Space: O(1)| Easy|
| 17 | [📓 Letter Combinations of a Phone Number](0017.ipynb) | <span title="Explore all candidates recursively; undo (backtrack) a choice when it leads to a dead end.">Backtracking</span> | Time: O(4^n), Space: O(n)| Medium|
| 22 | [📓 Generate Parentheses](0022.ipynb) | <span title="Use open/close counters as constraints; only add ( when opens < n and ) when closes < opens.">Backtracking (DFS)</span> | Time: $O\!\left(\frac{4^n}{\sqrt{n}}\right)$, Space: $O(n)$ | Medium |
| 39 | [📓 Combination Sum](0039.ipynb) | <span title="DFS with explicit undo steps; prune branches early when constraints are already violated.">Backtracking (DFS)</span> | Time: $O(N^{T/M})$, Space: $O(T/M)$ | Medium |
| 40 | [📓 Combination Sum II](0040.ipynb) | <span title="DFS with explicit undo steps; prune branches early when constraints are already violated.">Backtracking (DFS)</span> | Time: $O(2^N)$, Space: $O(N)$ | Medium |
| 46 | [📓 Permutations](0046.ipynb) | <span title="Swap each element to the current position, recurse on the suffix, then swap back to restore order.">Backtracking (Swap)</span> | Time: $O(n \times n!)$, Space: $O(n)$ | Medium |
| 47 | [📓 Permutations II](0047.ipynb) | <span title="Sort first, then skip duplicate elements at the same recursion depth to avoid repeated permutations.">Backtracking + Dedup</span> | Time: $O(n \times n!)$, Space: $O(n)$ | Medium |
| 77 | [📓 Combinations](0077.ipynb) | <span title="Fix a start index and recurse forward; prune branches where remaining elements cannot fill the combination.">Backtracking</span> | Time: $O\!\left(\binom{n}{k} \cdot k\right)$, Space: $O(k)$ | Medium |
| 78 | [📓 Subsets](0078.ipynb) | <span title="Record the running path at every step, then recurse from index+1 to generate all 2^n subsets.">Backtracking</span> | Time: $O(2^n \cdot n)$, Space: $O(n)$ | Medium |
| 79 | [📓 Word Search](0079.ipynb) | <span title="Mark each visited cell with a sentinel character in-place; restore it after the recursive call returns.">DFS + Backtracking</span> | Time: $O(m \cdot n \cdot 4^L)$, Space: $O(L)$ | Medium |
| 90 | [📓 Subsets II](0090.ipynb) | <span title="Sort first, then skip duplicate elements at the same recursion depth to avoid repeated subsets.">Backtracking + Dedup</span> | Time: $O(2^n \cdot n)$, Space: $O(n)$ | Medium |
| 93 | [📓 Restore IP Addresses](0093.ipynb) | <span title="Try 1-3 digit segments at each of 4 boundaries; prune segments outside 0-255 or with leading zeros.">Backtracking</span> | Time: $O(1)$, Space: $O(1)$ | Medium |
|131 | [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) | Backtracking | Time: O(2^n), Space: O(n)| Medium|
|216 | [Combination Sum III](https://leetcode.com/problems/combination-sum-iii/) | Backtracking | Time: O(2^n), Space: O(n)| Medium|
|254 | [Factor Combinations](https://leetcode.com/problems/factor-combinations/) | Backtracking | Time: O(n log n), Space: O(n)| Medium|
|267 | [Palindrome Permutation II](https://leetcode.com/problems/palindrome-permutation-ii/) | Backtracking | Time: O(n!), Space: O(n) | Medium|
|291 | [Word Pattern II](https://leetcode.com/problems/word-pattern-ii/) | Backtracking | Time: O(n!), Space: O(n) | Medium|
|294 | [Flip Game II](https://leetcode.com/problems/flip-game-ii/) | Backtracking | Time: O(n), Space: O(n)| Medium|
|320 | [Generalized Abbreviation](https://leetcode.com/problems/generalized-abbreviation/) | Backtracking | Time: O(2^n), Space: O(n)| Medium|
|351 | [Android Unlock Patterns](https://leetcode.com/problems/android-unlock-patterns/) | Backtracking | Time: O(n), Space: O(1)| Medium|
|491 | [Increasing Subsequences](https://leetcode.com/problems/increasing-subsequences/) | Backtracking | Time: O(2^n), Space: O(n)| Medium|
|610 | [Combination Sum III](https://leetcode.com/problems/combination-sum-iii/) | Backtracking | Time: O(n!), Space: O(n) | Medium|
| 1109 | [📓 Corporate Flight Bookings](1109.ipynb) | <span title="Mark +seats at booking start and -seats one past the end; a single prefix-sum pass yields per-flight counts.">Difference Array</span> | Time: $O(n + m)$, Space: $O(1)$ | Medium |
| 37 | [📓 Sudoku Solver](0037.ipynb) | <span title="Try digits 1-9 in each empty cell; validate row, column, and 3×3 box; backtrack on failure.">Backtracking</span> | Time: $O(9^m)$, Space: $O(m)$ | Hard |
| 51 | [N-Queens](https://leetcode.com/problems/n-queens/) | Backtracking | Time: O(n!), Space: O(n) | Hard|
| 52 | [N-Queens II](https://leetcode.com/problems/n-queens-ii/) | Backtracking | Time: O(n!), Space: O(n) | Hard|
|282 | [Expression Add Operators](https://leetcode.com/problems/expression-add-operators/) | Backtracking | Time: O(4^n), Space: O(n)| Hard|
|425 | [Word Squares](https://leetcode.com/problems/word-squares/) | Backtracking | Time: O(n^4), Space: O(n^2)| Hard|
|440 | [K-th Smallest in Lexicographical Order](https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/) | Backtracking | Time: O(n), Space: O(1)| Hard|
|488 | [Zuma Game](https://leetcode.com/problems/zuma-game/) | Backtracking | Time: O(n!), Space: O(n) | Hard|
|489 | [Robot Room Cleaner](https://leetcode.com/problems/robot-room-cleaner/) | Backtracking | Time: O(4^n), Space: O(n)| Hard|
|679 | [24 Game](https://leetcode.com/problems/24-game/) | Backtracking | Time: O(n!), Space: O(1) | Hard|
|996 | [Number of Squareful Arrays](https://leetcode.com/problems/number-of-squareful-arrays/) | Backtracking | Time: O(n!), Space: O(n) | Hard|
| 1421 | [N-Queens II](https://leetcode.com/problems/n-queens-ii/) | Backtracking | O(n!) Time, O(n) Space | Hard|
| 1286 | [Iterator for Combination](https://leetcode.com/problems/iterator-for-combination/) | Backtracking, Array| O(1) Time, O(n) Space| Medium|
| 1294 | [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) | Backtracking, Array| O(2^n) Time, O(n) Space| Medium|
| 1415 | [The k-th Lexicographical String of All Happy Strings of Length n](https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/) | Backtracking, DFS| O(3^n) Time, O(n) Space| Medium|
|902 | [Numbers At Most N Given Digit Set](https://leetcode.com/problems/numbers-at-most-n-given-digit-set/) | Backtracking, DFS| Time: O(n), Space: O(1)| Hard|
|980 | [Unique Paths III](https://leetcode.com/problems/unique-paths-iii/) | Backtracking, DFS| Time: O(n^2), Space: O(n^2)| Hard|
|698 | [Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) | Backtracking, DP | Time: O(2^n), Space: O(n)| Hard|
|473 | [Matchsticks to Square](https://leetcode.com/problems/matchsticks-to-square/) | Backtracking, Dynamic Programming| Time: O(4^n), Space: O(n)| Medium|
|526 | [Beautiful Arrangement](https://leetcode.com/problems/beautiful-arrangement/) | Backtracking, Dynamic Programming| Time: O(n!), Space: O(n) | Medium|
| 60 | [Permutation Sequence](https://leetcode.com/problems/permutation-sequence/) | Backtracking, Math | Time: O(n^2), Space: O(n)| Hard|
|842 | [Split Array into Fibonacci Sequence](https://leetcode.com/problems/split-array-into-fibonacci-sequence/) | Backtracking, Recursion| Time: O(n), Space: O(n)| Medium|
| 1076 | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | Backtracking, String | Time: O(3^n), Space: O(1)| Medium|
| 1307 | [Verbal Arithmetic Puzzle](https://leetcode.com/problems/verbal-arithmetic-puzzle/) | Backtracking, String | O(10!) Time, O(10) Space | Hard|

## BFS
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
| 429 | [📓 N-ary Tree Level Order Traversal](0429.ipynb) | <span title="Breadth-first search with a queue; visit all neighbors level by level.">BFS (Queue)</span> | Time: $O(n)$, Space: $O(n)$ | Easy |
| 286 | [📓 Walls and Gates](0286.ipynb) | <span title="Breadth-first search with a queue; visit all neighbors level by level.">BFS (Queue)</span> | Time: $O(m \cdot n)$, Space: $O(m \cdot n)$ | Medium |
| 433 | [📓 Minimum Genetic Mutation](0433.ipynb) | <span title="Breadth-first search with a queue; visit all neighbors level by level.">BFS (Queue)</span> | Time: $O(N^2 \cdot L)$, Space: $O(N)$ | Medium |
| 1091 | [📓 Shortest Path in Binary Matrix](1091.ipynb) | <span title="Breadth-first search with a queue; visit all neighbors level by level.">BFS (Queue)</span> | Time: $O(n^2)$, Space: $O(n^2)$ | Medium |
| 752 | [📓 Open the Lock](0752.ipynb) | <span title="Breadth-first search with a queue; visit all neighbors level by level.">BFS (Queue)</span> | Time: $O(10^4 + D)$, Space: $O(10^4 + D)$ | Medium |
|909 | [Snakes and Ladders](https://leetcode.com/problems/snakes-and-ladders/) | BFS| Time: O(n^2), Space: O(n)| Medium|
|317 | [Shortest Distance from All Buildings](https://leetcode.com/problems/shortest-distance-from-all-buildings/) | BFS| Time: O(m * n), Space: O(m * n)| Hard|
|499 | [The Maze III](https://leetcode.com/problems/the-maze-iii/) | BFS| Time: O(m * n), Space: O(m * n)| Hard|
|773 | [Sliding Puzzle](https://leetcode.com/problems/sliding-puzzle/) | BFS| Time: O(n^2), Space: O(n^2)| Hard|
|854 | [K-Similar Strings](https://leetcode.com/problems/k-similar-strings/) | BFS| Time: O(n * n!), Space: O(n!)| Hard|
|301 | [Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/) | BFS, Backtracking| Time: O(2^n), Space: O(n)| Hard|
|864 | [Shortest Path to Get All Keys](https://leetcode.com/problems/shortest-path-to-get-all-keys/) | BFS, Bitmask | Time: O(n * m), Space: O(n * m)| Hard|
|490 | [The Maze](https://leetcode.com/problems/the-maze/) | BFS, DFS | Time: O(m * n), Space: O(m * n)| Medium|
|934 | [Shortest Bridge](https://leetcode.com/problems/shortest-bridge/) | BFS, DFS | Time: O(n^2), Space: O(n)| Medium|
|127 | [Word Ladder](https://leetcode.com/problems/word-ladder/) | BFS, Graph | Time: O(n^2), Space: O(n)| Medium|
| 1091 | [Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | BFS, Graph | Time: O(n^2), Space: O(n^2)| Medium|
| 1129 | [Shortest Path with Alternating Colors](https://leetcode.com/problems/shortest-path-with-alternating-colors/) | BFS, Graph | Time: O(n), Space: O(n)| Medium|
|126 | [Word Ladder II](https://leetcode.com/problems/word-ladder-ii/) | BFS, Graph | Time: O(n^2), Space: O(n)| Hard|
| 1092 | [Shortest Path in a Grid with Obstacles Elimination](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/) | BFS, Graph | Time: O(n^2), Space: O(n^2)| Hard|
| 1094 | [Shortest Path in a Grid with Obstacles Elimination](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/) | BFS, Graph | Time: O(n^2), Space: O(n^2)| Hard|
|675 | [Cut Off Trees for Golf Event](https://leetcode.com/problems/cut-off-trees-for-golf-event/) | BFS, Graph, Priority Queue | Time: O(n log n), Space: O(n)| Hard|
| 1306 | [Jump Game III](https://leetcode.com/problems/jump-game-iii/) | BFS, Graph, Queue| O(n) Time, O(n) Space| Medium|
| 1284 | [Minimum Number of Flips to Convert Binary Matrix to Zero Matrix](https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/) | BFS, Matrix| O(n * m) Time, O(n * m) Space| Hard|
|778 | [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) | BFS, Priority Queue| Time: O(n log n), Space: O(n)| Hard|
|994 | [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | BFS, Queue | Time: O(n^2), Space: O(n)| Medium|
| 1197 | [Minimum Knight Moves](https://leetcode.com/problems/minimum-knight-moves/) | BFS, Queue | O(n) Time, O(n) Space| Medium|
| 1244 | [Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | BFS, Queue | O(n * m) Time, O(n * m) Space| Medium|
| 1263 | [Minimum Moves to Move a Robot to the Origin](https://leetcode.com/problems/minimum-moves-to-move-a-robot-to-the-origin/) | BFS, Queue | O(n) Time, O(n) Space| Medium|
| 1210 | [Minimum Moves to Reach Target with Rotations](https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/) | BFS, Queue | O(n) Time, O(n) Space| Hard|
| 1| 293 | [📓 Flip Game](0293.ipynb) | <span title="One sweep through the data, typically updating a counter or maximum in place.">Single Scan</span> | Time: O(n²), Space: O(n) per result | Easy |
| 1345 | [Jump Game IV](https://leetcode.com/problems/jump-game-iv/) | BFS, Queue | O(n) Time, O(n) Space| Hard|
|505 | [The Maze II](https://leetcode.com/problems/the-maze-ii/) | Breadth-First Search | O(MN) Time, O(MN) Space| Medium|

## Binary Indexed Tree
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
| 315 | [📓 Count of Smaller Numbers After Self](0315.ipynb) | <span title="Fenwick tree: update index i with i += i & -i; prefix-query with i -= i & -i. O(log n) per op.">Binary Indexed Tree</span> | Time: $O(n \log n)$, Space: $O(n)$ | Hard |

## Binary Search
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
| 35 | [📓 Search Insert Position](0035.ipynb) | <span title="Halve the search space each step by comparing the midpoint to a monotone predicate.">Binary Search</span> | Time: $O(\log n)$, Space: $O(1)$ | Easy |
| 278 | [📓 First Bad Version](0278.ipynb) | <span title="Halve the search space each step by comparing the midpoint to a monotone predicate.">Binary Search</span> | Time: $O(\log n)$, Space: $O(1)$ | Easy |
| 367 | [📓 Valid Perfect Square](0367.ipynb) | <span title="Halve the search space each step by comparing the midpoint to a monotone predicate.">Binary Search</span> | Time: $O(\log n)$, Space: $O(1)$ | Easy |
| 374 | [📓 Guess Number Higher or Lower](0374.ipynb) | <span title="Halve the search space each step by comparing the midpoint to a monotone predicate.">Binary Search</span> | Time: $O(\log n)$, Space: $O(1)$ | Easy |
| 441 | [📓 Arranging Coins](0441.ipynb) | <span title="Halve the search space each step by comparing the midpoint to a monotone predicate.">Binary Search</span> | Time: $O(\log n)$, Space: $O(1)$ | Easy |
| 475 | [📓 Heaters](0475.ipynb) | <span title="Halve the search space each step by comparing the midpoint to a monotone predicate.">Binary Search</span> | Time: $O(n \log n)$, Space: $O(1)$ | Easy |
| 704 | [📓 Binary Search](0704.ipynb) | <span title="Halve the search space each step by comparing the midpoint to a monotone predicate.">Binary Search</span> | Time: $O(\log n)$, Space: $O(1)$ | Easy |
| 744 | [📓 Find Smallest Letter Greater Than Target](0744.ipynb) | <span title="Halve the search space each step by comparing the midpoint to a monotone predicate.">Binary Search</span> | Time: $O(\log n)$, Space: $O(1)$ | Easy |
| 33 | [📓 Search in Rotated Sorted Array](0033.ipynb) | <span title="One half is always sorted; check if target falls in the sorted half and narrow accordingly.">Binary Search with Pivot Detection</span> | Time: O(log n), Space: O(1) | Medium |
| 34 | [📓 Find First and Last Position of Element in Sorted Array](0034.ipynb) | <span title="Two separate binary searches: one for the leftmost index, one for the rightmost index.">Two Binary Searches</span> | Time: O(log n), Space: O(1) | Medium |
| 74 | [📓 Search a 2D Matrix](0074.ipynb) | <span title="Treat the 2D matrix as a 1D array; map flat index → (row, col) with mid/cols and mid%cols.">Binary Search on Flattened Index</span> | Time: O(log(m * n)), Space: O(1) | Medium |
| 81 | [📓 Search in Rotated Sorted Array II](0081.ipynb) | <span title="When arr[lo] == arr[mid], can't determine sorted half — increment lo to skip the duplicate.">Binary Search with Duplicate Handling</span> | Time: O(n) worst, O(log n) avg, Space: O(1) | Medium |
| 153 | [📓 Find Minimum in Rotated Sorted Array](0153.ipynb) | <span title="Compare arr[mid] to arr[hi] to determine which half contains the minimum.">Binary Search on Rotation Pivot</span> | Time: O(log n), Space: O(1) | Medium |
| 154 | [📓 Find Minimum in Rotated Sorted Array II](0154.ipynb) | <span title="When arr[mid] == arr[hi], can't determine which half has the min — decrement hi safely.">Binary Search with Duplicate Shrinking</span> | Time: O(n) worst, O(log n) avg, Space: O(1) | Medium |
| 162 | [📓 Find Peak Element](0162.ipynb) | <span title="Move toward the rising slope: if arr[mid] < arr[mid+1] the peak is to the right.">Binary Search on Gradient</span> | Time: O(log n), Space: O(1) | Medium |
| 240 | [📓 Search a 2D Matrix II](0240.ipynb) | <span title="Start at top-right corner of a sorted 2D matrix; eliminate a row or column each step.">Staircase Search</span> | Time: O(m + n), Space: O(1) | Medium |
| 275 | [📓 H-Index II](0275.ipynb) | <span title="Binary search directly on the answer value; use a feasibility check to halve the range.">Binary Search on Answer</span> | Time: O(log n), Space: O(1) | Medium |
| 436 | [📓 Find Right Interval](0436.ipynb) | <span title="Sort interval start points; for each query end, binary search for the smallest start ≥ end.">Binary Search on Sorted Starts</span> | Time: O(n log n), Space: O(n) | Medium |
| 540 | [📓 Single Element in a Sorted Array](0540.ipynb) | <span title="Before the lone element, each pair starts at an even index; use that parity invariant to binary search.">Binary Search on Parity</span> | Time: O(log n), Space: O(1) | Medium |
| 702 | [📓 Search in a Sorted Array of Unknown Size](0702.ipynb) | <span title="Double the window (1,2,4,8…) until the target is within range, then binary search inside.">Exponential Search + Binary Search</span> | Time: O(log n), Space: O(1) | Medium |
| 875 | [📓 Koko Eating Bananas](0875.ipynb) | <span title="Binary search on Koko's eating rate; count hours needed at each rate to find the minimum.">Binary Search on Eating Speed</span> | Time: O(n log m), Space: O(1) | Medium |
| 1060 | [📓 Missing Element in Sorted Array](1060.ipynb) | <span title="Count how many numbers are missing up to index i; binary search for the boundary.">Binary Search on Missing Count</span> | Time: O(log n), Space: O(1) | Medium |
| 1095 | [📓 Find in Mountain Array](1095.ipynb) | <span title="Find mountain peak, then binary search the ascending half, then the descending half.">Three Binary Searches</span> | Time: O(log n), Space: O(1) | Medium |
| 1264 | [Page Completion](https://leetcode.com/problems/page-completion/) | Binary Search| O(log n) Time, O(1) Space| Medium|
| 1482 | [📓 Minimum Number of Days to Make m Bouquets](1482.ipynb) | <span title="Halve the search space each step by comparing the midpoint to a monotone predicate.">Binary Search</span> | O(n log n) Time, O(1) Space| Medium|
|668 | [📓 Kth Smallest Number in Multiplication Table](0668.ipynb) | <span title="Halve the search space each step by comparing the midpoint to a monotone predicate.">Binary Search</span> | Time: O(n log m), Space: O(1)| Hard|
|774 | [📓 Minimize Max Distance to Gas Station](0774.ipynb) | <span title="Halve the search space each step by comparing the midpoint to a monotone predicate.">Binary Search</span> | Time: O(n log m), Space: O(1)| Hard|
|793 | [📓 Preimage Size of Factorial Zeroes Function](0793.ipynb) | <span title="Halve the search space each step by comparing the midpoint to a monotone predicate.">Binary Search</span> | Time: O(log n), Space: O(1)| Hard|
| 1419 | [📓 Minimum Number of Frogs Croaking](1419.ipynb) | <span title="Halve the search space each step by comparing the midpoint to a monotone predicate.">Binary Search</span> | O(n log n) Time, O(1) Space| Hard|
| 852 | [📓 Peak Index in a Mountain Array](0852.ipynb) | <span title="Halve the search space each step by comparing the midpoint to a monotone predicate.">Binary Search</span> | Time: $O(\log n)$, Space: $O(1)$ | Medium |
| 1233 | [📓 Remove Sub-Folders from the Filesystem](1233.ipynb) | <span title="Sort the array then binary search; or sort + two-pointer sweep after the search.">Binary Search, Array</span> | O(n log n) Time, O(n) Space| Medium|
| 1285 | [Find the Right Interval](https://leetcode.com/problems/find-the-right-interval/) | Binary Search, Array | O(n log n) Time, O(n) Space| Medium|
| 1300 | [📓 Sum of Mutated Array Closest to Target](1300.ipynb) | <span title="Sort the array then binary search; or sort + two-pointer sweep after the search.">Binary Search, Array</span> | O(n log n) Time, O(1) Space| Medium|
| 1459 | [Find the Start and End of the Range](https://leetcode.com/problems/find-the-start-and-end-of-the-range/) | Binary Search, Array | O(log n) Time, O(1) Space| Medium|
| 1231 | [📓 Divide Chocolate](1231.ipynb) | <span title="Binary search for the insert position within a DP transition (e.g., patience sorting for LIS).">Binary Search, Dynamic Programming</span> | O(n log n) Time, O(1) Space| Medium|
|410 | [📓 Split Array Largest Sum](0410.ipynb) | <span title="Binary search for the insert position within a DP transition (e.g., patience sorting for LIS).">Binary Search, Dynamic Programming</span> | Time: O(n log m), Space: O(n)| Hard|
| 1011 | [📓 Capacity To Ship Packages Within D Days](1011.ipynb) | <span title="Greedily simulate a feasibility check (e.g., days or capacity) inside a binary-search loop.">Binary Search, Greedy</span> | Time: O(n log m), Space: O(1)| Medium|
| 1211 | [Divide Chocolate](https://leetcode.com/problems/divide-chocolate/) | Binary Search, Math| O(n log n) Time, O(1) Space| Medium|
| 1283 | [📓 Find the Smallest Divisor Given a Threshold](1283.ipynb) | <span title="Combine binary search with a mathematical formula to evaluate the feasibility predicate.">Binary Search, Math</span> | O(n log m) Time, O(1) Space| Medium|
|327 | [📓 Count of Range Sum](0327.ipynb) | <span title="Merge sort to count inversions or range sums; binary search for the split boundary.">Binary Search, Merge Sort</span> | Time: O(n log n), Space: O(n)| Hard|
| 1498 | [📓 Number of Subsequences That Satisfy the Given Sum Condition](1498.ipynb) | <span title="Sort first, then binary search for target positions or boundaries.">Binary Search, Sorting</span> | O(n log n) Time, O(n) Space| Medium|
| 1062 | [📓 Longest Repeating Substring](1062.ipynb) | <span title="Binary search on length; use rolling hash or suffix array to detect duplicate substrings.">Binary Search, String</span> | Time: O(n log n), Space: O(n)| Hard|
|719 | [📓 Find K-th Smallest Pair Distance](0719.ipynb) | <span title="Sort first; binary search for the right boundary; sliding window counts pairs in O(n).">Binary Search, Two Pointer</span> | Time: O(n log n), Space: O(1)| Hard|

## Binary Search Tree
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
| 700 | [📓 Search in a Binary Search Tree](0700.ipynb) | <span title="Iterative BST traversal using the ordering property: go left if val < node, else right.">Iterative (BST property)</span> | Time: $O(h)$, Space: $O(1)$ | Easy |
|701 | [📓 Insert into a Binary Search Tree](0701.ipynb) | <span title="Exploit BST ordering: go left when target < node, right when target > node.">Binary Search Tree</span> | Time: O(h), Space: O(1)| Easy|
|729 | [📓 My Calendar I](0729.ipynb) | <span title="Exploit BST ordering: go left when target < node, right when target > node.">Binary Search Tree</span> | Time: O(log n), Space: O(n)| Medium|
|731 | [📓 My Calendar II](0731.ipynb) | <span title="Exploit BST ordering: go left when target < node, right when target > node.">Binary Search Tree</span> | Time: O(log n), Space: O(n)| Medium|
|538 | [📓 Convert BST to Greater Tree](0538.ipynb) | <span title="Use BST ordering property to search, insert, or traverse in O(h) time.">Binary Search Tree (BST)</span> | Time: O(n), Space: O(h)| Easy|
|510 | [📓 Inorder Successor in BST II](0510.ipynb) | <span title="Use BST ordering property to search, insert, or traverse in O(h) time.">Binary Search Tree (BST)</span> | Time: O(h), Space: O(1)| Medium|
|519 | [📓 Random Flip Matrix](0519.ipynb) | <span title="Use BST ordering property to search, insert, or traverse in O(h) time.">Binary Search Tree (BST)</span> | Time: O(log n), Space: O(n)| Medium|
|528 | [📓 Random Pick with Weight](0528.ipynb) | <span title="Use BST ordering property to search, insert, or traverse in O(h) time.">Binary Search Tree (BST)</span> | Time: O(log n), Space: O(n)| Medium|
|530 | [📓 Minimum Absolute Difference in BST](0530.ipynb) | <span title="Use BST ordering property to search, insert, or traverse in O(h) time.">Binary Search Tree (BST)</span> | Time: O(n), Space: O(h)| Medium|

## Binary Tree
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|543 | [📓 Diameter of Binary Tree](0543.ipynb) | <span title="Recursive DFS over a binary tree; return values up the call stack to accumulate the answer.">Binary Tree</span> | Time: O(n), Space: O(h)| Easy|
|617 | [📓 Merge Two Binary Trees](0617.ipynb) | <span title="Recursive DFS over a binary tree; return values up the call stack to accumulate the answer.">Binary Tree</span> | Time: O(n), Space: O(h)| Easy|
|623 | [📓 Add One Row to Tree](0623.ipynb) | <span title="Recursive DFS over a binary tree; return values up the call stack to accumulate the answer.">Binary Tree</span> | Time: O(n), Space: O(h)| Medium|
|637 | [📓 Average of Levels in Binary Tree](0637.ipynb) | <span title="Level-order traversal with a queue; process all nodes at each depth before moving deeper.">Binary Tree (BFS)</span> | Time: O(n), Space: O(n)| Easy|
|563 | [📓 Binary Tree Tilt](0563.ipynb) | <span title="Pre/in/post-order recursive traversal; propagate depth, sums, or lengths up from leaves.">Binary Tree (DFS)</span> | Time: O(n), Space: O(h)| Easy|
| 549 | [📓 Binary Tree Longest Consecutive Sequence II](0549.ipynb) | <span title="Visit left, right, then root; aggregate subtree results on the way back up.">DFS Post-order</span> | Time: O(n), Space: O(h) | Medium |
| 545 | [📓 Boundary of Binary Tree](0545.ipynb) | <span title="Three separate DFS passes: left boundary top-down, all leaves, right boundary bottom-up.">DFS Three-pass Boundary</span> | Time: O(n), Space: O(h) | Medium |
| 513 | [📓 Find Bottom Left Tree Value](0513.ipynb) | <span title="Queue-based BFS; collect all nodes at each depth before advancing to the next level.">BFS Level Order</span> | Time: O(n), Space: O(n) | Medium |
| 515 | [📓 Find Largest Value in Each Tree Row](0515.ipynb) | <span title="Queue-based BFS; collect all nodes at each depth before advancing to the next level.">BFS Level Order</span> | Time: O(n), Space: O(n) | Medium |
| 536 | [📓 Construct Binary Tree from String](0536.ipynb) | <span title="Recursively parse a string into a tree by tracking an index through the input character by character.">Recursive Parsing</span> | Time: O(n), Space: O(n) | Medium |
| 1161 | [📓 Maximum Level Sum of a Binary Tree](1161.ipynb) | <span title="Queue-based BFS; collect all nodes at each depth before advancing to the next level.">BFS Level Order</span> | Time: O(n), Space: O(n) | Medium |
| 606 | [📓 Construct String from Binary Tree](0606.ipynb) | <span title="Visit root first, then recurse into children, adding parentheses around non-empty subtrees.">DFS Pre-order with Parentheses</span> | Time: O(n), Space: O(n) | Easy |

## Bit Manipulation
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
| 136 | [📓 Single Number](0136.ipynb) | <span title="XOR all elements; duplicate values cancel out (a ^ a = 0), leaving the unique value.">XOR</span> | Time: O(n), Space: O(1) | Easy |
| 190 | [📓 Reverse Bits](0190.ipynb) | <span title="Shift source bits one at a time into a result register, reversing their order.">Bit-by-bit Reversal</span> | Time: O(1), Space: O(1) | Easy |
| 191 | [📓 Number of 1 Bits](0191.ipynb) | <span title="Clear the lowest set bit with n &= (n-1) and count iterations to find the bit count in O(k).">Brian Kernighan's Algorithm</span> | Time: O(k), Space: O(1) | Easy |
| 371 | [📓 Sum of Two Integers](0371.ipynb) | <span title="Simulate addition with XOR for the sum bits and AND+shift for the carry; repeat until carry is zero.">Bit Manipulation (carry simulation)</span> | Time: O(1), Space: O(1) | Easy |
| 401 | [📓 Binary Watch](0401.ipynb) | <span title="Enumerate all 720 valid watch times; filter by total set bits equaling the given number.">Bit Manipulation (enumerate all times)</span> | Time: O(1), Space: O(1) | Easy |
| 461 | [📓 Hamming Distance](0461.ipynb) | <span title="XOR two numbers to isolate differing bits, then count set bits (popcount) for Hamming distance.">XOR + Popcount</span> | Time: O(1), Space: O(1) | Easy |
| 476 | [📓 Number Complement](0476.ipynb) | <span title="Build a mask of all 1s up to the highest set bit, then XOR with it to flip those bits.">Bit Mask Flip</span> | Time: O(log n), Space: O(1) | Easy |
| 762 | [📓 Prime Number of Set Bits in Binary Representation](0762.ipynb) | <span title="Count set bits (popcount); check if the count is prime using a precomputed bitmask of primes ≤ 20.">Bit Manipulation + Prime Mask</span> | Time: O(n), Space: O(1) | Easy |
| 1404 | [📓 Number of Steps to Reduce a Number in Binary Representation to One](1404.ipynb) | <span title="Scan bits right-to-left with a carry variable; odd bits cost 2 steps, even bits cost 1.">Linear Scan with Carry</span> | O(log n) Time, O(1) Space| Easy|
| 89 | [📓 Gray Code](0089.ipynb) | <span title="Generate each Gray code as i XOR (i >> 1) for all i in [0, 2^n) — O(1) per element.">Binary-Reflected XOR Formula</span> | Time: O(2^n), Space: O(2^n)| Medium|
|137 | [📓 Single Number II](0137.ipynb) | <span title="For each bit position, sum counts across all numbers; mod 3 isolates the unique number's bits.">Bit-Count Mod 3</span> | Time: O(n), Space: O(1)| Medium|
|201 | [📓 Bitwise AND of Numbers Range](0201.ipynb) | <span title="Right-shift both endpoints until equal; the common prefix, shifted back, is the answer.">Common Prefix (Right Shift)</span> | Time: O(1), Space: O(1)| Medium|
|260 | [📓 Single Number III](0260.ipynb) | <span title="XOR all values to get x^y; split by the lowest differing bit into two groups; XOR each group.">XOR Partition by Lowest Differing Bit</span> | Time: O(n), Space: O(1)| Medium|
|318 | [📓 Maximum Product of Word Lengths](0318.ipynb) | <span title="Encode each word's letters as a 26-bit mask; zero AND means disjoint character sets.">Bitmask per Word</span> | Time: O(n^2), Space: O(n)| Medium|
|393 | [📓 UTF-8 Validation](0393.ipynb) | <span title="Use bitmasks (0x80, 0xC0, 0xE0, 0xF0, 0xF8) to classify each byte; track expected continuations.">Bit-Masking In-Place</span> | Time: O(n), Space: O(1)| Medium|
|477 | [📓 Total Hamming Distance](0477.ipynb) | <span title="For each bit, count 1-bits (k); contribution is k*(n-k) since 1s pair with 0s across all numbers.">Per-Bit Population Count</span> | Time: O(n), Space: O(1)| Medium|
| 1108 | [📓 IP Address to CIDR](1108.ipynb) | <span title="Greedily take the largest power-of-two-aligned CIDR block fitting the current IP and count.">Greedy Largest Aligned Block</span> | Time: O(1), Space: O(1)| Medium|
| 1238 | [📓 Circular Permutation in Binary Representation](1238.ipynb) | <span title="XOR each Gray code i^(i>>1) with the start offset to rebase the circular permutation.">Gray Code with Start XOR</span> | O(n) Time, O(1) Space| Medium|
| 1442 | [📓 Count Triplets That Can Form Two Arrays of Equal XOR](1442.ipynb) | <span title="Use prefix XOR; when prefix[i]==prefix[k+1] the subarray XOR is zero, giving k-i valid triplets.">Prefix XOR</span> | O(n^2) Time, O(n) Space| Hard|
| 1274 | [Prime Number of Set Bits in Binary Representation](https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/) | Bit Manipulation, Math | O(n) Time, O(1) Space| Easy|
| 1453 | [Find the Longest Substring Containing Vowels in Even Counts](https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/) | Bit Manipulation, Prefix Sum | O(n) Time, O(1) Space| Medium|

## Bit Masking
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
| 1125 | [📓 Smallest Sufficient Team](1125.ipynb) | <span title="Bitmask each skill set; dp[mask] tracks the smallest team covering exactly the skills in mask.">Bitmask DP over Skill Sets</span> | Time: O(n), Space: O(n)| Hard|

## Bitmask
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
| 1371 | [📓 Find the Longest Substring Containing Vowels in Even Counts](1371.ipynb) | <span title="Track vowel parity as a 5-bit XOR state; when state recurs, the gap has all even vowel counts.">Bitmask Prefix XOR + HashMap</span> | O(n) Time, O(1) Space| Medium|

## Boyer-Moore Voting Algorithm
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|229 | [Majority Element II](https://leetcode.com/problems/majority-element-ii/) | Boyer-Moore Voting Algorithm | Time: O(n), Space: O(1)| Medium|

## Bucket Sort
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|220 | [Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/) | Bucket Sort| Time: O(n), Space: O(n)| Medium|

## Deque
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|239 | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Deque| Time: O(n), Space: O(k)| Hard|
|862 | [Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/) | Deque, Sliding Window| Time: O(n), Space: O(n)| Hard|

## DFS
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|386 | [Lexicographical Numbers](https://leetcode.com/problems/lexicographical-numbers/) | DFS| Time: O(n), Space: O(1)| Medium|
|417 | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | DFS| Time: O(m * n), Space: O(m * n)| Medium|
|695 | [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | DFS| Time: O(n), Space: O(n)| Medium|
|936 | [Stamping the Sequence](https://leetcode.com/problems/stamping-the-sequence/) | DFS| Time: O(n^2), Space: O(n)| Hard|
|959 | [Regions Cut By Slashes](https://leetcode.com/problems/regions-cut-by-slashes/) | DFS| Time: O(n^2), Space: O(n^2)| Hard|
|733 | [Flood Fill](https://leetcode.com/problems/flood-fill/) | DFS, BFS | Time: O(n), Space: O(n)| Easy|
|130 | [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) | DFS, BFS | Time: O(m * n), Space: O(m * n)| Medium|
|200 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | DFS, BFS | Time: O(m * n), Space: O(m * n)| Medium|
|797 | [All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/) | DFS, Backtracking| Time: O(n * 2^n), Space: O(n)| Medium|
| 1067 | [Path with Maximum Gold](https://leetcode.com/problems/path-with-maximum-gold/) | DFS, Backtracking| Time: O(n^2), Space: O(n^2)| Medium|
|465 | [Optimal Account Balancing](https://leetcode.com/problems/optimal-account-balancing/) | DFS, Backtracking| Time: O(2^n), Space: O(n)| Hard|
| 1020 | [Number of Enclaves](https://leetcode.com/problems/number-of-enclaves/) | DFS, Graph | Time: O(n^2), Space: O(n)| Medium|
| 1270 | [All Paths from Source Lead to Destination](https://leetcode.com/problems/all-paths-from-source-lead-to-destination/) | DFS, Graph | O(n * m) Time, O(n * m) Space| Medium|
| 1015 | [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) | DFS, Graph, Binary Search| Time: O(n log n), Space: O(n)| Hard|
|694 | [Number of Distinct Islands](https://leetcode.com/problems/number-of-distinct-islands/) | DFS, Hash Set| Time: O(n), Space: O(n)| Medium|
| 1219 | [Path with Maximum Gold](https://leetcode.com/problems/path-with-maximum-gold/) | DFS, Matrix| O(n * m) Time, O(n * m) Space| Medium|
| 1254 | [Number of Closed Islands](https://leetcode.com/problems/number-of-closed-islands/) | DFS, Matrix| O(n * m) Time, O(n * m) Space| Medium|
| 1114 | [Print in Order](https://leetcode.com/problems/print-in-order/) | DFS, Multi-threading | Time: O(1), Space: O(1)| Easy|
| 1115 | [Print Foo Bar Alternately](https://leetcode.com/problems/print-foo-bar-alternately/) | DFS, Multi-threading | Time: O(1), Space: O(1)| Medium|
|339 | [Nested List Weight Sum](https://leetcode.com/problems/nested-list-weight-sum/) | DFS, Recursion | Time: O(n), Space: O(h)| Easy|
|364 | [Nested List Weight Sum II](https://leetcode.com/problems/nested-list-weight-sum-ii/) | DFS, Recursion | Time: O(n), Space: O(h)| Medium|
| 1066 | [Building a Castle](https://leetcode.com/problems/building-a-castle/) | DFS, Simulation| Time: O(n), Space: O(n)| Easy|
|329 | [Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | DFS, Topological Sort| Time: O(m * n), Space: O(m * n)| Hard|
| 1144 | [Binary Tree Coloring Game](https://leetcode.com/problems/binary-tree-coloring-game/) | DFS, Tree| Time: O(n), Space: O(n)| Medium|
| 1145 | [Binary Tree Coloring Game II](https://leetcode.com/problems/binary-tree-coloring-game-ii/) | DFS, Tree| Time: O(n), Space: O(n)| Hard|
|711 | [Number of Distinct Islands II](https://leetcode.com/problems/number-of-distinct-islands-ii/) | DFS, Union-Find| Time: O(n), Space: O(n)| Hard|
|547 | [Friend Circles](https://leetcode.com/problems/friend-circles/) | Depth-First Search (DFS), Union-Find | Time: O(n^2), Space: O(n)| Medium|

## Difference Array
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|370 | [Range Addition](https://leetcode.com/problems/range-addition/) | Difference Array | Time: O(n), Space: O(n)| Medium|

## Dijkstra
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|787 | [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | Dijkstra, Graph| Time: O(E log V), Space: O(V)| Medium|

## Divide and Conquer
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|372 | [Super Pow](https://leetcode.com/problems/super-pow/) | Divide and Conquer | Time: O(log k), Space: O(1)| Medium|
|395 | [Longest Substring with At Least K Repeating Characters](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/) | Divide and Conquer | Time: O(n log n), Space: O(n)| Medium|
|932 | [Beautiful Array](https://leetcode.com/problems/beautiful-array/) | Divide and Conquer | Time: O(n log n), Space: O(n)| Medium|
|427 | [Construct Quad Tree](https://leetcode.com/problems/construct-quad-tree/) | Divide and Conquer, Recursion| Time: O(n), Space: O(n)| Medium|

## Doubly Linked List
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|432 | [All O`one Data Structure](https://leetcode.com/problems/all-oone-data-structure/)| Doubly Linked List, Hash Map | Time: O(1), Space: O(n)| Hard|

## Dynamic Programming
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|746 | [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | DP | Time: O(n), Space: O(n)| Easy|
| 1137 | [Nth Tribonacci Number](https://leetcode.com/problems/nth-tribonacci-number/) | DP | Time: O(n), Space: O(1)| Easy|
| 1043 | [Partition Array for Maximum Sum](https://leetcode.com/problems/partition-array-for-maximum-sum/) | DP | Time: O(n^2), Space: O(n)| Medium|
| 1080 | [Largest Sum of Averages](https://leetcode.com/problems/largest-sum-of-averages/) | DP | Time: O(n^2), Space: O(n^2)| Medium|
| 1135 | [Cutting a Rod](https://leetcode.com/problems/cutting-a-rod/) | DP | Time: O(n^2), Space: O(n)| Medium|
| 1140 | [Stone Game II](https://leetcode.com/problems/stone-game-ii/) | DP | Time: O(n^2), Space: O(n^2)| Medium|
| 1143 | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | DP | Time: O(m * n), Space: O(m * n)| Medium|
|689 | [Maximum Sum of 3 Non-Overlapping Subarrays](https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/) | DP | Time: O(n), Space: O(n)| Hard|
|730 | [Count Different Palindromes](https://leetcode.com/problems/count-different-palindromes/) | DP | Time: O(n^2), Space: O(n^2)| Hard|
|756 | [Pyramid Transition Matrix](https://leetcode.com/problems/pyramid-transition-matrix/) | DP | Time: O(n^3), Space: O(n^2)| Hard|
| 1000 | [Merge Stones](https://leetcode.com/problems/merge-stones/) | DP | Time: O(n^2), Space: O(n^2)| Hard|
|764 | [Largest Plus Sign](https://leetcode.com/problems/largest-plus-sign/) | DP, 2D Array | Time: O(n^2), Space: O(n^2)| Medium|
|983 | [Minimum Cost For Tickets](https://leetcode.com/problems/minimum-cost-for-tickets/) | DP, Array| Time: O(n), Space: O(n)| Medium|
| 1279 | [Frog Jump II](https://leetcode.com/problems/frog-jump-ii/) | DP, Array| O(n) Time, O(n) Space| Medium|
| 1458 | [Max Dot Product of Two Subsequences](https://leetcode.com/problems/max-dot-product-of-two-subsequences/) | DP, Array| O(n^2) Time, O(n^2) Space| Hard|
|903 | [Valid Permutations for DI Sequence](https://leetcode.com/problems/valid-permutations-for-di-sequence/) | DP, Backtracking | Time: O(n^2), Space: O(n)| Hard|
|967 | [Numbers With Same Consecutive Differences](https://leetcode.com/problems/numbers-with-same-consecutive-differences/) | DP, Backtracking | Time: O(2^n), Space: O(1)| Hard|
| 1029 | [Find Minimum Number Of Nodes That Can Produce All Distinct Subsets](https://leetcode.com/problems/find-minimum-number-of-nodes-that-can-produce-all-distinct-subsets/) | DP, Backtracking | Time: O(2^n), Space: O(1)| Hard|
| 1030 | [Find Minimum Number of Pairs That Can Produce All Distinct Subsets](https://leetcode.com/problems/find-minimum-number-of-pairs-that-can-produce-all-distinct-subsets/) | DP, Backtracking | Time: O(2^n), Space: O(1)| Hard|
| 1031 | [Find Minimum Number Of Nodes That Can Produce All Distinct Subsets](https://leetcode.com/problems/find-minimum-number-of-nodes-that-can-produce-all-distinct-subsets/) | DP, Backtracking | Time: O(2^n), Space: O(1)| Hard|
| 1032 | [Find Minimum Number of Pairs That Can Produce All Distinct Subsets](https://leetcode.com/problems/find-minimum-number-of-pairs-that-can-produce-all-distinct-subsets/) | DP, Backtracking | Time: O(2^n), Space: O(1)| Hard|
| 1478 | [Max Sum of Rectangle No Larger Than K](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/) | DP, Binary Search| O(n^2 log n) Time, O(n) Space| Hard|
|956 | [Tallest Billboard](https://leetcode.com/problems/tallest-billboard/) | DP, Bitmask| Time: O(n * sum), Space: O(sum)| Hard|
| 1016 | [Partition Array Into Two Arrays To Minimize Sum Difference](https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/) | DP, Bitmask| Time: O(n * sum), Space: O(sum)| Hard|
| 1349 | [Maximum Students Taking Exam](https://leetcode.com/problems/maximum-students-taking-exam/) | DP, Bitmasking | O(n^2) Time, O(n) Space| Hard|
|688 | [Knight Probability in Chessboard](https://leetcode.com/problems/knight-probability-in-chessboard/) | DP, Chessboard | Time: O(n^2 * k), Space: O(n^2)| Medium|
| 1411 | [Number of Ways to Paint N × 3 Grid](https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/) | DP, Combinatorics| O(n) Time, O(1) Space| Hard|
|963 | [Minimum Area Rectangle II](https://leetcode.com/problems/minimum-area-rectangle-ii/) | DP, Geometry, Sort | Time: O(n log n), Space: O(n)| Hard|
| 1039 | [Minimum Score Triangulation of Polygon](https://leetcode.com/problems/minimum-score-triangulation-of-polygon/) | DP, Graph| Time: O(n^3), Space: O(n^2)| Hard|
| 1077 | [Project Management](https://leetcode.com/problems/project-management/) | DP, Graph| Time: O(n), Space: O(n)| Hard|
| 1024 | [Video Stitching](https://leetcode.com/problems/video-stitching/) | DP, Greedy | Time: O(n), Space: O(n)| Medium|
| 1105 | [Filling Bookcase Shelves](https://leetcode.com/problems/filling-bookcase-shelves/) | DP, Greedy | Time: O(n^2), Space: O(n^2)| Medium|
| 1449 | [Form Largest Integer With Digits That Add up to Target](https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/) | DP, Greedy | O(target^2) Time, O(target) Space| Hard|
|871 | [Minimum Number of Refueling Stops](https://leetcode.com/problems/minimum-number-of-refueling-stops/) | DP, Greedy, Heap | Time: O(n^2), Space: O(n)| Hard|
|873 | [Length of Longest Fibonacci Subsequence](https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/) | DP, Hash Map | Time: O(n^2), Space: O(n)| Medium|
| 1048 | [Longest String Chain](https://leetcode.com/problems/longest-string-chain/) | DP, Hash Map | Time: O(n^2), Space: O(n)| Medium|
|691 | [Sticker to Spell Word](https://leetcode.com/problems/sticker-to-spell-word/) | DP, Hash Map | Time: O(n * m * k), Space: O(n)| Hard|
| 1107 | [Gift Card Purchase](https://leetcode.com/problems/gift-card-purchase/) | DP, Knapsack | Time: O(n^2), Space: O(n)| Medium|
| 1049 | [Last Stone Weight II](https://leetcode.com/problems/last-stone-weight-ii/) | DP, Knapsack Problem | Time: O(n * S), Space: O(S)| Medium|
| 1035 | [Uncrossed Lines](https://leetcode.com/problems/uncrossed-lines/) | DP, LCS| Time: O(m * n), Space: O(m * n)| Medium|
| 1269 | [Number of Ways to Stay in the Same Place After Some Moves](https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-moves/) | DP, Math | O(n) Time, O(n) Space| Medium|
|931 | [Minimum Falling Path Sum](https://leetcode.com/problems/minimum-falling-path-sum/) | DP, Matrix | Time: O(n^2), Space: O(n^2)| Medium|
| 1127 | [Mosaic Style Display](https://leetcode.com/problems/mosaic-style-display/) | DP, Matrix | Time: O(n^2), Space: O(n^2)| Medium|
| 1139 | [Largest 1-Bordered Square](https://leetcode.com/problems/largest-1-bordered-square/) | DP, Matrix | Time: O(n^2), Space: O(n^2)| Medium|
|673 | [Number of Longest Increasing Subsequence](https://leetcode.com/problems/number-of-longest-increasing-subsequence/) | DP, Segment Tree | Time: O(n^2), Space: O(n)| Medium|
|930 | [Binary Subarrays With Sum](https://leetcode.com/problems/binary-subarrays-with-sum/) | DP, Sliding Window | Time: O(n), Space: O(n)| Medium|
|975 | [Odd Even Jump](https://leetcode.com/problems/odd-even-jump/) | DP, Stack| Time: O(n log n), Space: O(n)| Hard|
| 1064 | [Number of Ways to Split a String](https://leetcode.com/problems/number-of-ways-to-split-a-string/) | DP, String | Time: O(n), Space: O(n)| Medium|
| 1068 | [Largest Palindromic Substring](https://leetcode.com/problems/largest-palindromic-substring/) | DP, String | Time: O(n^2), Space: O(n^2)| Medium|
|940 | [Distinct Subsequences II](https://leetcode.com/problems/distinct-subsequences-ii/) | DP, String | Time: O(n^2), Space: O(n)| Hard|
| 1055 | [Shortest Way to Form String](https://leetcode.com/problems/shortest-way-to-form-string/) | DP, String | Time: O(n * m), Space: O(n * m)| Hard|
| 1086 | [Largest Palindromic Substring](https://leetcode.com/problems/largest-palindromic-substring/) | DP, String | Time: O(n^2), Space: O(n^2)| Hard|
| 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Dynamic Programming| Time: O(n), Space: O(1)| Easy|
| 70 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Dynamic Programming| Time: O(n), Space: O(1)| Easy|
|5 | [📓 Longest Palindromic Substring](0005.ipynb) | <span title="Break the problem into overlapping subproblems; cache results to avoid recomputation.">Dynamic Programming</span> | Time: O(n^2), Space: O(n^2)| Medium|
| 62 | [Unique Paths](https://leetcode.com/problems/unique-paths/) | Dynamic Programming| Time: O(m * n), Space: O(m * n)| Medium|
| 63 | [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/) | Dynamic Programming| Time: O(m * n), Space: O(m * n)| Medium|
| 64 | [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) | Dynamic Programming| Time: O(m * n), Space: O(m * n)| Medium|
| 91 | [Decode Ways](https://leetcode.com/problems/decode-ways/) | Dynamic Programming| Time: O(n), Space: O(n)| Medium|
| 96 | [Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/) | Dynamic Programming| Time: O(n^2), Space: O(n)| Medium|
|120 | [Triangle](https://leetcode.com/problems/triangle/) | Dynamic Programming| Time: O(n^2), Space: O(n^2)| Medium|
|152 | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | Dynamic Programming| Time: O(n), Space: O(1)| Medium|
|198 | [House Robber](https://leetcode.com/problems/house-robber/) | Dynamic Programming| Time: O(n), Space: O(1)| Medium|
|213 | [House Robber II](https://leetcode.com/problems/house-robber-ii/) | Dynamic Programming| Time: O(n), Space: O(1)| Medium|
|221 | [Maximal Square](https://leetcode.com/problems/maximal-square/) | Dynamic Programming| Time: O(m * n), Space: O(m * n)| Medium|
|256 | [Paint House](https://leetcode.com/problems/paint-house/) | Dynamic Programming| Time: O(n), Space: O(1)| Medium|
|276 | [Paint Fence](https://leetcode.com/problems/paint-fence/) | Dynamic Programming| Time: O(n), Space: O(1)| Medium|
|279 | [Perfect Squares](https://leetcode.com/problems/perfect-squares/) | Dynamic Programming| Time: O(n√n), Space: O(n)| Medium|
|300 | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | Dynamic Programming| Time: O(n^2), Space: O(n)| Medium|
|309 | [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | Dynamic Programming| Time: O(n), Space: O(n)| Medium|
|322 | [Coin Change](https://leetcode.com/problems/coin-change/) | Dynamic Programming| Time: O(n * amount), Space: O(amount)| Medium|
|338 | [Counting Bits](https://leetcode.com/problems/counting-bits/) | Dynamic Programming| Time: O(n), Space: O(n)| Medium|
|343 | [Integer Break](https://leetcode.com/problems/integer-break/) | Dynamic Programming| Time: O(n), Space: O(n)| Medium|
|368 | [Largest Divisible Subset](https://leetcode.com/problems/largest-divisible-subset/) | Dynamic Programming| Time: O(n^2), Space: O(n)| Medium|
|375 | [Guess Number Higher or Lower II](https://leetcode.com/problems/guess-number-higher-or-lower-ii/) | Dynamic Programming| Time: O(n^2), Space: O(n^2)| Medium|
|376 | [Wiggle Subsequence](https://leetcode.com/problems/wiggle-subsequence/) | Dynamic Programming| Time: O(n), Space: O(n)| Medium|
|377 | [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/) | Dynamic Programming| Time: O(n * target), Space: O(target)| Medium|
|413 | [Arithmetic Slices](https://leetcode.com/problems/arithmetic-slices/) | Dynamic Programming| Time: O(n), Space: O(1)| Medium|
|416 | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | Dynamic Programming| Time: O(n * sum), Space: O(sum)| Medium|
|464 | [Can I Win](https://leetcode.com/problems/can-i-win/) | Dynamic Programming| Time: O(2^n), Space: O(2^n)| Medium|
|474 | [Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/) | Dynamic Programming| Time: O(m * n * max), Space: O(m * n * max)| Medium|
|486 | [Predict the Winner](https://leetcode.com/problems/predict-the-winner/) | Dynamic Programming| Time: O(n^2), Space: O(n^2)| Medium|
|494 | [Target Sum](https://leetcode.com/problems/target-sum/) | Dynamic Programming| Time: O(n * sum), Space: O(n * sum)| Medium|
|516 | [Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/) | Dynamic Programming| Time: O(n^2), Space: O(n^2)| Medium|
|518 | [Coin Change 2](https://leetcode.com/problems/coin-change-2/) | Dynamic Programming| Time: O(n * amount), Space: O(n * amount)| Medium|
|524 | [Longest Word in Dictionary through Deleting](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/) | Dynamic Programming| Time: O(n * m), Space: O(n * m)| Medium|
|583 | [Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/) | Dynamic Programming| Time: O(m * n), Space: O(m * n)| Medium|
|600 | [Non-negative Integers without Consecutive Ones](https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/) | Dynamic Programming| Time: O(log n), Space: O(log n)| Medium|
|634 | [Find the Derangement of an Array](https://leetcode.com/problems/find-the-derangement-of-an-array/) | Dynamic Programming| Time: O(n), Space: O(1)| Medium|
|638 | [Shopping Offers](https://leetcode.com/problems/shopping-offers/) | Dynamic Programming| Time: O(n * m), Space: O(n * m)| Medium|
|647 | [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | Dynamic Programming| Time: O(n^2), Space: O(n^2)| Medium|
|650 | [2 Keys Keyboard](https://leetcode.com/problems/2-keys-keyboard/) | Dynamic Programming| Time: O(n), Space: O(n)| Medium|
|651 | [4 Keys Keyboard](https://leetcode.com/problems/4-keys-keyboard/) | Dynamic Programming| Time: O(n^2), Space: O(n)| Medium|
|712 | [Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/) | Dynamic Programming| Time: O(m * n), Space: O(m * n)| Medium|
|714 | [Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) | Dynamic Programming| Time: O(n), Space: O(1)| Medium|
|718 | [Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/) | Dynamic Programming| Time: O(m * n), Space: O(m * n)| Medium|
|740 | [Delete and Earn](https://leetcode.com/problems/delete-and-earn/) | Dynamic Programming| Time: O(n), Space: O(n)| Medium|
|790 | [Domino and Tromino Tiling](https://leetcode.com/problems/domino-and-tromino-tiling/) | Dynamic Programming| Time: O(n), Space: O(n)| Medium|
|837 | [New 21 Game](https://leetcode.com/problems/new-21-game/) | Dynamic Programming| Time: O(n), Space: O(n)| Medium|
|926 | [Flip String to Monotone Increasing](https://leetcode.com/problems/flip-string-to-monotone-increasing/) | Dynamic Programming| Time: O(n), Space: O(1)| Medium|
|935 | [Knight Dialer](https://leetcode.com/problems/knight-dialer/) | Dynamic Programming| Time: O(n), Space: O(1)| Medium|
| 1416 | [Restore The Array](https://leetcode.com/problems/restore-the-array/) | Dynamic Programming| O(n) Time, O(n) Space| Medium|
| 10 | [📓 Regular Expression Matching](0010.ipynb) | <span title="Break the problem into overlapping subproblems; cache results to avoid recomputation.">Dynamic Programming</span> | Time: O(m * n), Space: O(m * n)| Hard|
| 44 | [Wildcard Matching](https://leetcode.com/problems/wildcard-matching/) | Dynamic Programming| Time: O(m * n), Space: O(m * n)| Hard|
| 72 | [Edit Distance](https://leetcode.com/problems/edit-distance/) | Dynamic Programming| Time: O(m * n), Space: O(m * n)| Hard|
| 87 | [Scramble String](https://leetcode.com/problems/scramble-string/) | Dynamic Programming| Time: O(n^4), Space: O(n^4)| Hard|
| 97 | [Interleaving String](https://leetcode.com/problems/interleaving-string/) | Dynamic Programming| Time: O(m * n), Space: O(m * n)| Hard|
|115 | [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) | Dynamic Programming| Time: O(m * n), Space: O(m * n)| Hard|
|123 | [Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) | Dynamic Programming| Time: O(n), Space: O(1)| Hard|
|132 | [Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/) | Dynamic Programming| Time: O(n^2), Space: O(n^2)| Hard|
|174 | [Dungeon Game](https://leetcode.com/problems/dungeon-game/) | Dynamic Programming| Time: O(m * n), Space: O(m * n)| Hard|
|188 | [Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/) | Dynamic Programming| Time: O(k * n), Space: O(k * n)| Hard|
|265 | [Paint House II](https://leetcode.com/problems/paint-house-ii/) | Dynamic Programming| Time: O(nk), Space: O(k) | Hard|
|312 | [Burst Balloons](https://leetcode.com/problems/burst-balloons/) | Dynamic Programming| Time: O(n^3), Space: O(n^2)| Hard|
|403 | [Frog Jump](https://leetcode.com/problems/frog-jump/) | Dynamic Programming| Time: O(n^2), Space: O(n)| Hard|
|418 | [Sentence Screen Fitting](https://leetcode.com/problems/sentence-screen-fitting/) | Dynamic Programming| Time: O(n * m), Space: O(1)| Hard|
|446 | [Arithmetic Slices II - Subsequence](https://leetcode.com/problems/arithmetic-slices-ii-subsequence/) | Dynamic Programming| Time: O(n^2), Space: O(n^2)| Hard|
|466 | [Count The Repetitions](https://leetcode.com/problems/count-the-repetitions/) | Dynamic Programming| Time: O(n^2), Space: O(n)| Hard|
|471 | [Encode String with Shortest Length](https://leetcode.com/problems/encode-string-with-shortest-length/) | Dynamic Programming| Time: O(n^3), Space: O(n^2)| Hard|
|517 | [Super Washing Machines](https://leetcode.com/problems/super-washing-machines/) | Dynamic Programming| Time: O(n^2), Space: O(n)| Hard|
|546 | [Remove Boxes](https://leetcode.com/problems/remove-boxes/) | Dynamic Programming| Time: O(n^3), Space: O(n^3)| Hard|
|552 | [Student Attendance Record II](https://leetcode.com/problems/student-attendance-record-ii/) | Dynamic Programming| Time: O(n), Space: O(n)| Hard|
|568 | [Maximum Vacation Days](https://leetcode.com/problems/maximum-vacation-days/) | Dynamic Programming| Time: O(n^2), Space: O(n^2)| Hard|
|612 | [Student Attendance Record III](https://leetcode.com/problems/student-attendance-record-iii/) | Dynamic Programming| Time: O(n), Space: O(n)| Hard|
|629 | [K Inverse Pairs Array](https://leetcode.com/problems/k-inverse-pairs-array/) | Dynamic Programming| Time: O(n * k), Space: O(n * k)| Hard|
|639 | [Decode Ways II](https://leetcode.com/problems/decode-ways-ii/) | Dynamic Programming| Time: O(n), Space: O(1)| Hard|
|644 | [Maximum Average Subarray II](https://leetcode.com/problems/maximum-average-subarray-ii/) | Dynamic Programming| Time: O(n log n), Space: O(1)| Hard|
|656 | [Coin Path](https://leetcode.com/problems/coin-path/) | Dynamic Programming| Time: O(n^2), Space: O(n)| Hard|
|664 | [Strange Printer](https://leetcode.com/problems/strange-printer/) | Dynamic Programming| Time: O(n^3), Space: O(n^2)| Hard|
|805 | [Split Array With Same Average](https://leetcode.com/problems/split-array-with-same-average/) | Dynamic Programming| Time: O(2^n), Space: O(n)| Hard|
|818 | [Race Car](https://leetcode.com/problems/race-car/) | Dynamic Programming| Time: O(n), Space: O(n)| Hard|
|913 | [Cat and Mouse](https://leetcode.com/problems/cat-and-mouse/) | Dynamic Programming| Time: O(n^3), Space: O(n^2)| Hard|
| 1330 | [Super Egg Drop](https://leetcode.com/problems/super-egg-drop/) | Dynamic Programming| O(k * log n) Time, O(k * log n) Space| Hard|
| 1335 | [Minimum Difficulty of a Job Schedule](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/) | Dynamic Programming| O(n^2) Time, O(n) Space| Hard|
| 1155 | [Number of Dice Rolls With Target Sum](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/) | Dynamic Programming, Array | O(n * target) Time, O(n * target) Space| Medium|
| 1186 | [Maximum Subarray Sum with One Deletion](https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/) | Dynamic Programming, Array | O(n) Time, O(n) Space| Medium|
| 1193 | [Maximum Profit of Operating a Centennial Wheel](https://leetcode.com/problems/maximum-profit-of-operating-a-centennial-wheel/) | Dynamic Programming, Array | O(n) Time, O(n) Space| Medium|
| 1194 | [Target Sum](https://leetcode.com/problems/target-sum/) | Dynamic Programming, Array | O(n * sum) Time, O(n * sum) Space| Medium|
| 1199 | [Minimum Time to Build Blocks](https://leetcode.com/problems/minimum-time-to-build-blocks/) | Dynamic Programming, Array | O(n) Time, O(n) Space| Medium|
| 1223 | [Dice Roll Simulation](https://leetcode.com/problems/dice-roll-simulation/) | Dynamic Programming, Array | O(n) Time, O(n) Space| Medium|
| 1262 | [Greatest Sum Divisible by Three](https://leetcode.com/problems/greatest-sum-divisible-by-three/) | Dynamic Programming, Array | O(n) Time, O(1) Space| Medium|
| 1322 | [Longest Arithmetic Subsequence](https://leetcode.com/problems/longest-arithmetic-subsequence/) | Dynamic Programming, Array | O(n^2) Time, O(n) Space| Medium|
| 1400 | [Find Good Days to Rob the Bank](https://leetcode.com/problems/find-good-days-to-rob-the-bank/) | Dynamic Programming, Array | O(n) Time, O(n) Space| Medium|
| 1420 | [Find Good Days to Rob the Bank](https://leetcode.com/problems/find-good-days-to-rob-the-bank/) | Dynamic Programming, Array | O(n) Time, O(n) Space| Medium|
| 1195 | [Frog Jump](https://leetcode.com/problems/frog-jump/) | Dynamic Programming, Array | O(n^2) Time, O(n) Space| Hard|
| 1215 | [Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/) | Dynamic Programming, Array | O(n^2) Time, O(n^2) Space| Hard|
| 1220 | [Count Vowels Permutation](https://leetcode.com/problems/count-vowels-permutation/) | Dynamic Programming, Array | O(n) Time, O(1) Space| Hard|
| 1235 | [Job Scheduler](https://leetcode.com/problems/job-scheduler/) | Dynamic Programming, Array | O(n^2) Time, O(n^2) Space| Hard|
| 1240 | [Tiling a Rectangle with the Fewest Squares](https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/) | Dynamic Programming, Array | O(m * n) Time, O(m * n) Space| Hard|
| 1340 | [Jump Game V](https://leetcode.com/problems/jump-game-v/) | Dynamic Programming, Array | O(n) Time, O(n) Space| Hard|
| 1388 | [Pizza With 3n Slices](https://leetcode.com/problems/pizza-with-3n-slices/) | Dynamic Programming, Array | O(n^2) Time, O(n) Space| Hard|
|542 | [01 Matrix](https://leetcode.com/problems/01-matrix/) | Dynamic Programming, BFS | Time: O(m * n), Space: O(m * n)| Medium|
|140 | [Word Break II](https://leetcode.com/problems/word-break-ii/) | Dynamic Programming, Backtracking| Time: O(n^3), Space: O(n)| Hard|
|514 | [Freedom Trail](https://leetcode.com/problems/freedom-trail/) | Dynamic Programming, Binary Search | Time: O(m * n), Space: O(m * n)| Hard|
|576 | [Out of Boundary Paths](https://leetcode.com/problems/out-of-boundary-paths/) | Dynamic Programming, DFS | Time: O(m * n * maxMove), Space: O(m * n)| Medium|
| 1397 | [Find All Good Strings](https://leetcode.com/problems/find-all-good-strings/) | Dynamic Programming, DFS | O(n) Time, O(1) Space| Hard|
| 1406 | [Stone Game III](https://leetcode.com/problems/stone-game-iii/) | Dynamic Programming, DP| O(n) Time, O(n) Space| Hard|
| 1463 | [Cherry Pickup II](https://leetcode.com/problems/cherry-pickup-ii/) | Dynamic Programming, DP| O(n^2) Time, O(n^2) Space| Hard|
| 1473 | [Paint House III](https://leetcode.com/problems/paint-house-iii/) | Dynamic Programming, DP| O(n^2) Time, O(n) Space| Hard|
|813 | [Largest Sum of Averages](https://leetcode.com/problems/largest-sum-of-averages/) | Dynamic Programming, DP Table| Time: O(n^2), Space: O(n^2)| Medium|
|877 | [Stone Game](https://leetcode.com/problems/stone-game/) | Dynamic Programming, DP Table| Time: O(n^2), Space: O(n^2)| Medium|
|741 | [Cherry Pickup](https://leetcode.com/problems/cherry-pickup/) | Dynamic Programming, DP Table| Time: O(n^2), Space: O(n^2)| Hard|
|801 | [Minimum Swaps To Make Sequences Increasing](https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/) | Dynamic Programming, DP Table| Time: O(n^2), Space: O(n)| Hard|
|808 | [Soup Servings](https://leetcode.com/problems/soup-servings/) | Dynamic Programming, DP Table| Time: O(n), Space: O(n)| Hard|
|823 | [Binary Trees With Factors](https://leetcode.com/problems/binary-trees-with-factors/) | Dynamic Programming, DP Table| Time: O(n^2), Space: O(n)| Hard|
|879 | [Profitable Schemes](https://leetcode.com/problems/profitable-schemes/) | Dynamic Programming, DP Table| Time: O(n * m), Space: O(n * m)| Hard|
|887 | [Super Egg Drop](https://leetcode.com/problems/super-egg-drop/) | Dynamic Programming, DP Table| Time: O(K * log N), Space: O(K)| Hard|
|920 | [Number of Music Playlists](https://leetcode.com/problems/number-of-music-playlists/) | Dynamic Programming, DP Table| Time: O(n * k), Space: O(n * k)| Hard|
| 1301 | [Number of Paths with Max Score](https://leetcode.com/problems/number-of-paths-with-max-score/) | Dynamic Programming, Graph | O(n * m) Time, O(n * m) Space| Hard|
|139 | [Word Break](https://leetcode.com/problems/word-break/) | Dynamic Programming, Hash Set| Time: O(n^2), Space: O(n)| Medium|
| 1218 | [Longest Arithmetic Subsequence of Given Difference](https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/) | Dynamic Programming, HashMap | O(n) Time, O(n) Space| Medium|
| 1255 | [Maximum Score Words Formed by Letters](https://leetcode.com/problems/maximum-score-words-formed-by-letters/) | Dynamic Programming, HashMap | O(n * m) Time, O(n) Space| Medium|
| 1266 | [Number of Ways to Stay in the Same Place After Some Moves](https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-moves/) | Dynamic Programming, Math| O(n) Time, O(n) Space| Medium|
| 1289 | [Minimum Falling Path Sum II](https://leetcode.com/problems/minimum-falling-path-sum-ii/) | Dynamic Programming, Matrix| O(n * m) Time, O(n * m) Space| Medium|
|264 | [Ugly Number II](https://leetcode.com/problems/ugly-number-ii/) | Dynamic Programming, Min-Heap| Time: O(n log n), Space: O(n)| Medium|
|548 | [Split Array with Equal Sum](https://leetcode.com/problems/split-array-with-equal-sum/) | Dynamic Programming, Prefix Sum| Time: O(n^2), Space: O(n)| Hard|
| 1230 | [Toss Strange Coins](https://leetcode.com/problems/toss-strange-coins/) | Dynamic Programming, Probability | O(n) Time, O(1) Space| Hard|
| 1425 | [Constrained Subset Sum](https://leetcode.com/problems/constrained-subset-sum/) | Dynamic Programming, Queue | O(n log n) Time, O(n) Space| Hard|
| 1259 | [Maximal Sum of 4 Non-Overlapping Subarrays](https://leetcode.com/problems/maximal-sum-of-4-non-overlapping-subarrays/) | Dynamic Programming, Sliding Window| O(n) Time, O(n) Space| Hard|
| 1298 | [Maximum Sum of 3 Non-Overlapping Subarrays](https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/) | Dynamic Programming, Sliding Window| O(n) Time, O(n) Space| Hard|
| 85 | [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/) | Dynamic Programming, Stack | Time: O(m * n), Space: O(n)| Hard|
| 1246 | [Palindrome Removal](https://leetcode.com/problems/palindrome-removal/) | Dynamic Programming, String| O(n^2) Time, O(n^2) Space| Medium|
| 1216 | [Valid Palindrome III](https://leetcode.com/problems/valid-palindrome-iii/) | Dynamic Programming, String| O(n^2) Time, O(n^2) Space| Hard|
| 1278 | [Palindrome Partitioning III](https://leetcode.com/problems/palindrome-partitioning-iii/) | Dynamic Programming, String| O(n^2) Time, O(n^2) Space| Hard|
| 1312 | [Minimum Insertion Steps to Make a String Palindrome](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/) | Dynamic Programming, String| O(n^2) Time, O(n^2) Space| Hard|

## File I/O
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|194 | [Transpose File](https://leetcode.com/problems/transpose-file/) | File I/O | Time: O(1), Space: O(1)| Easy|
|195 | [Tenth Line](https://leetcode.com/problems/tenth-line/) | File I/O | Time: O(1), Space: O(1)| Easy|

## Floyd's Cycle Detection
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|457 | [Circular Array Loop](https://leetcode.com/problems/circular-array-loop/) | Floyd's Cycle Detection| Time: O(n), Space: O(1)| Medium|

## Game Theory
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|292 | [Nim Game](https://leetcode.com/problems/nim-game/) | Game Theory| Time: O(1), Space: O(1)| Easy|
|810 | [Chalkboard XOR Game](https://leetcode.com/problems/chalkboard-xor-game/) | Game Theory| Time: O(n), Space: O(1)| Hard|
|580 | [Game Winner](https://leetcode.com/problems/game-winner/) | Game Theory, Array | Time: O(n), Space: O(n)| Easy|

## Geometry
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|223 | [Rectangle Area](https://leetcode.com/problems/rectangle-area/) | Geometry | Time: O(1), Space: O(1)| Medium|
|469 | [Convex Polygon](https://leetcode.com/problems/convex-polygon/) | Geometry | Time: O(n), Space: O(1)| Medium|
|593 | [Valid Square](https://leetcode.com/problems/valid-square/) | Geometry | Time: O(1), Space: O(1)| Medium|
|335 | [Self Crossing](https://leetcode.com/problems/self-crossing/) | Geometry | Time: O(n), Space: O(1)| Hard|
|587 | [Erect the Fence](https://leetcode.com/problems/erect-the-fence/) | Geometry | Time: O(n log n), Space: O(n)| Hard|
|149 | [Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/) | Geometry, Hash Map | Time: O(n^2), Space: O(n)| Hard|
|812 | [Largest Triangle Area](https://leetcode.com/problems/largest-triangle-area/) | Geometry, Math | Time: O(1), Space: O(1)| Easy|
|836 | [Rectangle Overlap](https://leetcode.com/problems/rectangle-overlap/) | Geometry, Math | Time: O(1), Space: O(1)| Easy|
| 1232 | [Check If It Is a Straight Line](https://leetcode.com/problems/check-if-it-is-a-straight-line/) | Geometry, Math | O(n) Time, O(1) Space| Easy|
|478 | [Generate Random Point in a Circle](https://leetcode.com/problems/generate-random-point-in-a-circle/) | Geometry, Math | Time: O(1), Space: O(1)| Medium|
| 1401 | [Circle and Rectangle Overlapping](https://leetcode.com/problems/circle-and-rectangle-overlapping/) | Geometry, Math | O(1) Time, O(1) Space| Medium|

## Graph
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
| 1034 | [Edge List to Adj List Conversion](https://leetcode.com/problems/edge-list-to-adj-list-conversion/) | Graph, Adjacency List| Time: O(E), Space: O(V)| Medium|
| 1045 | [Customer Orders Availability System](https://leetcode.com/problems/customer-orders-availability-system/) | Graph, Adjacency List| Time: O(n^2), Space: O(n)| Medium|
| 1477 | [Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/) | Graph, Array | O(n) Time, O(n) Space| Easy|
|310 | [Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/) | Graph, BFS | Time: O(n), Space: O(n)| Medium|
| 1036 | [Escape a Large Maze](https://leetcode.com/problems/escape-a-large-maze/) | Graph, BFS | Time: O(n), Space: O(n)| Medium|
| 1065 | [Train System](https://leetcode.com/problems/train-system/) | Graph, BFS | Time: O(n^2), Space: O(n)| Medium|
|749 | [Contain Virus](https://leetcode.com/problems/contain-virus/) | Graph, BFS | Time: O(n^2), Space: O(n^2)| Hard|
|753 | [Cracking the Safe](https://leetcode.com/problems/cracking-the-safe/) | Graph, BFS | Time: O(n^2), Space: O(n)| Hard|
|815 | [Bus Routes](https://leetcode.com/problems/bus-routes/) | Graph, BFS | Time: O(n * m), Space: O(n * m)| Hard|
|847 | [Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) | Graph, BFS | Time: O(n^2), Space: O(n^2)| Hard|
| 1377 | [Frog Position After T Seconds](https://leetcode.com/problems/frog-position-after-t-seconds/) | Graph, BFS | O(n) Time, O(n) Space| Hard|
| 1391 | [Check if There is a Valid Path in a Grid](https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/) | Graph, BFS, DFS| O(n * m) Time, O(n * m) Space| Medium|
|785 | [Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/)| Graph, BFS/DFS | Time: O(n + e), Space: O(n)| Medium|
|133 | [Clone Graph](https://leetcode.com/problems/clone-graph/) | Graph, DFS | Time: O(V + E), Space: O(V)| Medium|
|332 | [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) | Graph, DFS | Time: O(E log E), Space: O(E)| Medium|
|399 | [Evaluate Division](https://leetcode.com/problems/evaluate-division/) | Graph, DFS | Time: O(E), Space: O(V)| Medium|
|721 | [Accounts Merge](https://leetcode.com/problems/accounts-merge/) | Graph, DFS | Time: O(n), Space: O(n)| Medium|
|802 | [Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/) | Graph, DFS | Time: O(V + E), Space: O(V)| Medium|
|841 | [Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/) | Graph, DFS | Time: O(n), Space: O(n)| Medium|
|886 | [Possible Bipartition](https://leetcode.com/problems/possible-bipartition/) | Graph, DFS | Time: O(n + m), Space: O(n)| Medium|
|947 | [Most Stones Removed with Same Row or Column](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/) | Graph, DFS | Time: O(n), Space: O(n)| Medium|
|924 | [Minimize Malware Spread](https://leetcode.com/problems/minimize-malware-spread/) | Graph, DFS | Time: O(n^2), Space: O(n)| Hard|
| 1001 | [Grid Illuminated](https://leetcode.com/problems/grid-illuminated/) | Graph, DFS | Time: O(n), Space: O(n)| Hard|
| 1466 | [Reorder Routes to Make All Paths Lead to the City Zero](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/) | Graph, DFS, BFS| O(n) Time, O(n) Space| Medium|
|882 | [Reachable Nodes In Subdivided Graph](https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/) | Graph, DFS, BFS| Time: O(n^2), Space: O(n)| Hard|
|997 | [Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/) | Graph, DFS, In-degree| Time: O(n), Space: O(n)| Easy|
| 1027 | [Find The Town Judge](https://leetcode.com/problems/find-the-town-judge/) | Graph, DFS, In-degree| Time: O(n), Space: O(n)| Easy|
| 1079 | [Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/) | Graph, DFS, In-degree| Time: O(n), Space: O(n)| Easy|
|928 | [Minimize Malware Spread II](https://leetcode.com/problems/minimize-malware-spread-ii/) | Graph, DFS, Simulation | Time: O(n^2), Space: O(n)| Hard|
| 1192 | [Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/) | Graph, DFS, Union-Find | O(n + m) Time, O(n) Space| Hard|
|323 | [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | Graph, DFS/BFS | Time: O(V + E), Space: O(V)| Medium|
|743 | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Graph, Dijkstra| Time: O(E log V), Space: O(V)| Medium|
| 1334 | [Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) | Graph, Dijkstra| O(n^3) Time, O(n^2) Space| Medium|
| 1368 | [Minimum Cost to Make at Least One Valid Path in a Grid](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/) | Graph, Dijkstra, BFS | O(n * m) Time, O(n * m) Space| Hard|
|734 | [Sentence Similarity](https://leetcode.com/problems/sentence-similarity/) | Graph, Hash Map| Time: O(n), Space: O(n)| Easy|
| 1436 | [Destination City](https://leetcode.com/problems/destination-city/) | Graph, HashMap | O(n) Time, O(n) Space| Easy|
| 1311 | [Get Watched Videos by Your Friends](https://leetcode.com/problems/get-watched-videos-by-your-friends/) | Graph, HashMap | O(n + m) Time, O(n + m) Space| Medium|
| 1364 | [Jetpack](https://leetcode.com/problems/jetpack/) | Graph, Priority Queue| O(n log n) Time, O(n) Space| Medium|
|207 | [Course Schedule](https://leetcode.com/problems/course-schedule/) | Graph, Topological Sort| Time: O(V + E), Space: O(V + E)| Medium|
|210 | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | Graph, Topological Sort| Time: O(V + E), Space: O(V + E)| Medium|
|851 | [Loud and Rich](https://leetcode.com/problems/loud-and-rich/) | Graph, Topological Sort| Time: O(n + m), Space: O(n + m)| Medium|
|269 | [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) | Graph, Topological Sort| Time: O(V + E), Space: O(V + E)| Hard|
| 1136 | [Parallel Courses](https://leetcode.com/problems/parallel-courses/) | Graph, Topological Sort| Time: O(n), Space: O(n)| Hard|
| 1203 | [Sort Items by Groups Respecting Dependencies](https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/) | Graph, Topological Sort| O(n + m) Time, O(n + m) Space| Hard|
| 1462 | [Course Schedule IV](https://leetcode.com/problems/course-schedule-iv/) | Graph, Topological Sort| O(n^2) Time, O(n) Space| Hard|
| 1494 | [Parallel Courses II](https://leetcode.com/problems/parallel-courses-ii/) | Graph, Topological Sort| O(n^2) Time, O(n) Space| Hard|
| 1257 | [Smallest Common Region](https://leetcode.com/problems/smallest-common-region/) | Graph, Tree| O(n) Time, O(n) Space| Medium|
|277 | [Find the Celebrity](https://leetcode.com/problems/find-the-celebrity/) | Graph, Two Pointers| Time: O(n), Space: O(1)| Medium|
| 1042 | [Friendship Requests I: Individual Contributions](https://leetcode.com/problems/friendship-requests-i-individual-contributions/)| Graph, Union Find| Time: O(n * log n), Space: O(n)| Medium|
|737 | [Sentence Similarity II](https://leetcode.com/problems/sentence-similarity-ii/) | Graph, Union-Find| Time: O(n), Space: O(n)| Medium|
| 1319 | [Number of Operations to Make Network Connected](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) | Graph, Union-Find| O(n + m) Time, O(n) Space| Medium|
| 1484 | [Group Strings](https://leetcode.com/problems/group-strings/) | Graph, Union-Find| O(n log n) Time, O(n) Space| Medium|
| 1402 | [Redundant Connection II](https://leetcode.com/problems/redundant-connection-ii/) | Graph, Union-Find| O(n) Time, O(n) Space| Hard|

## Greedy
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|252 | [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) | Greedy | Time: O(n log n), Space: O(1)| Easy|
|455 | [Assign Cookies](https://leetcode.com/problems/assign-cookies/) | Greedy | Time: O(n log n), Space: O(1)| Easy|
|860 | [Lemonade Change](https://leetcode.com/problems/lemonade-change/) | Greedy | Time: O(n), Space: O(1)| Easy|
| 55 | [Jump Game](https://leetcode.com/problems/jump-game/) | Greedy | Time: O(n), Space: O(1)| Medium|
|122 | [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) | Greedy | Time: O(n), Space: O(1)| Medium|
|134 | [Gas Station](https://leetcode.com/problems/gas-station/) | Greedy | Time: O(n), Space: O(1)| Medium|
|397 | [Integer Replacement](https://leetcode.com/problems/integer-replacement/) | Greedy | Time: O(log n), Space: O(1)| Medium|
|406 | [Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/) | Greedy | Time: O(n^2), Space: O(n)| Medium|
|435 | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | Greedy | Time: O(n log n), Space: O(1)| Medium|
|484 | [Find Permutation](https://leetcode.com/problems/find-permutation/) | Greedy | Time: O(n), Space: O(1)| Medium|
|769 | [Max Chunks To Make Sorted](https://leetcode.com/problems/max-chunks-to-make-sorted/) | Greedy | Time: O(n), Space: O(1)| Medium|
|948 | [Bag of Tokens](https://leetcode.com/problems/bag-of-tokens/) | Greedy | Time: O(n log n), Space: O(1)| Medium|
| 1005 | [Maximize Sum of Array After K Negations](https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/) | Greedy | Time: O(n log n), Space: O(1)| Medium|
| 1057 | [Campus Bikes](https://leetcode.com/problems/campus-bikes/) | Greedy | Time: O(n log n), Space: O(1)| Medium|
| 1069 | [Minimum Swap to Make Strings Equal](https://leetcode.com/problems/minimum-swap-to-make-strings-equal/) | Greedy | Time: O(n), Space: O(1)| Medium|
| 45 | [Jump Game II](https://leetcode.com/problems/jump-game-ii/) | Greedy | Time: O(n), Space: O(1)| Hard|
|135 | [Candy](https://leetcode.com/problems/candy/) | Greedy | Time: O(n), Space: O(n)| Hard|
|330 | [Patching Array](https://leetcode.com/problems/patching-array/) | Greedy | Time: O(log n), Space: O(1)| Hard|
|411 | [Minimum Unique Word Abbreviation](https://leetcode.com/problems/minimum-unique-word-abbreviation/) | Greedy | Time: O(n^2), Space: O(n)| Hard|
|420 | [Strong Password Checker](https://leetcode.com/problems/strong-password-checker/) | Greedy | Time: O(n), Space: O(1)| Hard|
|667 | [Beautiful Arrangement II](https://leetcode.com/problems/beautiful-arrangement-ii/) | Greedy, Array| Time: O(n), Space: O(1)| Medium|
| 1151 | [Minimum Swaps to Arrange a Binary String](https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-string/) | Greedy, Array| Time: O(n), Space: O(1)| Medium|
| 1479 | [Maximize Palindrome Length From Subsequences](https://leetcode.com/problems/maximize-palindrome-length-from-subsequences/) | Greedy, DP | O(n) Time, O(n) Space| Medium|
| 1130 | [Minimum Cost Tree From Leaf Values](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/) | Greedy, DP | Time: O(n^2), Space: O(n^2)| Hard|
|334 | [Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/) | Greedy, Dynamic Programming| Time: O(n), Space: O(1)| Medium|
|763 | [Partition Labels](https://leetcode.com/problems/partition-labels/) | Greedy, Hash Map | Time: O(n), Space: O(n)| Medium|
| 1072 | [Flip Columns For Maximum Number of Equal Rows](https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/) | Greedy, Hash Map | Time: O(m * n), Space: O(m)| Medium|
| 1121 | [Divide Array in Sets of K Consecutive Numbers](https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/) | Greedy, Hash Map | Time: O(n), Space: O(n)| Medium|
|659 | [Split Array into Consecutive Subsequences](https://leetcode.com/problems/split-array-into-consecutive-subsequences/) | Greedy, Hash Map | Time: O(n), Space: O(n)| Hard|
|253 | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) | Greedy, Heap | Time: O(n log n), Space: O(n)| Medium|
|358 | [Rearrange String k Distance Apart](https://leetcode.com/problems/rearrange-string-k-distance-apart/) | Greedy, Heap | Time: O(n log k), Space: O(n)| Hard|
|630 | [Course Schedule III](https://leetcode.com/problems/course-schedule-iii/) | Greedy, Heap | Time: O(n log n), Space: O(n)| Hard|
| 1150 | [Split Array into Consecutive Subsequences](https://leetcode.com/problems/split-array-into-consecutive-subsequences/) | Greedy, Heap | Time: O(n log n), Space: O(n)| Hard|
| 1383 | [Maximum Performance of a Team](https://leetcode.com/problems/maximum-performance-of-a-team/) | Greedy, Heap | O(n log n) Time, O(n) Space| Hard|
|621 | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | Greedy, Heap, Hash Map | Time: O(n log n), Space: O(n)| Medium|
|767 | [Reorganize String](https://leetcode.com/problems/reorganize-string/) | Greedy, Priority Queue | Time: O(n log n), Space: O(n)| Medium|
| 1093 | [Car Pooling](https://leetcode.com/problems/car-pooling/) | Greedy, Simulation | Time: O(n), Space: O(1)| Medium|
|995 | [Minimum Number of K Consecutive Bit Flips](https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/) | Greedy, Sliding Window | Time: O(n), Space: O(1)| Hard|
|452 | [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | Greedy, Sorting| Time: O(n log n), Space: O(1)| Medium|
|646 | [Maximum Length of Pair Chain](https://leetcode.com/problems/maximum-length-of-pair-chain/) | Greedy, Sorting| Time: O(n log n), Space: O(1)| Medium|
|826 | [Most Profit Assigning Work](https://leetcode.com/problems/most-profit-assigning-work/) | Greedy, Sorting| Time: O(n log n), Space: O(n)| Medium|
| 1007 | [Minimum Domino Rotations For Equal Row](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/) | Greedy, Sorting| Time: O(n), Space: O(1)| Medium|
| 1054 | [Distant Barcodes](https://leetcode.com/problems/distant-barcodes/) | Greedy, Sorting| Time: O(n log n), Space: O(n)| Medium|
| 1353 | [Maximum Number of Events That Can Be Attended](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/) | Greedy, Sorting| O(n log n) Time, O(n) Space| Medium|
|757 | [Set Intersection Size At Least Two](https://leetcode.com/problems/set-intersection-size-at-least-two/) | Greedy, Sorting| Time: O(n log n), Space: O(n)| Hard|
|321 | [Create Maximum Number](https://leetcode.com/problems/create-maximum-number/) | Greedy, Stack| Time: O(n), Space: O(n)| Hard|
|768 | [Max Chunks To Make Sorted II](https://leetcode.com/problems/max-chunks-to-make-sorted-ii/) | Greedy, Stack| Time: O(n), Space: O(n)| Hard|
| 1405 | [Longest Happy String](https://leetcode.com/problems/longest-happy-string/) | Greedy, String | O(n) Time, O(1) Space| Medium|
| 1147 | [Longest Chunked Palindrome Decomposition](https://leetcode.com/problems/longest-chunked-palindrome-decomposition/) | Greedy, String | Time: O(n^2), Space: O(n^2)| Hard|
|881 | [Boats to Save People](https://leetcode.com/problems/boats-to-save-people/) | Greedy, Two Pointers | Time: O(n log n), Space: O(1)| Medium|
|765 | [Couples Holding Hands](https://leetcode.com/problems/couples-holding-hands/) | Greedy, Union-Find | Time: O(n log n), Space: O(n)| Hard|

## Grid
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|361 | [Bomb Enemy](https://leetcode.com/problems/bomb-enemy/) | Grid, DFS| Time: O(m * n), Space: O(m * n)| Medium|

## Hash Map
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|1 | [📓 Two Sum](0001.ipynb) | <span title="Store key→value pairs for O(1) lookup; complement / seen-element checks in a single pass.">Hash Map</span> | Time: O(n), Space: O(n)| Easy|
|170 | [Two Sum III - Data structure design](https://leetcode.com/problems/two-sum-iii-data-structure-design/) | Hash Map | Time: O(1), Space: O(n)| Easy|
|242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Hash Map | Time: O(n), Space: O(n)| Easy|
|266 | [Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation/) | Hash Map | Time: O(n), Space: O(n)| Easy|
|290 | [Word Pattern](https://leetcode.com/problems/word-pattern/) | Hash Map | Time: O(n), Space: O(n)| Easy|
|350 | [Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/) | Hash Map | Time: O(n), Space: O(n)| Easy|
|359 | [Logger Rate Limiter](https://leetcode.com/problems/logger-rate-limiter/) | Hash Map | Time: O(1), Space: O(n)| Easy|
|383 | [Ransom Note](https://leetcode.com/problems/ransom-note/) | Hash Map | Time: O(n), Space: O(n)| Easy|
|387 | [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) | Hash Map | Time: O(n), Space: O(n)| Easy|
|389 | [Find the Difference](https://leetcode.com/problems/find-the-difference/) | Hash Map | Time: O(n), Space: O(n)| Easy|
|409 | [Longest Palindrome](https://leetcode.com/problems/longest-palindrome/) | Hash Map | Time: O(n), Space: O(n)| Easy|
|447 | [Number of Boomerangs](https://leetcode.com/problems/number-of-boomerangs/) | Hash Map | Time: O(n^2), Space: O(n)| Easy|
|511 | [Game Play Analysis I](https://leetcode.com/problems/game-play-analysis-i/) | Hash Map | Time: O(n), Space: O(n)| Easy|
|512 | [Game Play Analysis II](https://leetcode.com/problems/game-play-analysis-ii/) | Hash Map | Time: O(n), Space: O(n)| Easy|
|534 | [Game Play Analysis III](https://leetcode.com/problems/game-play-analysis-iii/) | Hash Map | Time: O(n), Space: O(n)| Easy|
|550 | [Game Play Analysis IV](https://leetcode.com/problems/game-play-analysis-iv/) | Hash Map | Time: O(n), Space: O(n)| Easy|
|574 | [Winning Candidate](https://leetcode.com/problems/winning-candidate/) | Hash Map | Time: O(n), Space: O(n)| Easy|
|594 | [Longest Harmonious Subsequence](https://leetcode.com/problems/longest-harmonious-subsequence/) | Hash Map | Time: O(n), Space: O(n)| Easy|
|697 | [Degree of an Array](https://leetcode.com/problems/degree-of-an-array/) | Hash Map | Time: O(n), Space: O(n)| Easy|
|706 | [Design HashMap](https://leetcode.com/problems/design-hashmap/) | Hash Map | Time: O(1), Space: O(n)| Easy|
|760 | [Find Anagram Mappings](https://leetcode.com/problems/find-anagram-mappings/) | Hash Map | Time: O(n), Space: O(n)| Easy|
|771 | [Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/) | Hash Map | Time: O(n), Space: O(n)| Easy|
|811 | [Subdomain Visit Count](https://leetcode.com/problems/subdomain-visit-count/) | Hash Map | Time: O(n), Space: O(n)| Easy|
| 1128 | [Number of Equivalent Domino Pairs](https://leetcode.com/problems/number-of-equivalent-domino-pairs/) | Hash Map | Time: O(n), Space: O(n)| Easy|
| 49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Hash Map | Time: O(n * k), Space: O(n * k)| Medium|
|244 | [Shortest Word Distance II](https://leetcode.com/problems/shortest-word-distance-ii/) | Hash Map | Time: O(1), Space: O(n)| Medium|
|249 | [Group Shifted Strings](https://leetcode.com/problems/group-shifted-strings/) | Hash Map | Time: O(nk), Space: O(nk)| Medium|
|288 | [Unique Word Abbreviation](https://leetcode.com/problems/unique-word-abbreviation/) | Hash Map | Time: O(n), Space: O(n)| Medium|
|299 | [Bulls and Cows](https://leetcode.com/problems/bulls-and-cows/) | Hash Map | Time: O(n), Space: O(n)| Medium|
|325 | [Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/) | Hash Map | Time: O(n), Space: O(n)| Medium|
|423 | [Reconstruct Original Digits from English](https://leetcode.com/problems/reconstruct-original-digits-from-english/) | Hash Map | Time: O(n), Space: O(1)| Medium|
|454 | [4Sum II](https://leetcode.com/problems/4sum-ii/) | Hash Map | Time: O(n^2), Space: O(n^2)| Medium|
|525 | [Contiguous Array](https://leetcode.com/problems/contiguous-array/) | Hash Map | Time: O(n), Space: O(n)| Medium|
|535 | [Encode and Decode TinyURL](https://leetcode.com/problems/encode-and-decode-tinyurl/) | Hash Map | Time: O(1), Space: O(n)| Medium|
|554 | [Brick Wall](https://leetcode.com/problems/brick-wall/) | Hash Map | Time: O(n), Space: O(n)| Medium|
|599 | [Minimum Index of a Repeated Element](https://leetcode.com/problems/minimum-index-of-a-repeated-element/) | Hash Map | Time: O(n), Space: O(n)| Medium|
|635 | [Design Log Storage System](https://leetcode.com/problems/design-log-storage-system/) | Hash Map | Time: O(1), Space: O(n)| Medium|
|750 | [Number of Corner Rectangles](https://leetcode.com/problems/number-of-corner-rectangles/) | Hash Map | Time: O(n^2), Space: O(n)| Medium|
|781 | [Rabbits in Forest](https://leetcode.com/problems/rabbits-in-forest/) | Hash Map | Time: O(n), Space: O(n)| Medium|
|792 | [Number of Matching Subsequences](https://leetcode.com/problems/number-of-matching-subsequences/) | Hash Map | Time: O(n), Space: O(n)| Medium|
| 1010 | [Pairs of Songs With Total Durations Divisible by 60](https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/) | Hash Map | Time: O(n), Space: O(n)| Medium|
|588 | [Design In-Memory File System](https://leetcode.com/problems/design-in-memory-file-system/) | Hash Map | Time: O(n), Space: O(n)| Hard|
|380 | [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) | Hash Map, Array| Time: O(1), Space: O(n)| Medium|
|974 | [Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/) | Hash Map, Array| Time: O(n), Space: O(n)| Medium|
| 1124 | [Longest Well-Performing Interval](https://leetcode.com/problems/longest-well-performing-interval/) | Hash Map, Array| Time: O(n), Space: O(n)| Medium|
|381 | [Insert Delete GetRandom O(1) - Duplicates allowed](https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/) | Hash Map, Array| Time: O(1), Space: O(n)| Hard|
|981 | [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) | Hash Map, BST| Time: O(1), Space: O(n)| Medium|
|460 | [LFU Cache](https://leetcode.com/problems/lfu-cache/) | Hash Map, Double Linked List | Time: O(1), Space: O(n)| Hard|
|146 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | Hash Map, Doubly Linked List | Time: O(1), Space: O(capacity) | Hard|
|451 | [Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/) | Hash Map, Heap | Time: O(n log n), Space: O(n)| Medium|
|692 | [Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/) | Hash Map, Heap | Time: O(n log k), Space: O(n)| Medium|
|355 | [Design Twitter](https://leetcode.com/problems/design-twitter/) | Hash Map, Linked List| Time: O(1), Space: O(n)| Medium|
|914 | [X of a Kind in a Deck of Cards](https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/) | Hash Map, Math | Time: O(n), Space: O(n)| Easy|
|822 | [Card Flipping Game](https://leetcode.com/problems/card-flipping-game/) | Hash Map, Set| Time: O(n), Space: O(n)| Medium|
| 30 | [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) | Hash Map, Sliding Window | Time: O(n * m), Space: O(n)| Hard|
| 76 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Hash Map, Sliding Window | Time: O(n), Space: O(n)| Hard|
|169 | [Majority Element](https://leetcode.com/problems/majority-element/) | Hash Map, Sorting| Time: O(n), Space: O(n)| Easy|
|846 | [Hand of Straights](https://leetcode.com/problems/hand-of-straights/) | Hash Map, Sorting| Time: O(n log n), Space: O(n)| Medium|
|954 | [Array of Doubled Pairs](https://leetcode.com/problems/array-of-doubled-pairs/) | Hash Map, Sorting| Time: O(n log n), Space: O(n)| Medium|
|726 | [Number of Atoms](https://leetcode.com/problems/number-of-atoms/) | Hash Map, Stack| Time: O(n), Space: O(n)| Hard|
|884 | [Uncommon Words from Two Sentences](https://leetcode.com/problems/uncommon-words-from-two-sentences/) | Hash Map, String | Time: O(n), Space: O(n)| Easy|
|609 | [Find Duplicate File in System](https://leetcode.com/problems/find-duplicate-file-in-system/) | Hash Map, String | Time: O(n), Space: O(n)| Medium|
|890 | [Find and Replace Pattern](https://leetcode.com/problems/find-and-replace-pattern/) | Hash Map, String | Time: O(n), Space: O(n)| Medium|
|916 | [Word Subsets](https://leetcode.com/problems/word-subsets/) | Hash Map, String | Time: O(n * m), Space: O(n)| Medium|
| 1084 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Hash Map, String | Time: O(n * k log k), Space: O(n)| Medium|
| 1173 | [Immediate Food Delivery I](https://leetcode.com/problems/immediate-food-delivery-i/) | HashMap, Array | O(n) Time, O(n) Space| Easy|
| 1346 | [Check If N and Its Double Exist](https://leetcode.com/problems/check-if-n-and-its-double-exist/) | HashMap, Array | O(n) Time, O(n) Space| Easy|
| 1394 | [Find Lucky Integer in an Array](https://leetcode.com/problems/find-lucky-integer-in-an-array/) | HashMap, Array | O(n) Time, O(n) Space| Easy|
| 1399 | [Count Largest Group](https://leetcode.com/problems/count-largest-group/) | HashMap, Array | O(n) Time, O(n) Space| Easy|
| 1158 | [Market Analysis I](https://leetcode.com/problems/market-analysis-i/) | HashMap, Array | O(n) Time, O(n) Space| Medium|
| 1164 | [Product Price at a Given Date](https://leetcode.com/problems/product-price-at-a-given-date/) | HashMap, Array | O(log n) Time, O(n) Space| Medium|
| 1174 | [Immediate Food Delivery II](https://leetcode.com/problems/immediate-food-delivery-ii/) | HashMap, Array | O(n) Time, O(n) Space| Medium|
| 1282 | [Group People Given the Group Size They Belong To](https://leetcode.com/problems/group-people-given-the-group-size-they-belong-to/) | HashMap, Array | O(n) Time, O(n) Space| Medium|
| 1497 | [Check If Array Pairs Are Divisible by K](https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/) | HashMap, Array | O(n) Time, O(n) Space| Medium|
| 1159 | [Market Analysis II](https://leetcode.com/problems/market-analysis-ii/) | HashMap, Array | O(n) Time, O(n) Space| Hard|
| 1224 | [Maximum Equal Frequency](https://leetcode.com/problems/maximum-equal-frequency/) | HashMap, Array | O(n) Time, O(n) Space| Hard|
| 1434 | [Number of Ways to Wear Different Hats to Each Other](https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/) | HashMap, Array | O(n * m) Time, O(n * m) Space| Hard|
| 1481 | [Least Number of Unique Integers after K Removals](https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/) | HashMap, Min-Heap| O(n log n) Time, O(n) Space| Medium|
| 1495 | [Least Number of Unique Integers After K Removals](https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/) | HashMap, Min-Heap| O(n log n) Time, O(n) Space| Medium|
| 1348 | [Tweet Counts Per Frequency](https://leetcode.com/problems/tweet-counts-per-frequency/) | HashMap, Queue | O(n) Time, O(n) Space| Medium|
| 1396 | [Design Underground System](https://leetcode.com/problems/design-underground-system/) | HashMap, Queue | O(1) Time, O(n) Space| Medium|
| 1157 | [Online Majority Element In Subarray](https://leetcode.com/problems/online-majority-element-in-subarray/) | HashMap, Queue | O(1) Time, O(n) Space| Hard|
| 1160 | [Find Words That Can Be Formed by Characters](https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/) | HashMap, Set | O(n) Time, O(n) Space| Easy|
| 1207 | [Unique Number of Occurrences](https://leetcode.com/problems/unique-number-of-occurrences/) | HashMap, Set | O(n) Time, O(n) Space| Easy|
| 1169 | [Invalid Transactions](https://leetcode.com/problems/invalid-transactions/) | HashMap, Set | O(n) Time, O(n) Space| Medium|
| 1487 | [Making File Names Unique](https://leetcode.com/problems/making-file-names-unique/) | HashMap, Set | O(n) Time, O(n) Space| Medium|
| 1297 | [Maximum Number of Occurrences of a Substring](https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/) | HashMap, Sliding Window| O(n) Time, O(n) Space| Medium|
| 1338 | [Reduce Array Size to The Half](https://leetcode.com/problems/reduce-array-size-to-the-half/) | HashMap, Sorting | O(n log n) Time, O(n) Space| Medium|
| 1418 | [Display Table of Food Orders in a Restaurant](https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/) | HashMap, Sorting | O(n log n) Time, O(n) Space| Medium|
| 1296 | [Divide Array in Sets of K Consecutive Numbers](https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/) | HashMap, Sorting | O(n log n) Time, O(n) Space| Hard|
| 1247 | [Minimum Number of Steps to Make Two Strings Anagram](https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/) | HashMap, String| O(n) Time, O(n) Space| Medium|
| 1256 | [Encoding the Keypad](https://leetcode.com/problems/encoding-the-keypad/) | HashMap, String| O(n) Time, O(n) Space| Medium|

## Hash Set
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Hash Set | Time: O(n), Space: O(n)| Easy|
|219 | [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) | Hash Set | Time: O(n), Space: O(n)| Easy|
|349 | [Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/) | Hash Set | Time: O(n), Space: O(n)| Easy|
|575 | [Distribute Candies](https://leetcode.com/problems/distribute-candies/) | Hash Set | Time: O(n), Space: O(n)| Easy|
|705 | [Design HashSet](https://leetcode.com/problems/design-hashset/) | Hash Set | Time: O(1), Space: O(n)| Easy|
| 36 | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | Hash Set | Time: O(n^2), Space: O(n^2)| Medium|
|187 | [Repeated DNA Sequences](https://leetcode.com/problems/repeated-dna-sequences/) | Hash Set | Time: O(n), Space: O(n)| Medium|
|356 | [Line Reflection](https://leetcode.com/problems/line-reflection/) | Hash Set | Time: O(n), Space: O(n)| Medium|
|128 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Hash Set | Time: O(n), Space: O(n)| Hard|
|888 | [Fair Candy Swap](https://leetcode.com/problems/fair-candy-swap/) | Hash Set, Array| Time: O(n), Space: O(n)| Easy|
|202 | [Happy Number](https://leetcode.com/problems/happy-number/) | Hash Set, Cycle Detection| Time: O(log n), Space: O(log n)| Easy|
|939 | [Minimum Area Rectangle](https://leetcode.com/problems/minimum-area-rectangle/) | Hash Set, Geometry | Time: O(n^2), Space: O(n)| Medium|
|804 | [Unique Morse Code Words](https://leetcode.com/problems/unique-morse-code-words/) | Hash Set, String | Time: O(n), Space: O(1)| Easy|
| 1198 | [Find Smallest Common Element in All Rows](https://leetcode.com/problems/find-smallest-common-element-in-all-rows/) | HashSet, Array | O(n * m) Time, O(n) Space| Medium|
| 1452 | [People Whose List of Favorite Companies Is Not a Subset of Another List](https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/) | HashSet, Array | O(n^2) Time, O(n^2) Space| Medium|
| 1461 | [Check If a String Contains All Binary Codes of Size K](https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/) | HashSet, Sliding Window| O(n) Time, O(2^k) Space| Medium|

## Heap
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|703 | [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | Heap | Time: O(log k), Space: O(k)| Easy|
|215 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Heap | Time: O(n log k), Space: O(k)| Medium|
|378 | [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | Heap | Time: O(k log n), Space: O(n)| Medium|
|295 | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Heap | Time: O(log n), Space: O(n)| Hard|
|480 | [Sliding Window Median](https://leetcode.com/problems/sliding-window-median/) | Heap | Time: O(n log k), Space: O(k)| Hard|
|786 | [K-th Smallest Prime Fraction](https://leetcode.com/problems/k-th-smallest-prime-fraction/) | Heap, Binary Search| Time: O(n log n), Space: O(n)| Hard|
| 23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Heap, Divide and Conquer | Time: O(n log k), Space: O(k)| Hard|
|347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Heap, Hash Map | Time: O(n log k), Space: O(n)| Medium|
| 1488 | [Avoid Flood in The City](https://leetcode.com/problems/avoid-flood-in-the-city/) | Heap, HashMap| O(n log n) Time, O(n) Space| Hard|
| 1439 | [Find the Kth Smallest Sum of a Matrix with Sorted Rows](https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/) | Heap, Matrix | O(k log n) Time, O(n) Space| Hard|
|632 | [Smallest Range Covering Elements from K Lists](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/) | Heap, Merge| Time: O(n log k), Space: O(k)| Hard|
| 1046 | [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) | Heap, Priority Queue | Time: O(n log n), Space: O(n)| Easy|
| 1500 | [Find the Median of a Data Stream](https://leetcode.com/problems/find-the-median-of-a-data-stream/) | Heap, Priority Queue | O(log n) Time, O(n) Space| Hard|
|571 | [Find Median Given Frequency of Numbers](https://leetcode.com/problems/find-median-given-frequency-of-numbers/) | Heap, Sorting| Time: O(n log n), Space: O(n)| Medium|
|973 | [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | Heap, Sorting| Time: O(n log k), Space: O(k)| Medium|
|218 | [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/) | Heap, Sweep Line | Time: O(n log n), Space: O(n)| Hard|
|502 | [IPO](https://leetcode.com/problems/ipo/) | Heap,Greedy| O(N log N) Time| Hard|

## Integer
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|7 | [📓 Reverse Integer](0007.ipynb) | <span title="Operate directly on the integer bits or digits without converting to a string.">Integer</span> | Time: O(log x), Space: O(1)| Easy|
|9 | [📓 Palindrome Number](0009.ipynb) | <span title="Operate directly on the integer bits or digits without converting to a string.">Integer</span> | Time: O(log x), Space: O(1)| Easy|
| 1185 | [Day of the Week](https://leetcode.com/problems/day-of-the-week/) | Integer| O(1) Time, O(1) Space| Easy|
| 1154 | [Day of the Year](https://leetcode.com/problems/day-of-the-year/) | Integer, Array | O(1) Time, O(1) Space| Easy|

## Interval
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|715 | [Range Module](https://leetcode.com/problems/range-module/) | Interval | Time: O(n), Space: O(n)| Hard|
|601 | [Human Traffic of Stadium](https://leetcode.com/problems/human-traffic-of-stadium/) | Interval, Prefix Sum | Time: O(n), Space: O(1)| Medium|
|759 | [Employee Free Time](https://leetcode.com/problems/employee-free-time/) | Interval, Priority Queue | Time: O(n log n), Space: O(n)| Hard|
| 1229 | [Meeting Scheduler](https://leetcode.com/problems/meeting-scheduler/) | Interval, Sorting| O(n log n) Time, O(1) Space| Medium|

## Iterator
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|281 | [Zigzag Iterator](https://leetcode.com/problems/zigzag-iterator/) | Iterator | Time: O(1), Space: O(k)| Medium|
|284 | [Peeking Iterator](https://leetcode.com/problems/peeking-iterator/) | Iterator | Time: O(1), Space: O(1)| Medium|

## Kadane's Algorithm
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|918 | [Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/) | Kadane's Algorithm, DP | Time: O(n), Space: O(1)| Medium|

## Linked List
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
| 21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Linked List| Time: O(m + n), Space: O(1)| Easy|
| 83 | [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) | Linked List| Time: O(n), Space: O(1)| Easy|
|141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Linked List| Time: O(n), Space: O(1)| Easy|
|160 | [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/) | Linked List| Time: O(m + n), Space: O(1)| Easy|
|203 | [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/) | Linked List| Time: O(n), Space: O(1)| Easy|
|206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Linked List| Time: O(n), Space: O(1)| Easy|
|237 | [Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/) | Linked List| Time: O(1), Space: O(1)| Easy|
|707 | [Design Linked List](https://leetcode.com/problems/design-linked-list/) | Linked List| Time: O(1), Space: O(n)| Easy|
| 1206 | [Design Linked List](https://leetcode.com/problems/design-linked-list/) | Linked List| O(1) Time, O(1) Space| Easy|
|2 | [📓 Add Two Numbers](0002.ipynb) | <span title="Singly-linked node chain; traverse with pointers and rewire next references in place.">Linked List</span> | Time: O(max(m, n)), Space: O(max(m, n))| Medium|
| 19 | [📓 Remove Nth Node From End of List](0019.ipynb) | <span title="Single left-to-right scan with two pointers; no second pass needed.">One-Pass Two Pointers</span> | Time: O(n), Space: O(1)| Medium|
| 24 | [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) | Linked List| Time: O(n), Space: O(1)| Medium|
| 61 | [Rotate List](https://leetcode.com/problems/rotate-list/) | Linked List| Time: O(n), Space: O(1)| Medium|
| 82 | [Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) | Linked List| Time: O(n), Space: O(1)| Medium|
| 86 | [Partition List](https://leetcode.com/problems/partition-list/) | Linked List| Time: O(n), Space: O(1)| Medium|
| 92 | [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/) | Linked List| Time: O(n), Space: O(1)| Medium|
|138 | [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | Linked List| Time: O(n), Space: O(n)| Medium|
|143 | [Reorder List](https://leetcode.com/problems/reorder-list/) | Linked List| Time: O(n), Space: O(1)| Medium|
|147 | [Insertion Sort List](https://leetcode.com/problems/insertion-sort-list/) | Linked List| Time: O(n^2), Space: O(1)| Medium|
|328 | [Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/) | Linked List| Time: O(n), Space: O(1)| Medium|
|369 | [Plus One Linked List](https://leetcode.com/problems/plus-one-linked-list/) | Linked List| Time: O(n), Space: O(1)| Medium|
|379 | [Design Phone Directory](https://leetcode.com/problems/design-phone-directory/) | Linked List| Time: O(1), Space: O(n)| Medium|
|430 | [Flatten a Multilevel Doubly Linked List](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/) | Linked List| Time: O(n), Space: O(1)| Medium|
|708 | [Insert into a Sorted Circular Linked List](https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/) | Linked List| Time: O(n), Space: O(1)| Medium|
|725 | [Split Linked List in Parts](https://leetcode.com/problems/split-linked-list-in-parts/) | Linked List| Time: O(n), Space: O(1)| Medium|
| 25 | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | Linked List| Time: O(n), Space: O(1)| Hard|
|142 | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) | Linked List, Floyd's Cycle Detection | Time: O(n), Space: O(1)| Medium|
|817 | [Linked List Components](https://leetcode.com/problems/linked-list-components/) | Linked List, Hash Set| Time: O(n), Space: O(n)| Medium|
| 1171 | [Remove Zero Sum Consecutive Nodes from Linked List](https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/) | Linked List, HashMap | O(n) Time, O(n) Space| Medium|
| 1290 | [Convert Binary Number in a Linked List to Integer](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/) | Linked List, Math| O(n) Time, O(1) Space| Easy|
| 1445 | [Add Two Integers in Linked List Representation](https://leetcode.com/problems/add-two-integers-in-linked-list-representation/) | Linked List, Math| O(n) Time, O(1) Space| Medium|
|148 | [Sort List](https://leetcode.com/problems/sort-list/) | Linked List, Merge Sort| Time: O(n log n), Space: O(1)| Medium|
| 1474 | [Delete N Nodes After M Nodes of a Linked List](https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/) | Linked List, Simulation| O(n) Time, O(1) Space| Medium|
|234 | [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) | Linked List, Stack | Time: O(n), Space: O(n)| Easy|
|445 | [Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/) | Linked List, Stack | Time: O(max(m, n)), Space: O(max(m, n))| Medium|
|109 | [Convert Sorted List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/) | Linked List, Tree| Time: O(n), Space: O(log n)| Medium|
|876 | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | Linked List, Two Pointers| Time: O(n), Space: O(1)| Easy|

## Manhatten Distance
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|296 | [Best Meeting Point](https://leetcode.com/problems/best-meeting-point/) | Manhatten Distance | Time: O(m * n), Space: O(1)| Hard|

## Math
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
| 13 | [📓 Roman to Integer](0013.ipynb) | <span title="Pure arithmetic or number-theory formula; no extra data structure needed.">Math</span> | Time: O(n), Space: O(1)| Easy|
| 69 | [Sqrt(x)](https://leetcode.com/problems/sqrtx/) | Math | Time: O(log x), Space: O(1)| Easy|
|168 | [Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/) | Math | Time: O(log n), Space: O(1)| Easy|
|171 | [Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/) | Math | Time: O(n), Space: O(1)| Easy|
|172 | [Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/) | Math | Time: O(log n), Space: O(1)| Easy|
|231 | [Power of Two](https://leetcode.com/problems/power-of-two/) | Math | Time: O(1), Space: O(1)| Easy|
|258 | [Add Digits](https://leetcode.com/problems/add-digits/) | Math | Time: O(1), Space: O(1)| Easy|
|263 | [Ugly Number](https://leetcode.com/problems/ugly-number/) | Math | Time: O(log n), Space: O(1)| Easy|
|326 | [Power of Three](https://leetcode.com/problems/power-of-three/) | Math | Time: O(log n), Space: O(1)| Easy|
|342 | [Power of Four](https://leetcode.com/problems/power-of-four/) | Math | Time: O(1), Space: O(1)| Easy|
|400 | [Nth Digit](https://leetcode.com/problems/nth-digit/) | Math | Time: O(log n), Space: O(1)| Easy|
|405 | [Convert a Number to Hexadecimal](https://leetcode.com/problems/convert-a-number-to-hexadecimal/) | Math | Time: O(1), Space: O(1)| Easy|
|412 | [Fizz Buzz](https://leetcode.com/problems/fizz-buzz/) | Math | Time: O(n), Space: O(1)| Easy|
|453 | [Minimum Moves to Equal Array Elements](https://leetcode.com/problems/minimum-moves-to-equal-array-elements/) | Math | Time: O(n), Space: O(1)| Easy|
|481 | [Magical String](https://leetcode.com/problems/magical-string/) | Math | Time: O(n), Space: O(n)| Easy|
|492 | [Construct the Rectangle](https://leetcode.com/problems/construct-the-rectangle/) | Math | Time: O(sqrt(n)), Space: O(1)| Easy|
|504 | [Base 7](https://leetcode.com/problems/base-7/) | Math | O(log N) Time| Easy|
|507 | [Perfect Number](https://leetcode.com/problems/perfect-number/) | Math | O(√N) Time | Easy|
|693 | [Binary Number with Alternating Bits](https://leetcode.com/problems/binary-number-with-alternating-bits/) | Math | Time: O(1), Space: O(1)| Easy|
|728 | [Self Dividing Numbers](https://leetcode.com/problems/self-dividing-numbers/) | Math | Time: O(n), Space: O(1)| Easy|
|751 | [IP to CIDR](https://leetcode.com/problems/ip-to-cidr/) | Math | Time: O(1), Space: O(1)| Easy|
|788 | [Rotated Digits](https://leetcode.com/problems/rotated-digits/) | Math | Time: O(n), Space: O(1)| Easy|
|789 | [Escape The Ghosts](https://leetcode.com/problems/escape-the-ghosts/) | Math | Time: O(1), Space: O(1)| Easy|
|908 | [Smallest Range I](https://leetcode.com/problems/smallest-range-i/) | Math | Time: O(n), Space: O(1)| Easy|
|999 | [Available Captures for Rook](https://leetcode.com/problems/available-captures-for-rook/) | Math | Time: O(1), Space: O(1)| Easy|
| 1009 | [Complement of Base 10 Integer](https://leetcode.com/problems/complement-of-base-10-integer/) | Math | Time: O(log n), Space: O(1)| Easy|
| 1025 | [Divisor Game](https://leetcode.com/problems/divisor-game/) | Math | Time: O(log n), Space: O(1)| Easy|
| 1134 | [Armstrong Number](https://leetcode.com/problems/armstrong-number/) | Math | Time: O(n), Space: O(1)| Easy|
| 1217 | [Play with Chips](https://leetcode.com/problems/play-with-chips/) | Math | O(n) Time, O(1) Space| Easy|
| 1241 | [A Number After a Double Reversal](https://leetcode.com/problems/a-number-after-a-double-reversal/) | Math | O(1) Time, O(1) Space| Easy|
| 1281 | [Subtract the Product and Sum of Digits of an Integer](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/) | Math | O(1) Time, O(1) Space| Easy|
| 1317 | [Convert Integer to the Sum of Two No-Zero Integers](https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/) | Math | O(n) Time, O(1) Space| Easy|
| 1323 | [Maximum 69 Number](https://leetcode.com/problems/maximum-69-number/) | Math | O(n) Time, O(1) Space| Easy|
| 1342 | [Number of Steps to Reduce a Number to Zero](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/) | Math | O(log n) Time, O(1) Space| Easy|
| 1347 | [Minimum Cost to Move Chips to the Same Position](https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/) | Math | O(n) Time, O(1) Space| Easy|
| 1360 | [Number of Days Between Two Dates](https://leetcode.com/problems/number-of-days-between-two-dates/) | Math | O(1) Time, O(1) Space| Easy|
| 1373 | [Maximum Sum of Digits in a String](https://leetcode.com/problems/maximum-sum-of-digits-in-a-string/) | Math | O(n) Time, O(1) Space| Easy|
| 1393 | [Capital Gain](https://leetcode.com/problems/capital-gain/) | Math | O(n) Time, O(1) Space| Easy|
| 12 | [📓 Integer to Roman](0012.ipynb) | <span title="Pure arithmetic or number-theory formula; no extra data structure needed.">Math</span> | Time: O(1), Space: O(1)| Medium|
| 29 | [Divide Two Integers](https://leetcode.com/problems/divide-two-integers/) | Math | Time: O(log n), Space: O(1)| Medium|
| 50 | [Pow(x, n)](https://leetcode.com/problems/powx-n/)| Math | Time: O(log n), Space: O(1)| Medium|
|319 | [Bulb Switcher](https://leetcode.com/problems/bulb-switcher/) | Math | Time: O(1), Space: O(1)| Medium|
|357 | [Count Numbers with Unique Digits](https://leetcode.com/problems/count-numbers-with-unique-digits/) | Math | Time: O(n), Space: O(1)| Medium|
|390 | [Elimination Game](https://leetcode.com/problems/elimination-game/) | Math | Time: O(n), Space: O(1)| Medium|
|396 | [Rotate Function](https://leetcode.com/problems/rotate-function/) | Math | Time: O(n), Space: O(1)| Medium|
|462 | [Minimum Moves to Equal Array Elements II](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/) | Math | Time: O(n), Space: O(1)| Medium|
|553 | [Optimal Division](https://leetcode.com/problems/optimal-division/) | Math | Time: O(n), Space: O(n)| Medium|
|558 | [Quadrangle Area](https://leetcode.com/problems/quadrangle-area/) | Math | Time: O(1), Space: O(1)| Medium|
|625 | [Minimum Factorization](https://leetcode.com/problems/minimum-factorization/) | Math | Time: O(sqrt(n)), Space: O(1)| Medium|
|640 | [Solve the Equation](https://leetcode.com/problems/solve-the-equation/) | Math | Time: O(n), Space: O(1)| Medium|
|672 | [Bulb Switcher II](https://leetcode.com/problems/bulb-switcher-ii/) | Math | Time: O(1), Space: O(1)| Medium|
|681 | [Next Closest Time](https://leetcode.com/problems/next-closest-time/) | Math | Time: O(1), Space: O(1)| Medium|
|738 | [Monotone Increasing Digits](https://leetcode.com/problems/monotone-increasing-digits/) | Math | Time: O(n), Space: O(1)| Medium|
|754 | [Reach a Number](https://leetcode.com/problems/reach-a-number/) | Math | Time: O(sqrt(n)), Space: O(1)| Medium|
|829 | [Consecutive Numbers Sum](https://leetcode.com/problems/consecutive-numbers-sum/) | Math | Time: O(sqrt(n)), Space: O(1)| Medium|
|858 | [Mirror Reflection](https://leetcode.com/problems/mirror-reflection/) | Math | Time: O(1), Space: O(1)| Medium|
|869 | [Reordered Power of 2](https://leetcode.com/problems/reordered-power-of-2/) | Math | Time: O(n), Space: O(1)| Medium|
|910 | [Smallest Range II](https://leetcode.com/problems/smallest-range-ii/) | Math | Time: O(n log n), Space: O(1)| Medium|
|949 | [Largest Time for Given Digits](https://leetcode.com/problems/largest-time-for-given-digits/) | Math | Time: O(1), Space: O(1)| Medium|
|964 | [Least Operators to Express Number](https://leetcode.com/problems/least-operators-to-express-number/) | Math | Time: O(log n), Space: O(1)| Medium|
|970 | [Powerful Integers](https://leetcode.com/problems/powerful-integers/) | Math | Time: O(log N), Space: O(1)| Medium|
|991 | [Broken Calculator](https://leetcode.com/problems/broken-calculator/) | Math | Time: O(log n), Space: O(1)| Medium|
| 1006 | [Clumsy Factorial](https://leetcode.com/problems/clumsy-factorial/) | Math | Time: O(log n), Space: O(1)| Medium|
| 1017 | [Convert to Base -2](https://leetcode.com/problems/convert-to-base-2/)| Math | Time: O(log n), Space: O(1)| Medium|
| 1228 | [Missing Number in Arithmetic Progression](https://leetcode.com/problems/missing-number-in-arithmetic-progression/) | Math | O(n) Time, O(1) Space| Medium|
| 1276 | [Number of Burgers with No Waste of Ingredients](https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/) | Math | O(1) Time, O(1) Space| Medium|
| 1321 | [Restaurant Profit](https://leetcode.com/problems/restaurant-profit/) | Math | O(1) Time, O(1) Space| Medium|
| 1344 | [Angle Between Hands of a Clock](https://leetcode.com/problems/angle-between-hands-of-a-clock/) | Math | O(1) Time, O(1) Space| Medium|
| 1362 | [Closest Divisors](https://leetcode.com/problems/closest-divisors/) | Math | O(sqrt(n)) Time, O(1) Space| Medium|
| 1390 | [Four Divisors](https://leetcode.com/problems/four-divisors/) | Math | O(n sqrt(n)) Time, O(1) Space| Medium|
|233 | [Number of Digit One](https://leetcode.com/problems/number-of-digit-one/) | Math | Time: O(log n), Space: O(1)| Hard|
|273 | [Integer to English Words](https://leetcode.com/problems/integer-to-english-words/) | Math | Time: O(n), Space: O(1)| Hard|
|458 | [Poor Pigs](https://leetcode.com/problems/poor-pigs/) | Math | Time: O(1), Space: O(1)| Hard|
|479 | [Largest Palindrome Product](https://leetcode.com/problems/largest-palindrome-product/) | Math | Time: O(n^2), Space: O(1)| Hard|
|483 | [Smallest Good Base](https://leetcode.com/problems/smallest-good-base/) | Math | Time: O(log n), Space: O(1)| Hard|
|564 | [Find the Closest Palindrome](https://leetcode.com/problems/find-the-closest-palindrome/) | Math | Time: O(n), Space: O(1)| Hard|
|660 | [Remove 9](https://leetcode.com/problems/remove-9/) | Math | Time: O(log n), Space: O(1)| Hard|
|780 | [Reaching Points](https://leetcode.com/problems/reaching-points/) | Math | Time: O(log n), Space: O(1)| Hard|
|906 | [Super Palindromes](https://leetcode.com/problems/super-palindromes/) | Math | Time: O(sqrt(n)), Space: O(1)| Hard|
|972 | [Equal Rational Numbers](https://leetcode.com/problems/equal-rational-numbers/) | Math | Time: O(1), Space: O(1)| Hard|
| 1012 | [Numbers With Repeated Digits](https://leetcode.com/problems/numbers-with-repeated-digits/) | Math | Time: O(log n), Space: O(1)| Hard|
|806 | [Number of Lines To Write String](https://leetcode.com/problems/number-of-lines-to-write-string/) | Math, Array| Time: O(n), Space: O(1)| Easy|
| 1118 | [Number of Days in a Month](https://leetcode.com/problems/number-of-days-in-a-month/) | Math, Array| Time: O(1), Space: O(1)| Easy|
| 1295 | [Find Numbers with Even Number of Digits](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/) | Math, Array| O(n) Time, O(1) Space| Easy|
| 1326 | [Minimum Cost to Move Chips to the Same Position](https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/) | Math, Array| O(n) Time, O(1) Space| Easy|
| 1073 | [Adding Two Negabinary Numbers](https://leetcode.com/problems/adding-two-negabinary-numbers/) | Math, Array| Time: O(n), Space: O(n)| Medium|
| 1131 | [Maximum of Absolute Value Expression](https://leetcode.com/problems/maximum-of-absolute-value-expression/) | Math, Array| Time: O(n), Space: O(1)| Medium|
| 1237 | [Rotate Function](https://leetcode.com/problems/rotate-function/) | Math, Array| O(n) Time, O(n) Space| Medium|
| 1251 | [Average Selling Price](https://leetcode.com/problems/average-selling-price/) | Math, Array| O(n) Time, O(1) Space| Medium|
| 1471 | [The k-th Factor of n](https://leetcode.com/problems/the-k-th-factor-of-n/) | Math, Array| O(n) Time, O(1) Space| Medium|
| 1492 | [The kth Factor of n](https://leetcode.com/problems/the-k-th-factor-of-n/)| Math, Array| O(n) Time, O(1) Space| Medium|
|365 | [Water and Jug Problem](https://leetcode.com/problems/water-and-jug-problem/) | Math, BFS| Time: O(max(a, b)), Space: O(max(a, b))| Medium|
|878 | [Nth Magical Number](https://leetcode.com/problems/nth-magical-number/) | Math, Binary Search| Time: O(log n), Space: O(1)| Hard|
|868 | [Binary Gap](https://leetcode.com/problems/binary-gap/) | Math, Bit Manipulation | Time: O(1), Space: O(1)| Easy|
| 1359 | [Count All Valid Pickup and Delivery Options](https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/) | Math, Dynamic Programming| O(n^2) Time, O(n) Space| Hard|
| 1175 | [Prime Arrangements](https://leetcode.com/problems/prime-arrangements/) | Math, Factorization| O(n) Time, O(1) Space| Easy|
| 1250 | [Check If It Is a Good Array](https://leetcode.com/problems/check-if-it-is-a-good-array/) | Math, GCD| O(n) Time, O(1) Space| Medium|
|892 | [Surface Area of 3D Shapes](https://leetcode.com/problems/surface-area-of-3d-shapes/) | Math, Geometry | Time: O(n^2), Space: O(1)| Easy|
| 1037 | [Valid Boomerang](https://leetcode.com/problems/valid-boomerang/) | Math, Geometry | Time: O(1), Space: O(1)| Easy|
| 1413 | [Minimum Value to Get Positive Step by Step Sum](https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/) | Math, Greedy | O(n) Time, O(1) Space| Easy|
| 1432 | [Max Difference You Can Get From Changing an Integer](https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/) | Math, Greedy | O(n) Time, O(1) Space| Medium|
| 1447 | [Simplified Fractions](https://leetcode.com/problems/simplified-fractions/) | Math, HashSet| O(n^2) Time, O(n) Space| Medium|
| 1457 | [Pseudoclassical Pairs](https://leetcode.com/problems/pseudoclassical-pairs/) | Math, HashSet| O(n^2) Time, O(n) Space| Hard|
|866 | [Prime Palindrome](https://leetcode.com/problems/prime-palindrome/) | Math, Prime| Time: O(n), Space: O(1)| Medium|
| 1201 | [Ugly Number III](https://leetcode.com/problems/ugly-number-iii/) | Math, Priority Queue | O(log N) Time, O(1) Space| Medium|
|883 | [Projection Area of 3D Shapes](https://leetcode.com/problems/projection-area-of-3d-shapes/) | Math, Simulation | Time: O(n^2), Space: O(1)| Easy|
| 1056 | [Confusing Number](https://leetcode.com/problems/confusing-number/) | Math, Simulation | Time: O(1), Space: O(1)| Easy|
| 1103 | [Distribute Candies to People](https://leetcode.com/problems/distribute-candies-to-people/) | Math, Simulation | Time: O(n), Space: O(1)| Easy|
| 1058 | [Minimize Rounding Errors](https://leetcode.com/problems/minimize-rounding-errors/) | Math, Simulation | Time: O(n), Space: O(1)| Medium|
| 1083 | [Ancient Chinese Remainder](https://leetcode.com/problems/ancient-chinese-remainder/) | Math, Simulation | Time: O(1), Space: O(1)| Medium|
| 1467 | [Probability of a Two Boxes Having the Same Label](https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-label/) | Math, Simulation | O(n) Time, O(1) Space| Hard|
|828 | [Count Unique Characters of All Substrings of a Given String](https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/) | Math, Sliding Window | Time: O(n^2), Space: O(1)| Hard|
| 1071 | [Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/) | Math, String | Time: O(n), Space: O(1)| Easy|
| 1085 | [Sum of Digits in the Minimum Number](https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/) | Math, String | Time: O(1), Space: O(1)| Easy|
| 1271 | [Hexspeak](https://leetcode.com/problems/hexspeak/) | Math, String | O(n) Time, O(1) Space| Easy|
|166 | [Fraction to Recurring Decimal](https://leetcode.com/problems/fraction-to-recurring-decimal/) | Math, String | Time: O(n), Space: O(n)| Medium|
|592 | [Fraction Addition and Subtraction](https://leetcode.com/problems/fraction-addition-and-subtraction/) | Math, String | Time: O(n), Space: O(1)| Medium|
| 1291 | [Sequential Digits](https://leetcode.com/problems/sequential-digits/) | Math, String | O(n) Time, O(1) Space| Medium|
| 65 | [Valid Number](https://leetcode.com/problems/valid-number/) | Math, String | Time: O(n), Space: O(1)| Hard|
|633 | [Sum of Square Numbers](https://leetcode.com/problems/sum-of-square-numbers/) | Math, Two Pointer| Time: O(sqrt(n)), Space: O(1)| Easy|

## Matrix
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|422 | [Valid Word Square](https://leetcode.com/problems/valid-word-square/) | Matrix | Time: O(n^2), Space: O(1)| Easy|
|566 | [Reshape the Matrix](https://leetcode.com/problems/reshape-the-matrix/) | Matrix | Time: O(m * n), Space: O(m * n)| Easy|
| 1427 | [Clockwise Rotation](https://leetcode.com/problems/clockwise-rotation/) | Matrix | O(n^2) Time, O(1) Space| Easy|
|562 | [Longest Line of Consecutive One in Matrix](https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/) | Matrix | Time: O(m * n), Space: O(1)| Medium|
| 1253 | [Reconstruct a 2-Row Binary Matrix](https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/) | Matrix | O(n * m) Time, O(1) Space| Medium|
| 1252 | [Cells with Odd Values in a Matrix](https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/) | Matrix, Array| O(n * m) Time, O(1) Space| Easy|
| 1260 | [Shift 2D Grid](https://leetcode.com/problems/shift-2d-grid/) | Matrix, Array| O(n * m) Time, O(n * m) Space| Easy|
| 1275 | [Find Winner on a Tic Tac Toe Game](https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/) | Matrix, Array| O(1) Time, O(1) Space| Easy|
| 1476 | [Subrectangle Query](https://leetcode.com/problems/subrectangle-query/) | Matrix, Array| O(1) Time, O(m*n) Space| Medium|
| 1162 | [As Far from Land as Possible](https://leetcode.com/problems/as-far-from-land-as-possible/) | Matrix, BFS| O(n * m) Time, O(n * m) Space| Medium|
| 1351 | [Count Negative Numbers in a Sorted Matrix](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/) | Matrix, Binary Search| O(n + m) Time, O(1) Space| Easy|
| 1428 | [Leftmost Column with at Least a One](https://leetcode.com/problems/leftmost-column-with-at-least-a-one/) | Matrix, Binary Search| O(m log n) Time, O(1) Space| Medium|
| 1277 | [Count Square Submatrices with All Ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones/) | Matrix, DP | O(n * m) Time, O(n * m) Space| Medium|
| 1267 | [Count Servers that Communicate](https://leetcode.com/problems/count-servers-that-communicate/) | Matrix, HashMap| O(n * m) Time, O(n * m) Space| Medium|
| 1380 | [Lucky Numbers in a Matrix](https://leetcode.com/problems/lucky-numbers-in-a-matrix/) | Matrix, HashSet| O(n * m) Time, O(n) Space| Medium|
| 1212 | [Matrix Block Sum](https://leetcode.com/problems/matrix-block-sum/) | Matrix, Prefix Sum | O(m * n) Time, O(m * n) Space| Medium|
| 1314 | [Matrix Block Sum](https://leetcode.com/problems/matrix-block-sum/) | Matrix, Prefix Sum | O(n * m) Time, O(n * m) Space| Medium|
| 1341 | [Matrix Block Sum](https://leetcode.com/problems/matrix-block-sum/) | Matrix, Prefix Sum | O(n * m) Time, O(n * m) Space| Medium|
| 1292 | [Maximum Side Length of a Square with Sum Less than or Equal to Threshold](https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/) | Matrix, Sliding Window | O(n * m) Time, O(1) Space| Medium|
| 1329 | [Sort Matrix Diagonally](https://leetcode.com/problems/sort-matrix-diagonally/) | Matrix, Sorting| O(n * m log n) Time, O(n * m) Space| Medium|

## Merge Sort
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
| 493 | [📓 Reverse Pairs](0493.ipynb) | <span title="Fenwick tree: update index i with i += i & -i; prefix-query with i -= i & -i. O(log n) per op.">Binary Indexed Tree</span> | Time: $O(n \log n)$, Space: $O(n)$ | Hard |

## Min-Heap
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|313 | [Super Ugly Number](https://leetcode.com/problems/super-ugly-number/) | Min-Heap | Time: O(k * log k), Space: O(k)| Medium|
|373 | [Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) | Min-Heap | Time: O(k log k), Space: O(k)| Medium|
|407 | [Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/) | Min-Heap, BFS| Time: O(n * m * log(n * m)), Space: O(n * m) | Hard|

## Multi-threading
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
| 1116 | [Print Zero Even Odd](https://leetcode.com/problems/print-zero-even-odd/) | Multi-threading| Time: O(1), Space: O(1)| Medium|
| 1117 | [Building H2O](https://leetcode.com/problems/building-h2o/) | Multi-threading| Time: O(1), Space: O(1)| Medium|

## Prefix Sum Array
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|303 | [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) | Prefix Sum Array | Time: O(1), Space: O(n)| Easy|

## Priority Queue
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
| 1167 | [Minimum Cost to Connect Sticks](https://leetcode.com/problems/minimum-cost-to-connect-sticks/) | Priority Queue, Array| O(n log n) Time, O(n) Space| Medium|
| 1354 | [Construct Target Array With Multiple Sums](https://leetcode.com/problems/construct-target-array-with-multiple-sums/) | Priority Queue, Greedy | O(n log n) Time, O(n) Space| Hard|
|855 | [Exam Room](https://leetcode.com/problems/exam-room/) | Priority Queue, Heap | Time: O(log n), Space: O(n)| Medium|

## Probability
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
| 1227 | [Airplane Seat Assignment Probability](https://leetcode.com/problems/airplane-seat-assignment-probability/) | Probability, Simulation| O(1) Time, O(1) Space| Medium|

## Queue
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|346 | [Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream/) | Queue| Time: O(1), Space: O(n)| Easy|
|933 | [Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/) | Queue| Time: O(1), Space: O(n)| Easy|
|353 | [Design Snake Game](https://leetcode.com/problems/design-snake-game/) | Queue| Time: O(1), Space: O(n)| Medium|
|950 | [Reveal Cards In Increasing Order](https://leetcode.com/problems/reveal-cards-in-increasing-order/) | Queue| Time: O(n log n), Space: O(n)| Medium|
| 1357 | [Apply Discount Every n Orders](https://leetcode.com/problems/apply-discount-every-n-orders/) | Queue, Array | O(1) Time, O(n) Space| Medium|
|362 | [📓 Design Hit Counter](1204.ipynb) | <span title="Fixed 300 slots indexed by timestamp % 300; overwrite stale slots on hit() and sum valid slots on getHits().">Circular Buffer</span>| Time: O(1), Space: O(n)| Medium|
| 1429 | [First Unique Number](https://leetcode.com/problems/first-unique-number/) | Queue, HashMap | O(n) Time, O(n) Space| Easy|
|225 | [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) | Queue, Stack | Time: O(1), Space: O(n)| Easy|
|649 | [Dota2 Senate](https://leetcode.com/problems/dota2-senate/) | Queue, String| Time: O(n), Space: O(n)| Medium|

## Random
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|497 | [Random Point in Non-overlapping Rectangles](https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/) | Random | Time: O(1), Space: O(n)| Medium|
|384 | [Shuffle an Array](https://leetcode.com/problems/shuffle-an-array/) | Random, Array| Time: O(n), Space: O(n)| Medium|
|470 | [Implement Rand10() Using Rand7()](https://leetcode.com/problems/implement-rand10-using-rand7/) | Random, Math | Time: O(1), Space: O(1)| Medium|

## Recursion
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|241 | [Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/) | Recursion| Time: O(2^n), Space: O(n)| Medium|
|779 | [K-th Symbol in Grammar](https://leetcode.com/problems/k-th-symbol-in-grammar/) | Recursion| Time: O(log n), Space: O(1)| Medium|
|509 | [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) | Recursion,Dynamic Programming| O(N) Time, O(1) Space| Easy|

## Regex
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|193 | [Valid Phone Numbers](https://leetcode.com/problems/valid-phone-numbers/) | Regex| Time: O(1), Space: O(1)| Easy|

## Reservoir Sampling
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|382 | [Linked List Random Node](https://leetcode.com/problems/linked-list-random-node/) | Reservoir Sampling | Time: O(n), Space: O(1)| Medium|
|398 | [Random Pick Index](https://leetcode.com/problems/random-pick-index/) | Reservoir Sampling | Time: O(1), Space: O(n)| Medium|

## Segment Tree
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|307 | [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) | Segment Tree | Time: O(log n), Space: O(n)| Medium|
|699 | [Falling Squares](https://leetcode.com/problems/falling-squares/) | Segment Tree | Time: O(n log n), Space: O(n)| Hard|
|732 | [My Calendar III](https://leetcode.com/problems/my-calendar-iii/) | Segment Tree | Time: O(log n), Space: O(n)| Hard|
|363 | [Max Sum of Rectangle No Larger Than K](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/) | Segment Tree, Binary Search| Time: O(n^2 log n), Space: O(n)| Hard|
|850 | [Rectangle Area II](https://leetcode.com/problems/rectangle-area-ii/) | Segment Tree, Geometry | Time: O(n log n), Space: O(n)| Hard|

## Set
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
| 1496 | [Path Crossing](https://leetcode.com/problems/path-crossing/) | Set, Array | O(n) Time, O(n) Space| Medium|
|898 | [Bitwise ORs of Subarrays](https://leetcode.com/problems/bitwise-ors-of-subarrays/) | Set, Bit Manipulation| Time: O(n), Space: O(n)| Hard|
| 1446 | [Count Distinct Integers After Reverse Operations](https://leetcode.com/problems/count-distinct-integers-after-reverse-operations/) | Set, Math| O(n log n) Time, O(n) Space| Medium|

## Sieve of Eratosthenes
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|204 | [Count Primes](https://leetcode.com/problems/count-primes/) | Sieve of Eratosthenes| Time: O(n log log n), Space: O(n)| Easy|

## Simulation
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
| 1050 | [Animals in a Zoo](https://leetcode.com/problems/animals-in-a-zoo/) | Simulation | Time: O(1), Space: O(1)| Easy|
|755 | [Pour Water](https://leetcode.com/problems/pour-water/) | Simulation | Time: O(n^2), Space: O(1)| Medium|
|794 | [Valid Tic-Tac-Toe State](https://leetcode.com/problems/valid-tic-tac-toe-state/) | Simulation | Time: O(1), Space: O(1)| Medium|
|885 | [Spiral Matrix III](https://leetcode.com/problems/spiral-matrix-iii/) | Simulation | Time: O(n * m), Space: O(1)| Medium|
| 1041 | [Robot Bounded In Circle](https://leetcode.com/problems/robot-bounded-in-circle/) | Simulation | Time: O(1), Space: O(1)| Medium|
| 1097 | [Game of Life](https://leetcode.com/problems/game-of-life/) | Simulation | Time: O(n * m), Space: O(1)| Medium|
| 1126 | [Active Businesses](https://leetcode.com/problems/active-businesses/) | Simulation, Array| Time: O(n), Space: O(n)| Medium|
|799 | [Champagne Tower](https://leetcode.com/problems/champagne-tower/) | Simulation, DP | Time: O(n^2), Space: O(n^2)| Medium|
| 1101 | [Path Crossing](https://leetcode.com/problems/path-crossing/) | Simulation, Graph| Time: O(n), Space: O(n)| Medium|
| 1075 | [Project Employees](https://leetcode.com/problems/project-employees/) | Simulation, Hash Map | Time: O(n), Space: O(n)| Medium|
|874 | [Walking Robot Simulation](https://leetcode.com/problems/walking-robot-simulation/) | Simulation, Set| Time: O(n), Space: O(n)| Easy|
| 1040 | [Moving Stones Until Consecutive](https://leetcode.com/problems/moving-stones-until-consecutive/) | Simulation, Sorting| Time: O(1), Space: O(1)| Easy|
| 1138 | [Alphabet Board Path](https://leetcode.com/problems/alphabet-board-path/) | Simulation, String | Time: O(n), Space: O(1)| Medium|

## Sliding Window
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|495 | [Teemo Attacking](https://leetcode.com/problems/teemo-attacking/) | Sliding Window | Time: O(n), Space: O(1)| Easy|
|159 | [Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/) | Sliding Window | Time: O(n), Space: O(1)| Medium|
|209 | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | Sliding Window | Time: O(n), Space: O(1)| Medium|
|340 | [Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/) | Sliding Window | Time: O(n), Space: O(k)| Medium|
|424 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Sliding Window | Time: O(n), Space: O(1)| Medium|
|438 | [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | Sliding Window | Time: O(n), Space: O(1)| Medium|
|487 | [Max Consecutive Ones II](https://leetcode.com/problems/max-consecutive-ones-ii/) | Sliding Window | Time: O(n), Space: O(1)| Medium|
| 1004 | [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) | Sliding Window, Array| Time: O(n), Space: O(1)| Medium|
| 1196 | [How Many Apples Can You Put into the Basket](https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/) | Sliding Window, Array| O(n) Time, O(1) Space| Medium|
| 1248 | [Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/) | Sliding Window, Array| O(n) Time, O(1) Space| Medium|
| 1343 | [Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/) | Sliding Window, Array| O(n) Time, O(1) Space| Medium|
| 1423 | [Maximum Points You Can Obtain from Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/) | Sliding Window, Array| O(n) Time, O(n) Space| Medium|
| 1242 | [Maximum Sum of Two Non-Overlapping Subarrays](https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/) | Sliding Window, Dynamic Programming| O(n) Time, O(1) Space| Medium|
| 1052 | [Grumpy Bookstore Owner](https://leetcode.com/problems/grumpy-bookstore-owner/) | Sliding Window, Greedy | Time: O(n), Space: O(1)| Medium|
|798 | [Smallest Rotation with Highest Score](https://leetcode.com/problems/smallest-rotation-with-highest-score/) | Sliding Window, Greedy | Time: O(n), Space: O(n)| Hard|
|3 | [📓 Longest Substring Without Repeating Characters](0003.ipynb) | <span title="Expand/shrink a window with a hash map tracking character frequencies.">Sliding Window, Hash Map</span> | Time: O(n), Space: O(min(n, m))| Medium|
| 1100 | [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | Sliding Window, Hash Map | Time: O(n), Space: O(1)| Medium|
|992 | [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/) | Sliding Window, Hash Map | Time: O(n), Space: O(k)| Hard|
| 1358 | [Number of Substrings Containing All Three Characters](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/) | Sliding Window, HashMap| O(n) Time, O(1) Space| Medium|
| 1239 | [LongestSubstringWithoutRepeatingCharacters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Sliding Window, HashSet| O(n) Time, O(n) Space| Medium|
| 1438 | [Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) | Sliding Window, Queue| O(n) Time, O(n) Space| Medium|
| 1208 | [Get Equal Substrings Within Budget](https://leetcode.com/problems/get-equal-substrings-within-budget/) | Sliding Window, String | O(n) Time, O(1) Space| Medium|
| 1234 | [Replace the Substring for Balanced String](https://leetcode.com/problems/replace-the-substring-for-balanced-string/) | Sliding Window, String | O(n) Time, O(1) Space| Medium|
| 1456 | [Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) | Sliding Window, String | O(n) Time, O(1) Space| Medium|
|727 | [Minimum Window Subsequence](https://leetcode.com/problems/minimum-window-subsequence/) | Sliding Window, Two Pointer| Time: O(n), Space: O(1)| Hard|
|795 | [Number of Subarrays with Bounded Maximum](https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/) | Sliding Window, Two Pointers | Time: O(n), Space: O(1)| Medium|
|904 | [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) | Sliding Window, Two Pointers | Time: O(n), Space: O(1)| Medium|
| 1014 | [Best Sightseeing Pair](https://leetcode.com/problems/best-sightseeing-pair/) | Sliding Window, Two Pointers | Time: O(n), Space: O(1)| Medium|

## Sorting
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|414 | [Third Maximum Number](https://leetcode.com/problems/third-maximum-number/) | Sorting| Time: O(n log n), Space: O(1)| Easy|
|506 | [Relative Ranks](https://leetcode.com/problems/relative-ranks/) | Sorting| O(N log N) Time| Easy|
| 1051 | [Height Checker](https://leetcode.com/problems/height-checker/) | Sorting| Time: O(n log n), Space: O(1)| Easy|
| 1059 | [The K Weakest Rows in a Matrix](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/) | Sorting| Time: O(m log m), Space: O(1)| Easy|
| 56 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Sorting| Time: O(n log n), Space: O(1)| Medium|
| 57 | [Insert Interval](https://leetcode.com/problems/insert-interval/) | Sorting| Time: O(n), Space: O(1)| Medium|
|179 | [Largest Number](https://leetcode.com/problems/largest-number/) | Sorting| Time: O(n log n), Space: O(n)| Medium|
|274 | [H-Index](https://leetcode.com/problems/h-index/) | Sorting| Time: O(n log n), Space: O(1)| Medium|
|360 | [Sort Transformed Array](https://leetcode.com/problems/sort-transformed-array/) | Sorting| Time: O(n log n), Space: O(n)| Medium|
|164 | [Maximum Gap](https://leetcode.com/problems/maximum-gap/) | Sorting| Time: O(n log n), Space: O(n)| Hard|
| 1365 | [How Many Numbers Are Smaller Than the Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/) | Sorting, Array | O(n log n) Time, O(n) Space| Easy|
| 1403 | [Minimum Subsequence in Non-Increasing Order](https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/) | Sorting, Array | O(n log n) Time, O(n) Space| Easy|
| 1460 | [Make Two Arrays Equal by Reversing Subarrays](https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/) | Sorting, Array | O(n log n) Time, O(n) Space| Easy|
| 1464 | [Max Product of Two Elements in an Array](https://leetcode.com/problems/max-product-of-two-elements-in-an-array/) | Sorting, Array | O(n log n) Time, O(1) Space| Easy|
| 1200 | [Minimum Absolute Difference](https://leetcode.com/problems/minimum-absolute-difference/) | Sorting, Array | O(n log n) Time, O(1) Space| Medium|
| 1288 | [Remove Covered Intervals](https://leetcode.com/problems/remove-covered-intervals/) | Sorting, Array | O(n log n) Time, O(n) Space| Medium|
| 1318 | [Maximum Product of Two Elements in an Array](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/) | Sorting, Array | O(n log n) Time, O(1) Space| Medium|
| 1320 | [Minimum Moves to Equal Array Elements II](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/) | Sorting, Array | O(n log n) Time, O(1) Space| Medium|
| 1336 | [The K Weakest Rows in a Matrix](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/) | Sorting, Array | O(n log n) Time, O(n) Space| Medium|
| 1337 | [The K Weakest Rows in a Matrix](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/) | Sorting, Array | O(n log n) Time, O(n) Space| Medium|
| 1363 | [Largest Multiple of Three](https://leetcode.com/problems/largest-multiple-of-three/) | Sorting, Array | O(n log n) Time, O(n) Space| Medium|
| 1082 | [Special Array With X Elements Greater Than or Equal X](https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/) | Sorting, Binary Search | Time: O(n log n), Space: O(1)| Easy|
| 1385 | [Find the Distance Value Between Two Arrays](https://leetcode.com/problems/find-the-distance-value-between-two-arrays/) | Sorting, Binary Search | O(n log n) Time, O(1) Space| Easy|
|354 | [Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/) | Sorting, Binary Search | Time: O(n log n), Space: O(n)| Hard|
| 1356 | [📓 Sort Integers by The Number of 1 Bits](1356.ipynb) | <span title="Precompute popcount for each element once, then sort by (popcount, value) as a composite key.">Precomputed Popcount + Stable Sort</span> | O(n log n) Time, O(n) Space| Medium|
| 1387 | [Sort Integers by The Number of 1 Bits](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/) | Sorting, Bit Manipulation| O(n log n) Time, O(n) Space| Medium|
| 1417 | [Rearrange the Array to Maximize Prefix Score](https://leetcode.com/problems/rearrange-the-array-to-maximize-prefix-score/) | Sorting, Greedy| O(n log n) Time, O(n) Space| Medium|
|857 | [Minimum Cost to Hire K Workers](https://leetcode.com/problems/minimum-cost-to-hire-k-workers/) | Sorting, Greedy| Time: O(n log n), Space: O(n)| Hard|
| 1122 | [Relative Sort Array](https://leetcode.com/problems/relative-sort-array/) | Sorting, Hash Map| Time: O(n log n), Space: O(n)| Easy|
|791 | [Custom Sort String](https://leetcode.com/problems/custom-sort-string/) | Sorting, Hash Map| Time: O(n log n), Space: O(n)| Medium|
| 1331 | [Rank Transform of an Array](https://leetcode.com/problems/rank-transform-of-an-array/) | Sorting, HashMap | O(n log n) Time, O(n) Space| Easy|
| 1366 | [Rank Teams by Votes](https://leetcode.com/problems/rank-teams-by-votes/) | Sorting, HashMap | O(n log n) Time, O(n) Space| Medium|
| 1407 | [Rank Teams by Votes](https://leetcode.com/problems/rank-teams-by-votes/) | Sorting, HashMap | O(n log n) Time, O(n) Space| Medium|
| 1465 | [Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts](https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/) | Sorting, Math| O(n log n) Time, O(1) Space| Medium|
|891 | [Sum of Subsequence Widths](https://leetcode.com/problems/sum-of-subsequence-widths/) | Sorting, Math| Time: O(n log n), Space: O(n)| Hard|
|912 | [Sort an Array](https://leetcode.com/problems/sort-an-array/) | Sorting, Quick Sort| Time: O(n log n), Space: O(1)| Medium|
|853 | [Car Fleet](https://leetcode.com/problems/car-fleet/) | Sorting, Stack | Time: O(n log n), Space: O(n)| Medium|
|969 | [Pancake Sorting](https://leetcode.com/problems/pancake-sorting/) | Sorting, Stack | Time: O(n^2), Space: O(n)| Medium|
| 1370 | [Increasing Decreasing String](https://leetcode.com/problems/increasing-decreasing-string/) | Sorting, String| O(n log n) Time, O(n) Space| Easy|
|937 | [Reorder Data in Log Files](https://leetcode.com/problems/reorder-data-in-log-files/) | Sorting, String| Time: O(n log n), Space: O(1)| Medium|
| 1433 | [Check If a String Can Break Another String](https://leetcode.com/problems/check-if-a-string-can-break-another-string/) | Sorting, String| O(n log n) Time, O(n) Space| Medium|
|611 | [Valid Triangle Number](https://leetcode.com/problems/valid-triangle-number/) | Sorting, Two Pointer | Time: O(n^2), Space: O(1)| Medium|
| 15 | [📓 3Sum](0015.ipynb) | <span title="Sort first, then use two pointers to find pairs or triplets in a single sweep.">Sorting, Two Pointers</span> | Time: O(n^2), Space: O(1)| Medium|
| 16 | [📓 3Sum Closest](0016.ipynb) | <span title="Sort first, then use two pointers to find pairs or triplets in a single sweep.">Sorting, Two Pointers</span> | Time: O(n^2), Space: O(1)| Medium|
| 18 | [📓 4Sum](0018.ipynb) | <span title="Sort first, then use two pointers to find pairs or triplets in a single sweep.">Sorting, Two Pointers</span> | Time: O(n^3), Space: O(1)| Medium|
| 75 | [Sort Colors](https://leetcode.com/problems/sort-colors/) | Sorting, Two Pointers| Time: O(n), Space: O(1)| Medium|
|259 | [3Sum Smaller](https://leetcode.com/problems/3sum-smaller/) | Sorting, Two Pointers| Time: O(n^2), Space: O(1)| Medium|
|280 | [Wiggle Sort](https://leetcode.com/problems/wiggle-sort/) | Sorting, Two Pointers| Time: O(n log n), Space: O(1)| Medium|
|324 | [Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/) | Sorting, Two Pointers| Time: O(n log n), Space: O(n)| Medium|
|982 | [Triples with Sum Less Than Target](https://leetcode.com/problems/triples-with-sum-less-than-target/) | Sorting, Two Pointers| Time: O(n^2), Space: O(1)| Medium|
|870 | [Advantage Shuffle](https://leetcode.com/problems/advantage-shuffle/) | Sorting, Two Pointers| Time: O(n log n), Space: O(n)| Hard|

## SQL
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|175 | [Combine Two Tables](https://leetcode.com/problems/combine-two-tables/) | SQL| Time: O(1), Space: O(1)| Easy|
|176 | [Second Highest Salary](https://leetcode.com/problems/second-highest-salary/) | SQL| Time: O(1), Space: O(1)| Easy|
|181 | [Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/) | SQL| Time: O(1), Space: O(1)| Easy|
|182 | [Duplicate Emails](https://leetcode.com/problems/duplicate-emails/) | SQL| Time: O(1), Space: O(1)| Easy|
|183 | [Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order/) | SQL| Time: O(1), Space: O(1)| Easy|
|184 | [Department Highest Salary](https://leetcode.com/problems/department-highest-salary/) | SQL| Time: O(1), Space: O(1)| Easy|
|192 | [Word Frequency](https://leetcode.com/problems/word-frequency/) | SQL| Time: O(1), Space: O(1)| Easy|
|196 | [Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails/) | SQL| Time: O(1), Space: O(1)| Easy|
|197 | [Rising Temperature](https://leetcode.com/problems/rising-temperature/) | SQL| Time: O(1), Space: O(1)| Easy|
|570 | [Managers with at Least 5 Direct Reports](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/) | SQL| Time: O(n), Space: O(1)| Easy|
|577 | [Employee Bonus](https://leetcode.com/problems/employee-bonus/) | SQL| Time: O(n), Space: O(1)| Easy|
|578 | [Get Highest Answer Rate Question](https://leetcode.com/problems/get-highest-answer-rate-question/) | SQL| Time: O(n), Space: O(1)| Easy|
|585 | [Investments in 2016](https://leetcode.com/problems/investments-in-2016/) | SQL| Time: O(n), Space: O(1)| Easy|
|595 | [Big Countries](https://leetcode.com/problems/big-countries/) | SQL| Time: O(n), Space: O(1)| Easy|
|596 | [Classes More Than 5 Students](https://leetcode.com/problems/classes-more-than-5-students/) | SQL| Time: O(n), Space: O(1)| Easy|
|597 | [Friend Requests I: Overall Acceptance Rate](https://leetcode.com/problems/friend-requests-i-overall-acceptance-rate/)| SQL| Time: O(n), Space: O(1)| Easy|
|618 | [Students Reporting Results](https://leetcode.com/problems/students-reporting-results/) | SQL| Time: O(n), Space: O(1)| Easy|
|620 | [Not Boring Movies](https://leetcode.com/problems/not-boring-movies/) | SQL| Time: O(n), Space: O(1)| Easy|
|626 | [Exchange Seats](https://leetcode.com/problems/exchange-seats/) | SQL| Time: O(n), Space: O(1)| Easy|
|627 | [Swap Salary](https://leetcode.com/problems/swap-salary/) | SQL| Time: O(1), Space: O(1)| Easy|
| 1141 | [User Activity for the Past 30 Days I](https://leetcode.com/problems/user-activity-for-the-past-30-days-i/) | SQL| Time: O(n), Space: O(n)| Easy|
| 1148 | [Article Views I](https://leetcode.com/problems/article-views-i/) | SQL| Time: O(n), Space: O(n)| Easy|
| 1179 | [Reformat Department Table](https://leetcode.com/problems/reformat-department-table/) | SQL| O(n) Time, O(n) Space| Easy|
| 1378 | [Replace Employee ID in a Table](https://leetcode.com/problems/replace-employee-id-in-a-table/) | SQL| O(1) Time, O(1) Space| Easy|
|177 | [Nth Highest Salary](https://leetcode.com/problems/nth-highest-salary/) | SQL| Time: O(1), Space: O(1)| Medium|
|178 | [Rank Scores](https://leetcode.com/problems/rank-scores/) | SQL| Time: O(1), Space: O(1)| Medium|
|180 | [Consecutive Numbers](https://leetcode.com/problems/consecutive-numbers/) | SQL| Time: O(1), Space: O(1)| Medium|
|262 | [Trips and Users](https://leetcode.com/problems/trips-and-users/) | SQL| Time: O(1), Space: O(1)| Medium|
|579 | [Find Cumulative Salary of an Employee](https://leetcode.com/problems/find-cumulative-salary-of-an-employee/) | SQL| Time: O(n), Space: O(1)| Medium|
|584 | [Find Customer Referee](https://leetcode.com/problems/find-customer-referee/) | SQL| Time: O(n), Space: O(1)| Medium|
|586 | [Customer Placing the Largest Number of Orders](https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/) | SQL| Time: O(n), Space: O(1)| Medium|
|607 | [Sales Person](https://leetcode.com/problems/sales-person/) | SQL| Time: O(n), Space: O(1)| Medium|
|631 | [Design Excel Sum Formula](https://leetcode.com/problems/design-excel-sum-formula/) | SQL| Time: O(n), Space: O(1)| Medium|
| 1142 | [User Activity for the Past 30 Days II](https://leetcode.com/problems/user-activity-for-the-past-30-days-ii/) | SQL| Time: O(n), Space: O(n)| Medium|
| 1149 | [Article Views II](https://leetcode.com/problems/article-views-ii/) | SQL| Time: O(n), Space: O(n)| Medium|
| 1152 | [Analyzing User Website Visit Pattern](https://leetcode.com/problems/analyzing-user-website-visit-pattern/) | SQL| Time: O(n), Space: O(n)| Medium|
|185 | [Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries/) | SQL| Time: O(1), Space: O(1)| Hard|

## Stack
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
| 20 | [📓 Valid Parentheses](0020.ipynb) | <span title="LIFO structure; push on open events, pop and process on close events.">Stack</span> | Time: O(n), Space: O(n)| Easy|
|155 | [Min Stack](https://leetcode.com/problems/min-stack/) | Stack| Time: O(1), Space: O(n)| Easy|
|232 | [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) | Stack| Time: O(1), Space: O(n)| Easy|
|496 | [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) | Stack| Time: O(n), Space: O(n)| Easy|
|682 | [Baseball Game](https://leetcode.com/problems/baseball-game/) | Stack| Time: O(n), Space: O(n)| Easy|
| 71 | [Simplify Path](https://leetcode.com/problems/simplify-path/) | Stack| Time: O(n), Space: O(n)| Medium|
|150 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Stack| Time: O(n), Space: O(n)| Medium|
|227 | [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/) | Stack| Time: O(n), Space: O(n)| Medium|
|255 | [Verify Preorder Serialization of a Binary Tree](https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/) | Stack| Time: O(n), Space: O(n)| Medium|
|331 | [Verify Preorder Serialization of a Binary Tree](https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/) | Stack| Time: O(n), Space: O(n)| Medium|
|385 | [Mini Parser](https://leetcode.com/problems/mini-parser/) | Stack| Time: O(n), Space: O(n)| Medium|
|388 | [Longest Absolute File Path](https://leetcode.com/problems/longest-absolute-file-path/) | Stack| Time: O(n), Space: O(n)| Medium|
|394 | [Decode String](https://leetcode.com/problems/decode-string/) | Stack| Time: O(n), Space: O(n)| Medium|
|402 | [Remove K Digits](https://leetcode.com/problems/remove-k-digits/) | Stack| Time: O(n), Space: O(n)| Medium|
|439 | [Ternary Expression Parser](https://leetcode.com/problems/ternary-expression-parser/) | Stack| Time: O(n), Space: O(n)| Medium|
|456 | [132 Pattern](https://leetcode.com/problems/132-pattern/) | Stack| Time: O(n), Space: O(n)| Medium|
|503 | [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) | Stack| O(N) Time, O(N) Space| Medium|
|636 | [Exclusive Time of Functions](https://leetcode.com/problems/exclusive-time-of-functions/) | Stack| Time: O(n), Space: O(n)| Medium|
|735 | [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/) | Stack| Time: O(n), Space: O(n)| Medium|
|739 | [Daily Temperature](https://leetcode.com/problems/daily-temperature/) | Stack| Time: O(n), Space: O(n)| Medium|
|856 | [Score of Parentheses](https://leetcode.com/problems/score-of-parentheses/) | Stack| Time: O(n), Space: O(n)| Medium|
|901 | [Online Stock Span](https://leetcode.com/problems/online-stock-span/) | Stack| Time: O(1), Space: O(n)| Medium|
|946 | [Validate Stack Sequences](https://leetcode.com/problems/validate-stack-sequences/) | Stack| Time: O(n), Space: O(n)| Medium|
|962 | [Maximum Width Ramp](https://leetcode.com/problems/maximum-width-ramp/) | Stack| Time: O(n), Space: O(n)| Medium|
| 1003 | [Check If Word Is Valid After Substitutions](https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/) | Stack| Time: O(n), Space: O(n)| Medium|
| 1019 | [Next Greater Node In Linked List](https://leetcode.com/problems/next-greater-node-in-linked-list/) | Stack| Time: O(n), Space: O(n)| Medium|
| 1047 | [Remove All Adjacent Duplicates In String II](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/) | Stack| Time: O(n), Space: O(n)| Medium|
| 84 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Stack| Time: O(n), Space: O(n)| Hard|
|224 | [Basic Calculator](https://leetcode.com/problems/basic-calculator/) | Stack| Time: O(n), Space: O(n)| Hard|
|591 | [Tag Validator](https://leetcode.com/problems/tag-validator/) | Stack| Time: O(n), Space: O(n)| Hard|
|716 | [Max Stack](https://leetcode.com/problems/max-stack/) | Stack| Time: O(1), Space: O(n)| Hard|
|736 | [Parse Lisp Expression](https://leetcode.com/problems/parse-lisp-expression/) | Stack| Time: O(n), Space: O(n)| Hard|
| 1441 | [Build an Array With Stack Operations](https://leetcode.com/problems/build-an-array-with-stack-operations/) | Stack, Array | O(n) Time, O(n) Space| Easy|
| 1475 | [Final Price with a Special Discount in a Shop](https://leetcode.com/problems/final-price-with-a-special-discount-in-a-shop/) | Stack, Array | O(n) Time, O(n) Space| Easy|
| 1188 | [Design a Stack With Increment Operation](https://leetcode.com/problems/design-a-stack-with-increment-operation/) | Stack, Array | O(1) Time, O(n) Space| Medium|
| 1310 | [Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/) | Stack, Array | O(n) Time, O(n) Space| Medium|
| 1381 | [Design a Stack With Increment Operation](https://leetcode.com/problems/design-a-stack-with-increment-operation/) | Stack, Array | O(1) Time, O(n) Space| Medium|
|907 | [Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/) | Stack, DP| Time: O(n), Space: O(n)| Medium|
| 32 | [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/) | Stack, Dynamic Programming | Time: O(n), Space: O(n)| Hard|
| 1489 | [Find the Most Competitive Subsequence](https://leetcode.com/problems/find-the-most-competitive-subsequence/) | Stack, Greedy| O(n) Time, O(n) Space| Medium|
|316 | [Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/) | Stack, Greedy| Time: O(n), Space: O(n)| Hard|
|895 | [Maximum Frequency Stack](https://leetcode.com/problems/maximum-frequency-stack/) | Stack, Hash Map| Time: O(1), Space: O(n)| Hard|
| 1265 | [Print Immutable Linked List in Reverse](https://leetcode.com/problems/print-immutable-linked-list-in-reverse/) | Stack, Linked List | O(n) Time, O(n) Space| Medium|
| 1472 | [Design Browser History](https://leetcode.com/problems/design-browser-history/) | Stack, Linked List | O(1) Time, O(n) Space| Medium|
| 1172 | [Dinner Plate Stacks](https://leetcode.com/problems/dinner-plate-stacks/) | Stack, Priority Queue| O(log n) Time, O(n) Space| Hard|
|341 | [Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/) | Stack, Recursion | Time: O(n), Space: O(n)| Medium|
| 1440 | [Evaluate Boolean Expression](https://leetcode.com/problems/evaluate-boolean-expression/) | Stack, Recursion | O(n) Time, O(n) Space| Medium|
|770 | [Basic Calculator IV](https://leetcode.com/problems/basic-calculator-iv/) | Stack, Recursion | Time: O(n), Space: O(n)| Hard|
|772 | [Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/) | Stack, Recursion | Time: O(n), Space: O(n)| Hard|
| 1499 | [Max Value of Equation](https://leetcode.com/problems/max-value-of-equation/) | Stack, Sliding Window| O(n) Time, O(n) Space| Medium|
|844 | [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/) | Stack, String| Time: O(n), Space: O(n)| Easy|
|921 | [Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/) | Stack, String| Time: O(n), Space: O(1)| Easy|
|678 | [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) | Stack, String| Time: O(n), Space: O(n)| Medium|
| 1106 | [Parsing A Boolean Expression](https://leetcode.com/problems/parsing-a-boolean-expression/) | Stack, String| Time: O(n), Space: O(n)| Medium|
| 1190 | [Reverse Substrings Between Each Pair of Parentheses](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/) | Stack, String| O(n) Time, O(n) Space| Medium|
| 1209 | [Remove All Adjacent Duplicates in String II](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/) | Stack, String| O(n) Time, O(n) Space| Medium|
| 1249 | [Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/) | Stack, String| O(n) Time, O(n) Space| Medium|

## String
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|8 | [📓 String to Integer (atoi)](0008.ipynb) | <span title="Character-by-character scan or two-pointer technique on the raw string.">String</span> | Time: O(n), Space: O(1)| Easy|
| 14 | [📓 Longest Common Prefix](0014.ipynb) | <span title="Character-by-character scan or two-pointer technique on the raw string.">String</span> | Time: O(n * m), Space: O(1)| Easy|
| 28 | [Implement strStr()](https://leetcode.com/problems/implement-strstr/) | String | Time: O(n), Space: O(1)| Easy|
| 38 | [Count and Say](https://leetcode.com/problems/count-and-say/) | String | Time: O(n), Space: O(1)| Easy|
| 58 | [Length of Last Word](https://leetcode.com/problems/length-of-last-word/) | String | Time: O(n), Space: O(1)| Easy|
| 67 | [Add Binary](https://leetcode.com/problems/add-binary/) | String | Time: O(max(m, n)), Space: O(max(m, n))| Easy|
|125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | String | Time: O(n), Space: O(1)| Easy|
|157 | [Read N Characters Given Read4](https://leetcode.com/problems/read-n-characters-given-read4/) | String | Time: O(n), Space: O(1)| Easy|
|246 | [Strobogrammatic Number](https://leetcode.com/problems/strobogrammatic-number/) | String | Time: O(n), Space: O(1)| Easy|
|408 | [Valid Word Abbreviation](https://leetcode.com/problems/valid-word-abbreviation/) | String | Time: O(n), Space: O(1)| Easy|
|415 | [Add Strings](https://leetcode.com/problems/add-strings/) | String | Time: O(n), Space: O(1)| Easy|
|434 | [Number of Segments in a String](https://leetcode.com/problems/number-of-segments-in-a-string/) | String | Time: O(n), Space: O(1)| Easy|
|459 | [Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/) | String | Time: O(n), Space: O(1)| Easy|
|482 | [License Key Formatting](https://leetcode.com/problems/license-key-formatting/) | String | Time: O(n), Space: O(1)| Easy|
|500 | [Keyboard Row](https://leetcode.com/problems/keyboard-row/) | String | Time: O(n), Space: O(1)| Easy|
|520 | [Detect Capital](https://leetcode.com/problems/detect-capital/) | String | Time: O(n), Space: O(1)| Easy|
|521 | [Longest Uncommon Subsequence I](https://leetcode.com/problems/longest-uncommon-subsequence-i/) | String | Time: O(n), Space: O(1)| Easy|
|541 | [Reverse String II](https://leetcode.com/problems/reverse-string-ii/) | String | Time: O(n), Space: O(n)| Easy|
|551 | [Student Attendance Record I](https://leetcode.com/problems/student-attendance-record-i/) | String | Time: O(n), Space: O(1)| Easy|
|557 | [Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/) | String | Time: O(n), Space: O(n)| Easy|
|657 | [Judge Route Circle](https://leetcode.com/problems/judge-route-circle/) | String | Time: O(n), Space: O(1)| Easy|
|680 | [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) | String | Time: O(n), Space: O(1)| Easy|
|686 | [Repeated String Match](https://leetcode.com/problems/repeated-string-match/) | String | Time: O(n), Space: O(1)| Easy|
|709 | [To Lower Case](https://leetcode.com/problems/to-lower-case/) | String | Time: O(n), Space: O(1)| Easy|
|824 | [Goat Latin](https://leetcode.com/problems/goat-latin/) | String | Time: O(n), Space: O(1)| Easy|
|925 | [Long Pressed Name](https://leetcode.com/problems/long-pressed-name/) | String | Time: O(n), Space: O(1)| Easy|
|953 | [Verifying an Alien Dictionary](https://leetcode.com/problems/verifying-an-alien-dictionary/) | String | Time: O(n), Space: O(1)| Easy|
| 1002 | [Find Common Characters](https://leetcode.com/problems/find-common-characters/) | String | Time: O(n), Space: O(1)| Easy|
| 1021 | [Remove Outermost Parentheses](https://leetcode.com/problems/remove-outermost-parentheses/) | String | Time: O(n), Space: O(1)| Easy|
| 1119 | [Remove Vowels from a String](https://leetcode.com/problems/remove-vowels-from-a-string/) | String | Time: O(n), Space: O(1)| Easy|
| 1221 | [Split a String in Balanced Strings](https://leetcode.com/problems/split-a-string-in-balanced-strings/) | String | O(n) Time, O(1) Space| Easy|
| 43 | [Multiply Strings](https://leetcode.com/problems/multiply-strings/) | String | Time: O(m * n), Space: O(m + n)| Medium|
|151 | [Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/) | String | Time: O(n), Space: O(1)| Medium|
|158 | [Read N Characters Given Read4 II - Call multiple times](https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/) | String | Time: O(n), Space: O(1)| Medium|
|161 | [One Edit Distance](https://leetcode.com/problems/one-edit-distance/) | String | Time: O(m * n), Space: O(1)| Medium|
|165 | [Compare Version Numbers](https://leetcode.com/problems/compare-version-numbers/) | String | Time: O(n), Space: O(1)| Medium|
|186 | [Reverse Words in a String II](https://leetcode.com/problems/reverse-words-in-a-string-ii/) | String | Time: O(n), Space: O(1)| Medium|
|247 | [Strobogrammatic Number II](https://leetcode.com/problems/strobogrammatic-number-ii/) | String | Time: O(n), Space: O(1)| Medium|
|271 | [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) | String | Time: O(n), Space: O(n)| Medium|
|468 | [Validate IP Address](https://leetcode.com/problems/validate-ip-address/) | String | Time: O(1), Space: O(1)| Medium|
|522 | [Longest Uncommon Subsequence II](https://leetcode.com/problems/longest-uncommon-subsequence-ii/) | String | Time: O(n^2), Space: O(n^2)| Medium|
|537 | [Complex Number Multiplication](https://leetcode.com/problems/complex-number-multiplication/) | String | Time: O(1), Space: O(1)| Medium|
|544 | [Output Contest Matches](https://leetcode.com/problems/output-contest-matches/) | String | Time: O(n log n), Space: O(n)| Medium|
|722 | [Remove Comments](https://leetcode.com/problems/remove-comments/) | String | Time: O(n), Space: O(1)| Medium|
|816 | [Ambiguous Coordinates](https://leetcode.com/problems/ambiguous-coordinates/) | String | Time: O(n^3), Space: O(n^3)| Medium|
|831 | [Masking Personal Information](https://leetcode.com/problems/masking-personal-information/) | String | Time: O(n), Space: O(1)| Medium|
|984 | [String Without AAA or BBB](https://leetcode.com/problems/string-without-aaa-or-bbb/) | String | Time: O(n), Space: O(1)| Medium|
| 1018 | [Binary Prefix Divisible By 5](https://leetcode.com/problems/binary-prefix-divisible-by-5/) | String | Time: O(n), Space: O(1)| Medium|
| 1088 | [Validate IP Address](https://leetcode.com/problems/validate-ip-address/) | String | Time: O(1), Space: O(1)| Medium|
| 1153 | [A Fancy String](https://leetcode.com/problems/a-fancy-string/) | String | Time: O(n), Space: O(1)| Medium|
| 1324 | [Print Words Vertically](https://leetcode.com/problems/print-words-vertically/) | String | O(n) Time, O(n) Space| Medium|
| 1328 | [Break a Palindrome](https://leetcode.com/problems/break-a-palindrome/) | String | O(n) Time, O(n) Space| Medium|
| 1332 | [Remove Palindromic Subsequences](https://leetcode.com/problems/remove-palindromic-subsequences/) | String | O(n) Time, O(1) Space| Medium|
| 68 | [Text Justification](https://leetcode.com/problems/text-justification/) | String | Time: O(n), Space: O(n)| Hard|
|248 | [Strobogrammatic Number III](https://leetcode.com/problems/strobogrammatic-number-iii/) | String | Time: O(n), Space: O(1)| Hard|
|527 | [Word Abbreviation](https://leetcode.com/problems/word-abbreviation/) | String | Time: O(n), Space: O(n)| Hard|
|555 | [Split Concatenated Strings](https://leetcode.com/problems/split-concatenated-strings/) | String | Time: O(n), Space: O(n)| Hard|
| 1096 | [Brace Expansion II](https://leetcode.com/problems/brace-expansion-ii/) | String | Time: O(n!), Space: O(n) | Hard|
|796 | [Rotate String](https://leetcode.com/problems/rotate-string/) | String, Array| Time: O(n), Space: O(1)| Easy|
|830 | [Positions of Large Groups](https://leetcode.com/problems/positions-of-large-groups/) | String, Array| Time: O(n), Space: O(1)| Easy|
|943 | [Shortest Distance to a Character](https://leetcode.com/problems/shortest-distance-to-a-character/) | String, Array| Time: O(n), Space: O(1)| Easy|
| 1189 | [Maximum Number of Words Found in Sentences](https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/) | String, Array| O(n) Time, O(1) Space| Easy|
| 1455 | [Check If a Word Occurs As a Prefix of Any Word in a Sentence](https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/) | String, Array| O(n) Time, O(1) Space| Easy|
|6 | [📓 Zigzag Conversion](0006.ipynb) | <span title="Combined string and array manipulation — typically build/compare character frequency counts.">String, Array</span> | Time: O(n), Space: O(n)| Medium|
| 1023 | [Camelcase Matching](https://leetcode.com/problems/camelcase-matching/) | String, Array| Time: O(n), Space: O(1)| Medium|
|306 | [Additive Number](https://leetcode.com/problems/additive-number/) | String, Backtracking | Time: O(n^3), Space: O(1)| Medium|
| 1316 | [Distinguishable Palindrome](https://leetcode.com/problems/distinguishable-palindrome/) | String, Backtracking | O(n!) Time, O(n) Space | Hard|
| 1044 | [Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/) | String, Binary Search, Hashing | Time: O(n log n), Space: O(n)| Hard|
| 1213 | [Split a String into Balanced Strings](https://leetcode.com/problems/split-a-string-into-balanced-strings/) | String, Count| O(n) Time, O(1) Space| Easy|
|696 | [Count Binary Substrings](https://leetcode.com/problems/count-binary-substrings/) | String, Counting | Time: O(n), Space: O(1)| Medium|
|467 | [Unique Substrings in Wraparound String](https://leetcode.com/problems/unique-substrings-in-wraparound-string/) | String, Dynamic Programming| Time: O(n), Space: O(1)| Medium|
|616 | [Add Bold Tag in String](https://leetcode.com/problems/add-bold-tag-in-string/) | String, Dynamic Programming| Time: O(n), Space: O(n)| Medium|
| 1435 | [Check if a string contains a valid palindrome](https://leetcode.com/problems/check-if-a-string-contains-a-valid-palindrome/) | String, Dynamic Programming| O(n^2) Time, O(n) Space| Medium|
| 1236 | [String Compression II](https://leetcode.com/problems/string-compression-ii/) | String, Dynamic Programming| O(n) Time, O(n) Space| Hard|
|843 | [Guess the Word](https://leetcode.com/problems/guess-the-word/) | String, Game Theory| Time: O(n^2), Space: O(1)| Hard|
| 1422 | [Maximum Score After Splitting a String](https://leetcode.com/problems/maximum-score-after-splitting-a-string/) | String, Greedy | O(n) Time, O(1) Space| Easy|
|205 | [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/) | String, Hash Map | Time: O(n), Space: O(n)| Easy|
|819 | [Most Common Word](https://leetcode.com/problems/most-common-word/) | String, Hash Map | Time: O(n), Space: O(n)| Easy|
|748 | [Shortest Completing Word](https://leetcode.com/problems/shortest-completing-word/) | String, Hash Map | Time: O(n), Space: O(n)| Medium|
|833 | [Find And Replace in String](https://leetcode.com/problems/find-and-replace-in-string/) | String, Hash Map | Time: O(n), Space: O(n)| Medium|
|859 | [Buddy Strings](https://leetcode.com/problems/buddy-strings/) | String, Hash Set | Time: O(n), Space: O(n)| Easy|
|929 | [Unique Email Addresses](https://leetcode.com/problems/unique-email-addresses/) | String, Hash Set | Time: O(n), Space: O(n)| Easy|
|758 | [Bold Words in String](https://leetcode.com/problems/bold-words-in-string/) | String, Hash Set | Time: O(n), Space: O(n)| Medium|
|893 | [Groups of Special-Equivalent Strings](https://leetcode.com/problems/groups-of-special-equivalent-strings/) | String, Hash Set | Time: O(n), Space: O(n)| Medium|
|966 | [Vowel Spellchecker](https://leetcode.com/problems/vowel-spellchecker/) | String, Hash Set | Time: O(n), Space: O(n)| Medium|
| 1165 | [Single-Row Keyboard](https://leetcode.com/problems/single-row-keyboard/) | String, HashMap| O(n) Time, O(1) Space| Easy|
| 1170 | [Compare Strings by Frequency of the Smallest Character](https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/) | String, HashMap| O(n) Time, O(n) Space| Easy|
| 1180 | [Count Substrings with Only One Distinct Letter](https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/) | String, HashMap| O(n) Time, O(n) Space| Easy|
| 1156 | [Swap For Longest Repeated Character Substring](https://leetcode.com/problems/swap-for-longest-repeated-character-substring/) | String, HashMap| O(n) Time, O(n) Space| Medium|
| 1177 | [Can Make Palindrome from Substring](https://leetcode.com/problems/can-make-palindrome-from-substring/) | String, HashMap| O(n) Time, O(n) Space| Medium|
| 1181 | [Before and After Puzzle](https://leetcode.com/problems/before-and-after-puzzle/) | String, HashMap| O(n) Time, O(n) Space| Medium|
|604 | [Design Compressed String Iterator](https://leetcode.com/problems/design-compressed-string-iterator/) | String, Iterator | Time: O(1), Space: O(1)| Easy|
| 1392 | [Longest Happy Prefix](https://leetcode.com/problems/longest-happy-prefix/) | String, KMP| O(n) Time, O(n) Space| Hard|
|214 | [Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/) | String, KMP Algorithm| Time: O(n), Space: O(n)| Hard|
|800 | [Similar RGB Color](https://leetcode.com/problems/similar-rgb-color/) | String, Math | Time: O(1), Space: O(1)| Easy|
| 1374 | [Generate a String With Characters That Have Odd Counts](https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/) | String, Math | O(n) Time, O(n) Space| Easy|
|761 | [Special Binary String](https://leetcode.com/problems/special-binary-string/) | String, Recursion| Time: O(n), Space: O(n)| Medium|
|880 | [Decoded String at Index](https://leetcode.com/problems/decoded-string-at-index/) | String, Simulation | Time: O(n), Space: O(1)| Medium|
| 1258 | [Synonym, Sort](https://leetcode.com/problems/synonym-sort/)| String, Sorting| O(n log n) Time, O(n) Space| Medium|
| 1451 | [Rearrange Words in a Sentence](https://leetcode.com/problems/rearrange-words-in-a-sentence/) | String, Sorting| O(n log n) Time, O(n) Space| Medium|
|899 | [Orderly Queue](https://leetcode.com/problems/orderly-queue/) | String, Sorting| Time: O(n log n), Space: O(n)| Hard|
| 1410 | [HTML Entity Parser](https://leetcode.com/problems/html-entity-parser/) | String, Stack| O(n) Time, O(n) Space| Easy|
| 1163 | [Last Substring in Lexicographical Order](https://leetcode.com/problems/last-substring-in-lexicographical-order/) | String, Stack| O(n) Time, O(1) Space| Hard|
|809 | [Expressive Words](https://leetcode.com/problems/expressive-words/) | String, Trie | Time: O(n), Space: O(n)| Medium|
|917 | [Reverse Only Letters](https://leetcode.com/problems/reverse-only-letters/) | String, Two Pointers | Time: O(n), Space: O(1)| Easy|

## Sweep Line
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|391 | [Perfect Rectangle](https://leetcode.com/problems/perfect-rectangle/) | Sweep Line | Time: O(n log n), Space: O(n)| Hard|

## Topological Sort
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|444 | [Sequence Reconstruction](https://leetcode.com/problems/sequence-reconstruction/) | Topological Sort | Time: O(n), Space: O(n)| Medium|

## Tree
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|226 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Tree | Time: O(n), Space: O(h)| Easy|
|404 | [Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves/) | Tree | Time: O(n), Space: O(h)| Easy|
|222 | [Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/) | Tree | Time: O(log^2 n), Space: O(log n)| Medium|
|285 | [Inorder Successor in BST](https://leetcode.com/problems/inorder-successor-in-bst/) | Tree | Time: O(h), Space: O(1)| Medium|
|431 | [Encode N-ary Tree to Binary Tree](https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/) | Tree | Time: O(n), Space: O(n)| Medium|
|450 | [Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/) | Tree | Time: O(h), Space: O(h)| Medium|
|654 | [Maximum Binary Tree](https://leetcode.com/problems/maximum-binary-tree/) | Tree | Time: O(n), Space: O(n)| Medium|
|655 | [Print Binary Tree](https://leetcode.com/problems/print-binary-tree/) | Tree | Time: O(n), Space: O(n)| Medium|
|663 | [Equal Tree Partition](https://leetcode.com/problems/equal-tree-partition/) | Tree | Time: O(n), Space: O(n)| Medium|
|666 | [Path Sum IV](https://leetcode.com/problems/path-sum-iv/) | Tree | Time: O(n), Space: O(n)| Medium|
|669 | [Trim a Binary Search Tree](https://leetcode.com/problems/trim-a-binary-search-tree/) | Tree | Time: O(n), Space: O(h)| Medium|
|671 | [Second Minimum Node In a Binary Tree](https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/) | Tree | Time: O(n), Space: O(n)| Medium|
|687 | [Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/) | Tree | Time: O(n), Space: O(h)| Medium|
|776 | [Split BST](https://leetcode.com/problems/split-bst/) | Tree | Time: O(h), Space: O(h)| Medium|
|783 | [Minimum Distance Between BST Nodes](https://leetcode.com/problems/minimum-distance-between-bst-nodes/) | Tree | Time: O(n), Space: O(n)| Medium|
|998 | [Maximum Binary Tree II](https://leetcode.com/problems/maximum-binary-tree-ii/) | Tree | Time: O(n), Space: O(n)| Medium|
|559 | [Maximum Depth of N-ary Tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/) | Tree (DFS) | Time: O(n), Space: O(n)| Easy|
|590 | [N-ary Tree Postorder Traversal](https://leetcode.com/problems/n-ary-tree-postorder-traversal/) | Tree (Postorder) | Time: O(n), Space: O(n)| Easy|
|589 | [N-ary Tree Preorder Traversal](https://leetcode.com/problems/n-ary-tree-preorder-traversal/) | Tree (Preorder)| Time: O(n), Space: O(n)| Easy|
|102 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Tree, BFS| Time: O(n), Space: O(n)| Medium|
|103 | [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) | Tree, BFS| Time: O(n), Space: O(n)| Medium|
|107 | [Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/) | Tree, BFS| Time: O(n), Space: O(n)| Medium|
|116 | [Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/) | Tree, BFS| Time: O(n), Space: O(1)| Medium|
|117 | [Populating Next Right Pointers in Each Node II](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/) | Tree, BFS| Time: O(n), Space: O(1)| Medium|
|199 | [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | Tree, BFS| Time: O(n), Space: O(n)| Medium|
|314 | [Binary Tree Vertical Order Traversal](https://leetcode.com/problems/binary-tree-vertical-order-traversal/) | Tree, BFS| Time: O(n log n), Space: O(n)| Medium|
|662 | [Maximum Width of Binary Tree](https://leetcode.com/problems/maximum-width-of-binary-tree/) | Tree, BFS| Time: O(n), Space: O(n)| Medium|
|958 | [Check Completeness of a Binary Tree](https://leetcode.com/problems/check-completeness-of-a-binary-tree/) | Tree, BFS| Time: O(n), Space: O(n)| Medium|
| 1104 | [Path In Zigzag Labelled Binary Tree](https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/) | Tree, BFS| Time: O(log n), Space: O(log n)| Medium|
| 1302 | [Deepest Leaves Sum](https://leetcode.com/problems/deepest-leaves-sum/) | Tree, BFS| O(n) Time, O(n) Space| Medium|
|272 | [Closest Binary Search Tree Value II](https://leetcode.com/problems/closest-binary-search-tree-value-ii/) | Tree, BFS| Time: O(h + k), Space: O(h)| Hard|
|987 | [Vertical Order Traversal of a Binary Tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/) | Tree, BFS| Time: O(n log n), Space: O(n)| Hard|
|993 | [Cousins in Binary Tree](https://leetcode.com/problems/cousins-in-binary-tree/) | Tree, BFS, DFS | Time: O(n), Space: O(n)| Easy|
|742 | [Closest Leaf in a Binary Tree](https://leetcode.com/problems/closest-leaf-in-a-binary-tree/) | Tree, BFS, DFS | Time: O(n), Space: O(n)| Medium|
| 1376 | [Time Needed to Inform All Employees](https://leetcode.com/problems/time-needed-to-inform-all-employees/) | Tree, BFS, DFS | O(n) Time, O(n) Space| Medium|
| 1261 | [Find Elements in a Contaminated Binary Tree](https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/) | Tree, BFS, HashSet | O(n) Time, O(n) Space| Medium|
|428 | [Serialize and Deserialize N-ary Tree](https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/) | Tree, BFS/DFS| Time: O(n), Space: O(n)| Medium|
|449 | [Serialize and Deserialize BST](https://leetcode.com/problems/serialize-and-deserialize-bst/) | Tree, BFS/DFS| Time: O(n), Space: O(n)| Medium|
|919 | [Complete Binary Tree Inserter](https://leetcode.com/problems/complete-binary-tree-inserter/) | Tree, BST| Time: O(1), Space: O(n)| Medium|
| 1008 | [Construct Binary Search Tree from Preorder Traversal](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/) | Tree, BST| Time: O(n), Space: O(n)| Medium|
| 1110 | [Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/) | Tree, BST| Time: O(log n), Space: O(1)| Medium|
| 1111 | [Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/) | Tree, BST| Time: O(log n), Space: O(1)| Medium|
| 1483 | [Kth Ancestor of a Tree Node](https://leetcode.com/problems/kth-ancestor-of-a-tree-node/) | Tree, Binary Lifting | O(log n) Time, O(n) Space| Hard|
|235 | [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | Tree, Binary Search| Time: O(h), Space: O(1)| Easy|
|270 | [Closest Binary Search Tree Value](https://leetcode.com/problems/closest-binary-search-tree-value/) | Tree, Binary Search| Time: O(h), Space: O(1)| Easy|
|100 | [Same Tree](https://leetcode.com/problems/same-tree/) | Tree, DFS| Time: O(n), Space: O(n)| Easy|
|101 | [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) | Tree, DFS| Time: O(n), Space: O(h)| Easy|
|104 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Tree, DFS| Time: O(n), Space: O(h)| Easy|
|110 | [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | Tree, DFS| Time: O(n), Space: O(h)| Easy|
|111 | [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/) | Tree, DFS| Time: O(n), Space: O(h)| Easy|
|112 | [Path Sum](https://leetcode.com/problems/path-sum/) | Tree, DFS| Time: O(n), Space: O(h)| Easy|
|144 | [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) | Tree, DFS| Time: O(n), Space: O(n)| Easy|
|145 | [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/) | Tree, DFS| Time: O(n), Space: O(n)| Easy|
|257 | [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/) | Tree, DFS| Time: O(n), Space: O(h)| Easy|
|572 | [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) | Tree, DFS| Time: O(n), Space: O(h)| Easy|
|965 | [Univalued Binary Tree](https://leetcode.com/problems/univalued-binary-tree/) | Tree, DFS| Time: O(n), Space: O(n)| Easy|
| 1022 | [Sum of Root To Leaf Binary Numbers](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/) | Tree, DFS| Time: O(n), Space: O(n)| Easy|
| 1026 | [Tree Sister](https://leetcode.com/problems/tree-sister/) | Tree, DFS| Time: O(n), Space: O(n)| Easy|
| 1028 | [Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves/) | Tree, DFS| Time: O(n), Space: O(n)| Easy|
| 1102 | [Path Sum IV](https://leetcode.com/problems/path-sum-iv/) | Tree, DFS| Time: O(n), Space: O(n)| Easy|
| 1315 | [Sum of Nodes with Even-Valued Grandparent](https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/) | Tree, DFS| O(n) Time, O(n) Space| Easy|
| 98 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | Tree, DFS| Time: O(n), Space: O(n)| Medium|
|113 | [Path Sum II](https://leetcode.com/problems/path-sum-ii/) | Tree, DFS| Time: O(n), Space: O(h)| Medium|
|114 | [Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/) | Tree, DFS| Time: O(n), Space: O(h)| Medium|
|129 | [Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/) | Tree, DFS| Time: O(n), Space: O(h)| Medium|
|236 | [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | Tree, DFS| Time: O(n), Space: O(h)| Medium|
|250 | [Count Univalue Subtrees](https://leetcode.com/problems/count-univalue-subtrees/) | Tree, DFS| Time: O(n), Space: O(h)| Medium|
|298 | [Binary Tree Longest Consecutive Sequence](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/) | Tree, DFS| Time: O(n), Space: O(h)| Medium|
|333 | [Largest BST Subtree](https://leetcode.com/problems/largest-bst-subtree/) | Tree, DFS| Time: O(n), Space: O(h)| Medium|
|366 | [Find Leaves of Binary Tree](https://leetcode.com/problems/find-leaves-of-binary-tree/) | Tree, DFS| Time: O(n), Space: O(h)| Medium|
|437 | [Path Sum III](https://leetcode.com/problems/path-sum-iii/) | Tree, DFS| Time: O(n), Space: O(h)| Medium|
|614 | [Binary Tree Longest Consecutive Sequence III](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-iii/) | Tree, DFS| Time: O(n), Space: O(h)| Medium|
|619 | [Binary Tree Longest Consecutive Sequence IV](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-iv/) | Tree, DFS| Time: O(n), Space: O(h)| Medium|
|814 | [Binary Tree Pruning](https://leetcode.com/problems/binary-tree-pruning/) | Tree, DFS| Time: O(n), Space: O(h)| Medium|
|863 | [All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) | Tree, DFS| Time: O(n), Space: O(n)| Medium|
|865 | [Smallest Subtree with all the Deepest Nodes](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/) | Tree, DFS| Time: O(n), Space: O(n)| Medium|
|979 | [Distribute Coins in Binary Tree](https://leetcode.com/problems/distribute-coins-in-binary-tree/) | Tree, DFS| Time: O(n), Space: O(n)| Medium|
|988 | [Smallest String Starting From Leaf](https://leetcode.com/problems/smallest-string-starting-from-leaf/) | Tree, DFS| Time: O(n), Space: O(n)| Medium|
| 1038 | [Binary Search Tree to Greater Sum Tree](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/) | Tree, DFS| Time: O(n), Space: O(n)| Medium|
| 1070 | [Largest BST Subtree](https://leetcode.com/problems/largest-bst-subtree/) | Tree, DFS| Time: O(n), Space: O(n)| Medium|
| 1078 | [Smallest Subtree with all the Deepest Nodes](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/) | Tree, DFS| Time: O(n), Space: O(n)| Medium|
| 1081 | [Smallest Subtree with all the Deepest Nodes](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/) | Tree, DFS| Time: O(n), Space: O(n)| Medium|
| 1112 | [Smallest Subtree with all the Deepest Nodes](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/) | Tree, DFS| Time: O(n), Space: O(n)| Medium|
| 1120 | [Path Sum III](https://leetcode.com/problems/path-sum-iii/) | Tree, DFS| Time: O(n), Space: O(n)| Medium|
| 1123 | [Lowest Common Ancestor of Deepest Leaves](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/) | Tree, DFS| Time: O(n), Space: O(n)| Medium|
| 1132 | [Brothers From Different Roots](https://leetcode.com/problems/brothers-from-different-roots/) | Tree, DFS| Time: O(n), Space: O(n)| Medium|
| 1245 | [Tree Diameter](https://leetcode.com/problems/tree-diameter/) | Tree, DFS| O(n) Time, O(n) Space| Medium|
| 1272 | [Delete Tree Nodes](https://leetcode.com/problems/delete-tree-nodes/) | Tree, DFS| O(n) Time, O(n) Space| Medium|
| 1273 | [Delete Nodes And Return Forest](https://leetcode.com/problems/delete-nodes-and-return-forest/) | Tree, DFS| O(n) Time, O(n) Space| Medium|
| 1325 | [Delete Leaves with a Given Value](https://leetcode.com/problems/delete-leaves-with-a-given-value/) | Tree, DFS| O(n) Time, O(n) Space| Medium|
| 1372 | [Longest ZigZag Path in a Binary Tree](https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/) | Tree, DFS| O(n) Time, O(n) Space| Medium|
| 1379 | [Find a Corresponding Node of a Binary Tree in a Clone of That Tree](https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/) | Tree, DFS| O(n) Time, O(n) Space| Medium|
| 1382 | [Balance a Binary Search Tree](https://leetcode.com/problems/balance-a-binary-search-tree/) | Tree, DFS| O(n) Time, O(n) Space| Medium|
| 1443 | [Minimum Time to Collect All Apples in a Tree](https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/) | Tree, DFS| O(n) Time, O(n) Space| Medium|
| 1448 | [Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | Tree, DFS| O(n) Time, O(n) Space| Medium|
| 1490 | [Clone N-ary Tree](https://leetcode.com/problems/clone-n-ary-tree/) | Tree, DFS| O(n) Time, O(n) Space| Medium|
| 99 | [Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/) | Tree, DFS| Time: O(n), Space: O(h)| Hard|
|124 | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Tree, DFS| Time: O(n), Space: O(h)| Hard|
|297 | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | Tree, DFS| Time: O(n), Space: O(n)| Hard|
|834 | [Sum of Distances in Tree](https://leetcode.com/problems/sum-of-distances-in-tree/) | Tree, DFS| Time: O(n), Space: O(n)| Hard|
| 1339 | [Maximum Product of Splitted Binary Tree](https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/) | Tree, DFS| O(n) Time, O(n) Space| Hard|
|872 | [Leaf-Similar Trees](https://leetcode.com/problems/leaf-similar-trees/) | Tree, DFS, BFS | Time: O(n), Space: O(n)| Easy|
|582 | [Kill Process](https://leetcode.com/problems/kill-process/) | Tree, DFS, BFS | Time: O(n), Space: O(n)| Medium|
|938 | [Range Sum of BST](https://leetcode.com/problems/range-sum-of-bst/) | Tree, DFS, BST | Time: O(n), Space: O(n)| Easy|
| 1430 | [Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree](https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/) | Tree, DFS, String| O(n) Time, O(n) Space| Medium|
|894 | [All Possible Full Binary Trees](https://leetcode.com/problems/all-possible-full-binary-trees/) | Tree, DP | Time: O(2^n), Space: O(2^n)| Hard|
|968 | [Binary Tree Cameras](https://leetcode.com/problems/binary-tree-cameras/) | Tree, DP | Time: O(n), Space: O(n)| Hard|
| 95 | [Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/) | Tree, Dynamic Programming| Time: O(4^n / sqrt(n)), Space: O(n)| Medium|
|337 | [House Robber III](https://leetcode.com/problems/house-robber-iii/) | Tree, Dynamic Programming| Time: O(n), Space: O(h)| Medium|
| 1225 | [Reports to the Boss](https://leetcode.com/problems/reports-to-the-boss/) | Tree, Graph| O(n) Time, O(n) Space| Medium|
|608 | [Tree Node](https://leetcode.com/problems/tree-node/) | Tree, Hash Map | Time: O(n), Space: O(n)| Easy|
|690 | [Employee Importance](https://leetcode.com/problems/employee-importance/) | Tree, Hash Map | Time: O(n), Space: O(n)| Easy|
|652 | [Find Duplicate Subtrees](https://leetcode.com/problems/find-duplicate-subtrees/) | Tree, Hash Map | Time: O(n), Space: O(n)| Medium|
|653 | [Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/) | Tree, Hash Set | Time: O(n), Space: O(n)| Easy|
| 1| 485 | [📓 Max Consecutive Ones](0485.ipynb) | <span title="Process each element exactly once; maintain running state to build the result.">Single Pass</span> | Time: O(n), Space: O(1) | Easy |
|426 | [Convert Binary Search Tree to Sorted Doubly Linked List](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/) | Tree, In-order Traversal | Time: O(n), Space: O(h)| Medium|
|230 | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Tree, Inorder Traversal| Time: O(h + k), Space: O(h)| Medium|
| 1367 | [Linked List in Binary Tree](https://leetcode.com/problems/linked-list-in-binary-tree/) | Tree, Linked List| O(n) Time, O(n) Space| Medium|
|108 | [Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) | Tree, Recursion| Time: O(n), Space: O(log n)| Easy|
|897 | [Increasing Order Search Tree](https://leetcode.com/problems/increasing-order-search-tree/) | Tree, Recursion| Time: O(n), Space: O(n)| Easy|
|105 | [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | Tree, Recursion| Time: O(n), Space: O(n)| Medium|
|106 | [Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) | Tree, Recursion| Time: O(n), Space: O(n)| Medium|
|156 | [Binary Tree Upside Down](https://leetcode.com/problems/binary-tree-upside-down/) | Tree, Recursion| Time: O(n), Space: O(h)| Medium|
|889 | [Construct Binary Tree from Preorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/) | Tree, Recursion| Time: O(n), Space: O(n)| Medium|
|951 | [Flip Equivalent Binary Trees](https://leetcode.com/problems/flip-equivalent-binary-trees/) | Tree, Recursion| Time: O(n), Space: O(n)| Medium|
|971 | [Flip Binary Tree To Match Preorder Traversal](https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/) | Tree, Recursion| Time: O(n), Space: O(n)| Hard|
| 1305 | [All Elements in Two Binary Search Trees](https://leetcode.com/problems/all-elements-in-two-binary-search-trees/) | Tree, Sorting, Merge | O(n + m) Time, O(n + m) Space| Medium|
| 94 | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) | Tree, Stack| Time: O(n), Space: O(n)| Easy|
|173 | [Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/) | Tree, Stack| Time: O(1), Space: O(h)| Medium|
|501 | [Find Mode in Binary Search Tree](https://leetcode.com/problems/find-mode-in-binary-search-tree/) | Tree,Depth-First Search| O(N) Time,O(H) Space | Easy|
|508 | [Most Frequent Subtree Sum](https://leetcode.com/problems/most-frequent-subtree-sum/) | Tree,HashMap | O(N) Time, O(N) Space| Medium|

## TreeMap
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|352 | [Data Stream as Disjoint Intervals](https://leetcode.com/problems/data-stream-as-disjoint-intervals/) | TreeMap| Time: O(log n), Space: O(n)| Hard|

## Trie
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|720 | [Longest Word in Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/) | Trie | Time: O(n), Space: O(n)| Easy|
|208 | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | Trie | Time: O(n), Space: O(n)| Medium|
|211 | [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | Trie | Time: O(n), Space: O(n)| Medium|
|421 | [Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) | Trie | Time: O(n), Space: O(n)| Medium|
|677 | [Map Sum Pairs](https://leetcode.com/problems/map-sum-pairs/) | Trie | Time: O(1), Space: O(n)| Medium|
|820 | [Short Encoding of Words](https://leetcode.com/problems/short-encoding-of-words/) | Trie | Time: O(n), Space: O(n)| Medium|
|745 | [Prefix and Suffix Search](https://leetcode.com/problems/prefix-and-suffix-search/) | Trie | Time: O(n), Space: O(n)| Hard|
| 1408 | [String Matching in an Array](https://leetcode.com/problems/string-matching-in-an-array/) | Trie, Array| O(n) Time, O(n) Space| Easy|
| 1268 | [Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/) | Trie, Array| O(n * m) Time, O(n * m) Space| Medium|
|212 | [Word Search II](https://leetcode.com/problems/word-search-ii/) | Trie, Backtracking | Time: O(m * n * 4^L), Space: O(m * n)| Hard|
| 1178 | [Number of Valid Words for Each Puzzle](https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/) | Trie, Bitmasking | O(n) Time, O(n) Space| Hard|
|676 | [Implement Magic Dictionary](https://leetcode.com/problems/implement-magic-dictionary/) | Trie, Hash Map | Time: O(n), Space: O(n)| Medium|
|336 | [Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/) | Trie, Hash Map | Time: O(n^2), Space: O(n)| Hard|
|472 | [Concatenated Words](https://leetcode.com/problems/concatenated-words/) | Trie, Hash Set | Time: O(n * m^2), Space: O(n * m)| Hard|
| 1166 | [Design File System](https://leetcode.com/problems/design-file-system/) | Trie, HashMap| O(n) Time, O(n) Space| Medium|
| 1355 | [Count Words Obtained After Adding a Letter](https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/) | Trie, HashMap| O(n) Time, O(n) Space| Medium|
|648 | [Replace Words](https://leetcode.com/problems/replace-words/) | Trie, String | Time: O(n), Space: O(n)| Medium|
|642 | [Design Search Autocomplete System](https://leetcode.com/problems/design-search-autocomplete-system/) | Trie, String, Heap | Time: O(k), Space: O(k)| Hard|

## Two Pointers
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
|777 | [Swap Adjacent in LR String](https://leetcode.com/problems/swap-adjacent-in-lr-string/) | Two Pointer| Time: O(n), Space: O(1)| Medium|
|658 | [Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/) | Two Pointer, Binary Search | Time: O(log n + k), Space: O(k)| Medium|
|713 | [Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/) | Two Pointer, Sliding Window| Time: O(n), Space: O(1)| Medium|
|167 | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Two Pointers | Time: O(n), Space: O(1)| Easy|
|344 | [Reverse String](https://leetcode.com/problems/reverse-string/) | Two Pointers | Time: O(n), Space: O(1)| Easy|
|345 | [Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/) | Two Pointers | Time: O(n), Space: O(1)| Easy|
|392 | [Is Subsequence](https://leetcode.com/problems/is-subsequence/) | Two Pointers | Time: O(n), Space: O(1)| Easy|
| 1099 | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Two Pointers | Time: O(n), Space: O(1)| Easy|
| 11 | [📓 Container With Most Water](0011.ipynb) | <span title="Left and right pointers converge; move the pointer that makes progress toward the target.">Two Pointers</span> | Time: O(n), Space: O(1)| Medium|
|977 | [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) | Two Pointers, Array| Time: O(n), Space: O(1)| Easy|
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Two Pointers, Dynamic Programming| Time: O(n), Space: O(1)| Hard|
|978 | [Longest Turbulent Subarray](https://leetcode.com/problems/longest-turbulent-subarray/) | Two Pointers, Sliding Window | Time: O(n), Space: O(1)| Medium|
|986 | [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/) | Two Pointers, Sorting| Time: O(n), Space: O(1)| Medium|
| 1214 | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Two-pointer, Array | O(n) Time, O(1) Space| Easy|
| 1280 | [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/) | Two-pointer, Array | O(n + m) Time, O(n + m) Space| Medium|

## Union Find
| Serial No. | Problem Title | Data Structure | Time and Space Complexity | Level |
| :--- | :--- | :--- | :--- | :--- |
| 1061 | [Lexicographically Smallest Equivalent String](https://leetcode.com/problems/lexicographically-smallest-equivalent-string/) | Union Find | Time: O(n), Space: O(n)| Medium|
|305 | [Number of Islands II](https://leetcode.com/problems/number-of-islands-ii/) | Union Find | Time: O(n log n), Space: O(n)| Hard|
|952 | [Largest Component Size by Common Factor](https://leetcode.com/problems/largest-component-size-by-common-factor/) | Union Find | Time: O(n log n), Space: O(n)| Hard|
|261 | [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) | Union Find, DFS| Time: O(n), Space: O(n)| Medium|
|990 | [Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/) | Union Find, Graph| Time: O(n), Space: O(n)| Medium|
|684 | [Redundant Connection](https://leetcode.com/problems/redundant-connection/) | Union-Find | Time: O(n), Space: O(n)| Medium|
|685 | [Redundant Connection II](https://leetcode.com/problems/redundant-connection-ii/) | Union-Find | Time: O(n), Space: O(n)| Hard|
|839 | [Similar String Groups](https://leetcode.com/problems/similar-string-groups/) | Union-Find | Time: O(n^2), Space: O(n)| Hard|
|827 | [Making A Large Island](https://leetcode.com/problems/making-a-large-island/) | Union-Find, DFS| Time: O(n^2), Space: O(n^2)| Hard|
| 1202 | [Smallest String With Swaps](https://leetcode.com/problems/smallest-string-with-swaps/) | Union-Find, Graph| O(n log n) Time, O(n) Space| Medium|
| 1361 | [Validate Binary Tree Nodes](https://leetcode.com/problems/validate-binary-tree-nodes/) | Union-Find, Graph| O(n) Time, O(n) Space| Medium|
|803 | [Bricks Falling When Hit](https://leetcode.com/problems/bricks-falling-when-hit/) | Union-Find, Graph| Time: O(n * m), Space: O(n * m)| Hard|
| 1168 | [Optimize Water Distribution in a Village](https://leetcode.com/problems/optimize-water-distribution-in-a-village/) | Union-Find, Graph| O(n log n) Time, O(n) Space| Hard|
|602 | [Friend Requests II: The Final Count](https://leetcode.com/problems/friend-requests-ii-the-final-count/)| Union-Find, Hash Map | Time: O(n), Space: O(n)| Medium|

