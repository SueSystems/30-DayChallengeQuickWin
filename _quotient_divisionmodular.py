"""Get two integers and print:
quotient using integer division (/)and
modular(%) remainder
"""

import sys


def main():
    """Quotient using integer division (/)and modular remainder """
    a = int(input("Please enter a numbers: "))
    b = int(input("Please enter another number: "))
    quotient_division = a / b
    quotient_modular = a % b
    # quotient = int(sys.argv[1])
    # remainder = int(sys.argv[2])
    print("Results of Division is {} and modular is {}".format(quotient_division, quotient_modular))


if __name__ == "__main__":
    sys.exit(main())