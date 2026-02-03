from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        n = len(s)

        pCount = Counter(p)
        window = Counter(s[:k])
        result = []

        if pCount == window:
            result.append(0)

        for i in range(k, n):
            window[s[i]] += 1
            window[s[i-k]] -= 1

            if window[s[i-k]] == 0:
                del window[s[i-k]]
            
            if window == pCount:
                result.append(i-k+1)
            
        return result