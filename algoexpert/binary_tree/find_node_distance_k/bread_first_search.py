# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time complexity | O(n) space
def findNodesDistanceK(tree, target, k):
    parents = {}
    gather_parents(tree, parents)
    target_node = find_target_node(tree, parents, target)
    queue = [(target_node, 0)]
    seen = {target_node}
    while queue:
        node, distance = queue.pop(0)
        if distance == k:
            result = [node.value for node, _ in queue]
            result.append(node.value)
            return result
        neighbors = (node.left, node.right, parents[node.value])
        for node in neighbors:
            if node is None:
                continue
            if node in seen:
                continue
            seen.add(node)
            queue.append((node, distance + 1))
    return []


def find_target_node(tree, parents, target):
    if tree.value == target:
        return tree
    parent = parents[target]
    if parent.left and parent.left.value == target:
        return parent.left
    return parent.right


def gather_parents(node, parents, parent=None):
    if node is None:
        return
    parents[node.value] = parent
    gather_parents(node.left, parents, node)
    gather_parents(node.right, parents, node)
