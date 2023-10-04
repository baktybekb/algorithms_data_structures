# O(n) time | O(1) space
def firstNonRepeatingCharacter(string):
    mapper = {}
    for char in string:
        mapper[char] = mapper.get(char, 0) + 1
    for i in range(len(string)):
        if mapper[string[i]] == 1:
            return i
    return -1


if __name__ == '__main__':
    assert firstNonRepeatingCharacter("abcdcaf") == 1

