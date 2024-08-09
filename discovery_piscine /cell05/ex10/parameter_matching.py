#!/usr/bin/env python3
##Create a program called parameter_matching.py.
##This program should be executable.
##If a parameter is passed as an argument to the program, it should prompt the user to enter a word.
##If the word entered by the user is the same as the parameter passed, the program
##should display "Good job!". Otherwise, it should display "Nope, sorry..." followed by a newline.
##If the number of parameters passed to the program is different from 1, it should
##display "none" followed by a newline.

import sys

def main():
    if len(sys.argv) != 2:
        print("none")
        return

    parameter = sys.argv[1]
    user_input = input("What was the parameter? ")

    if user_input == parameter:
        print("Good job!")
    else:
        print("Nope, sorry...")

if __name__ == "__main__":
    main()


##verifica se o parametro passado entre aspas eh o mesmo do input se sim, good job se nao nop sorry