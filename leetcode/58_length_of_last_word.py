# O(n) time | O(1) space
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s) - 1, 0
        while s[i] == ' ':
            i -= 1
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        return length


if __name__ == '__main__':
    solution = Solution()
    assert solution.lengthOfLastWord(' collection') == 10
    assert solution.lengthOfLastWord(' name  ') == 4
