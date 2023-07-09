# O(2^(m + n)), m, n - length of one and two, respectively
# O(n + m) space, recursion depth
def interweavingStrings(one, two, three):
    if len(three) != len(one) + len(two):
        return False
    counter = [0]
    res = helper(one, two, three, 0, 0, counter)
    return res


def helper(one, two, three, i, j, counter):
    counter[0] += 1
    k = i + j
    if k == len(three):
        return True
    if i < len(one) and one[i] == three[k]:
        if helper(one, two, three, i + 1, j, counter):
            return True
    if j < len(two) and two[j] == three[k]:
        return helper(one, two, three, i, j + 1, counter)
    return False


if __name__ == '__main__':
    # 520 recursion calls
    interweavingStrings(one="aaaaaaaa", two="aaaaaaaab", three="aaaaaaaabaaaaaaaa")
