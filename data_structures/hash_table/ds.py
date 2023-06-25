"""Hash Table"""


class HashTable:
    def __init__(self, size=8):
        self.size = size
        self.count = 0
        self.table = [None] * self.size

    def hash_function(self, key):
        return hash(key) % self.size

    def __setitem__(self, key, value):
        idx = self.hash_function(key)
        if self.table[idx] is None:
            self.table[idx] = [(key, value)]
            self.count += 1
        else:
            for i, kv in enumerate(self.table[idx]):
                if kv[0] == key:
                    self.table[idx][i] = (key, value)
                    return
            self.table[idx].append((key, value))
            self.count += 1
        if self.count / self.size > 0.5:  # adjusting the load factor
            self._resize(2 * self.size)

    def get(self, key):
        return self.__getitem__(key)

    def __len__(self):
        return self.count

    def __getitem__(self, key):
        idx = self.hash_function(key)
        if self.table[idx]:
            for k, v in self.table[idx]:
                if k == key:
                    return v
        return None

    def __delitem__(self, key):
        idx = self.hash_function(key)
        if self.table[idx]:
            for i, kv in enumerate(self.table[idx]):
                if kv[0] == key:
                    del self.table[idx][i]
                    self.count -= 1
                    if len(self.table[idx]) == 0:
                        self.table[idx] = None
                    if self.size > 8 and self.count / self.size < 0.1:  # adjusting the load factor
                        self._resize(max(8, self.size // 2))  # ensuring the size never goes below initial
                    return
        raise KeyError('Key not found')

    def _resize(self, new_size):
        old_table = self.table
        self.size = new_size
        self.table = [None] * self.size
        self.count = 0
        for bucket in old_table:
            if bucket:
                for k, v in bucket:
                    self.__setitem__(k, v)

    def __contains__(self, key):
        return self.__getitem__(key) is not None

    def __iter__(self):
        for bucket in self.table:
            if bucket:
                for key, value in bucket:
                    yield key, value

    def keys(self):
        return (k for k, v in self)

    def values(self):
        return (v for k, v in self)

    def get_size(self):
        return self.size
