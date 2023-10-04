# https://www.algoexpert.io/questions/generate-document

# O(n + m) time | O(c) space
# c -- number of unique characters in `characters` -- or number of keys in `mapper`
def generateDocument(characters, document):
    if document == '':
        return True
    mapper = {}
    for char in characters:
        mapper[char] = mapper.get(char, 0) + 1
    for char in document:
        if char not in mapper or mapper[char] == 0:
            return False
        mapper[char] -= 1
    return True


if __name__ == '__main__':
    assert generateDocument("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!") == True

