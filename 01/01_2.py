with open('input.txt', 'r') as f:
    lines = f.readlines()

words = {'one': '1',
         'two': '2',
         'three': '3',
         'four': '4',
         'five': '5',
         'six': '6',
         'seven': '7',
         'eight': '8',
         'nine': '9'}

final_count = 0
first = ''
last = ''
buffer =''

for line in lines:
    line = line.rstrip('\n')
    for char in line:
        if char.isdigit():
            first = char
            break
        else:
            buffer += char
        for word in words:
            if word in buffer:
                first = words[word]
                break

        if first != '':
            break
    buffer = ''
    for char in line[::-1]:
        if char.isdigit():
            last = char
            break
        else:
            buffer = char + buffer
        for word in words:
            if word in buffer:
                last = words[word]
                break
        if last != '':
            break

    final_count += int(first + last)
    buffer = ''
    first = ''
    last = ''


print(final_count)