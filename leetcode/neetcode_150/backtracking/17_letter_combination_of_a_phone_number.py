from typing import List


# O(4^n * n) time | O(4^n * n) space
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res, part = [], []
        if not digits:
            return res
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def dfs(i):
            if i == len(digits):
                res.append(''.join(part))
                return
            for val in digit_map[digits[i]]:
                part.append(val)
                dfs(i + 1)
                part.pop()

        dfs(0)
        return res
