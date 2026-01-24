class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sSet = set()
        slow = 0
        result = 0 

        for fast in range(len(s)):
            while s[fast] in sSet:
                sSet.remove(s[slow])
                slow += 1
            sSet.add(s[fast])
            result = max(result, fast - slow + 1)
        return result
        