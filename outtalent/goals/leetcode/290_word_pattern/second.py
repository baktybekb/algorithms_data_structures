# https://leetcode.com/problems/word-pattern/description/

# O(p + s) time | O(k) space, k --> unique keys in map
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        map_index = {}
        for i in range(len(pattern)):
            char, word = pattern[i], words[i]
            char_key, word_key = f'char_{char}', f'word_{word}'
            if char_key not in map_index:
                map_index[char_key] = i
            if word_key not in map_index:
                map_index[word_key] = i
            if map_index[char_key] != map_index[word_key]:
                return False
        return True
