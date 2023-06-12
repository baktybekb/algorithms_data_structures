import unittest

"""
Problem:
    Union-find with specific canonical element.
    Add method find() to the union-find data type so that find(i)
    returns the largest element in the connected component containing i.
    The operations, union(), connected(), and find() should all take logarithmic time or better.
    For example, if one of the connected components is {1, 2, 6, 9}, then the find() method should return 9
    for each of the four elements in the connected components.
    use python
"""


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.max = list(range(n))

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
            self.max[root_y] = max(self.max[root_y], self.max[root_x])
            return
        self.parent[root_y] = root_x
        self.max[root_x] = max(self.max[root_x], self.max[root_y])
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def find_max(self, x):
        return self.max[self.find(x)]


class TestClass(unittest.TestCase):

    def test_case(self):
        union_find = UnionFind(10)
        logs = [(1, 4, 3), (2, 3, 8), (3, 6, 5), (4, 9, 4), (5, 2, 1), (6, 5, 0), (7, 7, 2), (8, 6, 1), (9, 7, 3)]
        for _, x, y in logs:
            union_find.union(x, y)
        self.assertEqual(9, union_find.find_max(9))

    def test_case_second(self):
        union_find = UnionFind(9)
        logs = [(1, 4, 3), (2, 3, 8), (3, 6, 5), (4, 8, 4), (5, 2, 1), (6, 5, 0), (7, 7, 2), (8, 6, 1)]
        for _, x, y in logs:
            union_find.union(x, y)
        self.assertEqual(8, union_find.find_max(4))
        self.assertEqual(7, union_find.find_max(2))
