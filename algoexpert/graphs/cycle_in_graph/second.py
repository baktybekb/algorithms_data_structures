# O(v + e) time | O(v) space
def cycleInGraph(edges):
    """
    0 white - not visited
    1 grey - visited
    2 black - not in stack, has no cycle, finished with that node
    """
    visited = [0] * len(edges)
    for node in range(len(edges)):
        if visited[node] >= 1:
            continue
        if has_cycle(edges, node, visited):
            return True
    return False


def has_cycle(edges, node, visited):
    visited[node] = 1
    for neighbor in edges[node]:
        if visited[neighbor] == 0:
            if has_cycle(edges, neighbor, visited):
                return True
        elif visited[neighbor] == 2:
            continue
        else:
            return True
    visited[node] = 2
    return False
