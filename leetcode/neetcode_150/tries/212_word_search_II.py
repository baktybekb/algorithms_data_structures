# https://leetcode.com/problems/word-search-ii/description/

from typing import List


# O(n * m) time | O(n * m) space
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add_word(word)
        found, visited = set(), set()

        def dfs(row, col, root):
            visited.add((row, col))
            root = root[board[row][col]]
            if trie.end in root:
                found.add(root[trie.end])
            for r_step, c_step in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                new_row, new_col = row + r_step, col + c_step
                if not 0 <= new_row < len(board) or not 0 <= new_col < len(board[0]):
                    continue
                if (new_row, new_col) in visited or board[new_row][new_col] not in root:
                    continue
                dfs(new_row, new_col, root)
            visited.remove((row, col))

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] not in trie.root:
                    continue
                dfs(row, col, trie.root)
        return list(found)


class Trie:
    def __init__(self):
        self.root = {}
        self.end = '*'

    def add_word(self, word):
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.end] = word

