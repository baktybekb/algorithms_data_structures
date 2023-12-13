from typing import List


# O(n^2) time | O(1) space
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            left, right = 0, len(mat) - 1
            while left < right:
                top, bottom = left, right
                for i in range(right - left):
                    top_left = mat[top][left + i]
                    mat[top][left + i] = mat[bottom - i][left]
                    mat[bottom - i][left] = mat[bottom][right - i]
                    mat[bottom][right - i] = mat[top + i][right]
                    mat[top + i][right] = top_left
                left += 1
                right -= 1
            if mat == target:
                return True
        return False

