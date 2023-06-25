import unittest


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]
        self.count = 0

    def hash_function(self, key):
        return hash(key) % self.size

    # this method only for testing
    def __getitem__(self, index):
        return self.table[index]

    def put(self, key, value):
        key_hash = self.hash_function(key)
        bucket: list = self.table[key_hash]
        key_found = False
        for i in range(len(bucket)):
            key_, value_ = bucket[i]
            if key_ == key:
                bucket[i] = (key, value)
                key_found = True
                break
        if not key_found:
            bucket.append((key, value))
            self.count += 1
        if self.count / self.size > 0.7:
            self._resize()

    def get(self, key):
        key_hash = self.hash_function(key)
        for k, v in self.table[key_hash]:
            if k == key:
                return v
        return None

    def delete(self, key):
        key_hash = self.hash_function(key)
        bucket = self.table[key_hash]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                del bucket[i]
                self.count -= 1
                break
        if self.count > 0 and self.count / self.size <= 0.2:
            self._resize(smaller=True)

    def _resize(self, smaller=False):
        old_table = self.table
        self.size = self.size // 2 if smaller else self.size * 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0
        for bucket in old_table:
            for key, value in bucket:
                self.put(key, value)

    def __str__(self):
        return str(self.table)

    def __len__(self):
        return self.count

    def __iter__(self):
        for bucket in self.table:
            for key, value in bucket:
                yield key, value

    def __contains__(self, key):
        key_hash = self.hash_function(key)
        return any(k == key for k, v in self.table[key_hash])

    def keys(self):
        return (key for key, value in self)

    def values(self):
        return (value for key, value in self)


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


if __name__ == '__main__':
    unittest.main()
