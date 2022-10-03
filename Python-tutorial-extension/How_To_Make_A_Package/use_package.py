from MyPackage.example_subpackage.main import main as sqrt

if __name__ == '__main__':
    inputs = [0, 1, 2, 3, 4]
    results = sqrt(inputs)
    for i, result in zip(inputs, results):
        print(f'sqrt({i}) = {result}')
