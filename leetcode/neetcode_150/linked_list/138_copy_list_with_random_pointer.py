from typing import Optional


class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


# O(n) time | O(n) space
class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        hash_table = {}
        node = head
        while node:
            hash_table[node] = Node(node.val)
            node = node.next
        node = head
        while node:
            copy = hash_table[node]
            copy.next = hash_table.get(node.next)
            copy.random = hash_table.get(node.random)
            node = node.next
        return hash_table.get(head)

