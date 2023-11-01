def longestMostFrequentPrefix(strings):
    trie = Trie()
    for word in strings:
        trie.insert(word)
    return trie.prefix_word[:trie.prefix_length]


class Trie:
    def __init__(self):
        self.root = {}
        self.prefix_count = 0
        self.prefix_length = 0
        self.prefix_word = 0

    def insert(self, word):
        node = self.root
        for i, char in enumerate(word):
            if char not in node:
                node[char] = {'count': 0}
            node = node[char]
            node['count'] += 1
            if node['count'] > self.prefix_count:
                self.prefix_count = node['count']
                self.prefix_length = i + 1
                self.prefix_word = word
            elif node['count'] == self.prefix_count and i + 1 > self.prefix_length:
                self.prefix_length = i + 1
                self.prefix_word = word
