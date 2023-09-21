from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # can add opened if opened < n
        # can add closed if closed < opened
        # stop if closed == opened == n
        stack = []
        res = []

        def backtrack(opened, closed):
            if opened == closed == n:
                res.append(''.join(stack))
            if opened < n:
                stack.append('(')
                backtrack(opened + 1, closed)
                stack.pop()
            if closed < opened:
                stack.append(')')
                backtrack(opened, closed + 1)
                stack.pop()

        backtrack(0, 0)
        return res


if __name__ == '__main__':
    solution = Solution()
    assert solution.generateParenthesis(n=3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
