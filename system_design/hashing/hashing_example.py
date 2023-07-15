from system_design.hashing.hashing_utils import hash_string, compute_score

server_set1 = [
    'server0',
    'server1',
    'server2',
    'server3',
    'server4',
    'server5',
]

server_set2 = [
    'server0',
    'server1',
    'server2',
    'server3',
    'server4',
]

usernames = [
    'username0',
    'username1',
    'username2',
    'username3',
    'username4',
    'username5',
    'username6',
    'username7',
    'username8',
    'username9',
]


def pick_server_simple(username, servers):
    hash_ = hash_string(username)
    return servers[hash_ % len(servers)]


def pick_server_rendezvous(username, servers):
    max_server = None
    max_score = None
    for server in servers:
        score = compute_score(username, server)
        if max_score is None or score > max_score:
            max_score = score
            max_server = server
    return max_server


def main():
    print('Simple Hashing Strategy:')
    for username in usernames:
        server1 = pick_server_simple(username, server_set1)
        server2 = pick_server_simple(username, server_set2)
        servers_are_equal = server1 == server2
        print(f'{username}: {server1} --> {server2} | equal: {servers_are_equal}')

    print('-' * 50)
    print('Rendezvous Hashing Strategy:')
    for username in usernames:
        server1 = pick_server_rendezvous(username, server_set1)
        server2 = pick_server_rendezvous(username, server_set2)
        servers_are_equal = server1 == server2
        print(f'{username}: {server1} --> {server2} | equal: {servers_are_equal}')


if __name__ == '__main__':
    main()

"""
Simple Hashing Strategy:
username0: server0 --> server2 | equal: False
username1: server1 --> server3 | equal: False
username2: server2 --> server4 | equal: False
username3: server3 --> server0 | equal: False
username4: server4 --> server1 | equal: False
username5: server5 --> server2 | equal: False
username6: server0 --> server3 | equal: False
username7: server1 --> server4 | equal: False
username8: server2 --> server0 | equal: False
username9: server3 --> server1 | equal: False
---------------------------------------------
Rendezvous Hashing Strategy:
username0: server2 --> server2 | equal: True
username1: server1 --> server1 | equal: True
username2: server0 --> server0 | equal: True
username3: server5 --> server4 | equal: False
username4: server3 --> server3 | equal: True
username5: server2 --> server2 | equal: True
username6: server1 --> server1 | equal: True
username7: server0 --> server0 | equal: True
username8: server5 --> server4 | equal: False
username9: server4 --> server4 | equal: True
"""
