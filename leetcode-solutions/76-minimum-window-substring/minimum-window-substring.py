from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        tCount = Counter(t)
        window = Counter()

        required = len(tCount)
        formed = 0

        min_len = float('inf')
        slow = 0
        index_store = (0, 0)

        for fast in range(len(s)):
            char = s[fast]
            window[char] += 1

            if char in tCount and tCount[char] == window[char]:
                formed += 1

            while formed == required:
                if fast - slow + 1 < min_len:
                    min_len = fast - slow + 1
                    index_store = (slow, fast)
                
                left_char = s[slow]
                window[left_char] -= 1

                if left_char in tCount and window[left_char] < tCount[left_char]:
                    formed -= 1

                slow += 1

        return "" if min_len == float('inf') else s[index_store[0]:index_store[1]+1] 
        