#!/usr/bin/env python3
##Create a program called free_range.py that takes two parameters.
##These two parameters will be two numbers.
##This program should be executable.
##You must construct an array containing all the values between these two numbers
##using a range. Then, you will display the array using the print function.
##If the number of parameters is different from 2, you should display ’none’ followed by a newline.

import sys

def main():
    if len(sys.argv) != 3:
        print("none")
        return

    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        print(list(range(start, end + 1)))
    except ValueError:
        print("none")

if __name__ == "__main__":
    main()