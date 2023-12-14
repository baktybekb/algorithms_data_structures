from typing import List


# O(1) time and space
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        def intersect(p_left, p_right, q_left, q_right):
            return min(p_right, q_right) > max(p_left, q_left)

        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        return intersect(x1, x2, x3, x4) and intersect(y1, y2, y3, y4)

