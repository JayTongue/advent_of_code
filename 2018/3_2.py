side_len = 1000
grid = [[[] for _ in range(side_len)] for _ in range(side_len)]

with open('2018/data/3.txt', 'r') as infile:
    claims = infile.read().split('\n')

for claim in claims:
    number, _,  start, dims = claim.split(' ')
    number = int(number[1:])
    start = tuple(map(int, start[:-1].split(',')))
    dims = tuple(map(int, dims.split('x')))
    for i in range(dims[0]):
        for j in range(dims[1]):
            grid[i+start[0]][j+start[1]].append(number)

for number in range(1, len(claims)+1):
    clean = True
    for row in grid:
        for col in row:
            if number in col and len(col) != 1:
                clean = False
                break
        if not clean:
            break
    if clean:
        print(number)
        break
