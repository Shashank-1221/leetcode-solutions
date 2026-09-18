def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT

# Local Tests
print("Test 1 (True Anagram):", isAnagram("anagram", "nagaram")) # Expected: True
print("Test 2 (Different Lengths):", isAnagram("rat", "car"))   # Expected: False