# O(1) time | O(1) space --> all method in LRUCache
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.list = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.update_most_recent(self.cache[key])
            return self.cache[key].value
        return -1

    def update_most_recent(self, node):
        self.list.set_head(node)

    def evict_least_recent(self):
        key = self.list.tail.key
        self.list.remove_tail()
        del self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
        else:
            if len(self.cache) == self.capacity:
                self.evict_least_recent()
            self.cache[key] = Node(key, value)
        self.update_most_recent(self.cache[key])


class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

    def remove_bindings(self):
        if self.next:
            self.next.prev = self.prev
        if self.prev:
            self.prev.next = self.next
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def set_head(self, node):
        if self.head == node:
            return
        if self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.tail.prev = node
            node.next = self.tail
            self.head = node
        else:
            if node == self.tail:
                self.remove_tail()
            node.remove_bindings()
            self.head.prev = node
            node.next = self.head
            self.head = node

    def remove_tail(self):
        if self.tail is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
