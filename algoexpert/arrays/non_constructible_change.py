# https://www.algoexpert.io/questions/non-constructible-change

# O(nlog(n)) time | O(1) space
def nonConstructibleChange(coins):
    coins.sort()
    current = 0
    for coin in coins:
        if current + 1 < coin:
            return current + 1
        current += coin
    return current + 1


if __name__ == '__main__':
    assert nonConstructibleChange(coins=[1, 2, 4]) == 8
    assert nonConstructibleChange(coins=[5, 7, 1, 1, 2, 3, 22]) == 20
