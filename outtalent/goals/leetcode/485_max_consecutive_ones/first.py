# https://leetcode.com/problems/max-consecutive-ones/description/

from typing import List


# O(n) time | O(1) space
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        total = i = 0
        while i < len(nums):
            while i < len(nums) and nums[i] == 0:
                i += 1
            start = i
            while i < len(nums) and nums[i] == 1:
                i += 1
            if i - start <= total:
                continue
            total = i - start
        return total






