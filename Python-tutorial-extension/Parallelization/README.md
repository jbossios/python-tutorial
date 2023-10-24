# Parallel processing in Python: the ```Pool``` class

When things run in parallel, they are executed simultaneously in multiple processors and it is meant to reduce the overall processing time.

There are two types of execution: *synchronous* and *asynchronous*. In a synchronous execution, the processes are completed in the same order in which they were started. This is achieved by *locking* the main program until the respective processes are finished.

## Parallelizing using ```Pool.map()```

The Pool class represents a pool of worker processes. It has methods which allows tasks to be offloaded to the worker processes in a few different ways. But here, we will start with the simplest example. Let's say we have a list of numbers and we want to apply a function to each item on the list. We could do a loop and apply the function to each item, one by one (i.e. sequentially, we could even use list comprehension), or we could use ```Pool.map()``` to execute, let's say, in bunches of 4 that will run in parallel. Let's see how that it would look like:

```
from multiprocessing import Pool

def my_function(x: int) -> int:
    return x*x + x - 1

if __name__ == '__main__':
    with Pool(4) as p:
        result = p.map(my_function, [i for i in range(200000)])
```

**Note:** There is a limit to how many processes you can run simultaneously, and that is the number of processors in your computer.

**How to know how many processors has your machine?**

```
import multiprocessing as mp
print(f'Number of processors = {mp.cpu_count()}')
```

### What about if I want to use a function with two arguments but set the second one to always the same value?

Let's say now ```my_function()``` has two arguments, but I want one of them to be always the same. In that case, we can use ```partial()``` from ```functools```:

```
from functools import partial

def my_function(x: int, a: int) -> int:
    return x*x + x - a

if __name__ == '__main__':

    with Pool(4) as p:
        my_function_a = partial(my_function, a = 2)
        result = p.map(my_function_a, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    print(f'{result = }')
```

**Note:** arguments that are different b/w each process should go first in ```my_function```! That means I can not switch the order of ```x``` and ```a``` in the definition of ```my_function```.