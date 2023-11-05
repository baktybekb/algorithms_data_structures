from typing import List


# O(2^target) time
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, subset = [], []

        def helper(i):
            cur_sum = sum(subset)
            if i == len(candidates) or cur_sum > target:
                return
            if cur_sum == target:
                res.append(subset.copy())
                return
            subset.append(candidates[i])
            helper(i)

            subset.pop()
            helper(i + 1)

        helper(0)
        return res

