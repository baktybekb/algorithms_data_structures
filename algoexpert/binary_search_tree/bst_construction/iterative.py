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
        bst = self
        while bst:
            if value < bst.value:
                if bst.left:
                    bst = bst.left
                else:
                    bst.left = BST(value)
                    break
            else:
                if bst.right:
                    bst = bst.right
                else:
                    bst.right = BST(value)
                    break
        return self

    # O(log(n)) time | O(1) space
    def contains(self, value):
        bst = self
        while bst:
            if bst.value == value:
                return True
            bst = bst.left if value < bst.value else bst.right
        return False

    # O(log(n)) time | O(1) space
    def remove(self, value, parent=None):
        current = self
        while current:
            if value < current.value:
                parent = current
                current = current.left
            elif value > current.value:
                parent = current
                current = current.right
            else:
                if current.left and current.right:
                    current.value = current.right.get_min_value()
                    current.right.remove(current.value, current)
                elif parent is None:
                    if current.left:
                        current.value = current.left.value
                        current.right = current.left.right
                        current.left = current.left.left
                    elif current.right:
                        current.value = current.right.value
                        current.left = current.right.left
                        current.right = current.right.right
                elif parent.left == current:
                    parent.left = current.left if current.left else current.right
                elif parent.right == current:
                    parent.right = current.right if current.right else current.left
                break
        return self

    # O(log(n)) time | O(1) space
    def get_min_value(self):
        current = self
        while current and current.left:
            current = current.left
        return current.value
