from typing import List


# O(n) time | O(n) space
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mapper = set()
        for num in nums:
            if num in mapper:
                return True
            mapper.add(num)
        return False
