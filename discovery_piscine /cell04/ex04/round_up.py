#!/usr/bin/env python3
##Create a program called round_up.py.
##This program should be executable.
##Your script will ask the user for a number.
##You should then display the entered number rounded up.

import math

try:
        number = float(input("Give me a number: "))
        print(math.ceil(number))
except ValueError:
        print("Invalid input. Please enter a valid number.")




##math.floor() arredonda para mais baixo
##math.ceil() arredonda para cima
##float para usar decimal