from typing import List


# O(n ^ 2) time | O(n) space
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.threeSum(nums=[-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert sol.threeSum(nums=[0, 0, 0, 0]) == [[0, 0, 0]]
    assert sol.threeSum(nums=[-2, 0, 0, 2, 2]) == [[-2, 0, 2]]

