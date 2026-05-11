with open('2017/data/1.txt', 'r') as infile:
    data = list(map(int, list(infile.read())))

sol = 0
for idx in range(-1, len(data)-1):
    pair = (data[idx], data[idx+1])
    if pair[0] == pair[1]:
        sol += pair[0]
print(sol)