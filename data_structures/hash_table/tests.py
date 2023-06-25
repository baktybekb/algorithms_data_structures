import unittest

from data_structures.hash_table.ds import HashTable


class TestHashTable(unittest.TestCase):
    def setUp(self) -> None:
        self.hash_table = HashTable(2)

    def test_put(self):
        key = 'test_key'
        self.hash_table.put(key, 'test_value')
        self.assertEqual(self.hash_table.get(key), 'test_value')

    def test_resize(self):
        for i in range(15):
            self.hash_table.put(f'key_{i}', f'value_{i}')
        self.assertEqual(len(self.hash_table), 15)

    def test_get(self):
        key = 'test_key'
        self.hash_table.put(key, 'test_value')
        self.assertEqual(self.hash_table.get(key), 'test_value')
        self.assertIsNone(self.hash_table.get('non_existing_key'))

    def test_delete(self):
        key = 'test_key'
        self.hash_table.put(key, 'test_value')
        self.hash_table.delete(key)
        self.assertIsNone(self.hash_table.get(key))

    def test_contains(self):
        key = 'test_key'
        self.hash_table.put(key, 'value')
        self.assertTrue(key in self.hash_table)
        self.assertFalse('non_existing_key' in self.hash_table)

    def test_keys(self):
        keys = ['first', 'second', 'third']
        for key in keys:
            self.hash_table.put(key, 'value')
        self.assertCountEqual(list(k for k in self.hash_table.keys()), keys)

    def test_values(self):
        values = ['first', 'second', 'third']
        keys = [1, 2, 3]
        for key, value in zip(keys, values):
            self.hash_table.put(key, value)
        self.assertCountEqual(list(v for v in self.hash_table.values()), values)

    def test_put_multiple_values_single_key(self):
        self.assertEqual(len(self.hash_table), 0)
        self.hash_table.put('key', 'value_1')
        self.hash_table.put('key', 'value_2')
        self.assertEqual(self.hash_table.get('key'), 'value_2')

    def test_collision(self):
        class TestObject:
            def __init__(self, id, hash_value):
                self.id = id
                self.hash_value = hash_value

            def __hash__(self):
                return self.hash_value

            def __eq__(self, other):
                return self.id == other.id

        key1 = TestObject(1, 0)
        key2 = TestObject(2, 0)
        value1, value2 = 'value1', 'value2'
        self.hash_table.put(key1, value1)
        self.hash_table.put(key2, value2)
        self.assertEqual(self.hash_table.get(key1), value1)
        self.assertEqual(self.hash_table.get(key2), value2)
        bucket_idx = self.hash_table.hash_function(key1)
        self.assertCountEqual(self.hash_table[bucket_idx], [(key1, value1), (key2, value2)])

    def test_size(self):
        initial_size = self.hash_table.get_size()
        keys = [f'key_{i}' for i in range(2 * initial_size)]
        values = [f'value_{i}' for i in range(2 * initial_size)]
        for key, value in zip(keys, values):
            self.hash_table.put(key, value)
        self.assertTrue(self.hash_table.get_size() > initial_size)
        self.assertTrue(self.hash_table.get_size() > 2 * initial_size)


