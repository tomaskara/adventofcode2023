import re

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

final_count = 0


for line in lines:
    match = False
    winning, numbers = line.split(': ')[1].split(' | ')
    winning_l = re.findall(r'\b\d+\b', winning)
    numbers_l = re.findall(r'\b\d+\b', numbers)
    result = 0.5
    for number in numbers_l:
        if number in winning_l:
            match = True
            result = result*2
    if match:
        final_count += result

print(int(final_count))
