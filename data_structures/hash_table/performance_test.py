import multiprocessing

from data_structures.hash_table.hash_table import HashTable
from data_structures.memory_usage import memory_usage

default_range = 100000


def hash_table_put(instance=None):
    table = HashTable() if instance else dict()
    for i in range(default_range):
        table[i] = i


def performance_test():
    process = multiprocessing.Process(target=hash_table_put, args=(HashTable,))
    _, max_usage = memory_usage(process)
    print(f'HashTable `put` memory usage(max): {max_usage} MiB')
    process = multiprocessing.Process(target=hash_table_put)
    _, max_usage = memory_usage(process)
    print(f'Python dict `put` memory usage(max): {max_usage} MiB')

    """
    HashTable `insert` memory usage(max): 88.484375 MiB
    Python dict `insert` memory usage(max): 25.390625 MiB
    """


if __name__ == '__main__':
    performance_test()
