"""Creating a dictionary
from a given data
"""


import sys


def main():
    """Creating a dictionary Person from given data
    name: "Alice"
    age: 25
    country: "Kenya"
"""
    """
    person = {
        "name": "Alice",
        "age": 25,
        "country": "Kenya"
    }
    """
    person = dict()
    person["name"] = "Alice"
    person["age"] = 25
    person["country"] = "Kenya"

    print(person)
    return 0


if __name__ == '__main__':
    sys.exit(main())