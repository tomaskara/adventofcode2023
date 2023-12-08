with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

instructions = lines[0]
nodes_dict = {}
for line in lines[2:]:
    node, lr = line.split(' = ')
    nodes_dict[node] = lr[1:-1].split(', ')

current_node = 'AAA'
steps = 0
ways = []
for key in nodes_dict.keys():
    if key[-1] == 'A':
        new_node = key
        while True:
            for instruction in instructions:
                if instruction == 'L':
                    new_node = nodes_dict[new_node][0]
                    steps += 1
                    if new_node[-1] == 'Z':
                        ways.append(steps)
                        steps = 0
                        break
                if instruction == 'R':
                    new_node = nodes_dict[new_node][1]
                    steps += 1
                    if new_node[-1] == 'Z':
                        ways.append(steps)
                        steps = 0
                        break
            else:
                continue
            break
    else:
        continue


def nsd(a, b):
    while b:
        a, b = b, a % b
    return a


def nsn(a, b):
    return a * b // nsd(a, b)


result = nsn(ways[0], ways[1])

for number in ways[2:]:
    result = nsn(result, number)

print(result)