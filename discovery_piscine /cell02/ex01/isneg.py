#!/usr/bin/env python3
##Create a program called isneg.py.
##This program should be executable.
##When executed, the program should prompt for a number to be entered.
##If the number is negative, the program should display "This number is negative."
##If the number is positive, the program should display "This number is positive."
##If the number is equal to zero, the program should display "This number is both positive and negative."


number = int(input("Please enter a number: "))

if number < 0:
    print("This number is negative")

if number == 0:
    print("This numeber is similar like positive and negative")

if number > 0:
    print ("This number is positive")


##para ter acesso a pasta usar no shell chmod 744 + nome do arquivo
##para executar usar ./ e o nome do arquivo
##para ter auto complete usar o fish no terminal