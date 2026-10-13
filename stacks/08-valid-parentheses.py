class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack

# Local Test Cases for VS Code
if __name__ == "__main__":
    sol = Solution()

    # Test 1: Typical Case
    assert sol.isValid("()[]{}") == True
    print("Test 1 Passed: Valid bracket sequence")

    # Test 2: Edge Case (Mismatched bracket types)
    assert sol.isValid("(]") == False
    print("Test 2 Passed: Mismatched bracket type")