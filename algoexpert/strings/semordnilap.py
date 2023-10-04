# https://www.algoexpert.io/questions/semordnilap

# O(n * m) time | O(n * m) space
def semordnilap(words):
    word_set = set(words)
    res = []
    for word in words:
        reverse = word[::-1]  # O(m) time | O(m) space
        if reverse in word_set and reverse != word:
            res.append([word, reverse])
            word_set.remove(word)
            word_set.remove(reverse)
    return res


if __name__ == '__main__':
    assert semordnilap(["dog", "hello", "god"]) == [['dog', 'god']]
