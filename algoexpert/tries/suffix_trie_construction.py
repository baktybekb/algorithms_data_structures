# https://www.algoexpert.io/questions/suffix-trie-construction

class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    # O(n^2) time | O(n^2) space
    def populateSuffixTrieFrom(self, string):
        for i in reversed(range(len(string))):
            node = self.root
            for j in range(i, len(string)):
                char = string[j]
                if char not in node:
                    node[char] = {}
                node = node[char]
            node[self.endSymbol] = True

    # O(m) space | O(1) space
    def contains(self, string):
        node = self.root
        for char in string:
            if char not in node:
                return False
            node = node[char]
        return self.endSymbol in node
