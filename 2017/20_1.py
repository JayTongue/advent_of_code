with open('2017/data/20.txt', 'r') as infile:
    data = [[list(map(int, j[3:-1].split(','))) for j in i.split(', ')] for i in infile.read().split('\n')]

def tick(p, v, a):
    v += a
    p += v
    return p, v, a

def manhattan_dist(particle):
    pos, _, _ = particle
    return sum(map(abs, pos))

winner = False
for _ in range(410):
    new_positions = []
    for count, particle in enumerate(data):
        pos, vel, acc = particle
        new_pos, new_vel, new_acc = [], [], []
        for idx in range(len(pos)):
            p, v, a = pos[idx], vel[idx], acc[idx]
            p, v, a = tick(p, v, a)
            new_pos.append(p) ; new_vel.append(v) ; new_acc.append(a)
        new_positions.append([new_pos, new_vel, new_acc])

    closest_val, closest_idx = float('inf'), 0
    for count, particle in enumerate(new_positions):
        dist = manhattan_dist(particle)
        if dist < closest_val:
            closest_idx = count ; closest_val = dist
    data = new_positions
print(closest_idx)
        