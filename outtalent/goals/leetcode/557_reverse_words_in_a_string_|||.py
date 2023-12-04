# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

# O(n) time | O(n) space
class Solution:
    def reverseWords(self, s: str) -> str:
        array = list(s)
        l = 0
        for r in range(len(s)):
            if r < len(s) - 1 and s[r] != ' ':
                continue
            start, end = l, r + (0 if r == len(s) - 1 else - 1)
            while start < end:
                array[start], array[end] = array[end], array[start]
                start += 1
                end -= 1
            l = r + 1
        return ''.join(array)
