# https://leetcode.com/problems/climbing-stairs/description/

# O(n) time | O(n) space
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        return self.helper(n, cache)

    def helper(self, n, cache):
        if n in cache:
            return cache[n]
        if n == 1:
            return 1
        if n == 2:
            return 2
        cache[n] = self.helper(n - 1, cache) + self.helper(n - 2, cache)
        return cache[n]


if __name__ == '__main__':
    Solution().climbStairs(10)
