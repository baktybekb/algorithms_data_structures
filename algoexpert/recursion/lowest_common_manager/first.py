# https://www.algoexpert.io/questions/lowest-common-manager

# O(n) time | O(h) space, h --> height of the tree
def getLowestCommonManager(topManager, reportOne, reportTwo):

    def helper(node):
        count = 0
        for child in node.directReports:
            child_info = helper(child)
            if child_info.target:
                return child_info
            count += child_info.count
        if node == reportOne or node == reportTwo:
            count += 1
        return TreeInfo(node if count == 2 else None, count)

    return helper(topManager).target


class TreeInfo:
    def __init__(self, target=None, count=0):
        self.target = target
        self.count = count


# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
