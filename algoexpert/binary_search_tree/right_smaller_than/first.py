# O(nlog(n)) time | O(n) space
def rightSmallerThan(array):
    if len(array) == 0:
        return array
    last_idx = len(array) - 1
    right_smaller = array[:]
    right_smaller[last_idx] = 0
    bst = SpecialBST(array[last_idx])
    for i in reversed(range(last_idx)):
        bst.insert(array[i], i, right_smaller)
    return right_smaller


class SpecialBST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.left_subtree_size = 0

    # O(log(n)) time
    def insert(self, value, idx, right_smaller, smaller_at_insert=0):
        if value < self.value:
            self.left_subtree_size += 1
            if self.left:
                self.left.insert(value, idx, right_smaller, smaller_at_insert)
            else:
                self.left = SpecialBST(value)
                right_smaller[idx] = smaller_at_insert
        else:
            smaller_at_insert += self.left_subtree_size
            if self.value < value:
                smaller_at_insert += 1
            if self.right:
                self.right.insert(value, idx, right_smaller, smaller_at_insert)
            else:
                self.right = SpecialBST(value)
                right_smaller[idx] = smaller_at_insert
