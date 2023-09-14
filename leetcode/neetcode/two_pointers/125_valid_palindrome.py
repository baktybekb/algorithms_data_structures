# O(n) time | O(1) space
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.is_alphanum(s[l]):
                l += 1
            while l < r and not self.is_alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def is_alphanum(self, char):
        return (
                ord('a') <= ord(char) <= ord('z') or
                ord('A') <= ord(char) <= ord('Z') or
                ord('0') <= ord(char) <= ord('9')
        )
