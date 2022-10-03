# Useful decorators

Decorators were introduced in [02_Introduction_Functions.ypynb](https://nbviewer.org/github/jbossios/python-tutorial/blob/master/Jupyter-Notebooks/02_Introduction_Functions.ipynb#decorators)

## cache from functools

Whenever a given computation could be used several times, it would be helpful to keep track of already computed calculations to speed up your code. For such occasions, the cache decorator becomes super helpful.

It is very easy to use, you just need to import cache from functools, i.e. ```from functools import cache``` and then apply the cache decorator to any function, for example:

```
@cache
def my_function(x: int) -> int:
    return x*x
```

Any time ```my_function(x)``` is called, the result for that given ```x``` is stored, and returned whenever ```my_function(x)``` is called again. You can find an working example in ```functools_cache.py```.
