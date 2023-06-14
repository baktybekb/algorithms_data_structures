def generateDocument(characters, document):
    counter = {}
    for char in characters:
        if char not in counter:
            counter[char] = 0
        counter[char] += 1
    for char in document:
        if char not in counter or counter[char] < 1:
            return False
        counter[char] -= 1
    return True
