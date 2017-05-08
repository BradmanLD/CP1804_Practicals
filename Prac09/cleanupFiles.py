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

    print(get_fixed_filename("AngelsWeHaveHeard.txt"))
    # make a new directory
    # os.mkdir('temp')

    # loop through each file in the (original) directory
    # for filename in os.listdir('.'):

        # ignore directories, just process files
        # if not os.path.isdir(filename):
            # new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
            # print(new_name)

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
    print("Original name is: " + filename)  # Used to test letter for loop
    for i, letter in enumerate(filename):
        if letter in string.ascii_uppercase and letter is not filename[0]:
            if filename[i - 1] == " ":
                filename = filename.replace(filename[i - 1], "_")

            elif filename[i - 1].islower():
                filename = filename[:i] + "_" + filename[i:]   # Can't change it here as it adds a letter

    return filename


main()
