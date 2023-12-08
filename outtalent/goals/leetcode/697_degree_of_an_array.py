# https://leetcode.com/problems/degree-of-an-array/description/

from typing import List


# O(n) time | O(n) space
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        hash_map, degree = {}, 0
        for index, num in enumerate(nums):
            if num in hash_map:
                hash_map[num][0] += 1
                hash_map[num][2] = index
            else:
                hash_map[num] = [1, index, index]
            if hash_map[num][0] <= degree:
                continue
            degree = hash_map[num][0]

        length = float('inf')
        for val, data in hash_map.items():
            if data[0] != degree:
                continue
            length = min(length, data[2] - data[1] + 1)
        return length

