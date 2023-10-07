from typing import List


# O(n) time | (1) space
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                return abs(num)
            nums[idx] *= -1

