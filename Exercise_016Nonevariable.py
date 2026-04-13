"""
Input in a Declared None Variable
"""

import sys


def main():
    """Adding value to None Declared variable"""
    x = None
    print(x)
   #x = input("Please Enter a word: ")
    x = int(input("Enter a number: "))
    print(x)
    return 0

if __name__ == "__main__":
    sys.exit(main())