from typing import List


# O(n) time | O(1) space
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        res = 0
        while l < r:
            if max_l <= max_r:
                l += 1
                if not l < r:
                    break
                diff = max_l - height[l]
                if diff > 0:
                    res += diff
                max_l = max(max_l, height[l])
            else:
                r -= 1
                if not l < r:
                    break
                diff = max_r - height[r]
                if diff > 0:
                    res += diff
                max_r = max(max_r, height[r])
        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert sol.trap(height=[4, 2, 0, 3, 2, 5]) == 9
