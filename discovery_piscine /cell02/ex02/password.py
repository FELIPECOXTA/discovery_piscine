#!/usr/bin/env python3
##Create a program called password.py.
##This program should be executable.
## The program should have a variable containing a password - password = "Python is awesome"
##When executed, the program should prompt for a password to be entered
##If the password is correct, the program should display "ACCESS GRANTED"; otherwise, it should display "ACCESS DENIED."

senha1 = "Anitta"
senha = input("Digite uma senha: ")

if senha == senha1:
    print("ACESSO CONCEDIDO")

else:
    print("ACESSO NEGADO")


##para ter acesso a pasta usar no shell chmod 744 + nome do arquivo
##para executar usar ./ e o nome do arquivo
##para ter auto complete usar o fish no terminal