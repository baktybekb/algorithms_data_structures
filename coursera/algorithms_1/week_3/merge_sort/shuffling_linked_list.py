"""
Problem:
    Given a singly linked list containing n items, rearrange the items uniformly at random.
    Your algorithm should consume a logarithmic (or constant) amount of extra memory and run in time proportional
    to n log n in the worst case.

    Hint: design a linear-time subroutine that can take two uniformly shuffled linked lists of sizes n1 and n2
    and combined them into a uniformly shuffled linked lists of size n1 + n2
"""
import random


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def get_size(node):
    size = 0
    while node:
        size += 1
        node = node.next
    return size


def shuffle(head):
    if head is None or head.next is None:
        return head
    slow = head
    fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = None
    left = shuffle(head)
    right = shuffle(slow)
    return merge_shuffle(left, right)


def merge_shuffle(node_one, node_two):
    dummy = Node(0)
    tail = dummy
    size_one = get_size(node_one)
    size_two = get_size(node_two)
    while node_one and node_two:
        probability = size_one / (size_one + size_two)
        if random.random() <= probability:
            tail.next = node_one
            node_one = node_one.next
            size_one -= 1
        else:
            tail.next = node_two
            node_two = node_two.next
            size_two -= 1
        tail = tail.next
    if node_one:
        tail.next = node_one
    else:
        tail.next = node_two
    return dummy.next


def test():
    nodes = [Node(i) for i in range(1, 7)]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    head = nodes[0]
    node = head
    while node:
        print(node.val, end=' ')
        node = node.next
    print()
    res = shuffle(head)
    node = res
    while node:
        print(node.val, end=' ')
        node = node.next


if __name__ == '__main__':
    test()
