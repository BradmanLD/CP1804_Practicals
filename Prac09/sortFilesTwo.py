import os
import shutil


def main():
    os.chdir("FilesToSort")
    # print(os.listdir("."))    # Check what directory I'm in

    file_types_to_categories = {}
    categories = set()
    for filename in os.listdir("."):
        file_type = filename[filename.find('.') + 1:]
        if file_type not in file_types_to_categories:
            category = input("What category would you like to sort {} files into?".format(file_type))
            categories.add(category)

            # print(filename[filename.find('.') + 1:])    # Print only the file type
            file_types_to_categories[file_type] = category



    # print(file_types_to_categories)   # Check that the for loop adds all the file types
    create_directories(categories)
    move_files_into_directories(file_types_to_categories)


def move_files_into_directories(file_types):
    for filename in os.listdir("."):
        if not os.path.isdir(filename):
            extension = filename[filename.find('.') + 1:]
            shutil.move(filename, file_types[extension])

            # shutil.move(filename,)
            # for file_type in file_types:
            #     if filename[filename.find('.') + 1:] == file_type:
            #         shutil.move(filename, file_type)


def create_directories(directory_names):
    # Create directories for the files
    for directory_name in directory_names:
        if directory_name not in os.listdir("."):
            # print(directory_name)
            os.mkdir(directory_name)


main()
