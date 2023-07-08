# O(n) time | O(1) space
def getNthFib(n):
    last_two = [0, 1]
    for i in range(3, n + 1):
        temp = sum(last_two)
        last_two[0] = last_two[1]
        last_two[1] = temp
    return last_two[0] if n <= 1 else last_two[1]
