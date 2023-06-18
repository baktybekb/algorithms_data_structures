class MyDict:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [None for _ in range(self.size)]
        self.cache = None

    def hash1(self, key):
        return hash(key) % self.size

    def hash2(self, key):
        return (hash(key) % (self.size - 1)) + 1

    def put(self, key, value):
        if self.cache and self.cache[0] == key:
            self.cache = (key, value)
        index = self.hash1(key)
        if self.buckets[index] is None:
            self.buckets[index] = (key, value)
        else:
            i = index
            while self.buckets[i] is not None:
                if self.buckets[i][0] == key:
                    self.buckets[i] = (key, value)
                    return
                i = (i + self.hash2(key)) % self.size
            self.buckets[i] = (key, value)
        if self.buckets.count(None) < self.size // 2:
            self.resize(2 * self.size)

    def get(self, key):
        if self.cache and self.cache[0] == key:
            return self.cache[1]
        index = self.hash1(key)
        if self.buckets[index] is not None:
            if self.buckets[index][0] == key:
                self.cache = self.buckets[index]
                return self.buckets[index][1]
            else:
                i = index
                while self.buckets[i] is not None and self.buckets[i][0] != key:
                    i = (i + self.hash2(key)) % self.size
                if self.buckets[i] is not None and self.buckets[i][0] == key:
                    self.cache = self.buckets[i]
                    return self.buckets[i][1]
        raise KeyError('Key not found')

    def delete(self, key):
        index = self.hash1(key)
        if self.buckets[index] is not None:
            if self.buckets[index][0] == key:
                self.buckets[index] = None
            else:
                i = index
                while self.buckets[i] is not None and self.buckets[i][0] != key:
                    i = (i + self.hash2(key)) % self.size
                if self.buckets[i] is not None and self.buckets[i][0] == key:
                    self.buckets[i] = None
        if self.buckets.count(None) > self.size * 3 // 4:
            self.resize(self.size // 2)

    def resize(self, new_size):
        old_buckets = self.buckets
        self.size = new_size
        self.buckets = [None for _ in range(self.size)]
        self.cache = None
        for bucket in old_buckets:
            if bucket is not None:
                self.put(*bucket)


def test_my_dict():
    d = MyDict()

    # Тест put и get
    d.put('test1', 1)
    assert d.get('test1') == 1

    # Тест обновления значения
    d.put('test1', 2)
    assert d.get('test1') == 2

    # Тест добавления нового значения
    d.put('test2', 3)
    assert d.get('test2') == 3

    # Тест удаления значения
    d.delete('test1')
    try:
        d.get('test1')
    except KeyError:
        print("KeyError raised correctly")

    # Тест автоматического изменения размера
    for i in range(100):
        d.put(f'test{i}', i)

    for i in range(100):
        assert d.get(f'test{i}') == i

    # Тест удаления значений и автоматического изменения размера
    for i in range(100):
        d.delete(f'test{i}')

    for i in range(100):
        try:
            d.get(f'test{i}')
        except KeyError:
            print(f"KeyError raised correctly for test{i}")


if __name__ == "__main__":
    test_my_dict()
