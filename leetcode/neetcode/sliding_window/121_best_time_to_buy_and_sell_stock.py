from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] <= prices[r]:
                profit = max(profit, prices[r] - prices[l])
                r += 1
            else:
                l = r
                r += 1
        return profit


if __name__ == '__main__':
    sol = Solution()
    assert sol.maxProfit(prices=[7, 1, 5, 3, 6, 4]) == 5
    assert sol.maxProfit(prices=[7, 6, 4, 3, 1]) == 0
