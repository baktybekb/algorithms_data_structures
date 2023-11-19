# https://leetcode.com/problems/min-cost-climbing-stairs/description/

from typing import List


# O(n) time | O(1) space
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 2], cost[i - 1])
        return cost[-1]


if __name__ == '__main__':
    sol = Solution()
    assert sol.minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
    assert sol.minCostClimbingStairs(cost=[10, 15, 20]) == 15
