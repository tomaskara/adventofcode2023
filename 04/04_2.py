import re

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

card_dict= {}
for line in lines:
    card_name = int(line.split(':')[0].split()[1])
    card_dict[card_name] = 1

for line in lines:
    matches = 0
    number_of_card = int(line.split(': ')[0].split()[1])
    cards = card_dict[number_of_card]
    winning, numbers = line.split(': ')[1].split(' | ')
    winning_l = re.findall(r'\b\d+\b', winning)
    numbers_l = re.findall(r'\b\d+\b', numbers)
    for number in numbers_l:
        if number in winning_l:
            matches += 1
    if matches > 0:
        while cards:
            for i in range(number_of_card+1, number_of_card+matches+1):
                card_dict[i] += 1
            cards -= 1

print(sum(card_dict.values()))
