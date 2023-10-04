# https://www.algoexpert.io/questions/longest-palindromic-substring

# O(n ^ 2) time | O(n) space
def longestPalindromicSubstring(string):
    start, end = 0, 1
    for i in range(len(string)):
        odd = helper(string, i - 1, i + 1)
        even = helper(string, i - 1, i)
        l, r = max(odd, even, key=lambda x: x[1] - x[0])
        if r - l <= end - start:
            continue
        start, end = l, r
    return string[start + 1:end]


def helper(string, l, r):
    while l >= 0 and r < len(string):
        if string[l] != string[r]:
            break
        l -= 1
        r += 1
    return l, r


if __name__ == '__main__':
    assert longestPalindromicSubstring("abaxyzzyxf") == 'xyzzyx'
