class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

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

    def remove(self, value, parent=None):
        if value < self.value:
            if self.left:
                self.left.remove(value, self)
            else:
                raise ValueError('value not found in a bst')
        elif value > self.value:
            if self.right:
                self.right.remove(value, self)
            else:
                raise ValueError('value not found in a bst')
        else:
            if self.left and self.right:
                self.value = self.right.get_min_value()
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
            elif parent.left is self:
                parent.left = self.left if self.left else self.right
            elif parent.right is self:
                parent.right = self.left if self.left else self.right
            return self

    def get_min_value(self):
        if self.left is None:
            return self.value
        return self.left.get_min_value()
