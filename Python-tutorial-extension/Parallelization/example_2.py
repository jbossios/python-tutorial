from multiprocessing import Pool
from functools import partial

def my_function(x: int, a: int) -> int:
    return x*x + x - a

if __name__ == '__main__':

    with Pool(4) as p:
        my_function_a = partial(my_function, a = 2)
        result = p.map(my_function_a, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    print(f'{result = }')