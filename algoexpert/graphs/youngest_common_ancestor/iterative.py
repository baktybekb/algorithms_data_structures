# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


# O(d) time | O(1) space, d --> depth of tree
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depth_one = find_depth(descendantOne)
    depth_two = find_depth(descendantTwo)
    diff = abs(depth_one - depth_two)
    if depth_one > depth_two:
        return find_ancestor(descendantOne, descendantTwo, diff)
    else:
        return find_ancestor(descendantTwo, descendantOne, diff)


def find_ancestor(lower, higher, diff):
    while diff > 0:
        lower = lower.ancestor
        diff -= 1
    while lower != higher:
        lower = lower.ancestor
        higher = higher.ancestor
    return lower


def find_depth(descendant):
    depth = 0
    while descendant:
        depth += 1
        descendant = descendant.ancestor
    return depth
