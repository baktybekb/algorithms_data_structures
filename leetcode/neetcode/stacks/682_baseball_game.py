# https://leetcode.com/problems/baseball-game/description/

from typing import List


# O(n) time | O(n) space
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for oper in operations:
            if oper == '+':
                stack.append(stack[-1] + stack[-2])
            elif oper == 'D':
                stack.append(stack[-1] * 2)
            elif oper == 'C':
                stack.pop()
            else:
                stack.append(int(oper))
        return sum(stack)
