# https://www.algoexpert.io/questions/longest-substring-without-duplication

# O(n) time | O(min(a, n)) space
# a = is the length of character alphabet in input string, i.e length of `sub_set`
def longestSubstringWithoutDuplication(string):
    sub_set = set()
    l = 0
    res_l = res_r = 0
    for r in range(len(string)):
        while string[r] in sub_set:
            sub_set.remove(string[l])
            l += 1
        sub_set.add(string[r])
        if r - l > res_r - res_l:
            res_l, res_r = l, r
    return string[res_l:res_r + 1]


if __name__ == '__main__':
    assert longestSubstringWithoutDuplication("clementisacap") == 'mentisac'
    assert longestSubstringWithoutDuplication("abc") == 'abc'
    assert longestSubstringWithoutDuplication("abcbde") == 'cbde'
