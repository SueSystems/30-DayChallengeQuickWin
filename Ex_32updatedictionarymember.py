"""Update a dictionary member
"""


import sys


def main():
    """Update age member of Person dictionary
"""

    person = {"name": "Alice", "age": 25,"country": "Kenya"}
    #person.update(age=26)
    #person.update({"age":26})
    person["age"] = 26
    print(f"Person age: {person['age']}")
    return 0


if __name__ == '__main__':
    sys.exit(main())