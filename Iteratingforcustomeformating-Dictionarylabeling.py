"""Iterating for customer formatting
    dictionary labeling method
"""


import sys


def main():
    """Iterating Dictionary labeling method"""
    inventory = {"shovels": 3, "sticks": 2}
    print("Items held:")
    for item, amount in inventory.items():
        print(f"- {item}: {amount}") # has not printed all the items
        return 0



if __name__ == "__main__":
    sys.exit(main())