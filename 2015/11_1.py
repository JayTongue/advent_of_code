with open('2015/data/11.txt', 'r') as infile:
    data = list(infile.read())
letters = list('abcdefghijklmnopqrstuvwxyz')

def find_runs(data):
    for i in range(len(data) - 2):
        chunk = data[i], data[i+1], data[i+2]
        run = data[i], data[i]+1, data[i]+2
        if chunk == run:
            return True
    return False

def find_bads(data):
    if any(map(lambda x: x in data, [8, 11, 14])):
        return False
    return True

def find_doubles(data):
    double_count = 0 
    for d in range(1, len(data)-1):
        if data[d] == data[d+1] and data[d-1] != data[d]:
            double_count += 1
    if double_count >= 2:
        return True
    return False

while True:
    positions = [letters.index(i) for i in data]
    positions[-1] += 1
    for pos in range(len(positions)-1, 0, -1):
        if positions[pos] <= len(letters) - 1:
            continue 
        else:
            positions[pos - 1] += 1
            positions[pos] =  positions[pos] % len(letters) 
    data = [letters[i] for i in positions]
    if all((find_runs(positions), find_doubles(positions), find_bads(positions))):
        break
print(''.join(data))

