name = "Gibson L-5 CES"
year = 1922
cost = 16035.40
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))
# Formatting Currency:
print("My {} would cost ${:,.2f}".format(name, cost))
# Aligning Columns:
numbers = [1, 19, 123, 456, -25]
for i in range(len(numbers)):
 print("Number {0} is {1:>5}".format(i + 1, numbers[i]))


# RANDOM QUESTIONS
# Smallest number on line 1: 5, Largest Number: 20 (Randint is just random number in range)
# Smallest number on line 2: 5, Largest Number: 9 (Range allows for a step)
# Smallest number on Line 3: 2.5, Largest Number: 5.5 (Uniform allows random to be decimal)
