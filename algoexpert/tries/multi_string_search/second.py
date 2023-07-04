# O(ns + bs) time | O(ns)
def multiStringSearch(bigString, smallStrings):
    """
    n = length of smallStrings
    s = length of the longest string
    b = length of bigString
    """
    trie = Trie()
    for string in smallStrings:
        trie.add(string)
    contained = {}
    for i in range(len(bigString)):
        node = trie.root
        for j in range(i, len(bigString)):
            letter = bigString[j]
            if letter not in node:
                break
            node = node[letter]
            if 'c' in node:
                print(node)
            if trie.end_symbol in node:
                contained[node[trie.end_symbol]] = ''
    return [string in contained for string in smallStrings]


class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = '*'

    def add(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.end_symbol] = string
