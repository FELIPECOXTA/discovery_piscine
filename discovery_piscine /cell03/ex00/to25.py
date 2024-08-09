#!/usr/bin/env python3
##Create a program called to25.py
##This program should be executable
##The program accepts user input. This input is a number, which you will store in a numeric variable.
##Next, create a loop that displays all the numbers from the input number up to 25.
##If the input number is greater than 25, display "Error" followed by a new line.
##Use a while loop.

numero = int(input("Insert a number: "))

if numero > 25:
    print("Error")

while numero <= 25:
    print(f"Inside the loop, my variable is {numero}")
    numero = numero + 1