## Problem: Reverse String (Easy)

**Link:** https://leetcode.com/problems/reverse-string/

### Approach

I used the two-pointer technique, with one pointer at the start of the list and one at the end. I swap the characters at both pointers, then move them toward each other until they meet. This reverses the string in place without creating a new list.

### Complexity

- Time: O(n)
- Space: O(1)

### Notes

Edge cases I tested were an empty list and a single character, where the loop never runs and the list stays the same. Python's `s[::-1]` is shorter, but it creates a new list, and this problem requires modifying the input in place.
