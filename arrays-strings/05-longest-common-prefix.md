## Problem: Longest Common Prefix (Easy)

**Link:** https://leetcode.com/problems/longest-common-prefix/

### Approach

I took the first string as the starting prefix and compared it with each remaining string. While a string doesn't start with the current prefix, I remove the last character of the prefix. If the prefix becomes empty, I return an empty string straight away.

### Complexity

- Time: O(S), where S is the total number of characters across all strings
- Space: O(1)

### Notes

Edge cases I tested were a list with no common prefix (such as ["dog", "car"]), a single-string list, and an empty string in the list. Comparing the strings column by column, character by character, is another approach I could try next time.
