# https://leetcode.com/problems/rotting-oranges/description/

from collections import deque
from typing import List


# O(n * m) time | O(n * m) space
class Solution:
    steps = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = minutes = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                if grid[row][col] == 1:
                    fresh_oranges += 1
        if fresh_oranges == 0:
            return 0
        while queue:
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
            minutes += 1
        return minutes - 1 if fresh_oranges == 0 else -1


