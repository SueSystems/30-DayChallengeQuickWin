"""Getting Float
Getting Temperature in Degree Celsius and giving in Fahrenheit
"""
import sys

def main():
    """Getting Temperature in Celsius and giving in Fahrenheit"""
    C = float(input("Enter Temperature in Degree Celsius: "))
    #F = C * 1.8 + 32
    F = C * 9/5 + 32
    print(F)

if __name__ == "__main__":
    sys.exit(main())
