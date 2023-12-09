# https://leetcode.com/problems/height-checker/description/

from typing import List


# O(nlog(n)) time | O(n) space
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        number = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                number += 1
        return number
