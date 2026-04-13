"""String Concatenation
Getting words from users and concatenating them
"""

import sys


def main():
    """Concatenation words with space between them"""
    word = input("Please type a word: ")
    anotherword = input("Please type another word: ")
    result  =  word + " " + anotherword
    print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())