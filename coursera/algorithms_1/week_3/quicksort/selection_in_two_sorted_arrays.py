"""
Problem:
Selection in two sorted arrays.
Given two sorted arrays a[] and b[], of length n1 and n2 and an integer 0 <= k < n1 + n2, design an algorithm to find
a key of rank k. The order of growth of the worst case running time of your algorithm should be lg(n), where n = n1 + n2
Version 1: n1 == n2 and k = n / 2
Version 2: k = n / 2
Version 3: no restrictions

Hint: there are two basic approaches.
Approach A: Compute the median in a[] and the median in b[]. Recur in a subproblem of roughly half the size.
Approach B: Design a constant-time algorithm to determine whether a[i] is a key of rank k. Use thes subroutine and
binary search.
Dealing with corner cases can be tricky.
"""


def findKthElement(arr1, arr2, k, start1 = 0, start2 = 0):
    if start1 == len(arr1):
        return arr2[start2 + k]
    if start2 == len(arr2):
        return arr1[start1 + k]
    if k == 0:
        return min(arr1[start1], arr2[start2])

    mid1 = min((k + 1) // 2, len(arr1) - start1)
    mid2 = min((k + 1) // 2, len(arr2) - start2)
    if arr1[start1 + mid1 - 1] < arr2[start2 + mid2 - 1]:
        return findKthElement(arr1, arr2, k - mid1, start1 + mid1, start2)
    else:
        return findKthElement(arr1, arr2, k - mid2, start1, start2 + mid2)


def test():
    arr1 = [1, 5, 6, 9, 12]
    arr2 = [2, 4, 7, 11, 10]
    # 1, 2, 4, 5, 6, 7, 9, 10, 10, 11, 12
    # 0, 1, 2  3  4  5  6  7   8   9   10
    k = 9
    print(findKthElement(arr1, arr2, k - 1))

    # arr1 = [1, 2, 3, 4, 5]
    # arr2 = [6, 7, 8, 9, 10]
    # k = 7
    # print(findKthElement(arr1, arr2, k - 1))  # Expected output: 7


if __name__ == '__main__':
    test()
