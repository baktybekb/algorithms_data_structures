def commonCharacters(strings):
    smallest = get_smallest_string(strings)
    porential_chars = set(smallest)
    for string in strings:
        helper(string, porential_chars)
    return porential_chars

def get_smallest_string(strings):
    smallest = strings[0]
    for i in range(1, len(strings)):
        if len(strings[i]) > len(smallest):
            smallest = strings[i]
    return smallest

def helper(string, porential_chars):
    for char in list(porential_chars):
        if char in set(string):
            continue
        porential_chars.remove(char)
