with open('input.txt', 'r') as f:
    lines = f.readlines()

final_count = 0
first = 0
last = 0

for line in lines:
    for char in line:
        if char.isdigit():
            first = char
            break
    for char in line[::-1]:
        if char.isdigit():
            last = char
            break
    final_count += int(first + last)


print(final_count)