from typing import List


# O(n * m) time | O(n * m) space
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        rows, cols = len(heights), len(heights[0])
        steps = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def dfs(row, col, visited):
            if (row, col) in visited:
                return
            visited.add((row, col))
            for r, c in steps:
                new_row, new_col = row + r, col + c
                if not 0 <= new_row < rows or not 0 <= new_col < cols:
                    continue
                if heights[new_row][new_col] < heights[row][col]:
                    continue
                dfs(new_row, new_col, visited)

        for col in range(cols):
            dfs(0, col, pacific)
            dfs(rows - 1, col, atlantic)

        for row in range(rows):
            dfs(row, 0, pacific)
            dfs(row, cols - 1, atlantic)

        result = []
        for height in pacific:
            if height not in atlantic:
                continue
            result.append(list(height))
        return result

