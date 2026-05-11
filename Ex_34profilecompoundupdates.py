"""Creates a profile from user inputs
name, age, city and compounds age_next_year by one"""


import sys


def main():
    """
    Part A
    Asks the user for:their name, age, city
    Stores the data in a dictionary called profile.
    Prints profile.

    Part B
    Adds a new key age_next_year whose value is the user’s age plus one.
    Prints the updated dictionary.
    """
    name = input("Please enter your name: ")
                #Assumption:
    #User entered a string-no special characters and numbers
    age = int(input("Please enter your age: "))
            #Assumption: User entered integer
    city = input("Please enter your city: ")
            #Assumption: User entered string
    profile = {"name": name, "age": age, "city": city}

    print(profile)

    age_next_year = profile["age"] + 1

    profile["age_next_year"] = age_next_year

    print(profile)
    return 0


if __name__ == "__main__":
    sys.exit(main())

