class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.num_sets = n

    # O(1) time nearly
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])  # updating parent == root for descendents, by using recursion
        return self.parent[x]

    # O(1) time nearly
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[px] < self.rank[py]:
            self.parent[px] = py
        else:
            self.parent[py] = px
            self.rank[px] += 1
        self.num_sets -= 1


def earliest_timestamp(n, logs):
    union_find = UnionFind(n)
    for timestamp, x, y in logs:
        union_find.union(x, y)
        if union_find.num_sets == 1:
            print(union_find.parent)
            print(union_find.rank)
            # all nums connected into one tree
            return timestamp
    return None


if __name__ == '__main__':
    logs = [(1, 4, 3), (2, 3, 8), (3, 6, 5), (4, 9, 4), (5, 2, 1), (6, 5, 0), (7, 7, 2), (8, 6, 1), (9, 7, 3)]
    n = 10
    print(earliest_timestamp(n, logs))
