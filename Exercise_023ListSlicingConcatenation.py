"""A new list by slicing and concatenation from a list of
 6 given number  [10, 20, 30, 40, 50, 60]"""


import sys

def main():
    """New list by slicing and concatenation from a list of
    6 given number  [10, 20, 30, 40, 50, 60] for the middle
     4 numbers"""
    my_list = [10, 20, 30, 40, 50, 60]
    print(my_list)
    #new_list = my_list[1:5]
    _0th = my_list[1:2]
    _1st = my_list[2:3]
    _2nd = my_list[3:4]
    _3rd = my_list[4:5]
    new_list = _0th + _1st + _2nd + _3rd
    print(new_list)
    return 0


if __name__ == '__main__':
    sys.exit(main())