import unittest

from data_structures.red_black_bst.red_black_bst import RedBlackTree


class TestRedBlackTree(unittest.TestCase):

    def setUp(self):
        self.rb_tree = RedBlackTree()

    def test_insert_root(self):
        self.rb_tree.insert(10)
        self.assertEqual(self.rb_tree.root.data, 10)
        self.assertEqual(self.rb_tree.root.color, 'black')

    def test_insert_and_recolor(self):
        self.rb_tree.insert(10)
        self.rb_tree.insert(15)
        self.assertEqual(self.rb_tree.root.right.data, 15)
        self.assertEqual(self.rb_tree.root.right.color, 'red')

    def test_insert_and_rotate(self):
        self.rb_tree.insert(10)
        self.rb_tree.insert(15)
        self.rb_tree.insert(20)
        # After insertion, the tree should have adjusted itself to maintain balance
        self.assertEqual(self.rb_tree.root.data, 15)
        self.assertEqual(self.rb_tree.root.color, 'black')
        self.assertEqual(self.rb_tree.root.left.data, 10)
        self.assertEqual(self.rb_tree.root.left.color, 'red')
        self.assertEqual(self.rb_tree.root.right.data, 20)
        self.assertEqual(self.rb_tree.root.right.color, 'red')

    # Add more test cases here...


if __name__ == '__main__':
    unittest.main()
