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
robo_steps = steps[1::2] ; meat_steps = steps[::2]

houses = {(0, 0)}
for steps in [robo_steps, meat_steps]:
    start = [0, 0] 
    for step in steps:
        start[0] += step[0] ; start[1] += step[1]
        houses.add(tuple(start))
print(len(houses))