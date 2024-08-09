#!/usr/bin/env python3
##Create a program called downcase_it.py.
##This program should be executable.
##The program takes a string as a parameter.
##It should display the string in lowercase, followed by a newline.
##If the number of parameters is different from 1, it should display "none" followed by a newline.

import sys

def main():
    if len(sys.argv) != 2:
        print("none")
    else:
        print(sys.argv[1].lower())

if __name__ == "__main__":
    main()