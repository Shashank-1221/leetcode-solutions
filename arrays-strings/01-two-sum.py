def twoSum(nums, target):
    prevMap = {}  # Stores value -> index mapping
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i

# --- LOCAL TEST CASES ---
# Test 1 (Typical case):
print("Test 1 Result:", twoSum([2, 7, 11, 15], 9)) 
# Expected Output: [0, 1]

# Test 2 (Edge case - duplicates):
print("Test 2 Result:", twoSum([3, 3], 6)) 
# Expected Output: [0, 1]