# Regular expressions

A regular expression (RE or also known as regex and regexp) is used for pattern recognition and search operations using strings. Regex functionality is offered in Python through the ```re``` module.

Let's say we have several strings and we want to identify those which only have integer numbers. In that case, one could do the following:

```
import re

def find_numbers(string: str) -> int:
    pattern = re.compile('[0-9]+')
    match = pattern.match(string)
    if match:
        return match, int(string)
    return match, None

strings = ['example', '23', 'test', '145']
results = map(find_numbers, strings)
numbers = [number for match, number in results if match]
print(f'Extracted numbers = {numbers}')
```

Let's break it into pieces, let's look at the following line:

```
pattern = re.compile('[0-9]+')
```

The above line compiles a pattern for recognizing any set of numbers. ```[0-9]``` means any number from 0 to 9, while ```[0-9]+``` means any number of numbers in that range. Furthermore, ```[amk]``` will match 'a', 'm', or 'k'. Ranges of REs can be indicated by giving two REs and separating them by a ```-```, for example ```[a-z]``` will match any lowercase ASCII letter

Let's look at the following line now:

```
match = pattern.match(string)
```

There we are testing ```string``` against the pattern defined above.

The above pattern was simple, it can easily get really complicated. Here is a summary of other helpful special REs (for more, please look [here](https://docs.python.org/3/library/re.html))

```+```: matches when 1 or more repetitions of the preceding RE. For example, ```ab+``` will match 'a' followed by any non-zero number of 'b's; i.e. it will not match just ‘a’.

```*```: matches 0 or more repetitions of the preceding RE. For example, ```ab*``` will match 'a', 'ab', or 'a' followed by any number of 'b's.

```^```: matches the start of the string

```[.]```: matches a single dot, ```[.]+``` any number of dots

```$```: matches the end of the string or just before the newline at the end of the string

```?```: matches 0 or 1 repetitions of the preceding RE. For example, ```ab?``` will match either 'a' or 'ab'.

```{m}```: specifies that exactly m copies of the previous RE should be matched. For example, ```a{6}``` will match only exactly six 'a' REs.

```\```: either escapes special REs (permitting you to match REs like '*', '?', etc), or signals a special sequence (see [here](https://docs.python.org/3/library/re.html)).

```\s```: matches a whitespace

```\S```: matches any RE which is not a whitespace RE.

```\w```: matches Unicode word REs

```(?P<name>...)```: matches whatever regular expression is inside the parenthesis, except for ```?P<name>```, the matched substring is accessible via the symbolic group name ```name```.

For example most of the above REs, see [example.py](https://github.com/jbossios/python-tutorial/blob/master/Python-tutorial-extension/RegularExpressions/example.py)