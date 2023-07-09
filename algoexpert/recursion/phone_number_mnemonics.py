# O(4^n * n) time | O(4^n * n) space
def phoneNumberMnemonics(phoneNumber):
    table = {
        '0': ('0',),
        '1': ('1',),
        '2': ('a', 'b', 'c'),
        '3': ('d', 'e', 'f'),
        '4': ('g', 'h', 'i'),
        '5': ('j', 'k', 'l'),
        '6': ('m', 'n', 'o'),
        '7': ('p', 'q', 'r', 's'),
        '8': ('t', 'u', 'v'),
        '9': ('w', 'x', 'y', 'z'),
    }
    result = []
    current = [None] * len(phoneNumber)
    pick_char(table, result, 0, phoneNumber, current)
    return result


def pick_char(table, result, idx, phone_number, current):
    if idx >= len(phone_number):
        result.append(''.join(current))
        return
    chars = table[phone_number[idx]]
    for i in range(len(chars)):
        current[idx] = chars[i]
        pick_char(table, result, idx + 1, phone_number, current)


if __name__ == '__main__':
    res = phoneNumberMnemonics('79')
    assert res == ['pw', 'px', 'py', 'pz', 'qw', 'qx', 'qy', 'qz', 'rw', 'rx', 'ry', 'rz', 'sw', 'sx', 'sy', 'sz']
