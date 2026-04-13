"""Get two integers and print:
quotient using /
integer division using //
remainder using %
"""

import sys


def main():
    """Quotient using division(/),
    integer division (//)- floor or ceiling
    and modular remainder % """
    _dividend = int(input("Please enter a numbers: "))
    _divisor = int(input("Please enter another number: "))
    quotient_division = _dividend / _divisor
    quotient_floor = _dividend // _divisor
    quotient_modular = _dividend % _divisor

    print("Results of Division is {} Integer Division {}\n and Modular is {}".format(quotient_division,quotient_floor ,quotient_modular))
    return 0


if __name__ == "__main__":
    sys.exit(main())