# https://leetcode.com/problems/happy-number/description/


class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1:
            current_sum = 0
            while n > 0:
                remainder = n % 10
                current_sum += remainder * remainder
                n = n // 10
            if current_sum in visited:
                return False
            visited.add(current_sum)
            n = current_sum
        return True


if __name__ == '__main__':
    sol = Solution()
    assert sol.isHappy(19) is True
    assert sol.isHappy(2) is False

