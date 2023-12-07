import copy

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


def best_ranges(start_range, category):
    rules = categories[category]
    good_ranges = []
    start_ranges = [start_range]
    for rule in rules:
        diff = int(rule[1] - rule[0])
        outcome_range = (rule[0], rule[0] + rule[2])
        for start_range in start_ranges:
            if outcome_range[0] > start_range[1] or outcome_range[1] < start_range[0]:
                continue
            else:
                intersection_start = max(start_range[0], outcome_range[0])
                intersection_end = min(start_range[1], outcome_range[1])
                new_good_range = (intersection_start, intersection_end)
                start_ranges.remove(start_range)
                if intersection_start > start_range[0] and intersection_end < \
                        start_range[1]:
                    start_ranges.append((start_range[0], intersection_start - 1))
                    start_ranges.append((intersection_end + 1, start_range[1]))

                elif intersection_start > start_range[0]:
                    start_ranges.append((start_range[0], intersection_start - 1))
                elif intersection_end < start_range[1]:
                    start_ranges.append((intersection_end + 1, start_range[1]))
                elif intersection_start == start_range[0] and intersection_end == \
                        start_range[1]:
                    good_input_range = (
                        new_good_range[0] + diff - 1, new_good_range[1] + diff - 1)
                    good_ranges.append(good_input_range)
                    continue

                good_input_range = (
                new_good_range[0] + diff - 1, new_good_range[1] + diff - 1)
                good_ranges.append(good_input_range)
    if len(start_ranges) > 0:
        for left_range in start_ranges:
            good_ranges.append(left_range)

    return good_ranges

seeds, categories = parse_input(lines)

best_categories = copy.deepcopy(categories)
best_categories = dict(reversed(best_categories.items()))
keys_best_categories = list(best_categories.keys())
locations = []

best_categories = dict(reversed(best_categories.items()))

first_category = best_categories['humidity-to-location']
sorted_rules = sorted(first_category, key=lambda x: x[0])

for best_rule in sorted_rules:
    possible_ranges = []
    start_range = (best_rule[1], (best_rule[1] + best_rule[2] - 1))
    for i in best_ranges(start_range, 'temperature-to-humidity'):
        for j in best_ranges(i, 'light-to-temperature'):
            for k in best_ranges(j, 'water-to-light'):
                for f in best_ranges(k, 'fertilizer-to-water'):
                    for l in best_ranges(f, 'soil-to-fertilizer'):
                        for possible_r in best_ranges(l, 'seed-to-soil'):
                            possible_ranges.append(possible_r)
    if len(possible_ranges) > 0:
        break

seed_ranges = list(zip(seeds[0::2], seeds[1::2]))

real_seed_ranges = []
for seed_range in seed_ranges:
    real_seed_range = (seed_range[0], seed_range[0] + seed_range[1] - 1)
    real_seed_ranges.append(real_seed_range)

cleared_ranges = []
for possible_range in possible_ranges:
    for r_seed_range in real_seed_ranges:
        if r_seed_range[0] > possible_range[1]:
            continue
        elif r_seed_range[1] < possible_range[0]:
            continue
        else:
            intersection_s = max(r_seed_range[0], possible_range[0])
            intersection_e = min(r_seed_range[1], possible_range[1])
            clear_range = (intersection_s, intersection_e)
            cleared_ranges.append(clear_range)


min_location = 100000000000000000

for clear_range in cleared_ranges:
    # for seed in range(cleared_ranges[0][0],int(cleared_ranges[0][1])):
    for seed in range(clear_range[0], clear_range[1]):
        location = next_cat(next_cat(next_cat(next_cat(next_cat(next_cat(next_cat(seed,
                                                                                  categories[
                                                                                      'seed-to-soil']),
                                                                         categories[
                                                                             'soil-to-fertilizer']),
                                                                categories[
                                                                    'fertilizer-to-water']),
                                                       categories['water-to-light']),
                                              categories['light-to-temperature']),
                                     categories['temperature-to-humidity']),
                            categories['humidity-to-location'])

        if location < min_location:
            min_location = location

print(min_location)

