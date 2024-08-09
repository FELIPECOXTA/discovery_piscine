#!/usr/bin/env python3
##Create a program called parameters.py.
##This program should be executable.
##The program will display the number of parameters passed to it, followed by a newline.

import sys

def main():

    num_params = len(sys.argv) - 1

    print(f"Number of parameters: {num_params}.")

if __name__ == "__main__":

    main()