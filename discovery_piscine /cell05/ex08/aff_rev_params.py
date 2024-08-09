#!/usr/bin/env python3
##Create a program called aff_rev_params.py.
##This program should be executable.
##When executed, the program should display all the strings passed as parameters,
##followed by a newline, in reverse order.
##If there are fewer than two parameters, it should display none followed by a newline.
import sys

def main():
    if len(sys.argv) < 3:
        print("none")
    else:
        for arg in reversed(sys.argv[1:]):
            print(arg)

if __name__ == "__main__":
    main()