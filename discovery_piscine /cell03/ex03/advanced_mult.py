##Create a program called advanced_mult.py.
##This program should be executable.
##This program will display all multiplication tables in the following format 
##You are only allowed to use two while loops.

#!/usr/bin/env python3
import sys

if len(sys.argv) >1:
    print("None")
    exit()
x = 0
while x <= 10:
    print(f"Tabela de  {x}: ", end= "")
    y = 0
    while y <= 10:
        print(f"{x*y:4}" , end ="")
        y += 1
    print()
    x += 1