## Problem: Reverse Linked List (Easy)
**Link:** https://leetcode.com/problems/reverse-linked-list/

### Approach
I used an iterative three-pointer technique with `prev`, `curr` and `nxt`. At each node I save the next node, point the current node back at `prev`, then move both pointers forward. This reverses the list in a single pass without extra memory.

### Complexity
- Time: O(n)
- Space: O(1)

### Notes
Saving `curr.next` before overwriting it is essential, otherwise the rest of the list is lost. Edge cases I tested were an empty list and a single node. A recursive solution is cleaner to write but uses O(n) stack space, so I'd try it next time for practice.
