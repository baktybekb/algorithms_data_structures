# O(n) time | O(n) space
def runLengthEncoding(string):
    result = []
    length = 1
    for i in range(1, len(string)):
        cur_char = string[i]
        prev_char = string[i - 1]
        if cur_char != prev_char or length == 9:
            result.append(str(length))
            result.append(prev_char)
            length = 0
        length += 1
    result.append(str(length))
    result.append(string[-1])
    return ''.join(result)
