from typing import List


# O(log(n)) time | O(1) space
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1


if __name__ == '__main__':
    solution = Solution()
    assert solution.search(nums=[-1, 0, 3, 5, 9, 12], target=9) == 4
