"""
Problem:

Dutch national flag. Given an array of n buckets, each containing a red, white, or blue pebble, sort them by color.
The allowed operations are:
    swap(i, j): swap the pebble in bucket i with the pebble in bucket j.
    color(i): determine the color of the pebble in bucket i.
The performance requirements are as follows:
    at most n calls to color()
    at most n calls to swap()
    constant extra space

Hint: 3-way partitioning.
"""


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def sort_pebbles(array):
    # red = 0, 1 = white, blue = 2
    i = j = 0
    k = len(array) - 1
    while j <= k:
        if array[j] == 0:
            swap(array, i, j)
            i += 1
            j += 1
        elif array[j] == 1:
            j += 1
        else:
            swap(array, j, k)
            k -= 1
    return array


def test():
    assert sort_pebbles([2, 0, 1, 2, 1, 0]) == [0, 0, 1, 1, 2, 2]
    assert sort_pebbles([1, 2, 0, 1, 2, 0, 1]) == [0, 0, 1, 1, 1, 2, 2]


if __name__ == '__main__':
    test()

