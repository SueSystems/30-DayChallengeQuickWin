"""If Construct
Getting integer from user and checking
if it is larger number 10
"""


import sys


def main():
    try:
        user_integer = int(input("Please enter an integer: "))
        #edge case: input can be empty, float, string
        if user_integer > 10:
            print("Large number")
            return 0

        #  false IF statement
        print("Small number")
        return 1  # Explicitly return a different value

    except ValueError:
        print("That wasn't an integer!")
        return 1

"""Return at the Very End
def main():
    try:
        user_integer = int(input("Please enter an integer: "))
    except ValueError:
        print("Invalid input! Please enter a whole number.")
        return 1  # Exit early if input is bad
   
    exit_code = 0 
    
    if user_integer > 10:
        print("Large number")
        # exit_code remains 0
    else:
        print("Small number")
        exit_code = 1
        
    return exit_code    
"""

if __name__ == '__main__':
    sys.exit(main())