import unittest

from data_structures.hash_table.hash_table import HashTable


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.ht = HashTable()

    def test_insert(self):
        self.assertEqual(len(self.ht), 0)
        self.ht['one'] = 1
        self.ht['two'] = 2
        self.assertEqual(self.ht['one'], 1)
        self.assertEqual(self.ht.get('three'), None)
        with self.assertRaises(ValueError) as e:
            _ = self.ht['three']
            self.assertEqual(str(e), 'key not found')

    def test_delete(self):
        self.ht['one'] = 1
        self.ht['two'] = 2
        self.assertEqual(len(self.ht), 2)
        self.assertEqual(self.ht.get('one'), 1)
        del self.ht['one']
        self.assertEqual(len(self.ht), 1)
        self.assertEqual(self.ht.get('one'), None)

    def test_collision(self):
        class TestObject:
            def __init__(self, id_, hash_value):
                self.id_ = id_
                self.hash_value = hash_value

            def __hash__(self):
                return self.hash_value

            def __eq__(self, other):
                return self.id_ == other.id_

            def __str__(self):
                return f'key: {self.id_}-{self.hash_value}'

        key1, key2 = TestObject(1, 0),  TestObject(2, 0)
        value1, value2 = 'value_1', 'value_2'
        self.ht[key1] = value1
        self.assertEqual(self.ht.get(key1), value1)

        idx = self.ht.hash_func(key1)
        self.assertEqual(len(self.ht.table[idx]), 1)

        self.ht[key2] = value2
        self.assertEqual(self.ht.get(key2), value2)
        self.assertEqual(len(self.ht.table[idx]), 2)
        self.assertEqual(str(self.ht.table[idx]), "key: 1-0: value_1 -> key: 2-0: value_2")

