# O(n * m) time | O(n * m) space
def interweavingStrings(one, two, three):
    if len(three) != len(one) + len(two):
        return False
    cache = [[None for j in range(len(two) + 1)] for i in range(len(one) + 1)]

    def helper(i, j):
        if cache[i][j] is not None:
            return cache[i][j]
        k = i + j
        if k == len(three):
            return True
        if i < len(one) and one[i] == three[k]:
            cache[i][j] = helper(i + 1, j)
            if cache[i][j]:
                return True
        if j < len(two) and two[j] == three[k]:
            cache[i][j] = helper(i, j + 1)
            return cache[i][j]
        cache[i][j] = False
        return False

    return helper(0, 0)
