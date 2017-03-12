try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished")


# QUESTIONS
# When will value error occur? When the input for either numerator or denominator isn't an integer
# When will ZeroDivisionError occur? When the algorithm calculates fraction and the users input
#   for the denominator was a 0
