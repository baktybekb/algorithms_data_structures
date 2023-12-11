from typing import List


# O(n * m) time | O(1) space
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    continue
                perimeter += 4
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
        return perimeter

