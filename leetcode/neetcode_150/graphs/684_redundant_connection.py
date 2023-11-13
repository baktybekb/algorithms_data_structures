# https://leetcode.com/problems/redundant-connection/description/

from typing import List


# O(n) time | O(n) space
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union_find = UnionFind(len(edges))
        for edge in edges:
            one, two = edge
            if union_find.find(one) == union_find.find(two):
                return edge
            union_find.union(one, two)


class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        for value in range(1, n + 1):
            self.parent[value] = value
            self.rank[value] = 0

    # ~O(1) time
    def find(self, value):
        if value not in self.parent:
            return
        if value != self.parent[value]:
            self.parent[value] = self.find(self.parent[value])
        return self.parent[value]

    # ~O(1) time
    def union(self, value1, value2):
        root1, root2 = self.find(value1), self.find(value2)
        if root1 is None or root2 is None:
            return
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1


