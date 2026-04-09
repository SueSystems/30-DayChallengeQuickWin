"""Converting an integer to a float.
Get integer from user and convert to float
"""

import sys

def main():
    """Converts input integer to a float."""
    x = int(input("Enter an number: "))
    y = float(x)
    print(x, y)

if __name__ == "__main__":
    sys.exit(main())