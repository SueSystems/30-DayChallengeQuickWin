"""Summary of Users Profile
name, age and country
"""

import sys
#import copy


def main():
    """Ask the user for:
        their name (string)
        their age (integer)
        their country (string)
        Store the results in a list 'profile = [name, age, country]'.

        Then produce a new list:
        'summary = [profile[0].upper(), profile[1] + 5, profile[2].lower()]'.

        Finally print both lists with clear labels.
"""
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    country = input("Please enter your country: ")
    profile = [name, age, country]

    print(profile)
    #PROFILE = [profile.upper[0] == [name, age, country]]
    #summary = copy.deepcopy(profile)
    #print(PROFILE)
    summary = [profile[0].upper(), profile[1] + 5, profile[2].lower()]

    print(f"Profile: {profile}")
    print(f"Summary: {summary}")
    return 0


if __name__ == "__main__":
    sys.exit(main())