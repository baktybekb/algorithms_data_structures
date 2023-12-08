# https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/

from typing import List


# O(n) time | O(1) space
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        array = [float('-inf')] * 2
        max_value_idx = 0
        for index, num in enumerate(nums):
            for j in reversed(range(len(array))):
                if num < array[j]:
                    continue
                if j == len(array) - 1:
                    max_value_idx = index
                for k in range(j):
                    array[k] = array[k + 1]
                array[j] = num
                break
        return max_value_idx if array[0] * 2 <= array[1] else -1

