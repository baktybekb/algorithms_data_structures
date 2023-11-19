# https://leetcode.com/problems/house-robber/description/

from typing import List


# O(n) time | O(1) space
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = rob2 = 0
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


if __name__ == '__main__':
    assert Solution().rob([2, 1, 1, 2]) == 4
