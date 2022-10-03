import math
import sys
sys.path.insert(0, './')  # insert at 1, 0 is the script path
sys.path.insert(0, '../')  # insert at 1, 0 is the script path
from example_subpackage.main import main


def test_sqrt():
    inputs = [0, 1, 2, 3, 4]
    result = main(inputs)
    if result == list(map(math.sqrt, inputs)):
        print('ALL OK')
    else:
        print(f'{result = }')
        print(f'{list(map(math.sqrt, inputs)) = }')
        print('BAD, exiting')
        sys.exit(1)


if __name__ == '__main__':
    test_sqrt()
