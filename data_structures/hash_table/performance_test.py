import multiprocessing
from data_structures.hash_table.ds import HashTable
from data_structures.memory_usage import memory_usage

default_range = 1000000


def hash_table_put():
    table = HashTable(5)
    for i in range(default_range):
        table.put(i, i)


def dict_put():
    table = dict()
    for i in range(default_range):
        table[i] = i


def performance_test():
    process = multiprocessing.Process(target=hash_table_put)
    measurements, max_usage = memory_usage(process)
    print(f'HashTable `put` memory usage(max): {max_usage} MiB')
    process = multiprocessing.Process(target=dict_put)
    measurements, max_usage = memory_usage(process)
    print(f'Python dict `put` memory usage(max): {max_usage} MiB')
    print('-' * 50)

    """
    HashTable `put` memory usage(max): 507.25 MiB
    Python dict `put` memory usage(max): 116.5 MiB
    --------------------------------------------------
    """


if __name__ == '__main__':
    performance_test()
