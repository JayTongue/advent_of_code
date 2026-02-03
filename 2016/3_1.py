with open('2016/data/3.txt','r') as infile:
    data = [sorted(list(map(int, [b for b in a.split(' ') if b]))) for a in infile.read().split('\n')]
sol = map(lambda x: x[0] + x[1] > x[2], data)
print(sum(sol))