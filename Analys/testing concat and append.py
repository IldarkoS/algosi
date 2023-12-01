import time
import random

array = [random.randint(1,100) for _ in range(1000)]


def time_score(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        time.sleep(1)
        end = time.time()
        print(f"Время работы: {end - start}")
        return res
    return wrapper

@time_score
def append(array: list):
    return array.append(1)

@time_score
def cuncat(array: list):
    return array + [1]

@time_score
def test1():
    l = []
    for i in range(100000):
        l = l + [i]

@time_score
def test2():
    l = []
    for i in range(100000):
        l.append(i)

@time_score
def test3():
    l = [i for i in range(100000)]

@time_score
def test4():
    l = list(range(100000))


if __name__ == "__main__":
    # append(array)
    # cuncat(array)
    test1()
    test2()
    test3()
    test4()