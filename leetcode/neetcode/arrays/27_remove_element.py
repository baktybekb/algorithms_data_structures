from typing import List


# O(n) time | O(1) space
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


if __name__ == '__main__':
    Solution().removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2)
