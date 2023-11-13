# Do not edit the class below except for
# the constructor and the createSet, find,
# and union methods. Feel free to add new
# properties and methods to the class.
class UnionFind:
    def __init__(self):
        self.parents = {}
        self.rank = {}

    # O(1) time
    def createSet(self, value):
        self.parents[value] = value
        self.rank[value] = 0

    # O(alpha(n) --> ~O(1)) time
    def find(self, value):
        if value not in self.parents:
            return
        if value != self.parents[value]:
            self.parents[value] = self.find(self.parents[value])
        return self.parents[value]

    # ~O(1) time
    def union(self, valueOne, valueTwo):
        root_one, root_two = self.find(valueOne), self.find(valueTwo)
        if root_one is None or root_two is None:
            return
        if self.rank[root_one] > self.rank[root_two]:
            self.parents[root_two] = root_one
        elif self.rank[root_one] < self.rank[root_two]:
            self.parents[root_one] = root_two
        else:
            self.parents[root_two] = root_one
            self.rank[root_one] += 1
