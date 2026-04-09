"""Input and Output
Getting the input from the user and give output with it
"""
import sys

def main():
    """Getting input from the user and greeting them"""
    name = input("What is your name? ")
    print(f"Hello {name}!")

if __name__ == "__main__":
    sys.exit(main())