import math

def knightConnection(knight_a, knight_b):
    steps = [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]
    queue = [[knight_a[0], knight_a[1], 0]]
    visited = {to_string(knight_a)}
    while True:
        position = queue.pop(0)  # O(1) time complexity in a theory
        if position[0] == knight_b[0] and position[1] == knight_b[1]:
            return math.ceil(position[2] / 2)
        for step in steps:
            next_position = [position[0] + step[0], position[1] + step[1]]
            str_position = to_string(next_position)
            if str_position in visited:
                continue
            next_position.append(position[2] + 1)
            queue.append(next_position)
            visited.add(str_position)
    return -1


def to_string(position):
    return '.'.join(map(str, position))
