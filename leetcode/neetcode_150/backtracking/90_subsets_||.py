# https://leetcode.com/problems/subsets-ii/description/
from typing import List


# O(n * 2^n) time | O(2^n) space
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []
        nums.sort()

        def helper(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            helper(i + 1)

            subset.pop()
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            helper(i + 1)

        helper(0)
        return res


if __name__ == '__main__':
    Solution().subsetsWithDup([1, 2, 3])
