# https://leetcode.com/problems/subsets/description/
from typing import List


# O(n * 2^n) time | O(2 ^ n + n) space
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):

            if i == len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res


if __name__ == '__main__':
    Solution().subsets(nums=[1, 2, 3])
