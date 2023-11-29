# https://leetcode.com/problems/longest-palindrome/description/

# O(s) time | O(1) space
class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_map = {}
        for char in s:
            if char not in char_map:
                char_map[char] = 0
            char_map[char] += 1
        length, has_odd = 0, False
        for amount in char_map.values():
            if amount % 2 == 0:
                length += amount
            else:
                length += amount - 1
                has_odd = True
        if has_odd:
            length += 1
        return length
