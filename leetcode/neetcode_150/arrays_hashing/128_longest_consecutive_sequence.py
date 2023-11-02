from typing import List


# O(n) time | O(n) space
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
        longest = 0
        for num in nums:
            if num - 1 in nums_set:
                continue
            i = 1
            while num + i in nums_set:
                i += 1
            longest = max(longest, i)
        return longest


if __name__ == '__main__':
    sol = Solution()
    assert sol.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]) == 4
