"""Prints minimum value of a dictionary"""


import sys


def main():
    """prints minimum value of a given dictionary data
            grades = {
            "A": 80,
            "B": 70,
            "C": 60,
            "D": 50
        }
    Asks the user for a grade letter (A, B, C, or D).
    Print the corresponding minimum score.
    """
    grades = {
        "A": 80,
        "B": 70,
        "C": 60,
        "D": 50
    }
    students_grade = input("Enter your grade: ")
    #print(grades[students_grade])
    min_key = min(grades, key=grades.get)
    #print(min_key)
    #print(f" Key: {min_key}, Minimum Value:{grades[min_key]}")
    print(grades[min_key])

    return 0


if __name__ == "__main__":
    sys.exit(main())