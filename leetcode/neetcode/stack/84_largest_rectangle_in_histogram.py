from typing import List


# O(n) time | O(n) space
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                j, hei = stack.pop()
                area = max(area, hei * (i - j))
                start = j
            stack.append((start, height))
        while stack:
            i, hei = stack.pop()
            area = max(area, hei * (len(heights) - i))
        return area


if __name__ == '__main__':
    solution = Solution()
    assert solution.largestRectangleArea(heights=[2, 1, 5, 6, 2, 3]) == 10
    assert solution.largestRectangleArea(heights=[2, 4]) == 4
    assert solution.largestRectangleArea(heights=[2, 1, 2]) == 3
    assert solution.largestRectangleArea(heights=[3, 6, 5, 7, 4, 8, 1, 0]) == 20
