from typing import List


# O(n) time | O(n) space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        multiplier = 1
        for i in range(len(nums)):
            result[i] *= multiplier
            multiplier *= nums[i]
        multiplier = 1
        for i in reversed(range(len(nums))):
            result[i] *= multiplier
            multiplier *= nums[i]
        return result


if __name__ == '__main__':
    sol = Solution()
    assert sol.productExceptSelf(nums=[1, 2, 3, 4]) == [24, 12, 8, 6]
