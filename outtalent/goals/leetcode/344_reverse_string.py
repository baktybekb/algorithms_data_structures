# https://leetcode.com/problems/reverse-string/description/

from typing import List


# O(n) time | O(1) space
class Solution:
    def reverseString(self, array: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(array) - 1
        while l < r:
            array[l], array[r] = array[r], array[l]
            l += 1
            r -= 1

