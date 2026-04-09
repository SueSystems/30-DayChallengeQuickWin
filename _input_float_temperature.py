"""Getting Float
Getting Temperature in Degree Celsius and giving in Fahrenheit
"""
import sys

def main():
    """Getting Temperature in Celsius and giving in Fahrenheit"""
    _temperature = float(input("Enter Temperature in Degree Celsius: "))
    result = _temperature * 1.8 + 32
    # F = C * 9/5 + 32
    print(result)

if __name__ == "__main__":
    sys.exit(main())
