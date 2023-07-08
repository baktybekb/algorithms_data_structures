# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
# O(n) time | O(d) space, depth of nested arrays in array
def productSum(array, depth=1):
    total = 0
    for item in array:
        if type(item) == list:
            total += productSum(item, depth + 1)
        else:
            total += item
    return total * depth
