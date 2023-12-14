# https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/

from typing import List


# O(n * 2^n) time | O(n) space
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = [0]
        self.traverse(0, nums, [], total)
        return total[0]

    def traverse(self, index, nums, subset, total):
        if index == len(nums):
            subset_total = 0
            for val in subset:
                subset_total ^= val
            total[0] += subset_total
            return
        subset.append(nums[index])
        self.traverse(index + 1, nums, subset, total)

        subset.pop()
        self.traverse(index + 1, nums, subset, total)


if __name__ == '__main__':
    sol = Solution()
    assert sol.subsetXORSum([5, 1, 6]) == 28
