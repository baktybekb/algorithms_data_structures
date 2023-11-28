# https://leetcode.com/problems/length-of-last-word/description/


# O(n) time | O(1) space
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        right = len(s) - 1
        while s[right] == ' ':
            right -= 1
        left = right
        while left >= 0 and s[left] != ' ':
            left -= 1
        return right - left

