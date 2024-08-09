#!/usr/bin/env python3
##Create a program called multiplication_table.py.
##This program should be executable.
##The program accepts user input. This input is a number, which you will store in a numeric variable.
##This number represents the multiplication table you will display. (For example, if the input is 2, you need to display the table for 2)


n = int(input("Tabuada de: "))
i = 0 

while i < 10:
    m = n * i
    print(n, "x", i,"=", m)
    i += 1