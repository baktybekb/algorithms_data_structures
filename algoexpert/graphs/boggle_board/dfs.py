# https://www.algoexpert.io/questions/boggle-board

# O(n * m * 8^s + ws) time | O(n * m + ws)
# s - length of the longest string in words, w - length of list of words
def boggleBoard(board, words):
    trie = Trie()
    for word in words:
        trie.add(word)
    rows, cols = len(board), len(board[0])
    visited, result = set(), set()
    steps = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1))

    def dfs(row, col, node):
        if board[row][col] not in node:
            return
        place = (row, col)
        if place in visited:
            return
        visited.add(place)
        node = node[board[row][col]]
        if trie.end in node:
            result.add(node[trie.end])
        for r, c in steps:
            new_row, new_col = row + r, col + c
            if not 0 <= new_row < rows or not 0 <= new_col < cols:
                continue
            dfs(new_row, new_col, node)
        visited.remove(place)

    for row in range(rows):
        for col in range(cols):
            dfs(row, col, trie.root)
    return list(result)


class Trie:
    def __init__(self):
        self.root = {}
        self.end = '#'

    def add(self, word):
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.end] = word
