"""
Write a program that asks the user how many “quick picks” they wish to generate. The program then
generates that many lines of output. Each line consists of six random numbers between 1 and 45.
Each line should not contain any repeated number. Each line of numbers should be displayed in
ascending order.
Note: Python's random function has a sample method, which returns a selection from a list. This is a
nice way to solve this problem... but it's too easy :) Do not use it for this program.
"""
import random


def main():
    random_num_list = []
    number_of_quick_picks = int(input("How many quick picks? "))
    for quick_pick in range(0, number_of_quick_picks):
        for i in range(0, 6):
            random_number = random.randint(1, 45)
            while random_number in random_num_list:
                random_number = random.randint(1, 45)
            random_num_list.append(random_number)
            if i == 5:
                random_num_list.sort()
                print('{:2d} {:2d} {:2d} {:2d} {:2d} {:2d}'.format(random_num_list[0], random_num_list[1],
                                                                   random_num_list[2],
                                                                   random_num_list[3], random_num_list[4],
                                                                   random_num_list[5]))
                random_num_list.clear()


main()
