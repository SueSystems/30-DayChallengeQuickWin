"""Getting and integer
Giving out its square and cube
"""


import sys


def main():
    """Square and Cube of an integer"""
    _number = int(input("Enter an number: "))

    _square = _number ** 2
    _cube = _number ** 3


    #print(f"Square is {_square} and cube is {_cube}") or
    #print(f"Square: {_square}, Cube: {_cube}").format() # f-string format python 3.6
    #print("Square: {}, Cube: {}".format(_square, _cube)) # .format()
    print("The Square is {} and its cube is {}".format(_square, _cube))
    return 0


if __name__ == "__main__":
    sys.exit(main())