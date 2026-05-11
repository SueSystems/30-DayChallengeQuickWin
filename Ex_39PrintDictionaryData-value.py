"""Prints the dictionary data.value()"""


import sys


def main():
    """data = {"a": 1, "b": 2, "c": 3}

    Prints the result of data.value().
    """
    data = {"a": 1, "b": 2, "c": 3}

    """
    print(data["a"])
    print(data["b"])
    print(data["c"])
    """
    print(*data.values())
    return 0


if __name__ == '__main__':
    sys.exit(main())