import os


os.chdir("FilesToSort")
# print(os.listdir("."))    # Check what directory I'm in

file_types = []
for filename in os.listdir("."):
    file_types.append(filename[filename.find('.') + 1:])
    # print(filename[filename.find('.') + 1:])    # Print only the file type

# print(file_types)   # Check that the for loop adds all the file types
