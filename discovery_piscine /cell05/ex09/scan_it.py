#!/usr/bin/env python3
# #• Create a program called scan_it.py.
## • This program should take two parameters.
## • The first parameter is a keyword to search for in a string.
## • The second parameter is the string to be searched.
## • This program should be executable.
## • When executed, the program should display the number of times the keyword appears in the string.
## • If the number of parameters is different from 2 or if the first string does not appear
## in the second, it should display none followed by a newline
import sys

def main():
    if len(sys.argv) != 3:
        print("none")
    else:
        keyword = sys.argv[1]
        string_to_search = sys.argv[2]
        count = string_to_search.count(keyword)
        if count == 0:
            print("none")
        else:
            print(count)

if __name__ == "__main__":
    main()