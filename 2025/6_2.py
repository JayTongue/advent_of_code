from math import prod

with open('2025/data/6.txt', 'r') as infile:
    data = infile.read().split('\n')
    operators = data[-1]
    data = data[:-1]

indexes = [count for count, i in enumerate(operators) if i != ' ']
ranged_idxs = []
for ct, idx in enumerate(indexes[:-1]):
    ranged_idxs.append((idx, indexes[ct+1]))
ranged_idxs.append((indexes[-1], len(operators)+1))

operators = [j for j in operators if j != ' ']
sol = 0

for cycle_count, limits in enumerate(ranged_idxs):
    s, e = limits
    problem = []
    for d in data:
        problem.append(d[s:e])
    if all([n[-1] == ' ' for n in problem]):
        problem = [n[:-1] for n in problem]

    total_col = []
    for pos in range(max([len(n) for n in problem])):
        col = int(''.join([p[pos] for p in problem if p[pos] != ' ']))
        total_col.append(col)
    op = operators[cycle_count]
    if op == '+':
        sol += sum(total_col)
    if op == '*':
        sol +=  prod(total_col)

print(sol)
