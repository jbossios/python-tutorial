# How to create a package?

In some cases, one would like to use some modules across different projects or simply have things more organized. In such cases, one can create a package. Let's take a look at the following example where there is a package titled "MyPackage" which has the following content:

```
MyPackage/
├── __init__.py
└── example_subpackage/
    ├── __init__.py
    └── main.py
└── tests/
    └── test_package.py
```

MyPackage currently has two folders:
- A single subpackage called "example_subpackage"
- A folder called "tests/" which is used to test the "example_subpackage" subpackage with pytest (I will talk more about this later)

Inside the example_subpackage/ folder, there are two files, one module called ```main.py``` and a file named ```__init__.py```, the latter is empty and is needed such that one can import the main module from within the MyPackage/ folder. Let's take a look at ```main.py```. This module has a ```main()``` function which applies ```sqrt()``` to a list of input values (int or float):

```
def main(list_numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    '''
    Apply sqrt() to a list of numbers using map()
    '''
    return list(map(sqrt, list_numbers))
```

The additional ```__init__.py``` file within MyPackage/ contains:

```
from .package.main import main
```

This allows to import main from outside the MyPackage folder, i.e. to do the following:

```
from MyPackage.package.main import main as sqrt
```

as used in ```use_package.py``` located outside MyPackage/.


# How to implement a test using pytest

In the folder named ```tests/```, there is a file titled ```test_package.py``` which makes sure that main() from example_subpackage is implemented correctly. One could simply run ```python test_package.py``` inside the test/ folder. Alternatively, we can use pytest (within the MyPackage/ folder), i.e. run ```pytest``` (or ```python -m pytest```) and we would see the following:

```
=============================================================================================== test session starts ===============================================================================================
platform linux -- Python 3.8.10, pytest-7.1.1, pluggy-1.0.0
rootdir: /home/jbossios/cern/MyTutorials/python-tutorial/Python-tutorial-extension/Package/MyPackage
plugins: anyio-3.3.4
collected 1 item

test_package.py .                                                                                                                                                                                           [100%]

================================================================================================ 1 passed in 0.01s ================================================================================================
```

**NOTE #1:** to install pytest, please do ```pip install pytest```

**NOTE #1:** pytest will run all files of the form ```test_*.py``` or ```*_test.py``` in the current directory and its subdirectories, test functions must start with ```test_```, otherwise they will be skipped.

You can find more information about pytest in [How_To_Create_Tests/README.md](https://github.com/jbossios/python-tutorial/tree/master/Python-tutorial-extension/How_To_Create_Tests/README.md)
