#!/usr/bin/env python3
##Create a program called upcase_it.py that takes a string as a parameter.
##This program should be executable.
##The program should display the string in uppercase, followed by a newline.
##If the number of parameters is different from 1, display "none" followed by a newline.
import sys

def main():
    if len(sys.argv) != 2:
        print("none")
    else:
        print(sys.argv[1].upper())

if __name__ == "__main__":
    main()