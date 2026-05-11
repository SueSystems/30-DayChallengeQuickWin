"""json printing dictionary with labels"""


import json
import sys


def main():
    """json printing dictionary with labels"""

    my_dict = {"A": 1, "B": 2}
    print("Labeled Dictionary Output:")
    print(json.dumps(my_dict, indent=4))
    return 0

if __name__ == "__main__":
    sys.exit(main())