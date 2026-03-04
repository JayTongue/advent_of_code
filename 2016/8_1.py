with open('2016/data/8.txt', 'r') as infile:
    data = infile.read().split('\n')

starting_dim = (6, 50)
grid = [['.' for _ in range(starting_dim[1])] for _ in range(starting_dim[0])]

for instruction in data:
    instruction = instruction.split(' ')
    if len(instruction) == 2:
        rect_dim = list(map(int, instruction[1].split('x')))
        for row in range(rect_dim[1]):
            for col in range(rect_dim[0]):
                grid[row][col] = '#'
    elif len(instruction) == 5:
        idx = int(instruction[2].split('=')[1]) ; amount = int(instruction[4])
        swapping = []
        if instruction[1] == 'column':
            for row in grid:
                swapping.append(row[idx])
            swapping = swapping[len(swapping)-amount:] + swapping[:-amount]
            for swap_row_idx in range(len(swapping)):
                grid[swap_row_idx][idx] = swapping[swap_row_idx]
        elif instruction[1] == 'row':
            swapping = grid[idx][len(grid[0])-amount:] + grid[idx][:-amount]
            grid[idx] = swapping

print(sum([i.count('#') for i in grid]))