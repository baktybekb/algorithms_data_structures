from typing import List


# O(n) time | O(n) space
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                cur = stack.pop()
                stack.append(stack.pop() - cur)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                cur = stack.pop()
                stack.append(int(stack.pop() / cur))
            else:
                stack.append(int(token))
        return stack[-1]


if __name__ == '__main__':
    solution = Solution()
    assert solution.evalRPN(tokens=["2", "1", "+", "3", "*"]) == 9
    assert solution.evalRPN(tokens=["4", "13", "5", "/", "+"]) == 6
    assert solution.evalRPN(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
