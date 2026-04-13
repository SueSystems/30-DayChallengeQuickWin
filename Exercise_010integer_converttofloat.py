"""Converting an integer to a float.
Get integer from user and convert to float
"""

import sys


def main():
    """Converts input integer to a float."""
    _number = int(input("Enter an number: "))
    _float = float(_number)
    print(_number, _float)
    return 0


if __name__ == "__main__":
    sys.exit(main())