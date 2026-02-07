class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        min_diff = float('inf')
        result = 0

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                temp_diff = abs(total - target)

                if temp_diff < min_diff:
                    min_diff = temp_diff
                    result = total

                if total == target:
                    return total

                elif total > target:
                    right -= 1
                else:
                    left += 1
                    
        return result      