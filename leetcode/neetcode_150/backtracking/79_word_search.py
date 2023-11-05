# https://leetcode.com/problems/word-search/description/
from typing import List


# O(n * m) time | O(n * m) space
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            if i == len(word) - 1:
                return True
            visited.add((r, c))
            i += 1
            for r_step, c_step in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                new_r, new_c = r + r_step, c + c_step
                if (
                    not 0 <= new_r < rows or not 0 <= new_c < cols or
                    (new_r, new_c) in visited or
                    board[new_r][new_c] != word[i]
                ):
                    continue
                if dfs(new_r, new_c, i):
                    return True
            visited.remove((r, c))
            return False

        for row in range(rows):
            for col in range(cols):
                if board[row][col] != word[0]:
                    continue
                if dfs(row, col, 0):
                    return True
        return False
