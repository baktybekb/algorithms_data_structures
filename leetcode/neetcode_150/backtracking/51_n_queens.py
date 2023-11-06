from typing import List


# O(n!) | O(n^2) space
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diag = set()
        neg_diag = set()
        res = []
        board = [['.' for _ in range(n)] for row in range(n)]

        def helper(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return res
            for c in range(n):
                if c in cols or r - c in neg_diag or r + c in pos_diag:
                    continue
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = 'Q'

                helper(r + 1)

                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = '.'

        helper(0)
        return res

