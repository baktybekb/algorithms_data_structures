# O(v + e) time | O(v) space
def twoColorable(edges):
    colors = [None] * len(edges)
    stack = [0]
    while stack:
        node = stack.pop()
        if colors[node] is None:
            colors[node] = True
        for neighbor in edges[node]:
            if colors[neighbor] is None:
                colors[neighbor] = not colors[node]
                stack.append(neighbor)
            elif colors[neighbor] == colors[node]:
                return False
    return True
