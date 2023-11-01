# https://www.algoexpert.io/questions/shortest-unique-prefixes

# O(ns) time | O(ns) space
# s - length of longest string, n - number of strings
def shortestUniquePrefixes(strings):
    trie = Trie()
    for word in strings:
        trie.insert(word)
    output = [0] * len(strings)
    for i, word in enumerate(strings):
        node = trie.root
        for j, char in enumerate(word):
            if node[char]['count'] == 1:
                output[i] = word[:j + 1]
                break
            node = node[char]
        if output[i] != 0:
            continue
        output[i] = word
    return output


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {'count': 0}
            node[char]['count'] += 1
            node = node[char]
