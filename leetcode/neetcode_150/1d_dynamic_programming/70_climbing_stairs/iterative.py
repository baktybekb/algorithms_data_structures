# https://leetcode.com/problems/climbing-stairs/description/

# O(n) time | O(1) space
class Solution:
    def climbStairs(self, n: int) -> int:
        current, prev = 1, 1
        for i in range(n - 1):
            temp = current
            current += prev
            prev = temp
        return current

