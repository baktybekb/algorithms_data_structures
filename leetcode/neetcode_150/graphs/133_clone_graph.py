# https://leetcode.com/problems/clone-graph/description/

from typing import Optional


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# O(v + e) time | O(v) space
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_map = {}

        def dfs(node):
            root = Node(node.val)
            node_map[node] = root
            for nei in node.neighbors:
                if nei in node_map:
                    new_nei = node_map[nei]
                else:
                    new_nei = dfs(nei)
                root.neighbors.append(new_nei)
            return root

        return dfs(node) if node else None
