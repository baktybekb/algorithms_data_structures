import unittest
from data_structures.dynamic_array.ds import DynamicArray


class TestDynamicArray(unittest.TestCase):
    def setUp(self) -> None:
        self.array = DynamicArray()

    def test_append(self):
        self.array.append(1)
        self.assertEqual(self.array[0], 1)
        self.assertEqual(len(self.array), 1)

    def test_pop(self):
        self.array.extend([1, 2, 3, 4])
        self.array.pop(1)
        self.assertEqual(self.array[0], 1)
        self.assertEqual(self.array[1], 3)
        self.assertEqual(self.array[2], 4)
        self.assertEqual(len(self.array), 3)

    def test_insert(self):
        self.array.insert(0, 1)
        self.array.insert(1, 2)
        self.array.insert(1, 3)
        self.array.insert(1, 10)
        self.assertEqual(self.array[0], 1)
        self.assertEqual(self.array[1], 10)
        self.assertEqual(self.array[2], 3)
        self.assertEqual(self.array[3], 2)
        self.assertEqual(len(self.array), 4)

    def test_remove(self):
        self.array.extend([1, 2, 3, 4, 2])
        self.array.remove(2)
        desired = [i for i in self.array]
        self.assertEqual(desired, [1, 3, 4, 2])

    def test_remove_all(self):
        self.array.extend([1, 2, 3, 4, 2])
        self.array.remove_all(2)
        desired = [i for i in self.array]
        self.assertEqual(desired, [1, 3, 4])

    def test_iter(self):
        self.array.extend([1, 2, 3, 4])
        iterator = iter(self.array)
        self.assertEqual(next(iterator), 1)
        self.assertEqual(next(iterator), 2)
        self.assertEqual(next(iterator), 3)
        self.assertEqual(next(iterator), 4)
        with self.assertRaises(StopIteration):
            next(iterator)

    def test_errors(self):
        with self.assertRaises(IndexError):
            _ = self.array[0]
        with self.assertRaises(IndexError):
            self.array.pop()
        with self.assertRaises(ValueError):
            self.array.remove(1)
        with self.assertRaises(IndexError):
            self.array.insert(1, 1)
