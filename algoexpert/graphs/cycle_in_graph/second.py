# https://www.algoexpert.io/questions/cycle-in-graph

def cycleInGraph(edges):
    # 0 - not processed, 1 - in a process, 2 - finished (vertex doesn't make a cycle)
    marks = [0] * len(edges)

    def dfs(i):
        marks[i] = 1
        for dest in edges[i]:
            if marks[dest] == 2:
                continue
            if marks[dest] == 1 or dfs(dest):
                return True
        marks[i] = 2

    for i in range(len(edges)):
        if marks[i] == 2:
            continue
        if dfs(i):
            return True
    return False
