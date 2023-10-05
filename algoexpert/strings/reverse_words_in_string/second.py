# https://www.algoexpert.io/questions/reverse-words-in-string

# O(n) time | O(n) space --> better solution
def reverseWordsInString(string):
    array = list(string)
    reverse_list(array, 0, len(array) - 1)
    l = 0
    while l < len(array):
        r = l
        while r < len(array) and array[r] != ' ':
            r += 1
        reverse_list(array, l, r - 1)
        l = r + 1
    return ''.join(array)


def reverse_list(array, l, r):
    while l < r:
        array[l], array[r] = array[r], array[l]
        l += 1
        r -= 1


if __name__ == '__main__':
    assert reverseWordsInString("AlgoExpert is the best!") == 'best! the is AlgoExpert'
