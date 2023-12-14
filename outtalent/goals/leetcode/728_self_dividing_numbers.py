# https://leetcode.com/problems/self-dividing-numbers/description/

from typing import List


# O(n) time | O(n) space
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for val in range(left, right + 1):
            copy = val
            valid = True
            while copy > 0:
                remainder = copy % 10
                if remainder == 0 or val % remainder != 0:
                    valid = False
                    break
                copy = copy // 10
            if valid:
                res.append(val)
        return res


