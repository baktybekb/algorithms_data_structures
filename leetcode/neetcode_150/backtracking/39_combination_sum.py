from typing import List


# O(2^target) time
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, subset = [], []

        def helper(i, cur_sum):
            if cur_sum == target:
                res.append(subset.copy())
                return
            if i == len(candidates) or cur_sum > target:
                return
            subset.append(candidates[i])
            helper(i, cur_sum + candidates[i])

            subset.pop()
            helper(i + 1, cur_sum)

        helper(0, 0)
        return res

