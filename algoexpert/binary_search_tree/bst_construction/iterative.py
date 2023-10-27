# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # O(log(n)) time | O(1) space
    def insert(self, value):
        node = self
        while node:
            if value < node.value:
                if node.left:
                    node = node.left
                else:
                    node.left = BST(value)
                    break
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = BST(value)
                    break
        return self

    # O(log(n)) time | O(1) space
    def contains(self, value):
        node = self
        while node:
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                return True
        return False

    # O(log(n)) time | O(1) space
    def remove(self, value, parent=None):
        node = self
        while node:
            if value < node.value:
                parent = node
                node = node.left
            elif value > node.value:
                parent = node
                node = node.right
            else:
                if node.left and node.right:
                    node.value = node.right.find_min()
                    node.right.remove(node.value, node)
                elif parent is None:  # root node with only one child, or none child
                    if node.left:
                        node.value = node.left.value
                        node.right = node.left.right
                        node.left = node.left.left
                    elif node.right:
                        node.value = node.right.value
                        node.left = node.right.left
                        node.right = node.right.right
                    else:
                        pass
                elif parent.left == node:
                    parent.left = node.left if node.left else node.right
                elif parent.right == node:
                    parent.right = node.left if node.left else node.right
                break
        return self

    def find_min(self):
        node = self
        while node and node.left:
            node = node.left
        return node.value
