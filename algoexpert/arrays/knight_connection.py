import math


# O(n * m) time | O(n * m) space
def knightConnection(knightA, knightB):
    moves = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))
    visited = set()
    queue = [(0, *knightA)]
    while queue:
        depth, x, y = queue.pop(0)  # O(1) in a theory
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if [x, y] == knightB:
            return math.ceil(depth / 2)
        for x_move, y_move in moves:
            new_x, new_y = x + x_move, y + y_move
            queue.append((depth + 1, new_x, new_y))


if __name__ == '__main__':
    knightConnection([3, 3], [0, 0])
