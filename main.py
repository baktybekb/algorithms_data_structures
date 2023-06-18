

class DynamicArray:
    def __init__(self):
        self.data = [None] * 1  # начинаем с одного элемента
        self.length = 0  # количество реально используемых ячеек

    def __str__(self):
        return str(self.data[:self.length])

    def append(self, value):
        # Если не хватает места, увеличиваем массив в два раза
        if self.length == len(self.data):
            self._resize(2 * len(self.data))
        self.data[self.length] = value
        self.length += 1

    def _resize(self, new_size):
        new_data = [None] * new_size
        for i in range(self.length):
            new_data[i] = self.data[i]
        self.data = new_data

    def pop(self):
        if self.length == 0:
            raise Exception("Array is empty")
        value = self.data[self.length - 1]
        self.data[self.length - 1] = None
        self.length -= 1
        return value

    def get(self, index):
        if index < 0 or index >= self.length:
            raise Exception("Index out of bounds")
        return self.data[index]

    def set(self, index, value):
        if index < 0 or index >= self.length:
            raise Exception("Index out of bounds")
        self.data[index] = value

    def index(self, value):
        for i in range(self.length):
            if self.data[i] == value:
                return i
        raise Exception("Value not found in array")

    def remove(self, value):
        index = self.index(value)  # находим индекс элемента
        # сдвигаем все элементы после найденного на один индекс влево
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        # очищаем последний элемент
        self.data[self.length - 1] = None
        self.length -= 1


if __name__ == '__main__':
    array = DynamicArray()
    
