class Node:
    def __init__(self, data, color="red", left=None, right=None, parent=None):
        self.data = data
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, "black")
        self.root = self.NIL

    def left_rotate(self, node):
        y = node.right
        node.right = y.left
        if y.left != self.NIL:
            y.left.parent = node
        y.parent = node.parent
        if node.parent == None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y

    def right_rotate(self, node):
        y = node.left
        node.left = y.right
        if y.right != self.NIL:
            y.right.parent = node
        y.parent = node.parent
        if node.parent == None:
            self.root = y
        elif node == node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y
        y.right = node
        node.parent = y

    def insert(self, data):
        node = Node(data)
        node.parent = None
        node.data = data
        node.left = self.NIL
        node.right = self.NIL
        node.color = "red"

        y = None
        x = self.root

        while x != self.NIL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = "black"
            return

        if node.parent.parent == None:
            return

        self.fix_insert(node)

    def fix_insert(self, k):
        while k.parent.color == "red":
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # Uncle
                if u.color == "red":
                    u.color = "black"
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right  # Uncle

                if u.color == "red":
                    u.color = "black"
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = "black"

    # def print_helper(self, node, indent, last):
    #     if node != self.NIL:
    #         print(indent, end="")
    #         if last:
    #             print("R----", end="")
    #             indent += "     "
    #         else:
    #             print("L----", end="")
    #             indent += "|    "
    #
    #         s_color = "RED" if node.color == "red" else "BLACK"
    #         print(str(node.data) + "(" + s_color + ")")
    #         self.print_helper(node.left, indent, False)
    #         self.print_helper(node.right, indent, True)

    # def pretty_print(self):
    #     self.print_helper(self.root, "", True)

    # Method to find a node in the tree
    def find(self, data):
        current_node = self.root

        while current_node != self.NIL:
            if data < current_node.data:
                current_node = current_node.left
            elif data > current_node.data:
                current_node = current_node.right
            else:
                return current_node  # Node found

        return None  # Node not found

    # # Method to perform deletion of a node
    # def delete(self, data):
    #     self.delete_node(self.find(data))
    #
    # # Helper method for delete operation
    # def delete_node(self, node):
    #     # More complicated than BST delete
    #     y_original_color = node.color
    #     if node.left == self.NIL:
    #         x = node.right
    #         self.rb_transplant(node, node.right)
    #     elif node.right == self.NIL:
    #         x = node.left
    #         self.rb_transplant(node, node.left)
    #     else:
    #         y = self.minimum(node.right)
    #         y_original_color = y.color
    #         x = y.right
    #         if y.parent != node:
    #             self.rb_transplant(y, y.right)
    #             y.right = node.right
    #             y.right.parent = y
    #         self.rb_transplant(node, y)
    #         y.left = node.left
    #         y.left.parent = y
    #         y.color = node.color
    #     if y_original_color == "black":
    #         self.fix_delete(x)
    #
    # # Fix the red-black tree
    # def fix_delete(self, x):
    #     while x != self.root and x.color == "black":
    #         if x == x.parent.left:
    #             s = x.parent.right
    #             if s.color == "red":
    #                 s.color = "black"
    #                 x.parent.color = "red"
    #                 self.left_rotate(x.parent)
    #                 s = x.parent.right
    #
    #             if s.left.color == "black" and s.right.color == "black":
    #                 s.color = "red"
    #                 x = x.parent
    #             else:
    #                 if s.right.color == "black":
    #                     s.left.color = "black"
    #                     s.color = "red"
    #                     self.right_rotate(s)
    #                     s = x.parent.right
    #
    #                 s.color = x.parent.color
    #                 x.parent.color = "black"
    #                 s.right.color = "black"
    #                 self.left_rotate(x.parent)
    #                 x = self.root
    #         else:
    #             s = x.parent.left
    #             if s.color == "red":
    #                 s.color = "black"
    #                 x.parent.color = "red"
    #                 self.right_rotate(x.parent)
    #                 s = x.parent.left
    #
    #             if s.right.color == "black" and s.left.color == "black":
    #                 s.color = "red"
    #                 x = x.parent
    #             else:
    #                 if s.left.color == "black":
    #                     s.right.color = "black"
    #                     s.color = "red"
    #                     self.left_rotate(s)
    #                     s = x.parent.left
    #
    #                 s.color = x.parent.color
    #                 x.parent.color = "black"
    #                 s.left.color = "black"
    #                 self.right_rotate(x.parent)
    #                 x = self.root
    #     x.color = "black"
    #
    # # Function to replace subtree as a child of its parent with another subtree
    # def rb_transplant(self, u, v):
    #     if u.parent == None:
    #         self.root = v
    #     elif u == u.parent.left:
    #         u.parent.left = v
    #     else:
    #         u.parent.right = v
    #     v.parent = u.parent
    #
    # # Function to find the node `minimum(node)` that will find the minimum node starting from a given node:
    # def minimum(self, node):
    #     while node.left != self.NIL:
    #         node = node.left
    #     return node

