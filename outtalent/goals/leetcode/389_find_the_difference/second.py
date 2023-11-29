# https://leetcode.com/problems/find-the-difference/description/

# O(s + t) time | O(1) space
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        code = 0
        for char in s:
            code ^= ord(char)
        for char in t:
            code ^= ord(char)
        return chr(code)
