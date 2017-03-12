"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
__author__ = 'Lindsay Ward'

MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            print(convert_celsius_to_fahrenheit(celsius))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            print(convert_fahrenheit_to_celsius(fahrenheit))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_fahrenheit_to_celsius(fahrenheit_temp):
    celsius = 5 / 9 * (fahrenheit_temp - 32)
    return celsius


def convert_celsius_to_fahrenheit(celsius_temp):
    fahrenheit = celsius_temp * 9.0 / 5 + 32
    return fahrenheit



