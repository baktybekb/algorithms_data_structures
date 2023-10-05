# O(1) time | O(1) space
def validIPAddresses(string):
    res = []
    for i in range(1, 4):
        current_ip = ['', '', '', '']
        current_ip[0] = string[:i]
        if not is_valid(current_ip[0]):
            continue
        for j in range(i + 1, i + min(len(string) - i, 4)):
            current_ip[1] = string[i:j]
            if not is_valid(current_ip[1]):
                continue
            for k in range(j + 1, j + min(len(string) - j, 4)):
                current_ip[2] = string[j:k]
                current_ip[3] = string[k:]
                if is_valid(current_ip[2]) and is_valid(current_ip[3]):
                    res.append('.'.join(current_ip))
    print(res)
    return res


def is_valid(string):
    string_int = int(string)
    if string_int > 255:
        return False
    return len(string) == len(str(string_int))


if __name__ == '__main__':
    assert validIPAddresses("1921680") == [
        '1.9.216.80', '1.92.16.80', '1.92.168.0', '19.2.16.80', '19.2.168.0', '19.21.6.80', '19.21.68.0', '19.216.8.0',
        '192.1.6.80', '192.1.68.0', '192.16.8.0'
    ]
