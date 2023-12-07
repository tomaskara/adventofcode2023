from collections import Counter

def evaluate_hand(hand):
    mod_order_of_hands = 'AKQT98765432J'[::-1]
    counter = Counter(hand)
    jacks = counter['J']
    most_common = counter.most_common(2)
    for common in most_common:
        if common[0] == 'J':
            continue
        else:
            counter[common[0]] += jacks
            counter['J'] -= jacks
            break
    values = []
    weight = 10
    additional_value = 0
    for card in hand:
        x = mod_order_of_hands.index(card)+1
        values.append(x)
    for val in values:
        additional_value += weight * val
        weight = weight / 100
    if any(count == 5 for count in counter.values()):
        value = 27000 + additional_value
    elif any(count == 4 for count in counter.values()):
        value = 16000 + additional_value
    elif any(count == 3 for count in counter.values()) and any(count == 2 for count in counter.values()):
        value = 10000 + additional_value
    elif any(count == 3 for count in counter.values()):
        value = 6000 + additional_value
    elif list(counter.values()).count(2) == 2:
        value = 3000 + additional_value
    elif any(count == 2 for count in counter.values()):
        value = 2000 + additional_value
    else:
        value = additional_value

    return value


with open('input.txt', 'r') as f:
    lines = [x.split() for x in f.read().splitlines()]

valuated_hands = []
for index, line in enumerate(lines):
    hand = line[0]
    value_of_hand = evaluate_hand(hand)
    lines[index].append(value_of_hand)

final_count = 0
sorted_lines = sorted(lines, key=lambda x: x[2])
for rank, hand in enumerate(sorted_lines):
    final_count += (int(hand[1]))*(rank+1)

print(final_count)




