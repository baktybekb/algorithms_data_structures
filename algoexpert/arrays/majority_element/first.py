# O(n) time | O(1) space
def majorityElement(array):
    answer = array[0]
    count = 1
    for i in range(1, len(array)):
        if count == 0:
            count += 1
            answer = array[i]
        elif array[i] == answer:
            count += 1
        else:
            count -= 1
    return answer


if __name__ == '__main__':
    assert majorityElement([1, 1, 2, 2, 7, 2, 2]) == 2
