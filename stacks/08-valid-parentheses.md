## Problem: Valid Parentheses (Easy)

**Link:** https://leetcode.com/problems/valid-parentheses/

### Approach

I used a stack to keep track of opening brackets. When I see an opening bracket I push it, and when I see a closing bracket I check that the top of the stack is its matching opener, then pop it. The string is valid only if every closing bracket matched and the stack is empty at the end.

### Complexity

- Time: O(n)
- Space: O(n)

### Notes

Edge cases I tested were a string that starts with a closing bracket (such as "]"), a string with leftover openers (such as "(("), and wrongly nested brackets like "([)]". I needed to check that the stack isn't empty before popping, otherwise an input like ")" would crash.
