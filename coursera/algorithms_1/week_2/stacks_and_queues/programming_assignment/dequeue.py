"""
Problem:
Write a generic data type for a deque and a randomized queue. The goal of this assignment is to implement elementary
data structures using arrays and linked lists, and to introduce you to generics and iterators.
Dequeue. A double-ended queue or deque (pronounced “deck”) is a generalization of a stack and a queue that supports
adding and removing items from either the front or the back of the data structure. Create a generic data type Deque
that implements the following API:

public class Deque<Item> implements Iterable<Item> {

    // construct an empty deque
    public Deque()

    // is the deque empty?
    public boolean isEmpty()

    // return the number of items on the deque
    public int size()

    // add the item to the front
    public void addFirst(Item item)

    // add the item to the back
    public void addLast(Item item)

    // remove and return the item from the front
    public Item removeFirst()

    // remove and return the item from the back
    public Item removeLast()

    // return an iterator over items in order from front to back
    public Iterator<Item> iterator()

    // unit testing (required)
    public static void main(String[] args)

}

Corner cases.  Throw the specified exception for the following corner cases:
    Throw an IllegalArgumentException if the client calls either addFirst() or addLast() with a null argument.
    Throw a java.util.NoSuchElementException if the client calls either removeFirst() or removeLast when the deque is
    empty.
    Throw a java.util.NoSuchElementException if the client calls the next() method in the iterator when there are no more
    items to return.
    Throw an UnsupportedOperationException if the client calls the remove() method in the iterator.

Unit testing.  Your main() method must call directly every public constructor and method to help verify that they work as prescribed (e.g., by printing results to standard output).

Performance requirements.  Your deque implementation must support each deque operation (including construction) in
constant worst-case time. A deque containing n items must use at most 48n + 192 bytes of memory. Additionally, your
iterator implementation must support each operation (including construction) in constant worst-case time.
"""
import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DequeIterator:
    def __init__(self, first_node):
        self.current_node = first_node

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_node is None:
            raise StopIteration
        value = self.current_node.value
        self.current_node = self.current_node.next
        return value


class Deque:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def size(self):
        return self.length

    def add_first(self, value):
        old_first = self.first
        self.first = Node(value)
        self.first.next = old_first
        if old_first is None:
            self.last = self.first
        else:
            old_first.prev = self.first
        self.length += 1

    def add_last(self, value):
        old_last = self.last
        self.last = Node(value)
        self.last.prev = old_last
        if old_last is None:
            self.first = self.last
        else:
            old_last.next = self.last
        self.length += 1

    def remove_first(self):
        if self.is_empty():
            raise IndexError('deque is empty')
        value = self.first.value
        self.first = self.first.next
        if self.first is None:
            self.last = None
        else:
            self.first.prev = None
        self.length -= 1
        return value

    def remove_last(self):
        if self.is_empty():
            raise IndexError('deque is empty')
        value = self.last.value
        self.last = self.last.prev
        if self.last is None:
            self.first = None
        else:
            self.last.next = None
        self.length -= 1
        return value

    def iterator(self):
        return DequeIterator(self.first)


class DequeTest(unittest.TestCase):
    def test_func(self):
        deque = Deque()
        deque.add_first(1)
        deque.add_last(2)
        self.assertEqual(deque.size(), 2)

        iterator = deque.iterator()
        self.assertEqual(next(iterator), 1)
        self.assertEqual(next(iterator), 2)

        self.assertEqual(deque.remove_first(), 1)
        self.assertEqual(deque.remove_last(), 2)
        self.assertEqual(deque.size(), 0)
        with self.assertRaises(IndexError) as er:
            deque.remove_first()
            self.assertEqual(er.exception, 'deque is empty')
