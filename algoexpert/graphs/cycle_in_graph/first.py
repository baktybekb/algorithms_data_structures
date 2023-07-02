# O(v + e) time | O(v) space
def cycleInGraph(edges):
    visited = [False] * len(edges)
    in_stack = [False] * len(edges)
    for node in range(len(edges)):
        if visited[node]:
            continue
        if has_cycle(edges, visited, in_stack, node):
            return True
    return False


def has_cycle(edges, visited, in_stack, node):
    visited[node] = True
    in_stack[node] = True
    for neighbor in edges[node]:
        if not visited[neighbor]:
            if has_cycle(edges, visited, in_stack, neighbor):
                return True
        elif in_stack[neighbor]:
            return True
    in_stack[node] = False
