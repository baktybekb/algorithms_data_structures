# https://leetcode.com/problems/longest-palindromic-substring/description/

# O(n^2) time | O(n) space
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_bound = [0, 0]
        for i in range(len(s)):
            self.check(i, i, s, res_bound)
            self.check(i - 1, i, s, res_bound)
        return s[res_bound[0]:res_bound[1] + 1]

    def check(self, l, r, s, res_bound):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        if r - l - 1 > res_bound[1] - res_bound[0]:
            res_bound[0] = l + 1
            res_bound[1] = r - 1
