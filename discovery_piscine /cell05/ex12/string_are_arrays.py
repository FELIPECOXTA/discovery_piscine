#!/usr/bin/env python3
##Create a program called string_are_arrays.py that takes a string as a parameter.
##This program should be executable.
##When executed, the program should display "z" for each occurrence of the character
##"z" in the string passed as a parameter, followed by a newline.
##If the number of parameters is different from 1, or if there are no "z" characters in
##the string, it should display "none" followed by a newline.

import sys

def main():
    if len(sys.argv) != 2:##verifica se o número de argumentos passados para o programa é diferente de 2.
        print("none")
        return

    parameter = sys.argv[1]
    z_count = parameter.count('z')

    if z_count == 0:
        print("none")
    else:
        print('z' * z_count)

if __name__ == "__main__":
    main()

##extrair da string o numero de z`s