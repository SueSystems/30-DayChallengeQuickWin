"""Ask the user for a value using input().

If the input is empty, print "No input provided".

Else if the input is numeric, print "Numeric input".

Else print "Text input".

Constraints:
No loops
No exception handling
Use:
.isdigit()
truthiness of strings
if / elif / else
"""


import sys


def main():
    """ Ask the user for a value using input().

If the input is empty, print "No input provided".

Else if the input is numeric, print "Numeric input".

Else print "Text input".

Use:
.isdigit()
truthiness of strings
if / elif / else
"""
    user_input = input("Please enter a  value: ")

    if user_input == "":
        print("No input provided")
        return 0
    elif user_input == user_input.isdigit(): # user_input.isnumeric(): to test numeric
        print("Numeric input")
        return 0
    else:
        print("Text input")
        return 0


if __name__ == "__main__":
    sys.exit(main())