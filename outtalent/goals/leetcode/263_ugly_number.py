# https://leetcode.com/problems/ugly-number/description/


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for option in (2, 3, 5):
            while n % option == 0:
                n = n // option
        return n == 1


if __name__ == '__main__':
    assert Solution().isUgly(18) is True


