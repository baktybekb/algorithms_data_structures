# https://leetcode.com/problems/reconstruct-itinerary/description/

from typing import List


# O(nlog(n)) time | O(n) space
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjacent_map = {}
        for source, dest in tickets:
            if source not in adjacent_map:
                adjacent_map[source] = []
            adjacent_map[source].append(dest)
        for source in adjacent_map:
            adjacent_map[source].sort(reverse=True)
        itinerary = []

        def dfs(source):
            while source in adjacent_map and adjacent_map[source]:
                dfs(adjacent_map[source].pop())
            itinerary.append(source)

        dfs('JFK')
        return itinerary[::-1]
