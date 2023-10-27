# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # O(log(n)) time | O(log(n)) space
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BST(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BST(value)
        return self

    # O(log(n)) time | O(log(n)) space
    def contains(self, value):
        if value < self.value:
            if self.left:
                return self.left.contains(value)
            else:
                return False
        elif value > self.value:
            if self.right:
                return self.right.contains(value)
            else:
                return False
        else:
            return True

    # O(log(n)) time | O(log(n)) space
    def remove(self, value, parent=None):
        if value < self.value:
            if self.left:
                self.left.remove(value, self)
        elif value > self.value:
            if self.right:
                self.right.remove(value, self)
        else:
            if self.left and self.right:
                self.value = self.right.find_min()
                self.right.remove(self.value, self)
            elif parent is None:
                if self.left:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    pass
            elif parent.left == self:
                parent.left = self.left if self.left else self.right
            elif parent.right == self:
                parent.right = self.left if self.left else self.right
        return self

    def find_min(self):
        if self.left is None:
            return self.value
        return self.left.find_min()
