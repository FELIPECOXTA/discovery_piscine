#!/usr/bin/env python3
# Take the previous program and modify it to only process values greater than 5 from the original array.
# For example, if your original array is [2, 8, 9, 48, 8, 22, -12, 2], you should have the following output:
# ?> ./play_with_arrays.py | retirar numeros que sao menos que 5 e soma 2 nos que sao maiores dentro do arrei  soma +2 para todoa vem o original arrey seja menor que 5

def main():
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    new_array = [x + 2 for x in original_array if x > 5]

    print("Original array:", original_array)
    print("Processed array (values greater than 5):", new_array)

if __name__ == "__main__":
    main()
