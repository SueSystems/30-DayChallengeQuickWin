"""MultiplyString
Multiply input string 3 times
"""

import sys


def main():
    """MultiplyString using *"""
    x = input("Input a phrase:  ")
    multiply_sentence =  x * 3
    print(multiply_sentence)
    return 0


if __name__ == "__main__":
    sys.exit(main())