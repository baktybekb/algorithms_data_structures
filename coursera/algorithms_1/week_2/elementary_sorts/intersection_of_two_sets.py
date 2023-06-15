"""
Problem:
Given two arrays a[] and b[], each containing n distinct 2D points in the plane, design a subquadratic algorithm to
count the number of points that are contained both in array a[] and array b[].
"""


def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            swap(array, j - 1, j)
            j -= 1
    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def count_common_points(a: list, b):
    a = insertion_sort(a)
    b = insertion_sort(b)
    i = j = 0
    count = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:
            count += 1
            i += 1
            j += 1
    return count


def test():
    a = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    b = [(2, 2), (4, 4), (6, 6), (8, 8), (10, 10)]
    assert count_common_points(a, b) == 2


if __name__ == '__main__':
    test()

