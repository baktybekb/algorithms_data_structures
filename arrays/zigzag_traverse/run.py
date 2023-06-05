# O(n) time | O(n) space
def zigzagTraverse(array):
    row, col = 0, 0
    height = len(array) - 1
    width = len(array[0]) - 1
    result = []
    going_down = True
    while is_within_the_bounds(row, col, height, width):
        result.append(array[row][col])
        if going_down:
            if col == 0 or row == height:
                going_down = False
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if row == 0 or col == width:
                going_down = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                col += 1
                row -= 1
    return result


def is_within_the_bounds(row, col, height, width):
    return 0 <= row <= height and 0 <= col <= width
