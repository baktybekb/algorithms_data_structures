# https://leetcode.com/problems/surrounded-regions/description/

from typing import List


# O(n * m) time | O(i), size of the longest region connected to the border (recursive call stack)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        steps = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def dfs(row, col):
            if board[row][col] != 'O':
                return
            board[row][col] = 1
            for r, c in steps:
                new_row, new_col = row + r, col + c
                if not 0 <= new_row < rows or not 0 <= new_col < cols:
                    continue
                dfs(new_row, new_col)

        for row in range(rows):
            for col in range(cols):
                border = row == 0 or row == rows - 1 or col == 0 or col == cols - 1
                if not border:
                    continue
                dfs(row, col)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 1:
                    board[row][col] = 'O'
