# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

from typing import List


# O(n) time | O(1) space
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert_idx = 1
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                continue
            nums[insert_idx] = nums[i]
            insert_idx += 1
        return insert_idx


if __name__ == '__main__':
    Solution().removeDuplicates([1, 1, 2])


