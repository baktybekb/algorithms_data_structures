# https://www.algoexpert.io/questions/one-edit

# O(n) time | O(1) space
def oneEdit(stringOne, stringTwo):
    if abs(len(stringOne) - len(stringTwo)) > 1:
        return False
    one = two = 0
    edit_count = 0
    while one < len(stringOne) and two < len(stringTwo):
        if stringOne[one] != stringTwo[two]:
            edit_count += 1
            if len(stringOne) < len(stringTwo):
                two += 1
            elif len(stringOne) > len(stringTwo):
                one += 1
            else:
                one += 1
                two += 1
        else:
            one += 1
            two += 1
    return edit_count <= 1


if __name__ == '__main__':
    assert oneEdit('hello', 'hollo') is True
    assert oneEdit('hello', 'hell') is True
    assert oneEdit('hello', 'ehel') is False

