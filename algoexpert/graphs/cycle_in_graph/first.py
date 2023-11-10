# https://www.algoexpert.io/questions/cycle-in-graph

# O(v + e) time | O(v) space
def cycleInGraph(edges):
    path = set()  # hash set for tracking visited vertices while dfs()
    processed = [False] * len(edges)  # list of vertices that does not make a cycle

    def dfs(idx):
        path.add(idx)
        for dest in edges[idx]:
            if processed[dest]:
                continue
            if dest in path or dfs(dest):
                return True
        path.remove(idx)
        processed[idx] = True

    for i in range(len(edges)):
        if processed[i]:
            continue
        if dfs(i):
            return True
    return False
