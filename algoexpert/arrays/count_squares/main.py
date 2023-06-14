# O(n^2) time | O(n) space
def countSquares(points):
    points_set = set()
    for point in points:
        points_set.add(point_to_str(point))
    count = 0
    for point_a in points:
        for point_b in points:
            if point_a == point_b:
                continue
            mid_point = [(point_a[0] + point_b[0]) / 2, (point_a[1] + point_b[1]) / 2]
            x_distance = point_a[0] - mid_point[0]
            y_distance = point_a[1] - mid_point[1]
            point_c = [mid_point[0] - y_distance, mid_point[1] + x_distance]
            point_d = [mid_point[0] + y_distance, mid_point[1] - x_distance]
            if point_to_str(point_c) in points_set and point_to_str(point_d) in points_set:
                count += 1
    return count / 4


def point_to_str(point):
    if point[0] % 1 == 0 and point[1] % 1 == 0:
        point = [int(coordinate) for coordinate in point]
    return '.'.join([str(coordinate) for coordinate in point])
