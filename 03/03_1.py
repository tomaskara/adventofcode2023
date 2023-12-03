with open('input.txt', 'r') as f:
    lines = f.read().splitlines()


def check_neighbors_symbols(row, col):
    symbols = ['*','+','/','=','#','%','$', '&', '@', '-']
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1,-1), (1, 1), (-1, 1), (1,-1)]
    for direction in directions:
        new_row = row + direction[0]
        new_col = col + direction[1]

        if 0 <= new_row < len(lines) and 0 <= new_col < len(lines[0]):
            if lines[new_row][new_col] in symbols:
                return True
        else:
            continue
    return False


number = ''
final_count = 0

for line_n, line in enumerate(lines):
    new_index = 0
    for char_n, char in enumerate(line):
        number = ''
        if char_n < new_index:
            continue
        if char.isdigit():
            number += char
            new_index = char_n
            while True:
                new_index += 1
                if new_index < len(line):
                    if line[new_index].isdigit():
                        number += line[new_index]
                    else:
                        break
                else:
                    break
            for i in range(char_n,new_index):
                if check_neighbors_symbols(line_n, i):
                    final_count += int(number)
                    break


print(final_count)