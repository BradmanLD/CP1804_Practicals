LOWER_BOUND = 33
UPPER_BOUND = 127
character = str(input("Enter a character: "))
print("The ASCII code for {} is {}".format(character, ord(character)))
number = int(input("Enter a number between {} and {}: ".format(LOWER_BOUND, UPPER_BOUND)))
while number < LOWER_BOUND or number > UPPER_BOUND:
    number = int(input("Invalid number, Enter a number between {} and {}: ".format(LOWER_BOUND, UPPER_BOUND)))
print("The character for {} is {}".format(number, chr(number)))
for i in range(LOWER_BOUND, UPPER_BOUND):
    print("{0} {1:>6}".format(i, chr(i)))
