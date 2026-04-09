"""Update Integer
using +=, -=, *=, and **= (compute powers) and print each result.
"""

import sys

def main():
    """Updating a given integer x = 10 using +=, -=, *=, **=
    x +=  Same as x + 10
    """
    x = 10

    x += 10
    print(f"After +=: {x}")

    x -= 10
    print(f"After -=: {x}")

    x *= 10
    print(f"After *=: {x}")

    x **= 10
    print(f"After **=: {x}")

    """ 
    To keep the original x and save the results into new names
    _sum = x + 10        # Use + instead of +=
    _subtract = x - 10   # Use - instead of -=
    _multiply = x * 10   # Use * instead of *=
    _powersquare = x ** 10
    
    print(f"Sum: {_sum}, Sub: {_subtract}, Mult: {_multiply}, Power: {_powersquare}")
    """


if __name__ == "__main__":
    sys.exit(main())

