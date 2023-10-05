# https://www.algoexpert.io/questions/minimum-characters-for-words

# O(n * m) time | O(k) space
# k --> number of keys in `total` hash_table
def minimumCharactersForWords(words):
    total = {}
    for word in words:
        word_map = {}
        for char in word:
            word_map[char] = word_map.get(char, 0) + 1
        for key in word_map:
            if key not in total:
                total[key] = word_map[key]
                continue
            if word_map[key] <= total[key]:
                continue
            total[key] = word_map[key]
    res = []
    for char, freq in total.items():
        for _ in range(freq):
            res.append(char)
    return res


if __name__ == '__main__':
    assert minimumCharactersForWords(["this", "that", "did", "deed", "them!", "a"]) == [
        "t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"
    ]

