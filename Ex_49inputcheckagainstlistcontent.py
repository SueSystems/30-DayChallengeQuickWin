"""Given:

colors = ["red", "green", "blue"]

Asks the user for a color.

If the color is in the list, print "Color available", else print "Color not found".
"""

import sys


def main():
    """Asks the user to gaze a color option in store
    and confirms if the color is in the list.
    """
    try:
        user_input = input("Please enter a name of color: ").strip()
    except ValueError:
        print("Error! Please enter a valid name of color")
        return 1

    if user_input == "red":
        # for case-insensitive if user_input.lower() == "red":
        print("Color available")
        return 0
    elif user_input == "green":
        print("Color available")
        return 0
    elif user_input == "blue":
        print("Color available")
    else:
        print("Color not found")


    return 0



if __name__ == "__main__":
    sys.exit(main())

