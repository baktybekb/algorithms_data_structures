# O(n * m) time | O(1) space
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            for i in reversed(range(left, right)):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            for i in reversed(range(top, bottom)):
                res.append(matrix[i][left])
            left += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    assert solution.spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
