

def print_pyramid_loop(rows):
    current_row = 1
    while current_row-1 != rows:
        print(current_row + (current_row - 1) + (current_row - 2) + (current_row - 3) + 2 + 1)
        current_row += 1

# print_pyramid_loop(6)


def print_pyramid_recursive(row):
    if row > 0:
        print_pyramid_recursive(row-1)
        print(row + (row - 1) + (row -2) + (row - 3) + 2 + 1)   # Do it second so the pyramid starts with largest num.


print_pyramid_recursive(6)