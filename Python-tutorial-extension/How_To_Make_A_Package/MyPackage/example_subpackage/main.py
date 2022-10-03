from math import sqrt
from typing import List
from typing import Union


def main(list_numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    '''
    Apply sqrt() to a list of numbers using map()
    '''
    return list(map(sqrt, list_numbers))


if __name__ == '__main__':
    numbers = [i for i in range(10)]
    results = main(numbers)
    print(f'sqrt{numbers} = {results}')
