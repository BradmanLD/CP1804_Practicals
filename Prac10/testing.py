"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from Prac07.car import Car


def repeat_string(s, n):
    """
    repeat string s, n times, with spaces in between
    # """
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # Hint: "-".join(["yo", "yo"] -> "yo-yo"

    # assert test with custom message - used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"
    assert test_car.fuel == 0

    test_car = Car(fuel=20)
    assert test_car.fuel == 20

    test_car.drive(15)
    assert test_car.odometer == 15
    # Note that Car's __init__ function sets the fuel in one of two ways: using the value passed in or the default
    # You should test both of these


run_tests()


def format_phrase(phrase):
    # Important: start with a function header and just use pass as the body
    # then add doctests so that:
    # 'hello' -> ''Hello.'
    # 'It is an ex parrot.' -> 'It is an ex parrot.'
    # and one more you decide (that's valid!)
    # then write the body of the function so that the tests pass
    """
            >>> format_phrase("hello")
            'Hello.'
            >>> format_phrase("It is an ex parrot.")
            'It is an ex parrot.'
            >>> format_phrase("it did the thing.")
            'It did the thing.'
            """
    formatted_phrase = phrase[0].upper()
    phrase = phrase[1:]
    for i, letter in enumerate(phrase):
        if i == len(phrase) - 1 and phrase[-1] != ".":
            formatted_phrase += letter + "."
        else:
            formatted_phrase += letter
    return formatted_phrase

# doctest.testmod()
