"""Sum of inputs replaced by square and cube
of first and last numbers"""

import sys

def main():
    """Ask the user to enter four integers.
        Store them in 'nums'.
        Replace:
        the first number with its square.
        the last number with its cube.
        The compute and print the sum of all four numbers
        # 1. Ask for input (returns a string)
        # 2. Split the string by commas (returns a list of strings)
        # 3. Convert each string in that list to an int using a comprehension.
        """
    nums = [int(n) for n in input("Enter four numbers separated by a comma: ").split(",")]
    print(nums)
    nums[0] = nums[0]*2
    nums[-1] = nums[-1]*3
    print(nums)
    sum = nums[0]+nums[1]+nums[2]+nums[3]
    print(sum)
    return 0


if __name__ == "__main__":
    sys.exit(main())