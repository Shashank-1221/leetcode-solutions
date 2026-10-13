## Problem: Move Zeroes (Easy)

**Link:** https://leetcode.com/problems/move-zeroes/

### Approach

I used a two-pointer technique with a `write` pointer that marks where the next non-zero value should go. I loop through the array, and each time I find a non-zero value I swap it into the `write` position and move that pointer forward. This pushes all zeros to the end in place while keeping the order of the non-zero values.

### Complexity

- Time: O(n)
- Space: O(1)

### Notes

Edge cases I tested were an array of all zeros, an array with no zeros, and a single element. The swap only matters when `write` and the current index differ, so I could skip it when they are equal for a small improvement.
