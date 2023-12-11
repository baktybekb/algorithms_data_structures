# https://leetcode.com/problems/island-perimeter/description/

from typing import List


# O(n * m) time | O(i), i - length of island
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols, steps = len(grid), len(grid[0]), ((0, 1), (0, -1), (1, 0), (-1, 0))
        perimeter = [0]
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 1:
                    continue
                self.dfs(grid, row, col, rows, cols, perimeter, steps)
                return perimeter[0]

    def dfs(self, grid, row, col, rows, cols, perimeter, steps):
        grid[row][col] = 2
        for r, c in steps:
            new_row, new_col = row + r, col + c
            if not 0 <= new_row < rows or not 0 <= new_col < cols or grid[new_row][new_col] == 0:
                perimeter[0] += 1
                continue
            if grid[new_row][new_col] == 2:
                continue
            self.dfs(grid, new_row, new_col, rows, cols, perimeter, steps)


if __name__ == '__main__':
    sol = Solution()
    sol.islandPerimeter(grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]])
