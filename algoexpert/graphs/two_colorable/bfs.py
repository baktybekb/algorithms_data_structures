# https://www.algoexpert.io/questions/two-colorable

from collections import deque


# O(v + e) time | O(v) space
def twoColorable(edges):
    colors = [None] * len(edges)  # 1 - white, 2 - black, None - wasn't processed yet

    def bfs(i, color):
        queue = deque([(i, color)])
        while queue:
            idx, color = queue.popleft()
            colors[idx] = color
            next_color = 1 if color == 2 else 2
            for dest in edges[idx]:
                if colors[dest] == next_color:
                    continue
                if colors[dest] == color:
                    return False
                queue.append((dest, next_color))
        return True

    return bfs(0, 1)
