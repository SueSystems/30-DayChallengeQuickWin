"""Creating Independent Copy of Numbers list
by slicing
"""

import sys


def main():
    """Create Independent Copy of Numbers list by slicing
    of a given list of numbers: "items = [10, 20, 30]",
    Print both original and independent copy of numbers
    """
    items = [10, 20, 30]
    independent_copy = items[:]
    print(items)
    print(independent_copy)
    return 0


if __name__ == '__main__':
    sys.exit(main())