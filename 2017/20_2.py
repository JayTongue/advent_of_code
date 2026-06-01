with open('2017/data/20.txt', 'r') as infile:
    data = [[list(map(int, j[3:-1].split(','))) for j in i.split(', ')] for i in infile.read().split('\n')]

def tick(p, v, a):
    v += a
    p += v
    return p, v, a

winner = False
for _ in range(40):
    new_positions = []
    for count, particle in enumerate(data):
        pos, vel, acc = particle
        new_pos, new_vel, new_acc = [], [], []
        for idx in range(len(pos)):
            p, v, a = pos[idx], vel[idx], acc[idx]
            p, v, a = tick(p, v, a)
            new_pos.append(p) ; new_vel.append(v) ; new_acc.append(a)
        new_positions.append([new_pos, new_vel, new_acc])
    remove = set()
    for count_1, pos_1 in enumerate(new_positions):
        for count_2, pos_2 in enumerate(new_positions):
            if pos_1[0] == pos_2[0] and count_1 != count_2:
                remove |= {count_1, count_2}
    
    data = [np for count, np in enumerate(new_positions) if count not in remove]
    
print(len(data))
        