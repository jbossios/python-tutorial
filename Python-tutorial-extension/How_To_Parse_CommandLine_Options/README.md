# argparse

Let's say you need to pass information to a python script, if that's so, then ```argparse``` is what you need.

In ```Example.py``` you can find a simple example of how to use ```argparse```. In this example, we would like to be able to provide an input file name (i.e. a string) and to be able to, optionally, turn ON something in our code. Hence, we would like to be able to do things like these:

```
python Example.py --inputFile file.txt
python Example.py --inputFile file.txt --enableSomething
```

Let's take a look at the code. We first create the argument parser:

```
parser = argparse.ArgumentParser()
```

Then, we add all possible arguments. In this case, we want to pass a string with the ```--inputFile``` flag and we need the option to enable something if we want to with the ```enableSomething``` flag. We do this in the following way:

```
parser.add_argument('--inputFile', action='store', dest='input_file', default='', help='Input file')
parser.add_argument('--enableSomething',action='store_true', dest='enable_something', default=False, help='Enable option to do something')
```

Note that we are using the ```action``` keyword to say to store the provided value (```action='store'```) or to store ```True``` (```action='store_true'```) to the destination variable. The destination variable will be (by default) equal to the flag but it can be customize with the ```dest``` keyword. The ```default`` keyboard can be used to set a default value when an argument/flag is not provided. The ```help``` keyrword can be used to construct a helper which can be printed with ```python --help``` and/or be printed when an argument is not provided.

Once all aguments were defined we parse the arguments provided by the user:

```
args = parser.parse_args()
```

We can then access the values set to each argument in the following way:

```
args.dest_name
```

where ```dest_name``` is the name of the flag, if ```dest``` is not provided, or what was provided to ```dest```.

In ```Example.py```, a protection was added to ensure an input file is always provided. If --inputFile was not provided, the helper is printed (see below) and the program exits:

```
usage: Example.py [-h] [--inputFile INPUT_FILE] [--enableSomething]

optional arguments:
  -h, --help            show this help message and exit
  --inputFile INPUT_FILE
                        Input file
  --enableSomething     Enable option to do something
```

For more information and examples, please see [here](https://docs.python.org/3/library/argparse.html)
