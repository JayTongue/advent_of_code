import ast
import numpy as np
from itertools import product

with open('2025/data/10.txt', 'r') as infile:
    data = [i.strip('\n').split(' ') for i in infile.read().splitlines('\n')]
    lights = [list(map(lambda l: 0 if l == '.' else 1, list(i[0][1:-1]))) for i in data]
    buttons = [list(map(ast.literal_eval, j[1:-1])) for j in data]
    buttons = [list(map(lambda b: b if isinstance(b, tuple) else (b,), butt)) for butt in buttons]
    joltage = [ast.literal_eval(k[-1]) for k in data]
data = list(zip(lights, buttons, joltage))

sol = 0
for lights, buttons, joltage in data:
    prob_min = float('inf')
    butt_arr = np.zeros((len(buttons), len(lights)), dtype=np.int_)
    for b_count, b in enumerate(buttons):
        for elem in b:
            butt_arr[b_count][elem] = 1
    butt_arr = butt_arr.T
    lights = np.array(lights)

    for perm in list(product([0, 1], repeat=len(buttons))):
        perm = np.array(perm, dtype=np.int_)
        result = (butt_arr @ perm) % 2

        if np.array_equal(result, lights):
            prob_min = min(prob_min, sum(perm))
    sol += prob_min
print(sol)
        
