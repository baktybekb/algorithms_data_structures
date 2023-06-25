import threading
import time
import psutil
import multiprocessing


def memory_usage(process: multiprocessing.Process, interval=0.01):
    mem_usage_data = []

    def profiler():
        p = psutil.Process(process.pid)
        while process.is_alive():
            mem_info = p.memory_info()  # returning bytes
            mem_usage_data.append(mem_info.rss / 1024 / 1024)
            time.sleep(interval)

    thread = threading.Thread(target=profiler)
    process.start()
    thread.start()
    process.join()
    thread.join()
    return mem_usage_data, max(mem_usage_data)


def test_func():
    a = []
    for i in range(1000000):
        a.insert(i, i)


if __name__ == '__main__':
    proc = multiprocessing.Process(target=test_func)
    measurements, max_usage = memory_usage(proc, 0.01)
    print(max_usage)
