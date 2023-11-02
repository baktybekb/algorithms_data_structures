from typing import List


# O(n) time | O(1) space
class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        left_max = [0] * length
        right_max = [0] * length
        min_lr = [0] * length
        for i in range(1, length):
            left_max[i] = max(left_max[i - 1], height[i - 1])
        for i in reversed(range(length - 1)):
            right_max[i] = max(right_max[i + 1], height[i + 1])
        for i in range(length):
            min_lr[i] = min(left_max[i], right_max[i])
        res = 0
        for i in range(length):
            diff = min_lr[i] - height[i]
            if diff > 0:
                res += diff
        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert sol.trap(height=[4, 2, 0, 3, 2, 5]) == 9
