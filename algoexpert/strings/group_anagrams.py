# https://www.algoexpert.io/questions/group-anagrams

# O(n * mlog(m)) time | O(n * m) space
def groupAnagrams(words):
    mapper = {}
    for word in words:
        sorted_word = ''.join(sorted(word))  # O(mlog(m)) time
        if sorted_word in mapper:
            mapper[sorted_word].append(word)
        else:
            mapper[sorted_word] = [word]
    return list(mapper.values())


if __name__ == '__main__':
    assert groupAnagrams(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]) == [
        ["yo", "oy"],
        ["act", "tac", "cat"],
        ["flop", "olfp"],
        ["foo"]
    ]
