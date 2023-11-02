from typing import List


# O(log(min(n, m))) time | O(1) space
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        small = nums1 if len(nums1) <= len(nums2) else nums2
        big = nums1 if len(nums1) > len(nums2) else nums2
        left = 0
        right = len(small) - 1
        target = (len(small) + len(big) - 1) // 2
        while True:
            partition = (left + right) // 2
            big_partition = target - (partition + 1)

            small_left_max = small[partition] if partition >= 0 else float('-inf')
            small_right_min = small[partition + 1] if partition + 1 < len(small) else float('inf')
            big_left_max = big[big_partition] if big_partition >= 0 else float('-inf')
            big_right_min = big[big_partition + 1] if big_partition + 1 < len(big) else float('inf')

            if small_left_max > big_right_min:
                right = partition - 1
            elif big_left_max > small_right_min:
                left = partition + 1
            else:
                if (len(small) + len(big)) % 2 == 0:
                    return (max(small_left_max, big_left_max) + min(big_right_min, small_right_min)) / 2
                return max(small_left_max, big_left_max)


if __name__ == '__main__':
    sol = Solution()
    assert sol.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]) == 2.5
    assert sol.findMedianSortedArrays(nums1=[1], nums2=[]) == 1
