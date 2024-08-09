#!/usr/bin/env python3
##Create a program called append_it.py.
##This program should be executable.
##The program will display each parameter passed as an argument, one by one, by
##appending it with "ism".
##If the parameter already ends with "ism", it will be skipped and not displayed. If
##there are no parameters, it should display "none" followed by a newline.

import sys

def main():
    if len(sys.argv) == 1:
        print("none")
        return

    for param in sys.argv[1:]:
        if not param.endswith("ism"):
            print(f"{param}ism")

if __name__ == "__main__":
    main()

##acrescenta ism no final de cada palavra  