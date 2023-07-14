class Node:
    def __init__(self, value, left=None, right=None, parent=None, color='red'):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, color='black')
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        y.parent = x.parent
        if y.left != self.NIL:
            y.left.parent = x
        if x.parent is None:
            self.root = y
        elif x.parent.left == x:
            x.parent.left = y
        elif x.parent.right == x:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        y.parent = x.parent
        if y.right != self.NIL:
            y.right.parent = x
        if x.parent is None:
            self.root = y
        elif x.parent.left == x:
            x.parent.left = y
        elif x.parent.right == x:
            x.parent.right = y
        y.right = x
        x.parent = y

    def insert(self, value):
        node = Node(value, left=self.NIL, right=self.NIL, color='red')
        y = None
        x = self.root
        while x != self.NIL:
            y = x
            if node.value < x.value:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y is None:
            self.root = node
        elif node.value < y.value:
            y.left = node
        else:
            y.right = node
        self.insert_fix(node)

    def insert_fix(self, node):
        while node != self.root and node.parent.color == 'red':
            if node.parent.parent.left == node.parent:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    uncle.color = 'black'
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node.parent.right == node:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    uncle.color = 'black'
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node.parent.left == node:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.left_rotate(node.parent.parent)
        self.root.color = 'black'

    def find(self, value):
        node = self.root
        while node != self.NIL:
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                return node
        return None

    def delete(self, value):
        node = self.find(value)
        if node is None:
            raise ValueError('value not found')
        self.delete_node(node)

    def delete_node(self, node):
        y = node
        y_original_color = y.color
        if node.left == self.NIL:
            x = node.right
            self.transplant(node, node.right)
        elif node.right == self.NIL:
            x = node.left
            self.transplant(node, node.left)
        else:
            y = self.minimum(y.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node:
                x.parent = node
            else:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color
        if y_original_color == 'black':
            self.delete_fix(x)

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u.parent.left == u:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        while node and node.left != self.NIL:
            node = node.left
        return node

    def delete_fix(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                sibling = x.parent.right
                if sibling.color == 'red':
                    x.parent.color = 'red'
                    sibling.color = 'black'
                    self.left_rotate(x.parent)
                    sibling = x.parent.right
                if sibling.left.color == sibling.right.color == 'black':
                    sibling.color = 'red'
                    x = x.parent
                else:
                    if sibling.right.color == 'black':
                        sibling.color = 'red'
                        sibling.left.color = 'black'
                        self.right_rotate(sibling)
                        sibling = x.parent.right
                    sibling.color = x.parent.color
                    x.parent.color = 'black'
                    sibling.right.color = 'black'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                sibling = x.parent.left
                if sibling.color == 'red':
                    x.parent.color = 'red'
                    sibling.color = 'black'
                    self.right_rotate(x.parent)
                    sibling = x.parent.left
                if sibling.left.color == sibling.right.color == 'black':
                    sibling.color = 'red'
                    x = x.parent
                else:
                    if sibling.left.color == 'black':
                        sibling.color = 'red'
                        sibling.right.color = 'black'
                        self.left_rotate(sibling)
                        sibling = x.parent.left
                    sibling.color = x.parent.color
                    x.parent.color = 'black'
                    sibling.left.color = 'black'
                    self.right_rotate(x.parent)
                    x = self.root
        self.root.color = 'black'


def count_black_nodes(node, nil):
    if node is None or node == nil:
        return 1
    count = 1 if node.color == 'black' else 0
    left_black_nodes = count_black_nodes(node.left, nil)
    right_black_nodes = count_black_nodes(node.right, nil)
    assert left_black_nodes == right_black_nodes
    return count + left_black_nodes


def dfs(node, nil):
    if node is None or node == nil:
        return
    if node.color == 'red':
        assert node.left.color == node.right.color == 'black'
    dfs(node.left, nil)
    dfs(node.right, nil)


def test():
    tree = RedBlackTree()
    nums = [i for i in range(10)]
    for num in nums:
        tree.insert(num)
    for num in nums:
        assert tree.find(num) is not None
    count_black_nodes(tree.root, tree.NIL)
    dfs(tree.root, tree.NIL)

    for num in nums:
        tree.delete(num)
        assert tree.find(num) is None


if __name__ == '__main__':
    test()
