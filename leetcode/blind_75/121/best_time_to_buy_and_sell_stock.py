from typing import List


class Solution:
    # O(n) time | O(1) space
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit


if __name__ == '__main__':
    solution = Solution()
    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5

