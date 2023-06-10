# O(n) time | O(1) space
def threeNumberSort(array, order):
    buckets = [0, 0, 0]
    for num in array:
        index = order.index(num)
        buckets[index] += 1
    start = 0
    for i in range(3):
        count = buckets[i]
        for j in range(start, count + start):
            array[j] = order[i]
            start += 1
    return array
