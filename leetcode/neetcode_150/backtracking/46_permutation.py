# https://leetcode.com/problems/permutations/description/
from typing import List


# O(n! * n) time | O(n! * n) space
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(res, 0, nums)
        return res

    def helper(self, res, i, array):
        if i == len(array):
            res.append(array.copy())
            return
        for j in range(i, len(array)):
            self.swap(i, j, array)
            self.helper(res, i + 1, array)
            self.swap(i, j, array)

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]


if __name__ == '__main__':
    Solution().permute([1, 2, 3])
