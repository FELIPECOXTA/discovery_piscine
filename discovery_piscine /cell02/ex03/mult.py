##Create a program called mult.py.
##This program should be executable.
##When executed, the program should prompt for two numbers to be entered.
##The program will display whether the result of multiplying the two numbers is positive, negative, or zero.
##Then the program will display the result of the multiplication.

#!/usr/bin/env python3

numero1 = int (input("Insira o primeiro numero: "))


numero2 = int (input("Insira o segundo numero: "))


resultado = numero1 * numero2
##print(numero1, "x" ,numero2, "=" ,resultado)
print(f"{numero1} x {numero2} = {resultado}")

if resultado < 0:
    print("Este numero e negativo.")
elif resultado > 0:
    print("Este numero e positivo")
else:
    print("Este numero e zero.")

##para ter acesso a pasta usar no shell chmod 744 + nome do arquivo
##para executar usar ./ e o nome do arquivo
##para ter auto complete usar o fish no terminal