# https://leetcode.com/problems/keyboard-row/description/

from typing import List


# O(n * m) time | O(n) space, n - len(words), m - length of the longest word
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        data = ('qwertyuiop', 'asdfghjkl', 'zxcvbnm')
        char_map = {}
        for i in range(len(data)):
            for char in data[i]:
                char_map[char] = i
        res = []
        for word in words:
            if all(char_map[word[0].lower()] == char_map[char.lower()] for char in word):
                res.append(word)
        return res

