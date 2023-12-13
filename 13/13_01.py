import numpy as np


with open('input.txt') as f:
    input_blocks = f.read().strip().split('\n\n')
    arrays = [np.array([list(row) for row in block.split('\n')]) for block in input_blocks]

final_count = 0
count = 0

for n, array in enumerate(arrays):
    find = False
    rows, cols = array.shape
    #vertical find
    for col in range(cols):
        col += 1
        if cols == col:
            break
        start = 0
        if col > cols//2:
            start = col-(cols-col)
        left_part = array[:, start:col]
        right_part = array[:, col:col+len(left_part[0])]
        right_part_flip = np.fliplr(right_part)
        if np.array_equal(left_part, right_part_flip):
            final_count += col
            count += 1
            find = True
            break
    if not find:
        #horizontal find
        for row in range(rows):
            row += 1
            start = 0
            if row > rows//2:
                start = row-(rows-row)
            up_part = array[start:row,:]
            down_part = array[row:row+len(up_part), :]
            down_part_flip = np.flipud(down_part)
            if np.array_equal(up_part, down_part_flip):
                final_count += row*100
                count += 1
                break

print(final_count)



