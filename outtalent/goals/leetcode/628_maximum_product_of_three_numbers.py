# https://leetcode.com/problems/maximum-product-of-three-numbers/description/

from functools import reduce
from typing import List


# O(n) time | O(1) space
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max_array = [float('-inf')] * 3
        min_array = [float('inf')] * 2
        for num in nums:
            self.fill_the_array(max_array, num, True)
            self.fill_the_array(min_array, num, False)
        return max(
            reduce(self.product, max_array),
            reduce(self.product, min_array) * max_array[-1]
        )

    def product(self, x, y):
        return x * y

    def fill_the_array(self, array, value, search_max):
        length = 3 if search_max else 2
        for i in reversed(range(length)):
            if search_max:
                if array[i] > value:
                    continue
            else:
                if array[i] < value:
                    continue

            for j in range(i):
                array[j] = array[j + 1]
            array[i] = value
            break
