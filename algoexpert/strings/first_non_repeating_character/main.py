# O(n) space | O(1) space
def firstNonRepeatingCharacter(string):
    counter = {}
    for char in string:
        counter[char] = counter.get(char, 0) + 1
    for i in range(len(string)):
        if counter[string[i]] == 1:
            return i
    return -1
