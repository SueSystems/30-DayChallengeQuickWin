"""Reading List Content
from my_list exercise 19
"""

import sys


def main():
    """Creates  a list and input 3 words from the user
    Reads/print the first word the last word
    the length of the list"""

    my_list = list()
    my_list.append("Not")
    my_list.append("yet")
    my_list.append("understood")
    print(my_list[0], my_list[1],len(my_list))
    return 0


if __name__ == "__main__":
    sys.exit(main())
