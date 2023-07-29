# O(v + e) time | O(v) space
def cycleInGraph(edges):
    """
    white = 0
    grey = 1
    black = 2
    """
    in_stack = [0] * len(edges)
    for i in range(len(edges)):
        if dfs(i, edges, in_stack):
            return True
    return False


def dfs(i, edges, in_stack):
    in_stack[i] = 1
    for neighbor in edges[i]:
        if in_stack[neighbor] == 0:
            if dfs(neighbor, edges, in_stack):
                return True
        elif in_stack[neighbor] == 2:
            continue
        else:
            return True
    in_stack[i] = 2
    return False


if __name__ == '__main__':
    assert cycleInGraph(
        edges=[
            [1, 3],
            [2, 3, 4],
            [0],
            [],
            [2, 5],
            []
        ]
    ) is True

