# https://leetcode.com/problems/third-maximum-number/description/

from typing import List


# O(n) time | O(1) space
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        array = [float('-inf')] * 3
        for value in nums:
            self.insert(array, value)
        if array[0] == float('-inf'):
            return array[-1]
        return array[0]

    def insert(self, array, value):
        for i in reversed(range(len(array))):
            if array[i] > value:
                continue
            if array[i] == value:
                break
            for j in range(0, i):
                array[j] = array[j + 1]
            array[i] = value
            break



