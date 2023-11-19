# https://leetcode.com/problems/longest-palindromic-substring/description/

# O(n^2) time | O(n) space
class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = end = 0
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > end - start:
                start = l + 1
                end = r - 1

            l, r = i - 1, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > end - start:
                start = l + 1
                end = r - 1
        return s[start:end + 1]
