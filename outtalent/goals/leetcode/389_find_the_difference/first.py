# https://leetcode.com/problems/find-the-difference/description/

# O(s + t) time | O(1) space
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        char_map = {}
        for char in s:
            if char not in char_map:
                char_map[char] = 0
            char_map[char] += 1

        for char in t:
            if char not in char_map or char_map[char] == 0:
                return char
            char_map[char] -= 1

