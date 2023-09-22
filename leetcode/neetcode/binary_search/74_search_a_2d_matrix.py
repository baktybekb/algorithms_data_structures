from typing import List


# O(log(n * m)) time | O(1) space
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1
        while top <= bot:
            row = (top + bot) // 2
            if matrix[row][0] > target:
                bot = row - 1
            elif matrix[row][-1] < target:
                top = row + 1
            else:
                break
        if not top <= bot:
            return False
        row = (top + bot) // 2
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    assert solution.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3) is True
    assert solution.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13) is False
    assert solution.searchMatrix(matrix=[[1]], target=1) is True
    assert solution.searchMatrix(matrix=[[1], [3], [5]], target=3) is True
