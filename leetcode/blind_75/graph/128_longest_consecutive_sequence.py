from typing import List

# O(n) time | O(n) space
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        sequence = 0
        for num in nums:
            if num - 1 not in num_set:
                i = 1
                while num + i in num_set:
                    i += 1
                sequence = max(sequence, i)
        return sequence
