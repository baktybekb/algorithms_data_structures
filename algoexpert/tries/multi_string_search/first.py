# O(b^2 + ns) time | O(b^2 + n)
def multiStringSearch(bigString, smallStrings):
    """
    n = length of smallStrings
    s = the longest string in smallStrings
    b = bigString
    """
    trie = Trie()
    trie.build(bigString)
    result = [True] * len(smallStrings)
    for i, string in enumerate(smallStrings):
        if trie.contains(string):
            continue
        result[i] = False
    return result


class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = '*'

    def build(self, string):
        for i in range(len(string)):
            node = self.root
            for j in range(i, len(string)):
                letter = string[j]
                if letter not in node:
                    node[letter] = {}
                node = node[letter]

    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return True
