## Problem: Two Sum (Easy)

**Link:** https://leetcode.com/problems/two-sum/

### Approach

I used a hash map to store each number's index as I loop through the array. For each number I check whether its complement (target minus the number) is already in the map. This avoids a nested loop.

### Complexity

- Time: O(n)
- Space: O(n)

### Notes

Duplicates such as [3, 3] with target 6 work because the complement is checked before the current number is stored.
