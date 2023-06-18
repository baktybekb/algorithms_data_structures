class DynamicArray:
    def __init__(self):
        self.length = 0
        self.capacity = 1
        self.data = self._make_array(self.capacity)

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        if not 0 <= index < self.length:
            raise IndexError('Index out of bounds')
        return self.data[index]

    def append(self, value):
        if self.length == self.capacity:
            self._resize(2 * self.capacity)
        self.data[self.length] = value
        self.length += 1

    def _resize(self, new_capacity):
        new_data = self._make_array(new_capacity)
        for i in range(self.length):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def _make_array(self, capacity):
        return [None] * capacity

