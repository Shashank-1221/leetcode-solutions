## Problem: Binary Search (Easy)

**Link:** https://leetcode.com/problems/binary-search/

### Approach

I kept two pointers, `left` and `right`, around the part of the sorted array that could still contain the target. At each step I checked the middle element, then discarded the half that cannot contain the target. This halves the search range every time, which is much faster than scanning every element.

### Complexity

- Time: O(log n)
- Space: O(1)

### Notes

Edge cases I tested were a target that isn't in the array (return -1), a single-element array, and a target at the first or last position. I used `left + (right - left) // 2` for the middle, which avoids integer overflow in other languages.
