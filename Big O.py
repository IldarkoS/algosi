import random
import time


array = [random.randint(1,100) for _ in range(100)]


def time_score(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"Время работы: {end - start}")
        return res
    return wrapper


@time_score
def first(array: list) -> int:
    min_int = None
    for i in array:
        for j in array:
            if i>j and (min_int is None or min_int > j):
                min_int=j

    return min_int

@time_score
def second(array: list) -> int:
    # time.sleep(1)
    min_int = array[0]
    for i in array:
        if i < min_int:
            min_int = i

    return min_int


if __name__ == "__main__":
    print(first(array))
    print(second(array))