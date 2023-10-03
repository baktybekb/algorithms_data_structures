# https://www.algoexpert.io/questions/caesar-cipher-encryptor

# O(n) time | O(n) space
def caesarCipherEncryptor(string, key):
    key = key % 26
    res = []
    for char in string:
        new_code = ord(char) + key
        new_code = new_code if new_code <= 122 else new_code - 26
        res.append(chr(new_code))
    return ''.join(res)


