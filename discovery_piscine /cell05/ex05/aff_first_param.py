#!/usr/bin/env python3
##Create a program called aff_first_param.py.
##This program should be executable.
##The program displays the first string parameter passed, followed by a newline.
##If there are no parameters, display "none" followed by a newline.
import sys

def main():

    if len(sys.argv) > 1:

        print(sys.argv[1])

    else:

        print("none")


if __name__ == "__main__":

    main()