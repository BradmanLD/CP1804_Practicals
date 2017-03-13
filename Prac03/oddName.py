"""
Bradman Davis
"""


def main():
    step = int(input("Enter the step: "))
    name = get_name()
    print_sliced_name(name, step)


def print_sliced_name(name, step):
    print(name[::step])


def get_name():
    name = input("Enter your name: ")
    while name.strip() == "":
        name = str(input("Invalid Input, Enter your name: "))
    return name

main()
