from data_structures.heap.heap import Heap, min_heap_func, max_heap_func
import unittest


class Test(unittest.TestCase):
    def test_max_heap(self):
        self.heap = Heap([5, 3, 0, 2, 3, 9, 7, 6, 1], max_heap_func)

        self.assertEqual(self.heap.peek(), 9)
        self.heap.insert(12)
        self.assertEqual(self.heap.peek(), 12)

        self.heap.remove()
        self.heap.remove()
        self.assertEqual(self.heap.peek(), 7)

    def test_min_heap(self):
        self.heap = Heap([5, 3, 0, 0, 2, 3, 9, 7, 6, 1], min_heap_func)

        self.assertEqual(self.heap.peek(), 0)
        self.heap.insert(-10)
        self.assertEqual(self.heap.peek(), -10)

        self.heap.remove()
        self.heap.remove()
        self.assertEqual(self.heap.peek(), 0)
        self.heap.remove()
        self.assertEqual(self.heap.peek(), 1)

