# O(n ^ 2) time | O(n) space
def countSquares(points):
    hash_set = set((tuple(i) for i in points))
    squares = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            point_a, point_b = points[i], points[j]
            mid_point = (
                (point_a[0] + point_b[0]) / 2,
                (point_a[1] + point_b[1]) / 2
            )
            if all(coord.is_integer() for coord in mid_point):
                mid_point = tuple(map(lambda x: int(x), mid_point))
            x_dist = point_a[0] - mid_point[0]
            y_dist = point_a[1] - mid_point[1]
            point_c = mid_point[0] + y_dist, mid_point[1] - x_dist
            point_d = mid_point[0] - y_dist, mid_point[1] + x_dist
            if point_c in hash_set and point_d in hash_set:
                squares += 1
    return squares / 2


if __name__ == '__main__':
    assert countSquares(
        [
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1],
        ]
    ) == 1
