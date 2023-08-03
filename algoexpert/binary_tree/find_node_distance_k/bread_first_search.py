# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(n) space
def findNodesDistanceK(tree, target, k):
    parents = {}
    find_parents(tree, None, parents)
    target_node = get_target_node(target, tree, parents)
    array = []
    bfs(target_node, k, array, parents)
    return array


def bfs(target_node, k, array, parents):
    queue = [(target_node, 0)]
    visited = set()
    while queue:
        node, distance = queue.pop(0)  # O(1) in a theory
        visited.add(node)
        if distance == k:
            array.append(node.value)
            array.extend((i[0].value for i in queue))
            return
        distance += 1
        for node in (node.left, node.right, parents[node.value]):
            if node is None:
                continue
            if node in visited:
                continue
            queue.append((node, distance))


def find_parents(node, parent, parents):
    if node is None:
        return
    parents[node.value] = parent
    find_parents(node.left, node, parents)
    find_parents(node.right, node, parents)


def get_target_node(target, node, parents):
    if node.value == target:
        return node
    parent = parents[target]
    if parent.left and parent.left.value == target:
        return parent.left
    else:
        return parent.right



