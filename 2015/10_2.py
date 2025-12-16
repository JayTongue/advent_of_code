with open('2015/data/10.txt', 'r') as infile:
    data = list(map(int, list(infile.read())))

for i in range(50):
    new_iter = []
    dig = data[0] ; count = 1
    for d in data[1:]:
        if d == dig:
            count += 1
        else:
            new_iter.append(count) ; new_iter.append(dig)
            dig = d ; count = 1
    new_iter.append(count) ; new_iter.append(dig)
    data = new_iter
print(len(data))