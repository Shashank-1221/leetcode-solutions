from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

# Local Test Cases for VS Code
if __name__ == "__main__":
    sol = Solution()

    # Test 1: Typical Case
    assert sol.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    print("Test 1 Passed: Common prefix exists")

    # Test 2: Edge Case (No common prefix)
    assert sol.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    print("Test 2 Passed: No common prefix edge case")          