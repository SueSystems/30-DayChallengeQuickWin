"""New list from Selected words with prefix a and A"""

import sys


def main():
    """Get 5 words from user and create a new list
    of words with prefix a and A"""
    words = [
            input("Please enter a word: "),
            input("Please enter a word: "),
            input("Please enter a word: "),
            input("Please enter a word: "),
            input("Please enter a word: "),
    ]
    print(words)

    a_words = [words for words in words if words.lower().startswith('a')]
    print(a_words)
    return 0


if __name__ == "__main__":
    sys.exit(main())
