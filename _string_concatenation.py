"""String Concatenation
Getting words from users and concatenating them
"""

import sys

def main():
    """Concatenation words with space between them"""
    x = input("Please type a word: ")
    y = input("Please type another word: ")
    z  =  x + " " + y
    print(z)


if __name__ == "__main__":
    sys.exit(main())