with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

instructions = lines[0]
nodes_dict = {}
for line in lines[2:]:
    node, lr = line.split(' = ')
    nodes_dict[node] = lr[1:-1].split(', ')

current_node = 'AAA'
steps = 0
while True:
    for instruction in instructions:
        if instruction == 'L':
            current_node = nodes_dict[current_node][0]
            steps += 1
        else:
            current_node = nodes_dict[current_node][1]
            steps += 1
        if current_node == 'ZZZ':
            break
    else:
        continue
    break

print(steps)