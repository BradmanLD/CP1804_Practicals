"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import os, shutil
import string
__author__ = 'Lindsay Ward'


def main():
    # print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir('Lyrics/Christmas')
    # print a list of all files (test)
    # print(os.listdir('.'))

    # make a new directory
    # os.mkdir('temp')

    # loop through each file in the (original) directory
    for filename in os.listdir('.'):

        # ignore directories, just process files
        if not os.path.isdir(filename):
            # new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
            # print(new_name)

            fixed_filename = get_fixed_filename(filename)
            # print(fixed_filename)
            os.rename(filename, fixed_filename)

            # Option 1: rename file to new name - in place
            # os.rename(filename, new_name)

            # Option 2: move file to new place, with new name
            # shutil.move(filename, 'temp/' + new_name)


    # Processing subdirectories using os.walk()
    # os.chdir('..')
    # for dir_name, subdir_list, file_list in os.walk('.'):
    #     print("In", dir_name)
    #     print("\tcontains subdirectories:", subdir_list)
    #     print("\tand files:", file_list)


def get_fixed_filename(filename):
    # Try going through the filename character by character and adding it to a newname character by character
    print("Original name is: " + filename)  # Used to test letter for loop
    new_string = ""
    for i, letter in enumerate(filename):
        previous_letter = filename[i - 1]
        if i == 0:
            new_string += letter.upper()

        elif previous_letter in "_ ":
            new_string += letter.upper()

        elif previous_letter == "(":
            new_string += letter.upper()

        elif letter.islower() and previous_letter != " " and previous_letter != "_":
            new_string += letter

        elif letter.isupper() and previous_letter.islower():
            new_string += "_" + letter

        elif letter == " " and previous_letter != " ":
            new_string += "_"

        elif letter.isupper() and previous_letter.isupper():
            new_string += "_" + letter

        else:
            new_string += letter

    return new_string

main()
