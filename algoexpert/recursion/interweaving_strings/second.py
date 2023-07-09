# O(n * m) time | O(n * m) space
def interweavingStrings(one, two, three):
    if len(three) != len(one) + len(two):
        return False
    cache = [[None for j in range(len(two) + 1)] for i in range(len(one) + 1)]
    res = helper(one, two, three, 0, 0, cache)
    return res


def helper(one, two, three, i, j, cache):
    if cache[i][j] is not None:
        return cache[i][j]
    k = i + j
    if k == len(three):
        return True
    if i < len(one) and one[i] == three[k]:
        cache[i + 1][j] = helper(one, two, three, i + 1, j, cache)
        if cache[i + 1][j]:
            return True
    if j < len(two) and two[j] == three[k]:
        cache[i][j + 1] = helper(one, two, three, i, j + 1, cache)
        return cache[i][j + 1]
    return False


if __name__ == '__main__':
    # 54 recursive calls
    interweavingStrings(one="aaaaaaaa", two="aaaaaaaab", three="aaaaaaaabaaaaaaaa")
