# https://leetcode.com/problems/distribute-candies/description/

from typing import List


# O(n) time | O(n) space
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        types_set = set(candyType)
        return min(len(types_set), len(candyType) // 2)

