from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # left sorted side
            if nums[l] < nums[mid]:
                # left sorted side
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # right sorted side
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


if __name__ == '__main__':
    sol = Solution()
    assert sol.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0) == 4
    assert sol.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3) == -1
    assert sol.search(nums=[4, 5, 6, 7, 8, 1, 2, 3], target=8) == 4
