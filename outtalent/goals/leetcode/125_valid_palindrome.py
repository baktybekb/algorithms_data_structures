# https://leetcode.com/problems/valid-palindrome/description/

# O(n) time | O(1) space
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if not self.is_valid(s[left]):
                left += 1
            elif not self.is_valid(s[right]):
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        return True

    def is_valid(self, char):
        code = ord(char)
        return (
            ord('a') <= code <= ord('z') or
            ord('A') <= code <= ord('Z') or
            ord('0') <= code <= ord('9')
        )

