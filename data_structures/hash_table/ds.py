"""Hash Table"""


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
        bucket = self.table[key_hash]
        return next((v for k, v in bucket if k == key), None)


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

    def get_size(self):
        return self.size

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
