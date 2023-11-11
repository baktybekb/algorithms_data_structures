# https://leetcode.com/problems/number-of-islands/description/

from typing import List


# O(n * m) time | O(s) space, s --> size of biggest island (recursive call stack)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_islands = 0
        rows, cols = len(grid), len(grid[0])
        steps = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def color_the_island(row, col):
            grid[row][col] = '0'
            for r, c in steps:
                new_row, new_col = row + r, col + c
                if not 0 <= new_row < rows or not 0 <= new_col < cols:
                    continue
                if grid[new_row][new_col] != '1':
                    continue
                color_the_island(new_row, new_col)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != '1':
                    continue
                color_the_island(row, col)
                number_of_islands += 1
        return number_of_islands
