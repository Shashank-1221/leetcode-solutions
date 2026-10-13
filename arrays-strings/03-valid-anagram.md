## Problem: Valid Anagram (Easy)

**Link:** https://leetcode.com/problems/valid-anagram/

### Approach

I counted the frequency of each character in both strings using a hash map (or `Counter` in Python) and compared the two counts. If the strings have different lengths they can't be anagrams, so I return False early. Otherwise they are anagrams only when every character appears the same number of times in both.

### Complexity

- Time: O(n)
- Space: O(1), because the alphabet is limited to 26 lowercase letters

### Notes

Edge cases I tested were strings of different lengths and repeated letters such as "aacc" versus "ccac". Sorting both strings and comparing them also works, but it costs O(n log n), so counting is faster.
