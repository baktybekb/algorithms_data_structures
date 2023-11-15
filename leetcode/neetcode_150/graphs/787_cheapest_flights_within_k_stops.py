# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

from typing import List


# O(E * k) time | O(n) space
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n  # price values for each city
        prices[src] = 0
        for i in range(k + 1):
            current_iteration_prices = prices.copy()
            for source, destination, price in flights:
                if prices[source] == float('inf'):  # we still didn't reach this source, no reason to go further
                    continue
                if prices[source] + price < current_iteration_prices[destination]:
                    current_iteration_prices[destination] = prices[source] + price
            prices = current_iteration_prices
        return prices[dst] if prices[dst] != float('inf') else -1

