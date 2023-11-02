from typing import List


# O(n) time | O(1) space
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total < target:
                l += 1
            elif total > target:
                r -= 1
            else:
                return [l + 1, r + 1]


if __name__ == '__main__':
    sol = Solution()
    assert sol.twoSum(numbers=[2, 7, 11, 15], target=9) == [1, 2]
