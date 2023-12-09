with open('input.txt', 'r') as f:
    lines = f.read().splitlines()


def calculate_diff(numbers: list,diff_list):
    diff = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
    diff_list.append(diff)
    if sum(diff) == 0 and max(diff) == 0:
        return diff_list[::-1]
    else:
        return calculate_diff(diff,diff_list)

final_count = 0
for line in lines:
    numbers = [int(x) for x in line.split()]
    diff_list = []
    diff_list = calculate_diff(numbers, diff_list)
    count = 0
    temp_value = 0
    for ls in diff_list[1:]:
        temp_value = ls[0]-temp_value
    new_item = int(numbers[0])-temp_value
    final_count += new_item


print(final_count)