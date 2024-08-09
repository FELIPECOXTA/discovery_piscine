#!/usr/bin/env python3
##Create a program called up_low.py.
##This program should be executable.
##Your script will ask the user for a string.
##You should then display the string with uppercase letters changed to lowercase and vice versa.

def main():
    user_input = input("Enter a string: ")
    swapped_string = swap_case(user_input)
    print(swapped_string)

def swap_case(s):
    return s.swapcase()

if __name__ == "__main__":
    main()

##if __name__ == "__main__": verifica se o script está sendo executado diretamente 
##(ou seja, não foi importado como um módulo em outro arquivo Python).  
