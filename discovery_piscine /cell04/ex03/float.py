#!/usr/bin/env python3
##Create a program called float.py.
##This program should be executable.
##Your script will ask the user for a number.
##You should then display whether the entered number is a decimal or not.

def main():
    try:
        user_input = float(input("Give me a number: "))
        if user_input.is_integer():
            print("This number is an integer.")
        else:
            print("This number is a decimal.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
   main()
