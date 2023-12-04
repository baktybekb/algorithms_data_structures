# https://leetcode.com/problems/summary-ranges/description/

from typing import List


# O(n) time | O(n) space
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        array = []
        i = 0
        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                i += 1
            if start == nums[i]:
                array.append(str(start))
            else:
                array.append(f'{start}->{nums[i]}')
            i += 1
        return array


if __name__ == '__main__':
    sol = Solution()
    assert sol.summaryRanges(nums=[0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
    assert sol.summaryRanges(nums=[0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]
