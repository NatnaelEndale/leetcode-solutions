import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        min_val = float('inf')

        while left <= right:
            mid = (left + right) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)

            if hours <= h:
                right = mid - 1
                min_val = min(min_val, mid)
            else:
                left = mid + 1
        
        return min_val