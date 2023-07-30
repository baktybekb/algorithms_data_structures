# O(8^l * wh + n * l) time | O(nl)
# l - longest word, w and h - width and height of board
# n - number of words
def boggleBoard(board, words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    found, visited = set(), set()

    def dfs(row, col, node):
        if (row, col) in visited:
            return
        if board[row][col] not in node:
            return
        visited.add((row, col))
        steps = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
        node = node[board[row][col]]
        if trie.end in node:
            found.add(node[trie.end])
        for r, c in steps:
            new_row, new_col = row + r, col + c
            if not 0 <= new_row < len(board) or not 0 <= new_col < len(board[new_row]):
                continue
            dfs(new_row, new_col, node)
        visited.remove((row, col))

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] not in trie.root:
                continue
            dfs(row, col, trie.root)
    return list(found)


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
