from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic, pacific = set(), set()
        rows, cols = len(heights), len(heights[0])

        def dfs(row, col, visited):
            visited.add((row, col))
            for r, c in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                new_row, new_col = row + r, col + c
                if not 0 <= new_row < rows or not 0 <= new_col < cols:
                    continue
                if (new_row, new_col) in visited:
                    continue
                if heights[new_row][new_col] < heights[row][col]:
                    continue
                dfs(row + r, col + c, visited)

        for col in range(cols):
            dfs(0, col, pacific)
            dfs(rows - 1, col, atlantic)

        for row in range(rows):
            dfs(row, 0, pacific)
            dfs(row, cols - 1, atlantic)

        result = []
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    result.append([row, col])
        return result
