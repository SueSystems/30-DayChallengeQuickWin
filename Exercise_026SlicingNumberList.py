"""Slicing a given list of numbers"""

import sys

def main():
    """Slicing "values = [5, 6, 7, 8]", to create "first_two"
    containing only the first two items using slicing"""
    nums = [5, 6, 7, 8]
    first_two = nums[:2]
    print(first_two)

    return 0


if __name__ == "__main__":
    sys.exit(main())