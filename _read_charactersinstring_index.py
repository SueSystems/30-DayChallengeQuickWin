"""Reading Characters in String
Using indexing
"""

import sys

def main():
    """ Get word from user and read character at both ends"""
    a = input("Please type a word: ")
    print(a[0],a[-1])

if __name__ == "__main__":
    sys.exit(main())
