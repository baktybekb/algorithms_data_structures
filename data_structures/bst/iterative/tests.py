import unittest
from .bst import BST


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.bst = BST(10)

    def test_bst(self):
        self.bst.insert(5).insert(10).insert(12).insert(2)

        self.assertTrue(self.bst.contains(5))
        self.assertTrue(self.bst.contains(2))
        self.assertTrue(self.bst.contains(12))
        self.assertFalse(self.bst.contains(1000))

        with self.assertRaises(ValueError) as e:
            self.bst.remove(9999)
            self.assertEqual(str(e), 'value not found in a bst')

        self.bst.remove(12)
        self.bst.remove(10)
        self.bst.remove(10)
        self.bst.remove(5)
        self.assertFalse(self.bst.contains(10))
        self.assertTrue(self.bst.contains(2))
