# https://leetcode.com/problems/max-consecutive-ones/description/

from typing import List


# O(n) time | O(1) space
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        return max(max_count, count)


