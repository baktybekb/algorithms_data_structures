# https://leetcode.com/problems/valid-parentheses/description/


# O(n) time | O(n) space
class Solution:
    def isValid(self, s: str) -> bool:
        brackets_map = {'}': '{', ']': '[', ')': '('}
        stack = []
        for char in s:
            if char in brackets_map:
                if not stack or stack[-1] != brackets_map[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0


