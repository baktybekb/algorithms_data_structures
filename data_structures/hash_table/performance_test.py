import multiprocessing

from data_structures.hash_table.ds import HashTable
from data_structures.memory_usage import memory_usage

default_range = 1000000


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
    HashTable `put` memory usage(max): 212.390625 MiB
    Python dict `put` memory usage(max): 118.546875 MiB
    """


if __name__ == '__main__':
    performance_test()
