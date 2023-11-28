# https://leetcode.com/problems/ransom-note/description/

# O(r + m) time | O(m) space
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_map = {}
        for char in magazine:
            if char not in char_map:
                char_map[char] = 0
            char_map[char] += 1
        for char in ransomNote:
            if char not in char_map or char_map[char] == 0:
                return False
            char_map[char] -= 1
        return True

