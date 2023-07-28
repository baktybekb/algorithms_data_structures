class WordDictionary:

    def __init__(self):
        self.root = {}
        self.end_symbol = '*'

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.end_symbol] = word

    def search(self, word: str) -> bool:
        def dfs(i, root):
            node = root
            for j in range(i, len(word)):
                char = word[j]
                if char == '.':
                    for child in node.values():
                        if dfs(j + 1, child):
                            return True
                    return False
                else:
                    if char not in node:
                        return False
                    node = node[char]
            return True if self.end_symbol in node else False
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


if __name__ == '__main__':
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("ba")
    wd.search("ba.")
