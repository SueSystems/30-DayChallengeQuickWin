"""Ask user for input for dictionary value
   change key name to UPPERCASE and key country to lowercase
"""


import sys, pprint, json


def main():
    """Asks the user for:name,birth year (integer),country
        Stores them in a dictionary profile.

        Then create a new dictionary summary with:
        "NAME" → uppercase name
        "age_in_2025" → 2025 - birth_year
        "country" → lowercase country
        Print both dictionaries with labels.
    """
    name = input("Enter your name: ")
        #user can enter numbers instead of text
    birth_year = int(input("Enter your birth year: "))
        #user can enter text instead of number
    country = input("Enter your country: ")
        #user can enter number instead of text

    profile = {"name": name, "birth_year": birth_year, "country": country}
    print(profile)

    # I have not understood the instruction for new dictionary
    new_dictionary = profile.copy()
    new_dictionary["NAME"] = new_dictionary.pop("name")
    print(new_dictionary)

    #Labeling of Dictionary Options
    #Option 1 : Simple Print
    print("Profile",profile)
    print("New Dictionary",new_dictionary)

    #Option 2 : Pretty Printing
    print("Profile:")
    pprint.pprint(profile)

    print("New Dictionary:")
    pprint.pprint(new_dictionary)

    #Option 3 : Json printing
    print("Profile:")
    print(json.dumps(profile, indent=4))
    print("New Dictionary:")

    return 0


if __name__ == "__main__":
    sys.exit(main())