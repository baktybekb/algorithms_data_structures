# O(n) time | O(1) space
def bestSeat(seats):
    longest, index = 0, -1
    l = 0
    while l < len(seats):
        r = l + 1
        while r < len(seats) and seats[r] == 0:
            r += 1
        length = r - l - 1
        if length > longest:
            longest = length
            index = (l + r) // 2
        l = r
    return index


if __name__ == '__main__':
    assert bestSeat([1, 0, 0, 1, 0, 0, 1]) == 1
    assert bestSeat([1, 0, 0, 1, 0, 0, 0, 1]) == 5

