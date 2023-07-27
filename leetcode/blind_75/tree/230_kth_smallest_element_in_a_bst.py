from typing import Optional


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self):
        self.last_visited_val = None
        self.number_of_visited = 0


class Solution:
    def kthSmallest(self, root: Optional[Node], k: int) -> int:
        tree_info = TreeInfo()
        self.helper(root, k, tree_info)
        return tree_info.last_visited_val

    def helper(self, node, k, tree_info):
        if node is None or tree_info.number_of_visited == k:
            return
        self.helper(node.left, k, tree_info)
        if tree_info.number_of_visited < k:
            tree_info.number_of_visited += 1
            tree_info.last_visited_val = node.val
            self.helper(node.right, k, tree_info)


if __name__ == '__main__':
    """
            4
        2       6
     1   3     5   7
    """
    node5 = Node(5)
    node7 = Node(7)
    node1 = Node(1)
    node3 = Node(3)
    node6 = Node(6, left=node5, right=node7)
    node2 = Node(2, left=node1, right=node3)
    node4 = Node(1, left=node2, right=node6)

    solution = Solution()
    assert solution.kthSmallest(node4, 2) == 2
    assert solution.kthSmallest(node4, 3) == 3

