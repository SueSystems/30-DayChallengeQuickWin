"""Print/Read a dictionary
member
"""


import sys


def main():
    """Print/Read members of Person dictionary
    name, age
"""

    person = {
        "name": "Alice",
        "age": 25,
        "country": "Kenya"
    }


    print(f"Person name: {person['name']}, age: {person['age']}")
    return 0


if __name__ == '__main__':
    sys.exit(main())