from functools import cache  # available in Python 3.9+

@cache  # equivalent to @lru_cache(maxsize=None) [smaller and faster than lru_cache with fixed maxsize]
def f(n):
    '''
    Fast implementation of fibonacci's serie using cache decorator
    '''
    if n <= 1:
        return n
    return f(n-1) - f(n-2)


def f_slow(n):
    '''
    Slow fibonacci's serie
    '''
    if n <= 1:
        return n
    return f_slow(n-1) - f_slow(n-2)


def main():
    n = 31
    
    # Use fast function
    print(f'Fast function:')
    import time
    start = time.perf_counter()
    for i in range(n):
        f(i)
    end = time.perf_counter()
    print(f'Time spent = {end-start}')

    # Use slow function
    print(f'Slow function:')
    import time
    start = time.perf_counter()
    for i in range(n):
        f_slow(i)
    end = time.perf_counter()
    print(f'Time spent = {end-start}')
   

if __name__ == '__main__':
    main()
