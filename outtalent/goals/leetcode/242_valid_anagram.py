# https://leetcode.com/problems/valid-anagram/description/

# O(s + t) time | O(s) space
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_map = {char: 0 for char in s}
        for char in s:
            char_map[char] += 1
        for char in t:
            if char not in char_map or char_map[char] == 0:
                return False
            char_map[char] -= 1
        return True
