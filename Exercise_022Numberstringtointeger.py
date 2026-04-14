"""Converting Number Strings to Integers at index"""

import sys

def main():
    """Receive numbers as strings input and convert them
    explicitly at index to integers"""

    numbers = [input("Enter first number: "),
               input("Enter second number: "),
               input("Enter third number: ")]
    numbers[0] = int(numbers[0])
    numbers[1] = int(numbers[1])
    numbers[2] = int(numbers[2])

    numbers_sum = numbers[0] + numbers[1] + numbers[2]

    print(numbers)
    print(numbers_sum)
    return 0

if __name__ == "__main__":
    sys.exit(main())
