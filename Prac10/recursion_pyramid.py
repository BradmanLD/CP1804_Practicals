

def calculate_number_of_blocks_loop(number_of_rows):
    total = 0
    for row in range(number_of_rows + 1):
        total += row
    return total

# print(calculate_number_of_blocks_loop(6))


def calculate_number_of_blocks_recursive(row_number):
    if row_number == 0:
        return 0
    return row_number + calculate_number_of_blocks_recursive(row_number - 1)


print(calculate_number_of_blocks_recursive(3))
