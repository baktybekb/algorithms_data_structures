# O(n * m) time | O(n * m) space
def zigzagTraverse(array):
    res = []
    go_down = True
    row = col = 0
    while row < len(array) and col < len(array[0]):
        res.append(array[row][col])
        if go_down:
            if row == len(array) - 1 or col == 0:
                go_down = False
                if row == len(array) - 1:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if row == 0 or col == len(array[0]) - 1:
                go_down = True
                if col == len(array[0]) - 1:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1
    return res


if __name__ == '__main__':
    assert zigzagTraverse([
        [1, 3, 4, 10],
        [2, 5, 9, 11],
        [6, 8, 12, 15],
        [7, 13, 14, 16]
    ]) == [i for i in range(1, 17)]
    assert zigzagTraverse([
        [1, 3],
        [2, 4],
        [5, 6],
    ]) == [i for i in range(1, 7)]
    assert zigzagTraverse([
        [1, 2, 3, 4],
    ]) == [i for i in range(1, 5)]
