from typing import List


# O(n) time | O(1) space
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_square = 0
        while l < r:
            max_square = max(
                max_square,
                min(height[l], height[r]) * (r - l)
            )
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_square


if __name__ == '__main__':
    sol = Solution()
    assert sol.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
