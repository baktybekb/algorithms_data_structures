# https://www.algoexpert.io/questions/two-colorable

# O(v + e) time | O(v) space
def twoColorable(edges):
    colors = [None] * len(edges)  # 1 - white, 2 - black, None - wasn't processed yet

    def dfs(idx, color):
        colors[idx] = color
        next_color = 1 if color == 2 else 2
        for dest in edges[idx]:
            if colors[dest] == next_color:
                continue
            if colors[dest] == color or not dfs(dest, next_color):
                return False
        return True

    return dfs(0, 1)

