# https://leetcode.com/problems/longest-harmonious-subsequence/description/

from typing import List


# O(n) time | O(n) space
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums_map = {}
        length = 0
        for num in nums:
            if num not in nums_map:
                nums_map[num] = 0
            nums_map[num] += 1
            if num - 1 in nums_map:
                length = max(length, nums_map[num - 1] + nums_map[num])
            if num + 1 in nums_map:
                length = max(length, nums_map[num + 1] + nums_map[num])
        return length

