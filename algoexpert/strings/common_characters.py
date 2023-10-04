# https://www.algoexpert.io/questions/common-characters

# O(n * m) time | O(m) space
def commonCharacters(strings):
    index = 0
    for i in range(1, len(strings)):
        if len(strings[i]) < len(strings[index]):
            index = i
    smallest = set(strings[index])
    for i in range(len(strings)):
        if i == index:
            continue
        string_set = set(strings[i])
        smallest = {char for char in smallest if char in string_set}
    return list(smallest)


