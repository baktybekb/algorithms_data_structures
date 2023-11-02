class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:

        def dfs(i, node):
            if i == len(word):
                return node.is_word
            char = word[i]
            if char == '.':
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True
                return False
            elif char in node.children:
                return dfs(i + 1, node.children[char])
            return False

        return dfs(0, self.root)



