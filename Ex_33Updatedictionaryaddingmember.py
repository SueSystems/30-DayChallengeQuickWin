"""Adding dictionary member
"""


import sys


def main():
    """Update Person dictionary
    Add a new key is_student with value False.
"""

    person = {"name": "Alice", "age": 25,"country": "Kenya"}
    person["age"] = 26
    person["is_student"] = False
    print(person)
    return 0


if __name__ == '__main__':
    sys.exit(main())