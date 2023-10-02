# https://www.algoexpert.io/questions/next-greater-element

# O(n) time | O(n) space
def nextGreaterElement(array):
    stack = []
    res = [-1] * len(array)
    for i in range(len(array) * 2):
        i = i % len(array)
        while stack and array[stack[-1]] < array[i]:
            res[stack.pop()] = array[i]
        stack.append(i)
    return res


if __name__ == '__main__':
    assert nextGreaterElement([2, 5, -3, -4, 6, 7, 2]) == [5, 6, 6, 6, 7, -1, 5]
