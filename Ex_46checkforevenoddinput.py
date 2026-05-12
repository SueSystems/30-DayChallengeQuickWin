"""Ask the user for a number.

Create a boolean variable is_even.

If is_even is True, print "Even number", else print "Odd number".
"""


import sys

def main():
    """Ask the user for a number.

Create a boolean variable is_even.

If is_even is True, print "Even number", else print "Odd number".
"""
    try:
        is_even = int(input("Enter an integer: "))

    except ValueError:
        print("Invalid input! Please enter an integer.")
        return 1


    if is_even % 2 == 0 :
        print("Even number")
    else:
        print("Odd number")
    return 0


if __name__ =="__main__":
    sys.exit(main())