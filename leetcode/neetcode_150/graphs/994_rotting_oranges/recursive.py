# https://leetcode.com/problems/rotting-oranges/description/

from collections import deque
from typing import List


# O(n * m) time | O(n * m) space
class Solution:
    steps = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue, fresh_oranges = deque(), 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                if grid[row][col] == 1:
                    fresh_oranges += 1
        if fresh_oranges == 0:
            return 0
        minutes, fresh_oranges = self.update_adjacent_cells(grid, queue, 0, rows, cols, fresh_oranges)
        return minutes if fresh_oranges == 0 else -1

    def update_adjacent_cells(self, grid, queue, minutes, rows, cols, fresh_oranges):
        if not queue:
            return minutes - 1, fresh_oranges
        for i in range(len(queue)):
            row, col = queue.popleft()
            for r, c in self.steps:
                new_row, new_col = row + r, col + c
                if not 0 <= new_row < rows or not 0 <= new_col < cols:
                    continue
                if grid[new_row][new_col] != 1:
                    continue
                grid[new_row][new_col] = 2
                fresh_oranges -= 1
                queue.append((new_row, new_col))
        return self.update_adjacent_cells(grid, queue, minutes + 1, rows, cols, fresh_oranges)


