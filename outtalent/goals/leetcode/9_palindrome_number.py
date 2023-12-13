# https://leetcode.com/problems/palindrome-number/description/

# O(n) time | O(1) space, n - length of x number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x > 0):
            return False
        y, copy = 0, x
        while x > 0:
            remainder = x % 10
            y = y * 10 + remainder
            x = x // 10
        return y == copy


if __name__ == '__main__':
    assert Solution().isPalindrome(x=121) is True
