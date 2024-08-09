#!/usr/bin/env python3
C##reate a program called count_it.py.
##This program should be executable.
##The program will display "parameters:" followed by the number of parameters
##passed as arguments, followed by a newline. Then, for each parameter, it will
##display the parameter itself and its length, followed by a newline.
##If there are no parameters, it should display "none" followed by a newline.

import sys

def main():
    if len(sys.argv) == 1:
        print("none")
        return

    print(f"parameters: {len(sys.argv) - 1}")
    for param in sys.argv[1:]:
        print(f"{param}: {len(param)}")

if __name__ == "__main__":
    main()

##vai pegar o tamanho do parametro dentre aspas