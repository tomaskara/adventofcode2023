with open('input.txt', 'r') as f:
    lines = f.read().splitlines()


def check_neighbors_numbers(row, col):
    parts = 0
    numbers = []
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1,-1), (1, 1), (-1, 1), (1,-1)]
    for direction in directions:
        new_row = row + direction[0]
        new_col = col + direction[1]

        if 0 <= new_row < len(lines) and 0 <= new_col < len(lines[0]):
            if lines[new_row][new_col].isdigit():
                parts += 1
                number = lines[new_row][new_col]
                position = 0
                right_no_find = False
                left_no_find = False
                while True:
                    position += 1
                    if (new_col+position) < len(line) and not right_no_find:
                        if lines[new_row][new_col+position].isdigit():
                            number += lines[new_row][new_col+position]
                        else:
                            right_no_find = True
                    else:
                        right_no_find = True
                    if (new_col-position) >= 0 and not left_no_find:
                        if lines[new_row][new_col-position].isdigit():
                            number = lines[new_row][new_col-position]+number
                        else:
                            left_no_find = True
                    else:
                        left_no_find = True
                    if right_no_find and left_no_find:
                        break
                if number in numbers:
                    parts -= 1
                else:
                    numbers.append(number)
        else:
            continue
    if parts == 2:
        return int(numbers[0])*int(numbers[1])
    else:
        return 0


final_count = 0

for line_n, line in enumerate(lines):
    new_index = 0
    for char_n, char in enumerate(line):
        if char == '*':
            final_count += check_neighbors_numbers(line_n,char_n)


print(final_count)