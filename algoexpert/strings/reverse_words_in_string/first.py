# https://www.algoexpert.io/questions/reverse-words-in-string

# O(n) time | O(n) space
def reverseWordsInString(string):
    res = []
    l = 0
    while l < len(string):
        r = l

        while r < len(string) and string[r] != ' ':
            r += 1
        res.append(string[l:r])
        l = r

        while r < len(string) and string[r] == ' ':
            r += 1
        res.append(string[l:r])
        l = r

    reverse_list(res, 0, len(res) - 1)
    return ''.join(res)


def reverse_list(array, l, r):
    while l < r:
        array[l], array[r] = array[r], array[l]
        l += 1
        r -= 1


if __name__ == '__main__':
    assert reverseWordsInString("AlgoExpert is the best!") == 'best! the is AlgoExpert'

