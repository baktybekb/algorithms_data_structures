"""
Problem:
A disorganized carpenter has a mixed pile of n nuts and n bolts. The goal is to find the corresponding pairs of nuts and
bolts. Each nut fits exactly one bolt and one bolt fits exactly one nut. By fitting nut and bolt together, the carpenter
can see which one is bigger (but the carpenter cannot compare two nuts or two bolts directly). Design an algorithm for
the problem that uses at most proportional to n log n compares (probabilistically).
Hint:
modify the quicksort partitioning part of quicksort
"""


def quick_sort(nuts, bolts, start, end):
    if start >= end:
        return
    pivot_idx = partition(nuts, bolts[start], start, end)
    partition(bolts, nuts[pivot_idx], start, end)
    quick_sort(nuts, bolts, start, pivot_idx - 1)
    quick_sort(nuts, bolts, pivot_idx + 1, end)


def partition(array, pivot, start, end):
    i = start
    j = end
    while i <= j:
        if array[i] <= pivot:
            i += 1
        else:
            swap(array, i, j)
            j -= 1
    swap(array, start, j)
    return j


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def test():
    nuts = [5, 3, 1, 7, 2]
    bolts = [2, 1, 5, 7, 3]
    quick_sort(nuts, bolts, 0, len(nuts) - 1)

    print('Nuts:', nuts)
    print('Bolts:', bolts)


if __name__ == '__main__':
    test()
