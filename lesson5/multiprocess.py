import multiprocessing
import time
import math


def time_decorator(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        print(time.time() - start_time)

    return inner


def work(num):
    return str(math.sqrt(math.sqrt(math.sqrt(num / 2) / 15 + 50000) * 25)) + 'H'


@time_decorator
def main_process():
    print('main')
    r = range(50_000_000)
    with open('file1.txt', 'w') as f:
        for i in r:
            result = work(i)
            print(result, file=f)


# main_process()
@time_decorator
def mp():
    print('mp')
    cpu_count = multiprocessing.cpu_count()
    print(f'{cpu_count=}')

    with multiprocessing.Pool(cpu_count) as p:
        r = range(50_000_000)
        with open('file2.txt', 'w') as f:
            tasks = p.map(work, r)
            for res in tasks:
                print(res, file=f)


mp()
