##Create a program called iszero.py
##This program should be executable. (Consider the permissions, especially)
##When executed, the program should prompt for a number to be entered.
##If the number is equal to zero, the program should display "This number is equal to zero."
##If the number is not equal to zero, the program should display "This number is different from zero."
#!/usr/bin/env python3

numero = int(input("Please enter a number: "))

if numero == 0:
    print("This number is equal to zero")
else:
    print("This number is different from zero")

##para ter acesso a pasta usar no shell chmod 744 + nome do arquivo e depois poder executar
##para executar usar ./ nome do arquivo enter
##para ter auto complete usar o fish no terminal