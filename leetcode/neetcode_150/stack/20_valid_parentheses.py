# O(n) time | O(n) space
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_map = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char not in char_map:
                stack.append(char)  # append open chars
                continue
            if not stack or char_map[char] != stack[-1]:
                return False
            stack.pop()
        return False if stack else True


if __name__ == '__main__':
    solution = Solution()
    assert solution.isValid(s="()[]{}") is True
    assert solution.isValid(s="(]") is False
    assert solution.isValid(s="()") is True
    assert solution.isValid(s='[') is False
