"""Creates a dictionary
with given values and updates with given values"""


import sys


def main():
    """Part A
        Creates a dictionary:
        stats = {"count": 10,"average": 4.5,"valid": True}
        Prints each value individually using key access.

        Part B
        Updates:
        "count" by increasing it by 5 using compound assignment
        "valid" to False
        Prints the final dictionary."""

    stats = {"count": 10, "average": 4.5, "valid": True}
    print(stats)

    stats["count"] = stats["count"] + 5
    stats["valid"] = False

    print(stats)
    return 0


if __name__ =='__main__':
    sys.exit(main())
