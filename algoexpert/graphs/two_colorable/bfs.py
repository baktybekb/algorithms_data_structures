# O(v + e) time | O(v) time
def twoColorable(edges: list[list[int]]):
    queue = [0]
    colors = [None] * len(edges)
    while queue:
        idx = queue.pop(0)  # O(1) in a theory
        if colors[idx] is None:
            colors[idx] = False
        for neighbor in edges[idx]:
            if colors[neighbor] is None:
                colors[neighbor] = not colors[idx]
                queue.append(neighbor)
            elif colors[neighbor] == colors[idx]:
                return False
    return True


if __name__ == '__main__':
    assert twoColorable(edges=[
        [1, 2],
        [0, 2, 3],
        [0, 1, 3],
        [1, 2]
    ]) is False
