from typing import List


# O(n) time | O(n) space
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        array = []
        for i in range(2):
            for n in nums:
                array.append(n)
        return array
