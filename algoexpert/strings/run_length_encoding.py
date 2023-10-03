def runLengthEncoding(string):
    count = 1
    res = []
    char = string[0]
    for i in range(1, len(string)):
        if count == 9:
            res.extend((str(count), char))
            count, char = 1, string[i]
            continue
        if string[i] == char:
            count += 1
        else:
            res.extend((str(count), char))
            count, char = 1, string[i]
    res.extend((str(count), char))
    return ''.join(res)


if __name__ == '__main__':
    assert runLengthEncoding("AAAAAAAAAAAAABBCCCCDD") == '9A4A2B4C2D'
    assert runLengthEncoding("........______=========AAAA   AAABBBB   BBB") == '8.6_9=4A3 3A4B3 3B'
