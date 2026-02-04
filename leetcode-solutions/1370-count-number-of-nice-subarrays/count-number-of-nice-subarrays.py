class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        hash_m = {0:1}
        count = 0
        prefix_sum = 0

        for num in nums:
            if num % 2 == 0:
                prefix_sum += 0
            else:
                prefix_sum += 1

            differ = prefix_sum - k

            if differ in hash_m:
                count += hash_m[differ]
            hash_m[prefix_sum] = hash_m.get(prefix_sum, 0) + 1

        return count