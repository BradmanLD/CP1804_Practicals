

def print_pyramid_loop(rows):
    total = 0
    for row in range(rows + 1):
        total += row
    print(total)

# print_pyramid_loop(6)


def required_number_of_blocks(row_number):
    if row_number == 0:
        return 0
    return row_number + required_number_of_blocks(row_number - 1)


print(required_number_of_blocks(3))
