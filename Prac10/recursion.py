"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)

#                               GOT  RETURN
# do_it(5) -> 5 % 2 + do_it(4)  [2]   [3]
# do_it(4) -> 4 % 2 + do_it(3)  [2]   [2]
# do_it(3) -> 3 % 2 + do_it(2)  [1]   [2]
# do_it(2) -> 2 % 2 + do_it(1)  [1]   [1]
# do_it(1) -> 1 % 2 + do_it(0)  [0]   [1]
# do_it(0) -> return 0          []    [0]
# .: The output is 3.

print(do_it(5))


def do_something(n):
    if n > 0:
        print(n ** 2)
        do_something(n - 1)

# do_something(4) -> do_something(3) -> do_something(2) -> do_something(1) -> do_something(0) -V
# do_something(-1) -> -1 ** 2 = 1, also I think python shows this as 1 instead of -1. To get 1 it would be (-1)**2.
# Wait it doesn't end, it will recurse until it hits the recursion limit.
# .: The output is like a thousand different numbers.

# SECOND ATTEMPT WITH RECURSION FIXED.
# do_something(4) -> 4 ** 2 = 16
# do_something(3) -> 3 ** 2 = 9
# do_something(2) -> 2 ** 2 = 4
# do_something(1) -> 1 ** 2 = 1
# .: Output is: 16, 9, 4, 1 ( , = new line)

do_something(4)

# TODO: 5. fix the do_something() function so that it works the way it is probably supposed to :)
