import unittest

from data_structures.queue.by_linked_list.queue import Queue


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.enqueue(5)
        self.queue.enqueue(10)

        self.assertEqual(self.queue.tail.value, 10)
        self.assertEqual(len(self.queue), 2)
        self.assertEqual(self.queue.peek(), 5)

        self.assertEqual(self.queue.dequeue(), 5)
        self.assertEqual(self.queue.peek(), 10)
        self.assertEqual(len(self.queue), 1)
        self.queue.dequeue()
        self.assertEqual(len(self.queue), 0)
        self.assertEqual(self.queue.tail, None)
        with self.assertRaises(IndexError) as e:
            self.queue.dequeue()
            self.assertEqual(str(e), 'queue is empty')
