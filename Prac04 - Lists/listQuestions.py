numbers = [3, 1, 4, 1, 5, 9, 2]


"""
numbers[0]      | is 3 because index starts at 0
numbers[-1]     | is 2 because -1 goes from end to start
numbers [3]     | is 1
numbers [:-1]   | is 3, 1, 4, 1, 5, 9 because :-1 slices the last value in the list
numbers [3:4]   | is 1 because it shows the range of indexes from 3-4
5 in numbers    | is True
7 in numbers    | is False
"3" in numbers  | is False
numbers + [6, 5, 3] | is [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

How to Achieve the following?
1. Change the first element of numbers to "ten"
    numbers[0] = "ten"

2. Change the last element of numbers to 1
    numbers[-1] = "1"

3. Get all the elements from numbers except the first two
    get_numbers = numbers[2:]

4. Check if 9 is an element of numbers
    9 in numbers
"""