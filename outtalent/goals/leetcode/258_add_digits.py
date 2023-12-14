# https://leetcode.com/problems/add-digits/description/

# O(1) time and space
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        remainder = num % 9
        return 9 if remainder == 0 else remainder

