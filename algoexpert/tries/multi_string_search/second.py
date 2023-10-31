# O(wn + bw) time | O(wn) space
# n - length of smallStrings, w - length of the longest word, b - length of the bigString
def multiStringSearch(bigString, smallStrings):
    trie = Trie()
    for i, word in enumerate(smallStrings):
        trie.add(word, i)
    found = [False] * len(smallStrings)
    for i in range(len(bigString)):
        if bigString[i] not in trie.root:
            continue
        j = i
        node = trie.root
        while j < len(bigString) and bigString[j] in node:
            if trie.end in node:
                found[node[trie.end]] = True
            node = node[bigString[j]]
            j += 1
        if trie.end not in node:
            continue
        found[node[trie.end]] = True
    return found


class Trie:
    def __init__(self):
        self.root = {}
        self.end = '*'

    def add(self, word, idx):
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.end] = idx
