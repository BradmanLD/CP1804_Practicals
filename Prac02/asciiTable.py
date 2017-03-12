LOWER_BOUND = 33
UPPER_BOUND = 127


def main():
    character = str(input("Enter a character: "))
    print("The ASCII code for {} is {}".format(character, ord(character)))
    ascii_number = get_number(LOWER_BOUND, UPPER_BOUND)
    print("The character for {} is {}".format(ascii_number, chr(ascii_number)))
    for i in range(LOWER_BOUND, UPPER_BOUND):
        print("{0} {1:>6}".format(i, chr(i)))


def get_number(lower, upper):
    number = 0
    while number < lower or number > upper:
        try:
            number = int(input("Enter a number between {} and {}: ".format(lower, upper)))
        except ValueError:
            print("Invalid Input: Try again.")
    return number


main()