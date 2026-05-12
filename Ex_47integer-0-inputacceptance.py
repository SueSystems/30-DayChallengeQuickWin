"""Ask the user for a number.
Print:
"Negative" if the number is less than 0
"Zero" if the number is 0
"Positive" otherwise"""


import sys


def main():
    """Ask the user for a number.
Print:
"Negative" if the number is less than 0
"Zero" if the number is 0
"Positive" otherwise
"""
    try:
        user_number = int(input("Enter your a number: "))

    except ValueError:
        print("Error. Please enter a number!")
        return 1

    if user_number < 0 :
        print("Negative")
    elif user_number == 0 :
        print("Zero")
    else:
        print("Positive")


    return 0

if __name__ == "__main__":
    sys.exit(main())