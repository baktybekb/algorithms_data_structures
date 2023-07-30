# O(v + e) time | O(v) space
def twoColorable(edges):
    colors = [None] * len(edges)
    return dfs(0, edges, colors)


def dfs(i, edges, colors):
    if colors[i] is None:
        colors[i] = False
    for neighbor in edges[i]:
        if colors[neighbor] is None:
            colors[neighbor] = not colors[i]
            if not dfs(neighbor, edges, colors):
                return False
        elif colors[neighbor] == colors[i]:
            return False
    return True
