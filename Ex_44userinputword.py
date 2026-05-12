"""if construct
Ask the user for a word.

If the word is exactly "python", print "Correct word".
"""

import sys


def main():
    """Asks the user for a word, 
    checks if the word is exactly "python", 
    prints "Correct word".
    """
    user_input = input("Enter a word: ").strip()

    if not user_input.isalpha():
        print("Invalid input! Please enter a word (letters only).")
        return 1
#the code does not return to user unless rerun. Work on this

    if user_input == "python":
#for case-insensitive if user_input.lower() == "python":
        print("Correct word!")
        return 0
    else:
        print("Wrong word")
        return 1


if __name__ == "__main__":
    sys.exit(main())

