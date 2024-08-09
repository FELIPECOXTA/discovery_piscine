#!/usr/bin/env python3
##Create a program called age.py.
##This program should be executable.
##The program asks the user to enter their age and then displays the user’s age in 10 years, 20 years, and 30 years.

age = int(input("Please tell me your age: "))

ageOne = 0
ageTwo = 0
ageTrhee = 0
ageOne = age+10
ageTwo = age+20
ageTrhee = age+30

print(f"You are currently {age} years old.")
print(f"In 10 years, you'll be {ageOne} years old.")
print(f"In 20 years, you'll be {ageTwo} years old.")
print(f"In 30 years, you'll be {ageTrhee} years old.")
