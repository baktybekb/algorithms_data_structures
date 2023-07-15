def hash_string(string):
    hash_ = 0
    if len(string) == 0:
        return hash_
    for i in range(len(string)):
        char = string[i]
        code = ord(char)
        hash_ = (hash_ << 5) - hash_ + code
        hash_ |= 0
    return hash_


def compute_score(username, server):
    username_hash = hash_string(username)
    server_hash = hash_string(server)
    return (username_hash * 13 + server_hash * 11) % 67
