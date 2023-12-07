with open('input.txt', 'r') as f:
    lines = f.read().splitlines()


def parse_input(lines):
    seeds_line = [int(x) for x in lines[0].split(':')[1].split()]

    categories = {}
    current_category = None
    for line in lines[1:]:
        if line.endswith(':'):
            current_category = line[:-1].strip().replace(' map', '')
            categories[current_category] = []
        elif line.strip():
            categories[current_category].append(list(map(int, line.split())))

    return seeds_line, categories


def next_cat(value, category):
    for rule in category:
        if rule[1] <= value <= (rule[1] + rule[2] - 1):
            value = value - (rule[1] - rule[0])
            break

    return value


seeds, categories = parse_input(lines)

min_location = 100000000000000000

for seed in seeds:
    location = next_cat(next_cat(next_cat(next_cat(next_cat(next_cat(next_cat(seed,
                                categories['seed-to-soil']),
                                categories['soil-to-fertilizer']),
                                categories['fertilizer-to-water']),
                                categories['water-to-light']),
                                categories['light-to-temperature']),
                                categories['temperature-to-humidity']),
                                categories['humidity-to-location'])
    if location < min_location:
        min_location = location

print(min_location)

