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
    if n < 0:
        print(n ** 2)
    do_something(n - 1)

# TODO: 3. write down what you think the output of this will be,
# TODO: 4. use the debugger to step through and see what's actually happening
# do_something(4)

# TODO: 5. fix the do_something() function so that it works the way it is probably supposed to :)
