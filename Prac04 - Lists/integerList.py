"""
Write a program that prompts the user for 5 numbers and then stores each of these in a list called
numbers. The program should then output various interesting things, as in the output below (green
represents user input).
"""


def main():
    numbers = []
    for i in range(5):
        number = int(input("Enter a number: "))
        numbers.append(number)
    print("The first number is ", numbers[0])
    print("The last number is ", numbers[-1])
    print("The smallest number is ", min(numbers))
    print("The largest number is", max(numbers))
    print("The average of the numbers is", sum(numbers)/len(numbers))


main()
