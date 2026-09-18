from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

# Local Test Cases for VS Code
if __name__ == "__main__":
    sol = Solution()

    # Test 1: Typical Case
    assert sol.search([-1, 0, 3, 5, 9, 12], 9) == 4
    print("Test 1 Passed: Target present in list")

    # Test 2: Edge Case (Target not in list)
    assert sol.search([-1, 0, 3, 5, 9, 12], 2) == -1
    print("Test 2 Passed: Target missing edge case")