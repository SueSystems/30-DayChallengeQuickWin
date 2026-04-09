"""Converting Minutes to Hours
Floats: Getting user input of minutes to be converted into hour
"""

import sys

def main():
    """Converts user input of minutes to Hours"""
    minutes = float(input("Enter  minutes: "))
    #hours = int(input("Enter a hour: "))

    print("You entered {} minutes which is {} hours.".format(minutes, minutes/60))



if __name__ == "__main__":
    sys.exit(main())