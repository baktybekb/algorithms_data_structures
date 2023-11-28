# https://leetcode.com/problems/first-unique-character-in-a-string/description/

# O(s) time | O(1) space
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_map = {}
        for char in s:
            if char not in char_map:
                char_map[char] = 0
            char_map[char] += 1
        for idx, char in enumerate(s):
            if char_map[char] == 1:
                return idx
        return -1
