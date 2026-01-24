class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        min_len = float('inf')
        slow = 0
        fast = 0
        window_sum = 0

        while fast < len(nums):
            window_sum += nums[fast]

            while window_sum >= target:
                min_len = min(min_len, fast - slow + 1)
                window_sum -= nums[slow]
                slow += 1
            fast += 1
        return min_len
        