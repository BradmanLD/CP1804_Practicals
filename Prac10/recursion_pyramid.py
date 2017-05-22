

def print_pyramid_loop(rows):
    total = 0
    for row in range(rows + 1):
        total += row
    print(total)

print_pyramid_loop(2)


def print_pyramid_recursive(row):
    if row > 0:
        print_pyramid_recursive(row-1)
        print(row + (row - 1) + (row -2) + (row - 3) + 2 + 1)   # Do it second so the pyramid starts with largest num.


# print_pyramid_recursive(6)
