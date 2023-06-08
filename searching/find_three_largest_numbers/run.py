# O(n) space | O(1) space
def findThreeLargestNumbers(array):
    result = [None, None, None]
    for num in array:
        if result[2] is None or num >= result[2]:
            shift(result, num, 2)
        elif result[1] is None or num >= result[1]:
            shift(result, num, 1)
        elif result[0] is None or num >= result[0]:
            shift(result, num, 0)
    return result


def shift(array, number, index):
    for i in range(index + 1):
        if i == index:
            array[index] = number
        else:
            array[i] = array[i + 1]
