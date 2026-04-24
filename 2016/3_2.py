with open('2016/data/3.txt','r') as infile:
    data = [list(map(int, [b for b in a.split(' ') if b])) for a in infile.read().split('\n')]

sol = 0
for d in range(0, len(data), 3):
    for place in range(len(data[d])):
        tri = sorted([data[chunk][place] for chunk in (d, d+1, d+2)])
        if tri[0] + tri[1] > tri[2]:
            sol += 1
print(sol)
