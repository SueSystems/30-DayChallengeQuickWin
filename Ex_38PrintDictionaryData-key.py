"""Prints the dictionary data.key()"""


import sys


def main():
    """data = {"a": 1, "b": 2, "c": 3}

    Prints the result of data.keys().
    """
    data = {"a": 1, "b": 2, "c": 3}

    print(*data.keys())
    return 0


if __name__ == '__main__':
    sys.exit(main())