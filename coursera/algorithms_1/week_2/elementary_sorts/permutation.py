"""
Problem:
 Given two integer arrays of size n, design a subquadratic algorithm to determine whether one is a permutation of the
 other.
That is, do they contain exactly the same entries but, possibly, in a different order.
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


def permutation(a, b):
    a = insertion_sort(a)
    b = insertion_sort(b)
    return a == b


def test():
    a = [1, 2, 4, 0, 2, 3]
    b = [3, 2, 2, 0, 4, 1]
    assert permutation(a, b) is True

    a = [1, 2, 4, 0, 2, 14]
    b = [3, 2, 2, 0, 4, 1]
    assert permutation(a, b) is False


if __name__ == '__main__':
    test()
