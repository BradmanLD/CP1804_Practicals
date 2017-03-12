"""
Bradman Davis
"""


def main():
    name = get_name()
    print_name(name)


def print_name(name):
    for char in name[::2]:
        print(char)


def get_name():
    name = str(input("Enter your name: "))
    return name

main()