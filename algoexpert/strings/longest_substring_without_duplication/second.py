# https://www.algoexpert.io/questions/longest-substring-without-duplication

# O(n) time | O(min(a, n)) space
# a = is the length of character alphabet in input string, i.e length of `mapper`
def longestSubstringWithoutDuplication(string):
    mapper = {}
    l = 0
    res_l = res_r = 0
    for r, char in enumerate(string):
        if char in mapper:
            l = max(l, mapper[char] + 1)
        mapper[char] = r
        if r - l > res_r - res_l:
            res_l, res_r = l, r
    return string[res_l:res_r + 1]


if __name__ == '__main__':
    assert longestSubstringWithoutDuplication("clementisacap") == 'mentisac'
    assert longestSubstringWithoutDuplication("abc") == 'abc'
    assert longestSubstringWithoutDuplication("abcbde") == 'cbde'
