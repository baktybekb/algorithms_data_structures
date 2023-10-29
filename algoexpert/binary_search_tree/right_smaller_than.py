# https://www.algoexpert.io/questions/right-smaller-than

# O(nlog(n)) time | O(n) space
def rightSmallerThan(array):
    output = [0] * len(array)
    if not array:
        return output
    las_idx = len(array) - 1
    bst = BST(array[las_idx])
    for idx in reversed(range(las_idx)):
        bst.insert(array[idx], idx, output)
    return output


class BST:
    def __init__(self, value, left_subtree=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.left_subtree = left_subtree

    def insert(self, value, idx, output, smaller_count=0):
        if value < self.value:
            self.left_subtree += 1
            if self.left:
                self.left.insert(value, idx, output, smaller_count)
            else:
                self.left = BST(value)
                output[idx] = smaller_count
        else:
            if value > self.value:
                smaller_count += 1
            smaller_count += self.left_subtree
            if self.right:
                self.right.insert(value, idx, output, smaller_count)
            else:
                self.right = BST(value)
                output[idx] = smaller_count
