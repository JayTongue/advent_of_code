import ast
import numpy as np
from itertools import product
from tqdm import tqdm

with open('2025/data/10.txt', 'r') as infile:
    data = [i.strip('\n').split(' ') for i in infile.read().splitlines('\n')]
    lights = [list(map(lambda l: 0 if l == '.' else 1, list(i[0][1:-1]))) for i in data]
    buttons = [list(map(ast.literal_eval, j[1:-1])) for j in data]
    buttons = [list(map(lambda b: b if isinstance(b, tuple) else (b,), butt)) for butt in buttons]
    joltage = [list(map(int, k[-1][1:-1].split(','))) for k in data]
data = list(zip(lights, buttons, joltage))

sol = 0
for lights, buttons, joltage in tqdm(data):
    prob_min = float('inf')
    butt_arr = np.zeros((len(buttons), len(lights)), dtype=np.int_)
    for b_count, b in enumerate(buttons):
        for elem in b:
            butt_arr[b_count][elem] = 1
    butt_arr = butt_arr.T
    joltage = np.array(joltage, dtype=np.int_)

    for perm in list(product(range(13), repeat=len(buttons))):
        perm = np.array(perm, dtype=np.int_)
        result = butt_arr @ perm

        if np.array_equal(result, joltage):
            prob_min = min(prob_min, sum(perm))
    sol += prob_min
print(sol)
        
