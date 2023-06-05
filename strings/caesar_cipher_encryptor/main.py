# O(n) time | O(n) space
def caesarCipherEncryptor(string, key):
    new_key = key % 26
    new_letters = []
    for letter in string:
        new_letters.append(get_letter(letter, new_key))
    return ''.join(new_letters)

def get_letter(letter, key):
    new_letter_code = ord(letter) + key
    return chr(new_letter_code if new_letter_code <= 122 else 96 + new_letter_code % 122)
