from typing import List


# O(n + k) time | O(k) time, k - range of unique numbers
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        frequency = [0] * (max(heights) + 1)
        for height in heights:
            frequency[height] += 1
        for i in range(1, len(frequency)):
            frequency[i] += frequency[i - 1]
        sorted_heights = [0] * len(heights)
        for height in heights:
            sorted_heights[frequency[height] - 1] = height
            frequency[height] -= 1
        number = 0
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                number += 1
        return number
