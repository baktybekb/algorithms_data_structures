# https://leetcode.com/problems/flipping-an-image/description/

from typing import List


# O(n * m) time | O(1) space
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in range(len(image)):
            array = image[row]
            l, r = 0, len(array) - 1
            while l < r:
                array[l], array[r] = array[r], array[l]
                l += 1
                r -= 1
        for row in range(len(image)):
            for col in range(len(image[0])):
                if image[row][col] == 0:
                    image[row][col] = 1
                else:
                    image[row][col] = 0
        return image

