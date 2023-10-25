# https://www.algoexpert.io/questions/max-path-sum-in-binary-tree

# O(n) time | O(h) space, h --> height of the tree
def maxPathSum(tree):
    total = tree.value

    def dfs(node):
        if node is None:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        as_branch = max(node.value, node.value + max(left, right))
        as_root = max(node.value, node.value + left + right)

        nonlocal total
        total = max(total, as_root, as_branch)
        return as_branch

    dfs(tree)
    return total
