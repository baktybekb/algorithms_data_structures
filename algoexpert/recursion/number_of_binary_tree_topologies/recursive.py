# O(n^2) time | O(n) space
def numberOfBinaryTreeTopologies(n):
    cache = {0: 1}

    def helper(tree_size):
        if tree_size in cache:
            return cache[tree_size]
        topologies = 0
        for left_size in range(n):
            right_size = n - 1 - left_size
            left_topologies = numberOfBinaryTreeTopologies(left_size)
            right_topologies = numberOfBinaryTreeTopologies(right_size)
            topologies += left_topologies * right_topologies
        cache[tree_size] = topologies
        return topologies

    return helper(n)
