from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        n = len(s2)

        if k > n:
            return False

        s1Counter = Counter(s1)
        window = Counter(s2[:k])

        if s1Counter == window:
            return True
        
        for i in range(k, n):
            window[s2[i]] += 1
            window[s2[i-k]] -= 1

            if window[s2[i-k]] == 0:
                del window[s2[i-k]]

            if window == s1Counter:
                return True
        return False
        