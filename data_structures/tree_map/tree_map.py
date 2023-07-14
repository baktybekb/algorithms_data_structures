from data_structures.red_black_bst.red_black_bst import count_black_nodes, dfs


class Node:
    """0 - red, 1 - black"""
    def __init__(self, key, value, left=None, right=None, parent=None, color=1):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color


class TreeMap:
    """0 - red, 1 - black"""
    def __init__(self):
        self.NIL = Node(None, None, color=2)
        self.root = self.NIL

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        y.parent = x.parent
        if y.left != self.NIL:
            y.left.parent = x
        if x.parent is None:
            self.root = y
        elif x.parent.left == x:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        y.parent = x.parent
        if y.right != self.NIL:
            y.right.parent = x
        if x.parent is None:
            self.root = y
        elif x.parent.left == x:
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y

    def insert(self, key, value):
        node = Node(key, value, left=self.NIL, right=self.NIL)
        y = None
        x = self.root
        while x != self.NIL:
            y = x
            x = x.left if node.key < x.key else x.right
        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node
        self._insert_fix(node)

    def _insert_fix(self, x):
        while x != self.root and x.parent.color == 0:
            if x.parent.parent.left == x.parent:
                uncle = x.parent.parent.right
                if uncle.color == 0:
                    x.parent.color = 1
                    uncle.color = 1
                    x.parent.parent.color = 0
                    x = x.parent.parent
                else:
                    if x.parent.right == x:
                        x = x.parent
                        self._left_rotate(x)
                    x.parent.color = 1
                    x.parent.parent.color = 0
                    self._right_rotate(x.parent.parent)
            else:
                uncle = x.parent.parent.left
                if uncle.color == 0:
                    uncle.color = 1
                    x.parent.color = 1
                    x.parent.parent.color = 0
                else:
                    if x.parent.left == x:
                        x = x.parent
                        self._right_rotate(x)
                    x.parent.color = 1
                    x.parent.parent.color = 0
                    self._left_rotate(x.parent.parent)
        self.root.color = 1

    def _find_node(self, key):
        node = self.root
        while node != self.NIL:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node
        return None

    def find(self, key):
        node = self._find_node(key)
        if node is None:
            return None
        return node.value

    def delete(self, key):
        node = self._find_node(key)
        if node is None:
            return
        self._delete_node(node)

    def _delete_node(self, node):
        y = node
        y_original_color = y.color
        if node.left == self.NIL:
            x = node.right
            self._transplant(node, node.right)
        elif node.right == self.NIL:
            x = node.left
            self._transplant(node, node.left)
        else:
            y = self._find_minimum(node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self._transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color
        if y_original_color == 1:
            self._delete_fix(x)

    def _delete_fix(self, x):
        while x != self.root and x.color == 1:
            if x.parent.left == x:
                sibling = x.parent.right
                if sibling.color == 0:
                    sibling.color = 1
                    x.parent.color = 0
                    self._left_rotate(x.parent)
                    sibling = x.parent.right
                if sibling.left.color == sibling.right.color == 1:
                    sibling.color = 0
                    x = x.parent
                else:
                    if sibling.right.color == 1:
                        sibling.left.color = 1
                        sibling.color = 0
                        self._right_rotate(sibling)
                        sibling = x.parent.right
                    sibling.color = x.parent.color
                    sibling.right.color = 1
                    x.parent.color = 1
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                sibling = x.parent.left
                if sibling.color == 0:
                    sibling.color = 1
                    x.parent.color = 0
                    self._right_rotate(x.parent)
                    sibling = x.parent.left
                if sibling.left.color == sibling.right.color == 1:
                    sibling.color = 0
                    x = x.parent
                else:
                    if sibling.left.color == 1:
                        sibling.right.color = 1
                        sibling.color = 0
                        self._left_rotate(sibling)
                        sibling = x.parent.left
                    sibling.color = x.parent.color
                    sibling.left.color = 1
                    x.parent.color = 1
                    self._right_rotate(x.parent)
                    x = self.root
        self.root.color = 1

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u.parent.left == u:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _find_minimum(self, node):
        if node == self.NIL:
            return
        while node != self.NIL and node.left != self.NIL:
            node = node.left
        return node


def test():
    tree = TreeMap()
    nums = [(i, i * 10) for i in range(10)]
    for key, value in nums:
        tree.insert(key, value)
    for key, value in nums:
        assert tree.find(key) is not None
    count_black_nodes(tree.root, tree.NIL)
    dfs(tree.root, tree.NIL)

    for key, value in nums:
        tree.delete(key)
        assert tree.find(key) is None


if __name__ == '__main__':
    test()
