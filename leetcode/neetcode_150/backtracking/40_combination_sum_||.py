# https://leetcode.com/problems/combination-sum-ii/description/
from typing import List


# O(n * 2^n) time
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, subset = [], []
        candidates.sort()

        def helper(i, cur_sum):
            if cur_sum == target:
                res.append(subset.copy())
                return
            if cur_sum > target or i == len(candidates):
                return
            subset.append(candidates[i])
            helper(i + 1, cur_sum + candidates[i])

            subset.pop()
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            helper(i + 1, cur_sum)

        helper(0, 0)
        return res
