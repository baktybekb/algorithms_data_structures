# https://www.algoexpert.io/questions/youngest-common-ancestor

class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


# O(d) time | O(1) space, d --> depth of the tree
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depth_one, depth_two = find_depth(descendantOne), find_depth(descendantTwo)
    while depth_one != depth_two:
        if depth_one < depth_two:
            descendantTwo = descendantTwo.ancestor
            depth_two -= 1
        else:
            descendantOne = descendantOne.ancestor
            depth_one -= 1
    while descendantOne != descendantTwo:
        descendantOne = descendantOne.ancestor
        descendantTwo = descendantTwo.ancestor
    return descendantOne


def find_depth(node):
    depth = 0
    while node:
        depth += 1
        node = node.ancestor
    return depth
