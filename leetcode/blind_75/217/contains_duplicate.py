from typing import List


class Solution:
    # O(n) time | O(n) space
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set()
        for num in nums:
            if num in unique_nums:
                return True
            unique_nums.add(num)
        return False


if __name__ == '__main__':
    solution = Solution()
    assert solution.containsDuplicate([1, 2, 3, 1]) == True
