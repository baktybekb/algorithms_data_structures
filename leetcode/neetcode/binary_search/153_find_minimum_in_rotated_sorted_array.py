from typing import List


# O(log(n)) time | O(1) space
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] < nums[r]:
                r = mid - 1
            else:
                l = mid + 1
        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.findMin(nums=[3, 4, 5, 1, 2]) == 1
    assert sol.findMin(nums=[11, 13, 15, 17]) == 11
