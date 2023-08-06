from typing import List


# O(w * h) time | O(1) space, width and height of the grid
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            grid[r][c] = '0'
            for r_, c_ in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                new_r, new_c = r + r_, c + c_
                if not 0 <= new_r < rows or not 0 <= new_c < cols:
                    continue
                if grid[new_r][new_c] == '0':
                    continue
                dfs(new_r, new_c)

        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '0':
                    continue
                dfs(row, col)
                count += 1
        return count
