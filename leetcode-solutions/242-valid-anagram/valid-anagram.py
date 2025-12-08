class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            s_arr = []
            t_arr = []
            for i in range(len(s)):
                s_arr.append(s[i])
                t_arr.append(t[i])
            s_arr.sort()
            t_arr.sort()

            if s_arr == t_arr:
                return True
            else: return False
        