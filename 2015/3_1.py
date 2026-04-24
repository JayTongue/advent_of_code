with open('2015/data/3.txt', 'r') as infile:
    data = list(infile.read())
steps = []
for d in data:
    if d == '^':
        steps.append((-1, 0))
    elif d == '>':
        steps.append((0, 1))
    elif d == '<':
        steps.append((0, -1))
    else:
        steps.append((1, 0))
start = [0, 0] ; houses = {tuple(start)}
for step in steps:
    start[0] += step[0] ; start[1] += step[1]
    houses.add(tuple(start))
print(len(houses))