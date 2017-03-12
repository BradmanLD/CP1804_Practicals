"""
Bradman Davis
"""


def main():
    name = get_name()
    print_second_letter(name)


def print_second_letter(name):
    for char in name[::2]:
        print(char)


def get_name():
    name = str(input("Enter your name: "))
    return name
