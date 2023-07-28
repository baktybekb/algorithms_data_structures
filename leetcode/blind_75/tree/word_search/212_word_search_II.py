from typing import List


# O(n * m * 4 * l) time | O(wl) space
# n - number of rows, m - number of columns
# w - number of words, l - the longest word
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        output = []

        def dfs(row, col, root):
            char = board[row][col]
            node = root[char]
            word = node.pop('*', False)
            if word:
                output.append(word)
            board[row][col] = '#'
            for r, c in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                new_row, new_col = row + r, col + c
                if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and board[new_row][new_col] in node:
                    dfs(new_row, new_col, node)
            board[row][col] = char
            if not node:
                root.pop(char)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in trie.root:
                    dfs(row, col, trie.root)
        return output


class Trie:
    def __init__(self):
        self.root = {}
        self.end = '*'

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.end] = word
