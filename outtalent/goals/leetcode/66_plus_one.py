# https://leetcode.com/problems/plus-one/description/

from typing import List


# O(n) time | O(1) space
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        remainder = 1
        for i in reversed(range(len(digits))):
            if remainder == 0:
                continue
            value = digits[i] + remainder
            if value == 10:
                digits[i] = 0
            else:
                digits[i] = value
                remainder = 0
        if remainder == 0:
            return digits
        digits.append(remainder)
        digits[0], digits[-1] = digits[-1], digits[0]
        return digits
