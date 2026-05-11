with open('2017/data/1.txt', 'r') as infile:
    d = list(map(int, list(infile.read())))

halfway = len(d)//2
sol = 0
for idx in range(len(d)):
    pair = (d[idx], d[idx-halfway])
    if pair[0] == pair[1]:
        sol += pair[0]
print(sol)