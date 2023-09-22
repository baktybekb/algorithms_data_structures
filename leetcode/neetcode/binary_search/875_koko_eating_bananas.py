from typing import List
import math


# O(log(max_pile)) * n) time | O(1) space
# max_pile = max(piles), n == len(piles)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_speed = r
        while l <= r:
            speed = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / speed)
            if hours <= h:
                min_speed = min(min_speed, speed)
                r = speed - 1
            else:
                l = speed + 1
        return min_speed


if __name__ == '__main__':
    sol = Solution()
    assert sol.minEatingSpeed(piles=[3, 6, 7, 11], h=8) == 4
