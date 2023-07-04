class Node:
    __slots__ = 'key', 'value', 'next'

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, key, value):
        if self.head is None:
            self.head = Node(key, value)
            self.length += 1
            return True
        node = self.head
        while node and node.next:
            if node.key == key:
                node.value = value
                return False
            node = node.next
        if node.key == key:
            node.value = value
            return False
        else:
            node.next = Node(key, value)
            self.length += 1
            return True

    def search(self, key):
        node = self.head
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def delete(self, key):
        if self.head is None:
            return False
        if self.head.key == key:
            self.head = self.head.next
            self.length -= 1
            return True
        node = self.head
        while node and node.next:
            if node.next.key == key:
                node.next = node.next.next
                self.length -= 1
                return True
            node = node.next
        return False

    def __str__(self):
        result = []
        node = self.head
        while node:
            result.append(f'{node.key}: {node.value}')
            node = node.next
        return ' -> '.join(result)

    def __len__(self):
        return self.length


class HashTable:

    def __init__(self, size=4):
        self.size = size
        self.count = 0
        self.table = [LinkedList() for _ in range(self.size)]

    def hash_func(self, key):
        return hash(key) % self.size

    def __setitem__(self, key, value):
        idx = self.hash_func(key)
        inserted = self.table[idx].insert(key, value)
        if not inserted:
            return
        self.count += 1
        if self.count / self.size <= 0.5:
            return
        self._resize(self.size * 2)

    def __getitem__(self, key):
        idx = self.hash_func(key)
        value = self.table[idx].search(key)
        if value:
            return value
        raise ValueError('key not found')

    def get(self, key):
        try:
            value = self.__getitem__(key)
        except ValueError:
            value = None
        return value

    def __delitem__(self, key):
        idx = self.hash_func(key)
        deleted = self.table[idx].delete(key)
        if not deleted:
            return
        self.count -= 1
        if self.count / self.size >= 0.3:
            return
        self._resize(self.size // 2)

    def __iter__(self):
        for linked_list in self.table:
            node = linked_list.head
            while node:
                yield node.key, node.value
                node = node.next

    def __len__(self):
        return self.count

    def keys(self):
        return (key for key, val in self)

    def values(self):
        return (val for key, val in self)

    def _resize(self, size):
        old_table = self.table
        self.size = max(4, size)
        self.table = [LinkedList() for _ in range(self.size)]
        self.count = 0
        for linked_list in old_table:
            node = linked_list.head
            while node:
                self.__setitem__(node.key, node.value)
                node = node.next
