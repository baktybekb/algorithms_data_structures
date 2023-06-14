# Do not edit the class below except for
# the constructor and the createSet, find,
# and union methods. Feel free to add new
# properties and methods to the class.
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def createSet(self, value):
        self.parent[value] = value
        self.rank[value] = 0

    def find(self, value):
        if value not in self.parent:
            return
        if value != self.parent[value]:
            self.parent[value] = self.find(self.parent[value])
        return self.parent[value]

    def union(self, value_one, value_two):
        if value_one not in self.parent or value_two not in self.parent:
            return
        root_one, root_two = self.find(value_one), self.find(value_two)
        if root_one == root_two:
            return
        if self.rank[root_two] > self.rank[root_one]:
            self.parent[root_one] = root_two
        else:
            self.parent[root_two] = root_one
            if self.rank[root_one] == self.rank[root_two]:
                self.rank[root_one] += 1
