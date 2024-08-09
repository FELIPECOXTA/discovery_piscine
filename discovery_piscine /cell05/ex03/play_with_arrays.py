#!/usr/bin/env python3
##Take the previous program and modify it to remove duplicates from the output.
##Note that you should not explicitly remove values from your arrays.
##For example, if your original array is [2, 8, 9, 48, 8, 22, -12, 2], the expected outputwould be:


def main():
    # Define the original array
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]

    # Create a new array by adding 2 to each value of the original array
    new_array = [x + 2 for x in original_array if x > 5]

    # Convert the new array to a set to remove duplicates
    unique_set = set(new_array)

    # Display both the original array and the unique set
    print("Original array:", original_array)
    print("Unique set:", unique_set)

if __name__ == "__main__":
    main()
