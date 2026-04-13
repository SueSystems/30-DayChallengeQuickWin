"""Variable Type Change"""

import sys


def main():
    """Variable Change type on None assignment"""
    _number = int(input("Enter a number: "))
    print(_number)
    # Variable in Python changes type since it is a symbolic
    # name or label that points to a specific location in memory
    # Reassigning Variable/dynamic type-Python is a
    # dynamically typed language. When reassignment is done
    #python move the pointer to the new memory location
    _number = None
    print(_number)
    return 0


if __name__ == "__main__":
    sys.exit(main())