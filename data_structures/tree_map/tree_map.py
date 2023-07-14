from data_structures.red_black_bst.red_black_bst import RED, BLACK, red_node_has_ony_black_children, count_black_nodes


class Node:
    """RED - red, BLACK - black"""
    def __init__(self, key, value, left=None, right=None, parent=None, color=RED):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color


class TreeMap:
    """RED - red, BLACK - black"""
    def __init__(self):
        self.NIL = Node(None, None, color=BLACK)
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
        while x != self.root and x.parent.color == RED:
            if x.parent.parent.left == x.parent:
                uncle = x.parent.parent.right
                if uncle.color == RED:
                    x.parent.color = BLACK
                    uncle.color = BLACK
                    x.parent.parent.color = RED
                    x = x.parent.parent
                else:
                    if x.parent.right == x:
                        x = x.parent
                        self._left_rotate(x)
                    x.parent.color = BLACK
                    x.parent.parent.color = RED
                    self._right_rotate(x.parent.parent)
            else:
                uncle = x.parent.parent.left
                if uncle.color == RED:
                    uncle.color = BLACK
                    x.parent.color = BLACK
                    x.parent.parent.color = RED
                    x = x.parent.parent
                else:
                    if x.parent.left == x:
                        x = x.parent
                        self._right_rotate(x)
                    x.parent.color = BLACK
                    x.parent.parent.color = RED
                    self._left_rotate(x.parent.parent)
        self.root.color = BLACK

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
            raise KeyError('key not found')
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
        if y_original_color == BLACK:
            self._delete_fix(x)

    def _delete_fix(self, x):
        while x != self.root and x.color == BLACK:
            if x.parent.left == x:
                sibling = x.parent.right
                if sibling.color == RED:
                    sibling.color = BLACK
                    x.parent.color = RED
                    self._left_rotate(x.parent)
                    sibling = x.parent.right
                if sibling.left.color == BLACK and sibling.right.color == BLACK:
                    sibling.color = RED
                    x = x.parent
                else:
                    if sibling.right.color == BLACK:
                        sibling.left.color = BLACK
                        sibling.color = RED
                        self._right_rotate(sibling)
                        sibling = x.parent.right
                    sibling.color = x.parent.color
                    sibling.right.color = BLACK
                    x.parent.color = BLACK
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                sibling = x.parent.left
                if sibling.color == RED:
                    sibling.color = BLACK
                    x.parent.color = RED
                    self._right_rotate(x.parent)
                    sibling = x.parent.left
                if sibling.left.color == BLACK and sibling.right.color == BLACK:
                    sibling.color = RED
                    x = x.parent
                else:
                    if sibling.left.color == BLACK:
                        sibling.right.color = BLACK
                        sibling.color = RED
                        self._left_rotate(sibling)
                        sibling = x.parent.left
                    sibling.color = x.parent.color
                    sibling.left.color = BLACK
                    x.parent.color = BLACK
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = BLACK

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u.parent.left == u:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _find_minimum(self, node):
        while node.left != self.NIL and node.left is not None:
            node = node.left
        return node

    def iter_func(self, node, nil):
        if node is None or node == nil:
            return
        yield from self.iter_func(node.left, nil)
        yield node
        yield from self.iter_func(node.right, nil)

    def __iter__(self):
        return self.iter_func(self.root, self.NIL)


def in_order_keys(node, nil, array):
    if node is None or node == nil:
        return
    in_order_keys(node.left, nil, array)
    array.append(node.key)
    in_order_keys(node.right, nil, array)


if __name__ == '__main__':
    tree = TreeMap()
    keys = [7, 3, 18, 10, 22, 8, 11, 26, 2, 6, 13]
    for key in keys:
        tree.insert(key, str(key))

    assert red_node_has_ony_black_children(tree.root, tree.NIL) is True
    count_black_nodes(tree.root, tree.NIL)

    for key in [10, 22, 8, 11, 26]:
        tree.delete(key)
        assert tree.find(key) is None
    assert red_node_has_ony_black_children(tree.root, tree.NIL) is True
    count_black_nodes(tree.root, tree.NIL)

    array = []
    in_order_keys(tree.root, tree.NIL, array)
    assert array == [2, 3, 6, 7, 13, 18]

    for node in tree:
        print(node.key)
