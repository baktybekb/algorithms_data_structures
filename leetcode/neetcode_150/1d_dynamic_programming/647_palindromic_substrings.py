# https://leetcode.com/problems/palindromic-substrings/description/


# O(n^2) time | O(1) space
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += self.count_palindrome(i, i, s)
            count += self.count_palindrome(i - 1, i, s)
        return count

    def count_palindrome(self, l, r, s):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            count += 1
        return count


