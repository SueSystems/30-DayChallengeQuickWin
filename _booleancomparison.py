"""Compares user inputs
 two numbers and print:
a > b
a == b
a != b
"""

import sys

def main():
    """comparison of user inputs"""
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    print(f"a > b: {a > b}")
    print(f"a == b: {a == b}")
    print(f"a != b: {a != b}")

if __name__ == "__main__":
    sys.exit(main())

