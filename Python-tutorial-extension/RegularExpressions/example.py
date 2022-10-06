import re


def extract_email_addresses(string: str) -> [str]:
    pattern = "[\w.+-]+@[-\w]+\.[-\w.]+"  # alternatively one could use "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    return re.findall(pattern, string)


def extract_user_information(string: str) -> dict:
    # Define regex pattern
    pattern = re.compile(
        "^name:(?P<name>([\w+\s]+));\s"
        "lastname:(?P<lastname>([\w+\s]+));\s"
        "address:(?P<address>([\w\s+,-]+));\s"
        "age:(?P<age>([0-9]+));\s"
        "profession:(?P<profession>([\w+\s]+))"
    )
    print(f'Extracting user information from: "{string}"')
    match = pattern.match(string)
    print(f'Result of pattern matching: {match}')
    if match:
        data = match.groupdict()
        return match, data
    return match, {}


if __name__ == '__main__':
    # Example #1
    print('\nExample #1:\n')
    string = 'You can write me to example1@gmail.com or example.2@gmail.com'
    print(f'Extracted email addresses from: "{string}":')
    print(extract_email_addresses(string))

    # Example #2
    print('\nExample #2:\n')
    # Define information to put into a string
    users = [
        [
            'name:Peter',
            'lastname:Smith',
            'address:street 42, 01123, Somewhere',
            'age:45',
            'profession:carpenter',
        ],
        [
            'name:David Ramiro',
            'lastname:Gonzalez Lopez',
            'address:streen-name 54, 01123, Some Country',
            'age:36',
            'profession:Data Scientist',
        ],
    ]
    # Create a single string with all the above information
    strings = ['; '.join(user) for user in users]  # prepare strings from which to extract user information
    for string in strings:
        match, data = extract_user_information(string)
        if match:
            print('A match was found!')
            print('Extracted information:')
            print(f'{data}\n')