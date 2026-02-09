class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        prefix_sum = 0
        count = 0
        h = {0 : 1}

        for num in nums:
            prefix_sum += num

            if prefix_sum - goal in h:
                count += h[prefix_sum - goal]

            h[prefix_sum] = h.get(prefix_sum, 0) + 1

        return count
        