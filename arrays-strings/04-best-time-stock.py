def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

# Local Test Cases
if __name__ == "__main__":
    # Test 1: Typical Case
    assert maxProfit([7, 1, 5, 3, 6, 4]) == 5
    print("Test 1 Passed: Typical stock prices")

    # Test 2: Edge Case (Monotonically decreasing / no profit possible)
    assert maxProfit([7, 6, 4, 3, 1]) == 0
    print("Test 2 Passed: Continuous price drop edge case")