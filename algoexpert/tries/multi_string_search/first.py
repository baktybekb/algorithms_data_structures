# O(b^2 + nw) time | O(b^2 + n) space
# n - length of smallStrings, b - length of bigString, w - length of the longest word
def multiStringSearch(bigString, smallStrings):
    trie = Trie()
    trie.add(bigString)
    found = [False] * len(smallStrings)
    for i in range(len(smallStrings)):
        if smallStrings[i][0] not in trie.root:
            continue
        node = trie.root
        failed = False
        for char in smallStrings[i]:
            if char not in node:
                failed = True
                break
            node = node[char]
        if failed:
            continue
        found[i] = True
    return found


class Trie:
    def __init__(self):
        self.root = {}
        self.end = '*'

    def add(self, string):
        for i in reversed(range(len(string))):
            node = self.root
            for j in range(i, len(string)):
                char = string[j]
                if char not in node:
                    node[char] = {}
                node = node[char]
            node[self.end] = True

