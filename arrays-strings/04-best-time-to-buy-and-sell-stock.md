## Problem: Best Time to Buy and Sell Stock (Easy)

**Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

### Approach

I made a single pass through the prices while tracking the lowest price seen so far. At each day I calculate the profit if I sold at that day's price, and I keep the maximum profit found. This works because the best buy day is always the minimum price before the sell day.

### Complexity

- Time: O(n)
- Space: O(1)

### Notes

Edge cases I tested were prices that only fall (such as [7, 6, 4, 3, 1]), where the answer is 0, and a single-element list. A brute-force nested loop would work but takes O(n^2) time, which is too slow for large inputs.
