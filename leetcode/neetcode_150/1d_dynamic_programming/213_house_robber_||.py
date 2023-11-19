# https://leetcode.com/problems/house-robber-ii/description/

from typing import List


# O(n) time | O(1) space
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        value1 = self.helper(0, len(nums) - 1, nums)
        value2 = self.helper(1, len(nums), nums)
        return max(value1, value2)

    def helper(self, start, end, nums):
        rob1 = rob2 = 0
        for i in range(start, end):
            n = nums[i]
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

