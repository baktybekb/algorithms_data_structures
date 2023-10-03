# https://www.algoexpert.io/questions/palindrome-check

# O(n) time | O(1) space
def isPalindrome(string):
    l, r = 0, len(string) - 1
    while l < r:
        if string[l] != string[r]:
            return False
        l += 1
        r -= 1
    return True

