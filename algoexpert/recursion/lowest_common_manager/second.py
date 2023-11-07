# https://www.algoexpert.io/questions/lowest-common-manager

# O(n) time | O(h) space, h --> height of the tree
def getLowestCommonManager(topManager, reportOne, reportTwo):
    target = [None]

    def helper(node):
        count = 0
        for child in node.directReports:
            child_count = helper(child)
            if child_count == 2:
                return child_count
            count += child_count
        if node == reportOne or node == reportTwo:
            count += 1
        if count == 2:
            target[0] = node
        return count

    helper(topManager)
    return target[0]


# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
