"""Word Repeated
Input word of using repeated number of input times
"""

import sys


def main():
    """Inputer word repeated number of input times"""
    word = input("Enter a word: ")
    count = int(input("Enter a number: "))

    #result = word * count
    print("{} repeated {} times".format(word, count))
    #print("The Word {} repeated {} times is {}.".format(word, count, count * word))
    return 0


if __name__== "__main__":
    sys.exit(main())
