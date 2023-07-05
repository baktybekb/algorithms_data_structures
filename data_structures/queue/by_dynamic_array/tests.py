from data_structures.queue.by_dynamic_array.queue import Queue
import unittest


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = Queue()

    def test_enqueue(self):
        self.assertEqual(len(self.queue), 0)
        self.queue.enqueue(1)
        self.assertEqual(len(self.queue), 1)
        self.queue.enqueue(5)
        self.assertEqual(self.queue.peek(), 1)
        self.assertEqual(len(self.queue), 2)
        self.queue.dequeue()
        self.queue.dequeue()
        self.assertEqual(len(self.queue), 0)
        with self.assertRaises(IndexError) as e:
            self.queue.peek()
            self.assertEqual(str(e), 'queue is empty')
