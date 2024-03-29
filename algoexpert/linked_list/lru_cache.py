# https://www.algoexpert.io/questions/lru-cache

# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.

# O(1) time | O(1) space --> all methods in LRUCache
class LRUCache:
    def __init__(self, max_size):
        self.max_size = max_size or 1
        self.cache = {}
        self.list = DoublyLinkedList()

    def insertKeyValuePair(self, key, value):
        if key in self.cache:
            self.cache[key].value = value
        else:
            if len(self.cache) == self.max_size:
                self.evict_least_recent()
            self.cache[key] = Node(key, value)
        self.update_most_recent(self.cache[key])

    def evict_least_recent(self):
        key = self.list.tail.key
        self.list.remove_tail()
        del self.cache[key]

    def update_most_recent(self, node):
        self.list.set_head(node)

    def getValueFromKey(self, key):
        if key not in self.cache:
            return None
        value = self.cache[key].value
        self.update_most_recent(self.cache[key])
        return value

    def getMostRecentKey(self):
        return self.list.head.key


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
        self.prev = None
        self.next = None


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
            node.next = self.head
            self.head.prev = node
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


