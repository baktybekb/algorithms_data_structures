# https://leetcode.com/problems/rectangle-overlap/description/

from typing import List


# O(1) time and space
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        if (x1 == x2 and y1 == y2) or (x3 == x4 and y3 == y4):
            return False
        return not (
                y2 <= y3 or
                y4 <= y1 or
                x2 <= x3 or
                x4 <= x1
        )


