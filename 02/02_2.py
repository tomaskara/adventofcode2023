import re

with open('input.txt', 'r') as f:
    lines = f.readlines()

final_count = 0

for line in lines:
    red = 0
    blue = 0
    green = 0
    line = line.rstrip('\n')
    game_id = int(re.findall(r'Game (\d+):', line)[0])
    sets = line.split(': ')[1].split('; ')
    for s in sets:
        draws = s.split(', ')
        for draw in draws:
            number, color = draw.split(' ')
            if color == 'red':
                if int(number) > red:
                    red = int(number)
            if color == 'blue':
                if int(number) > blue:
                    blue = int(number)
            if color == 'green':
                if int(number) > green:
                    green = int(number)
    count = red*blue*green
    final_count += count



print(final_count)