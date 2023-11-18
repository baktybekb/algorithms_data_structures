# https://www.algoexpert.io/questions/kruskals-algorithm

# O(e * log(e)) time | O(e + v) space
def kruskalsAlgorithm(edges):
    sorted_edges = []
    for index, vertex in enumerate(edges):
        for edge in vertex:
            # no duplicated edges with the same (source, destination) and reverse
            # graph is undirected, so we need only one edge, (source --> dest) or (dest --> source)
            if edge[0] < index:
                continue
            sorted_edges.append([index, *edge])
    sorted_edges.sort(key=lambda x: x[-1])
    union_find = UnionFind(len(edges))
    output = [[] for _ in range(len(edges))]
    for edge in sorted_edges:
        if union_find.connected(edge[0], edge[1]):
            continue
        union_find.union(edge[0], edge[1])
        # creating 2 edges for output, (source -- > dest) and (dest --> source)
        output[edge[0]].append([edge[1], edge[2]])
        output[edge[1]].append([edge[0], edge[2]])
    return output


class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.rank = {i: 0 for i in range(n)}

    def find(self, value):
        if value not in self.parent:
            return
        if value != self.parent[value]:
            self.parent[value] = self.find(self.parent[value])
        return self.parent[value]

    def union(self, value1, value2):
        root_one, root_two = self.find(value1), self.find(value2)
        if root_one is None or root_two is None:
            return
        if self.rank[root_one] < self.rank[root_two]:
            self.parent[root_one] = root_two
        elif self.rank[root_one] > self.rank[root_two]:
            self.parent[root_two] = root_one
        else:
            self.parent[root_two] = root_one
            self.rank[root_one] += 1

    def connected(self, value1, value2):
        return self.find(value1) == self.find(value2)
