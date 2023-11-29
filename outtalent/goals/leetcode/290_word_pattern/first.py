# https://leetcode.com/problems/word-pattern/description/

# O(p + s) time | O(k) space, k --> unique keys in map
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        char_map, word_map = {}, {}
        for idx, char in enumerate(pattern):
            word = words[idx]
            if char in char_map:
                if char_map[char] != word:
                    return False
            else:
                if word in word_map:
                    return False
                char_map[char] = word
                word_map[word] = char
        return True
