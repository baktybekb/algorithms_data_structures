from typing import List

# https://leetcode.com/problems/missing-number/description/


# O(n) time | O(1) space
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        val = 0
        for i in range(len(nums) + 1):
            val ^= i
            if i < len(nums):
                val ^= nums[i]
        return val


if __name__ == '__main__':
    solution = Solution()
    assert solution.missingNumber([3, 0, 1]) == 2
