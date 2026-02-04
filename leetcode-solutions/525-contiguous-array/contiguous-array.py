class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hash_map = {0:-1}
        num_zeros = 0
        num_ones = 0
        max_len = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                num_zeros += 1
            else:
                num_ones += 1

            differ = num_zeros - num_ones

            if differ in hash_map:
                max_len = max(max_len, i - hash_map[differ])
            else:
                hash_map[differ] = i
        
        return max_len
        