import multiprocessing
from data_structures.dynamic_array.ds import DynamicArray
from data_structures.memory_usage import memory_usage

default_range = 1000000


def ds_append(instance=None):
    array = DynamicArray() if instance else []
    for i in range(default_range):
        array.append(i)


def ds_insert(instance=None):
    array = DynamicArray() if instance else []
    for i in range(default_range):
        array.insert(i, [])


def performance_test():
    process = multiprocessing.Process(target=ds_append, args=(DynamicArray,))
    measurements, max_usage = memory_usage(process)
    print(f'DynamicArray append memory usage(max): {max_usage} MiB')
    process = multiprocessing.Process(target=ds_append)
    measurements, max_usage = memory_usage(process)
    print(f'Python list append memory usage(max): {max_usage} MiB')
    print('-' * 50)

    process = multiprocessing.Process(target=ds_insert, args=(DynamicArray,))
    measurements, max_usage = memory_usage(process)
    print(f'DynamicArray insert memory usage(max): {max_usage} MiB')
    process = multiprocessing.Process(target=ds_insert)
    measurements, max_usage = memory_usage(process)
    print(f'Python list insert memory usage(max): {max_usage} MiB')

    """
    DynamicArray append memory usage(max): 60.328125 MiB
    Python list append memory usage(max): 40.046875 MiB
    --------------------------------------------------
    DynamicArray insert memory usage(max): 89.046875 MiB
    Python list insert memory usage(max): 76.0625 MiB
    """


if __name__ == '__main__':
    performance_test()
