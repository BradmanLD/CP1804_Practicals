import os
import shutil


def main():
    os.chdir("FilesToSort")
    # print(os.listdir("."))    # Check what directory I'm in

    file_types = []
    for filename in os.listdir("."):
        file_type = filename[filename.find('.') + 1:]
        if file_type not in file_types:
            file_types.append(file_type)
            # print(filename[filename.find('.') + 1:])    # Print only the file type

    # print(file_types)   # Check that the for loop adds all the file types
    create_directories(file_types)
    move_files_into_directories(file_types)


def move_files_into_directories(file_types):
    for filename in os.listdir("."):
        if not os.path.isdir(filename):
            for file_type in file_types:
                if filename[filename.find('.') + 1:] == file_type:
                    shutil.move(filename, file_type)


def create_directories(file_types):
    # Create directories for the files
    for file_type in file_types:
        if file_type not in os.listdir("."):
            os.mkdir(file_type)
            # print("I went here")  # Testing the if statement


main()
