class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False

        pre = 0
        h = {0:-1}

        for i in range(len(nums)):
            pre += nums[i]
            rem = pre % k if k != 0 else pre

            if rem in h:
                if i - h[rem] >= 2:
                    return True 
            else:
                h[rem] = i

        return False
        