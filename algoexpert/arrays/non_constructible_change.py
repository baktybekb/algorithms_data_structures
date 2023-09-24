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
