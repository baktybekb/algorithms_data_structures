# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.
class LRUCache:
    def __init__(self, maxSize):
        self.current_size = 0
        self.hash_table = {}
        self.list = DoublyLinkedList()
        self.maxSize = maxSize or 1

    # O(1) time | O(1) space
    def insertKeyValuePair(self, key, value):
        if node := self.hash_table.get(key):
            node.value = value
            node.remove_bindings()
            self.list.set_head_to(node)
            return
        if self.current_size == self.maxSize:
            to_remove = self.list.tail.key
            self.list.remove_tail()
            del self.hash_table[to_remove]
        else:
            self.current_size += 1
        node = Node(key, value)
        self.list.set_head_to(node)
        self.hash_table[key] = node

    def getValueFromKey(self, key):
        if node := self.hash_table.get(key):
            self.list.set_head_to(node)
            return node.value
        return None

    def getMostRecentKey(self):
        if self.list.head:
            return self.list.head.key
        return None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def set_head_to(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        elif node == self.head:
            return
        elif self.head == self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail
        else:
            if self.tail == node:
                self.remove_tail()
            node.remove_bindings()
            node.next = self.head
            self.head.prev = node
            self.head = node

    def remove_tail(self):
        if self.tail is None:
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None


class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

    def remove_bindings(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        self.prev = None
        self.next = None

