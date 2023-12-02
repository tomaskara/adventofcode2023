import re

with open('input.txt', 'r') as f:
    lines = f.readlines()

final_count = 0

for line in lines:
    line = line.rstrip('\n')
    game_id = int(re.findall(r'Game (\d+):', line)[0])
    sets = line.split(': ')[1].split('; ')
    for s in sets:
        draws = s.split(', ')
        for draw in draws:
            number, color = draw.split(' ')
            if color == 'red' and int(number) > 12:
                break
            if color == 'blue' and int(number) > 14:
                break
            if color == 'green' and int(number) > 13:
                break
        else:
            continue
        break
    else:
        final_count += game_id
        continue


print(final_count)