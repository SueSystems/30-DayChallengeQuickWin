"""Ask the user for their age.

If the age is at least 18, print "Adult".

Otherwise, print "Minor".
"""


import sys


def main():
    """Ask the user for their age.

       If the age is at least 18, print "Adult".

     Otherwise, print "Minor".
    """
    try:
        user_age = int(input("Enter your age: "))
    
    except ValueError:
        print("Input error: Not a valid whole number.")
        return 1

    if user_age >= 18:
        print("Adult")
        return 0

    else:
        print("Minor")
        return 1

if __name__ == "__main__":
    sys.exit(main())