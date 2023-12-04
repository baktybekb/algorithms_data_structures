# https://leetcode.com/problems/valid-palindrome-ii/description/

# O(n) time | O(1) space
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                if self.is_palindrome(l + 1, r, s):
                    return True
                if self.is_palindrome(l, r - 1, s):
                    return True
                return False
            l += 1
            r -= 1
        return True

    def is_palindrome(self, l, r, s):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

