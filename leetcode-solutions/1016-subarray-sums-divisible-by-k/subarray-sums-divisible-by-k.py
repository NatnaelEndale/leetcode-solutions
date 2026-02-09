class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre = 0
        count = 0
        h = {0: 1}

        for num in nums :
            pre += num
            reminder = pre % k

            if reminder in h:
                count += h[reminder]

            h[reminder] = h.get(reminder, 0) + 1

        return count
        