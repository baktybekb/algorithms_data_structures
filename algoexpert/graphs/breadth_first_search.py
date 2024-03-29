# https://www.algoexpert.io/questions/breadth-first-search
from collections import deque


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(v + e) time | O(V) space
    def breadthFirstSearch(self, array):
        queue = deque((self,))
        while queue:
            node = queue.popleft()
            array.append(node.name)
            for child in node.children:
                queue.append(child)
        return array
