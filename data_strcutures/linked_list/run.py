import timeit
import collections
from memory_profiler import memory_usage


class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def set_head(self, node: Node):
        if self.head:
            self.insert_before(self.head, node)
            return
        self.head = node
        self.tail = node

    def set_tail(self, node: Node):
        if self.tail:
            self.insert_after(self.tail, node)
            return
        self.set_head(node)

    def insert_before(self, node: Node, node_to_insert: Node):
        if self.head == node_to_insert and self.tail == node_to_insert:
            return
        self.remove(node_to_insert)
        node_to_insert.next = node
        node_to_insert.prev = node.prev
        if node.prev:
            node.prev.next = node_to_insert
        else:
            self.head = node_to_insert
        node.prev = node_to_insert

    def insert_after(self, node: Node, node_to_insert: Node):
        if self.head == node_to_insert and self.tail == node_to_insert:
            return
        self.remove(node_to_insert)
        node_to_insert.next = node.next
        node_to_insert.prev = node
        if node.next:
            node.next.prev = node_to_insert
        else:
            self.tail = node_to_insert
        node.next = node_to_insert

    def insert_at_position(self, position: int, node_to_insert: Node):
        if position == 1:
            self.set_head(node_to_insert)
            return
        node = self.head
        cur_position = 1
        while cur_position != position:
            node = node.next
            cur_position += 1
        if node:
            self.insert_before(node, node_to_insert)
        else:
            self.set_tail(node_to_insert)

    def remove_nodes_with_value(self, value: int):
        node = self.head
        while node:
            next_node = node.next
            if node.value == value:
                self.remove(node)
            node = next_node

    def remove(self, node: Node):
        if self.head == node:
            self.head = self.head.next
        if self.tail == node:
            self.tail = self.tail.prev
        self.remove_bindings(node)

    def contains_node_with_value(self, value: int):
        node = self.head
        while node and node.value != value:
            node = node.next
        return node is not None

    def remove_bindings(self, node: Node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.next = None
        node.prev = None


def test_doubly_linked_list():
    # Create a new doubly linked list
    dll = DoublyLinkedList()

    # Create some nodes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    # Test setHead method
    dll.set_head(node1)
    assert dll.head == node1
    assert dll.tail == node1

    # Test setTail method
    dll.set_tail(node2)
    assert dll.head == node1
    assert dll.tail == node2
    assert dll.head.next == node2
    assert dll.tail.prev == node1

    # Test insertBefore method
    dll.insert_before(node2, node3)
    assert dll.head == node1
    assert dll.head.next == node3
    assert dll.tail == node2
    assert dll.tail.prev == node3

    # Test insertAfter method
    dll.insert_after(node3, node4)
    assert dll.head == node1
    assert dll.head.next == node3
    assert node3.next == node4
    assert dll.tail == node2
    assert dll.tail.prev == node4

    # Test insertAtPosition method
    node5 = Node(5)
    dll.insert_at_position(1, node5)
    assert dll.head == node5
    assert dll.head.next == node1
    assert node1.prev == node5

    # Test removeNodesWithValue method
    dll.remove_nodes_with_value(1)
    assert dll.head == node5
    assert dll.head.next == node3

    # Test containsNodeWithValue method
    assert dll.contains_node_with_value(5)
    assert not dll.contains_node_with_value(1)

    print("All test cases pass")


def append_items(data_structure):
    for i in range(10000):
        if isinstance(data_structure, DoublyLinkedList):
            data_structure.set_tail(Node(str(i)))
        else:
            data_structure.append(str(i))


def append_left_items(data_structure):
    for i in range(10000):
        if isinstance(data_structure, DoublyLinkedList):
            data_structure.set_head(Node(str(i)))
        else:
            data_structure: collections.deque
            data_structure.appendleft(str(i))


def insert_items(data_structure):
    for i in range(10000, 20000):
        if isinstance(data_structure, DoublyLinkedList):
            data_structure.insert_at_position(5000, Node(str(i)))
        else:
            data_structure: collections.deque
            data_structure.insert(5000, str(i))


def remove_items(data_structure):
    for _ in range(10000):
        if isinstance(data_structure, DoublyLinkedList):
            data_structure.remove(data_structure.head)
        else:
            data_structure: collections.deque
            data_structure.popleft()


def performance_test():
    dll = DoublyLinkedList()
    deque = collections.deque()

    # Time and monitor memory usage while appending 10,000 items to the DoublyLinkedList
    start_time = timeit.default_timer()
    start_mem = memory_usage(max_usage=True)
    append_items(dll)
    dll_time = timeit.default_timer() - start_time
    dll_mem = memory_usage(max_usage=True) - start_mem

    # Time and monitor memory usage while appending 10,000 items to the Python deque
    start_time = timeit.default_timer()
    start_mem = memory_usage(max_usage=True)
    append_items(deque)
    pd_time = timeit.default_timer() - start_time
    pd_mem = memory_usage(max_usage=True) - start_mem

    print(f"Custom DoublyLinkedList append time: {dll_time}, memory increase: {dll_mem} MiB")
    print(f"Python deque append time: {pd_time}, memory increase: {pd_mem} MiB")
    print('-' * 50)

    # Time and monitor memory usage while appending 10,000 items to the DoublyLinkedList
    start_time = timeit.default_timer()
    start_mem = memory_usage(max_usage=True)
    append_left_items(dll)
    dll_time = timeit.default_timer() - start_time
    dll_mem = memory_usage(max_usage=True) - start_mem

    # Time and monitor memory usage while appending 10,000 items to the Python deque
    start_time = timeit.default_timer()
    start_mem = memory_usage(max_usage=True)
    append_left_items(deque)
    pd_time = timeit.default_timer() - start_time
    pd_mem = memory_usage(max_usage=True) - start_mem

    print(f"Custom DoublyLinkedList append LEFT time: {dll_time}, memory increase: {dll_mem} MiB")
    print(f"Python deque append LEFT time: {pd_time}, memory increase: {pd_mem} MiB")
    print('-' * 50)

    # Time and monitor memory usage while inserting 10,000 items to the DoublyLinkedList
    start_time = timeit.default_timer()
    start_mem = memory_usage(max_usage=True)
    insert_items(dll)
    dll_time = timeit.default_timer() - start_time
    dll_mem = memory_usage(max_usage=True) - start_mem

    # Time and monitor memory usage while inserting 10,000 items to the Python deque
    start_time = timeit.default_timer()
    start_mem = memory_usage(max_usage=True)
    insert_items(deque)
    pd_time = timeit.default_timer() - start_time
    pd_mem = memory_usage(max_usage=True) - start_mem

    print(f"Custom DoublyLinkedList insert time: {dll_time}, memory increase: {dll_mem} MiB")
    print(f"Python deque insert time: {pd_time}, memory increase: {pd_mem} MiB")
    print('-' * 50)

    # Time and monitor memory usage while removing 10,000 items from the DoublyLinkedList
    start_time = timeit.default_timer()
    start_mem = memory_usage(max_usage=True)
    remove_items(dll)
    dll_time = timeit.default_timer() - start_time
    dll_mem = memory_usage(max_usage=True) - start_mem

    # Time and monitor memory usage while removing 10,000 items from the Python deque
    start_time = timeit.default_timer()
    start_mem = memory_usage(max_usage=True)
    remove_items(deque)
    pd_time = timeit.default_timer() - start_time
    pd_mem = memory_usage(max_usage=True) - start_mem

    print(f"Custom DoublyLinkedList remove time: {dll_time}, memory increase: {dll_mem} MiB")
    print(f"Python deque remove time: {pd_time}, memory increase: {pd_mem} MiB")
    print('-' * 50)


if __name__ == '__main__':
    # test_doubly_linked_list()
    performance_test()


"""
Custom DoublyLinkedList append time: 0.11486045899800956, memory increase: 2.09375 MiB
Python deque append time: 0.10655920899444027, memory increase: 0.6875 MiB
--------------------------------------------------
Custom DoublyLinkedList append LEFT time: 0.12363312499655876, memory increase: 2.15625 MiB
Python deque append LEFT time: 0.10984908300451934, memory increase: 0.75 MiB
--------------------------------------------------
Custom DoublyLinkedList insert time: 1.982004457997391, memory increase: 2.15625 MiB
Python deque insert time: 0.1509080420000828, memory increase: 0.703125 MiB
--------------------------------------------------
Custom DoublyLinkedList remove time: 0.11953887499839766, memory increase: 0.0 MiB
Python deque remove time: 0.10974508299841546, memory increase: 0.0 MiB
--------------------------------------------------
"""
