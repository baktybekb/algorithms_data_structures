"""Dynamic Array"""


class Iterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.iterable.length:
            raise StopIteration
        value = self.iterable[self.index]
        self.index += 1
        return value


class DynamicArray:
    def __init__(self):
        self.data = [None] * 1
        self.length = 0
        self.capacity = 1

    def append(self, value):
        if self.length == self.capacity:
            self._resize(self.capacity * 2)
        self.data[self.length] = value
        self.length += 1

    def __getitem__(self, index):
        if not 0 <= index < self.length:
            raise IndexError('Invalid index')
        return self.data[index]

    def __iter__(self):
        return Iterator(self)

    def __len__(self):
        return self.length

    def __str__(self):
        return str(self.data[:self.length])

    def pop(self, index=None):
        if self.length == 0:
            raise IndexError('List is empty')
        if index is None:
            index = self.length - 1
        if not 0 <= index < self.length:
            raise IndexError('Invalid index')
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        self.length -= 1
        if self.length > 0 and self.length == self.capacity // 4:
            self._resize(self.capacity // 2)

    def index(self, value):
        for i in range(self.length):
            if self.data[i] == value:
                return i
        raise ValueError('Not found')

    def insert(self, index, value):
        if not 0 <= index <= self.length:
            raise IndexError('index out of range')
        if self.length == self.capacity:
            self._resize(self.capacity * 2)
        for i in range(self.length, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value
        self.length += 1

    def _resize(self, capacity):
        new = [None] * capacity
        for i in range(self.length):
            new[i] = self.data[i]
        self.data = new
        self.capacity = capacity

    def remove_all(self, value):
        write_idx = 0
        original_length = self.length
        for read_idx in range(original_length):
            if self.data[read_idx] != value:
                self.data[write_idx] = self.data[read_idx]
                write_idx += 1
        self.length = write_idx
        if original_length > self.length:
            if self.length > 0 and self.length == self.capacity // 4:
                self._resize(self.capacity // 2)
        else:
            raise ValueError('Value not found')

    def remove(self, value):
        for i in range(self.length):
            if self.data[i] == value:
                self.pop(i)
                return
        raise ValueError('Value not found')

    def extend(self, iterable):
        for value in iterable:
            self.append(value)
