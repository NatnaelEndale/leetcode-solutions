class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        slow = 0
        for fast in range(1, len(nums)):
            if nums[slow] % 2 != 0 and nums[fast]%2==0:
                temp = nums[slow]
                nums[slow] = nums[fast]
                nums[fast] = temp
                slow += 1
            elif nums[slow] % 2 == 0:
                slow += 1
        return nums
        