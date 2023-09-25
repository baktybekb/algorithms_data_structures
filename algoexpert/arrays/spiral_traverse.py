# https://www.algoexpert.io/questions/spiral-traverse

# O(n) time | O(n) space, n == total number of elements
def spiralTraverse(array):
    top, bot = 0, len(array)
    l, r = 0, len(array[0])
    res = []
    while top < bot and l < r:
        for i in range(l, r):
            res.append(array[top][i])
        top += 1
        for i in range(top, bot):
            res.append(array[i][r - 1])
        r -= 1
        if not top < bot or not l < r:
            return res
        for i in reversed(range(l, r)):
            res.append(array[bot - 1][i])
        bot -= 1
        for i in reversed(range(top, bot)):
            res.append(array[i][l])
        l += 1
    return res


if __name__ == '__main__':
    spiralTraverse(
        [
            [1, 2, 3, 4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10, 9, 8, 7]
        ]
    )
    spiralTraverse(
        [
            [4, 2, 3, 6, 7, 8, 1, 9, 5, 10],
            [12, 19, 15, 16, 20, 18, 13, 17, 11, 14]
        ]
    )
