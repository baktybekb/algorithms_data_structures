def boggleBoard(board, words):
    """
    O(rc * 8^l + wl) time | O(rc + wl) space
    r - rows, c - columns, w - words count, l - length of the longest string in words

    wl - Trie() construction
    8^l - 8 recursive calls for letter on board, at most `l` times
    """

    trie = Trie()
    for word in words:
        trie.add(word)
    visited = [[False for col in row] for row in board]
    found_words = {}
    for row in range(len(board)):
        for col in range(len(board[row])):
            explore(row, col, board, visited, trie.root, found_words)
    return list(found_words.keys())


def explore(row, col, board, visited, trie, found_words):
    if visited[row][col]:
        return
    letter = board[row][col]
    if letter not in trie:
        return
    visited[row][col] = True
    trie = trie[letter]
    if '*' in trie:
        found_words[trie['*']] = ''
    for new_row, new_col in get_neighbors(row, col, board, visited):
        explore(new_row, new_col, board, visited, trie, found_words)
    visited[row][col] = False


def get_neighbors(row, col, board, visited):
    neighbors = []
    steps = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1))
    for r, c in steps:
        new_row, new_col = row + r, col + c
        if not 0 <= new_row < len(board) or not 0 <= new_col < len(board[new_row]):
            continue
        if visited[new_row][new_col]:
            continue
        neighbors.append((new_row, new_col))
    return neighbors


class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = '*'

    def add(self, string):
        node = self.root
        for i in range(len(string)):
            letter = string[i]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.end_symbol] = string
