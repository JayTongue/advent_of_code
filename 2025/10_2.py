import ast
from z3 import Int, Optimize, Sum, sat

with open('2025/data/10.txt', 'r') as infile:
    data = [i.strip('\n').split(' ') for i in infile.read().splitlines('\n')]
    lights = [list(map(lambda l: 0 if l == '.' else 1, list(i[0][1:-1]))) for i in data]
    buttons = [list(map(ast.literal_eval, j[1:-1])) for j in data]
    buttons = [list(map(lambda b: b if isinstance(b, tuple) else (b,), butt)) for butt in buttons]
    joltage = [list(map(int, k[-1][1:-1].split(','))) for k in data]
data = list(zip(lights, buttons, joltage))
sol = 0

for lights, buttons, joltage in data:
    n_buttons = len(buttons) ; n_lights = len(joltage)
    butt_arr = [[0] * n_buttons for _ in range(n_lights)]
    for b_idx, b in enumerate(buttons):
        for light_idx in b:
            butt_arr[light_idx][b_idx] = 1

    opt = Optimize()
    perm = [Int(f"p_{i}") for i in range(n_buttons)]

    for p in perm:
        opt.add(p >= 0, p <= 1000 )

    for i in range(n_lights):
        opt.add(Sum(butt_arr[i][j] * perm[j] for j in range(n_buttons)) == joltage[i])

    opt.minimize(Sum(perm))

    if opt.check() == sat:
        model = opt.model()
        prob_min = sum(model[p].as_long() for p in perm)

    sol += prob_min

print(sol)

