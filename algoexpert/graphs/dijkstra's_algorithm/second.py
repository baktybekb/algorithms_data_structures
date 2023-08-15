# O(v ^ 2 + e) time | O(v) space
def dijkstrasAlgorithm(start, edges):
    vertices_count = len(edges)
    min_distances = [float('inf') for i in range(vertices_count)]
    min_distances[start] = 0
    visited = set()
    while len(visited) != vertices_count:
        vertex, distance = get_min_distance_vertex(min_distances, visited)
        if distance == float('inf'):
            break
        visited.add(vertex)
        for edge in edges[vertex]:
            destination, distance_to_dest = edge
            if destination in visited:
                continue
            current_dest = min_distances[destination]
            new_path_dest = distance + distance_to_dest
            if new_path_dest >= current_dest:
                continue
            min_distances[destination] = new_path_dest
    return list(map(lambda x: -1 if x == float('inf') else x, min_distances))


def get_min_distance_vertex(distances, visited):
    distance = float('inf')
    vertex = None
    for vert, dist in enumerate(distances):
        if vert in visited:
            continue
        if dist < distance:
            distance = dist
            vertex = vert
    return vertex, distance


