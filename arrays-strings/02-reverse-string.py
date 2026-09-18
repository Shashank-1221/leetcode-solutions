def reverseString(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# Local Tests
s1 = ["h","e","l","l","o"]
reverseString(s1)
print("Test 1 (Typical):", s1) # Expected: ['o', 'l', 'l', 'e', 'h']

s2 = ["A"]
reverseString(s2)
print("Test 2 (Single Element):", s2) # Expected: ['A']