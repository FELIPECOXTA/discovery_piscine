#!/usr/bin/env python3
##Create a program called calculator.py.
##This program should be executable.
##Your script will ask the user for two numbers.
##You must store these numbers as numerical values in two variables.
##You should then display the result of their addition, subtraction, division, and multiplication.

first_number = input("Give me the first number: ")
second_number = input("Give me the second number: ")

try:
    first_number = float(first_number)
    second_number = float(second_number)

    print("Thank you!")
    print(f"{first_number} + {second_number} = {first_number + second_number}")
    print(f"{first_number} - {second_number} = {first_number - second_number}")
    
    if second_number != 0:
        print(f"{first_number} / {second_number} = {(first_number / second_number):,.2f}") ##:,.2fdetermino a quantidade de casas decimais vou demonstar apos a virgula (first_number / second_number):,.2f
    else:
        print("Division by zero is not allowed.")
        
    print(f"{first_number} * {second_number} = {first_number * second_number}")
except ValueError:
    print("Please enter valid numbers.")