# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

from typing import List


# O(n) time | O(1) space
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.helper(nums, 0, len(nums) - 1, len(nums) - k)

    def helper(self, array, start, end, k):
        while start < end:
            pivot = start
            l, r = start + 1, end
            while l <= r:
                if array[r] < array[pivot] < array[l]:
                    self.swap(l, r, array)
                if array[l] <= array[pivot]:
                    l += 1
                if array[r] >= array[pivot]:
                    r -= 1
            self.swap(pivot, r, array)
            if r == k:
                return array[r]
            if r < k:
                start = r + 1
            else:
                end = r - 1
        return array[start]

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]
