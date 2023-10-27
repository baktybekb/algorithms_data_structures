# https://www.algoexpert.io/questions/bst-traversal

# O(n) time | O(n) space
def inOrderTraverse(tree, array):
    def helper(node):
        if node is None:
            return
        helper(node.left)
        array.append(node.value)
        helper(node.right)

    helper(tree)
    return array


# O(n) time | O(n) space
def preOrderTraverse(tree, array):
    def helper(node):
        if node is None:
            return
        array.append(node.value)
        helper(node.left)
        helper(node.right)

    helper(tree)
    return array


# O(n) time | O(n) space
def postOrderTraverse(tree, array):
    def helper(node):
        if node is None:
            return
        helper(node.left)
        helper(node.right)
        array.append(node.value)

    helper(tree)
    return array
