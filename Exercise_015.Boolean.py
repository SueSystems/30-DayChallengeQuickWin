"""Boolean Prefix Checker
 for user input for a specific character.
"""


import sys


def main():
    """splits prefix at delimiter then Checks for specific
     character regardless of chase "a" or "A"with
     boolean expression
    """

    delimiter =":"
    _input = input("Please enter a word: ")
    prefix_to_check = ("a", "A")
    #is_match = _input.split(delimiter)[0] == prefix_to_check
    is_match = _input.split(delimiter)[0].startswith(prefix_to_check)
    print(is_match)


    return 0


if __name__ == "__main__":
    sys.exit(main())
