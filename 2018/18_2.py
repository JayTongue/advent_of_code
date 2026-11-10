import numpy as np

with open('2018/data/18.txt', 'r') as infile:
    grid = np.array([list(i) for i in infile.read().split('\n')])

def count_neighbors(grid, value):
    padded = np.pad(
        (grid == value).astype(int),
        1,
        constant_values=0,
    )

    return (
        padded[:-2, :-2]  + padded[:-2, 1:-1] + padded[:-2, 2:]
        + padded[1:-1, :-2]                   + padded[1:-1, 2:]
        + padded[2:, :-2] + padded[2:, 1:-1]  + padded[2:, 2:]
    )

def step(grid):
    trees = count_neighbors(grid, "|")
    lumberyards = count_neighbors(grid, "#")

    result = grid.copy()

    result[(grid == ".") & (trees >= 3)] = "|"
    result[(grid == "|") & (lumberyards >= 3)] = "#"
    result[(grid == "#") & ((lumberyards == 0) | (trees == 0))] = "."
    return result

def flatten(grid):
    return tuple([j for i in grid for j in i])

target = int(1e9)
seen_states = {}
count = 0
while count < target:
    flat = grid.tobytes()

    if flat in seen_states:
        cycle_length = count - seen_states[flat]
        remaining = (target - count) % cycle_length

        for _ in range(remaining):
            grid = step(grid)

        break

    seen_states[flat] = count
    grid = step(grid)
    count += 1

print(np.count_nonzero(grid == "#") * np.count_nonzero(grid == "|"))