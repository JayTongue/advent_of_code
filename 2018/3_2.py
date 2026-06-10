side_len = 1000
grid = [[0 for _ in range(side_len)] for _ in range(side_len)]

with open('2018/data/3.txt', 'r') as infile:
    claims = infile.read().split('\n')

check_dict = {}
for claim in claims:
    covering = []
    number, _,  start, dims = claim.split(' ')
    number = int(number[1:])
    start = tuple(map(int, start[:-1].split(',')))
    dims = tuple(map(int, dims.split('x')))
    for i in range(dims[0]):
        for j in range(dims[1]):
            grid[i+start[0]][j+start[1]] += 1
            covering.append((i+start[0], j+start[1]))
    check_dict[number] = covering

for key, val in check_dict.items():
    if all(grid[row][col] == 1 for row, col in val):
        print(key)
        break
