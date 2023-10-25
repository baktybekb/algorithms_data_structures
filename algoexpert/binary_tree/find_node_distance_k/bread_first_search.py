from collections import deque


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(n) space
def findNodesDistanceK(tree, target, k):
    parents = find_parents(tree)
    target_node = find_target_node(tree, target, parents)
    data, visited = [], set()
    queue = deque(((target_node, 0),))
    while queue:
        node, depth = queue.popleft()
        if node is None or node.value in visited:
            continue
        visited.add(node.value)
        if depth == k:
            data.append(node.value)
            continue
        depth += 1
        queue.append((node.left, depth))
        queue.append((node.right, depth))
        queue.append((parents[node.value], depth))
    return data


def find_target_node(tree, target, parents):
    parent = parents[target]
    if not parent:
        return tree
    if parent.left and parent.left.value == target:
        return parent.left
    return parent.right


def find_parents(tree):
    parents = {}

    def helper(node, parent):
        if node is None:
            return
        parents[node.value] = parent
        helper(node.left, node)
        helper(node.right, node)

    helper(tree, None)
    return parents





