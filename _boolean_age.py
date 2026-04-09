"""Boolean: Age enquiry
Get user input:age. Print whether they are at least 18 (True/False).
"""

import sys

def main():
    """Prints True/False if user age is at least 18."""
    age = int(input("Enter your age: "))
    if age < 18:
        print("False")
    else :
        print("True")

if __name__ == "__main__":
    sys.exit(main())