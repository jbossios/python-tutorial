from multiprocessing import Pool

def my_function(x: int) -> int:
    return x*x + x - 1

if __name__ == '__main__':
    with Pool(4) as p:
        result = p.map(my_function, [i for i in range(200000)])