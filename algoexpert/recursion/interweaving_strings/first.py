# O(2^(n + m)) time | O(n + m) time
def interweavingStrings(one, two, three):
    if len(three) != len(one) + len(two):
        return False

    def helper(i, j):
        k = i + j
        if k == len(three):
            return True
        if i < len(one) and one[i] == three[k]:
            if helper(i + 1, j):
                return True
        if j < len(two) and two[j] == three[k]:
            return helper(i, j + 1)
        return False

    return helper(0, 0)


if __name__ == '__main__':
    interweavingStrings(one="aaaaaa", two="aaaaaab", three="aaaaaabaaaaaa")
