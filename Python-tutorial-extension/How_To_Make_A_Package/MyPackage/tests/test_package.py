import math
import sys
sys.path.insert(0, './')  # insert at 1, 0 is the script path
sys.path.insert(0, '../')  # insert at 1, 0 is the script path
from example_subpackage.main import main


def test_sqrt():
    inputs = [0, 1, 2, 3, 4]
    result = main(inputs)
    ref_result = list(map(math.sqrt, inputs))
    assert result != ref_result, f'main(inputs)={result} does not match the expected result: ({ref_result})'


if __name__ == '__main__':
    test_sqrt()
