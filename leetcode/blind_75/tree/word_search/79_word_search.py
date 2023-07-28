from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()

        def dfs(row, col, idx):
            if idx == len(word):
                return True
            if (
                    not 0 <= row < len(board) or
                    not 0 <= col < len(board[0]) or
                    (row, col) in path or
                    board[row][col] != word[idx]
            ):
                return False
            path.add((row, col))
            result = (
                    dfs(row + 1, col, idx + 1) or
                    dfs(row - 1, col, idx + 1) or
                    dfs(row, col + 1, idx + 1) or
                    dfs(row, col - 1, idx + 1)
            )
            path.remove((row, col))
            return result

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, 0):
                    return True
        return False


if __name__ == '__main__':
    solution = Solution()
    assert solution.exist(board=[["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], word='AAB') is True

