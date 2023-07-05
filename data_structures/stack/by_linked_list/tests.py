from data_structures.stack.by_linked_list.stack import Stack
import unittest


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = Stack()

    def test_stack(self):
        self.assertEqual(len(self.stack), 0)
        self.assertEqual(self.stack.is_empty(), True)
        self.stack.push(5)
        self.stack.push(6)
        self.assertEqual(len(self.stack), 2)
        self.assertEqual(self.stack.is_empty(), False)
        self.assertEqual(self.stack.pop(), 6)
        self.assertEqual(self.stack.pop(), 5)
        with self.assertRaises(IndexError) as e:
            self.stack.pop()
            self.assertEqual(str(e), 'stack is empty')
