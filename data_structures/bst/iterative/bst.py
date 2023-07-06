class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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

    def contains(self, value):
        node = self
        while node:
            if value < node.value:
                if node.left:
                    node = node.left
                else:
                    return False
            elif value > node.value:
                if node.right:
                    node = node.right
                else:
                    return False
            else:
                return True

    def remove(self, value, parent=None):
        node = self
        while node:
            if value < node.value:
                if node.left:
                    parent = node
                    node = node.left
                else:
                    raise ValueError('value not found in a bst')
            elif value > node.value:
                if node.right:
                    parent = node
                    node = node.right
                else:
                    raise ValueError('value not found in a bst')
            else:
                if node.left and node.right:
                    node.value = node.right.get_min_value()
                    node.right.remove(node.value, node)
                elif parent is None:
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

    def get_min_value(self):
        node = self
        while node and node.left:
            node = node.left
        return node.value
