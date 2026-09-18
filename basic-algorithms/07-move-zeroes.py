from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
                last_non_zero += 1

# Local Test Cases for VS Code
if __name__ == "__main__":
    sol = Solution()

    # Test 1: Typical Case
    nums1 = [0, 1, 0, 3, 12]
    sol.moveZeroes(nums1)
    assert nums1 == [1, 3, 12, 0, 0]
    print("Test 1 Passed: Mixed zeros and non-zeros")

    # Test 2: Edge Case (No zeros present)
    nums2 = [1, 2, 3]
    sol.moveZeroes(nums2)
    assert nums2 == [1, 2, 3]
    print("Test 2 Passed: No zeros present")