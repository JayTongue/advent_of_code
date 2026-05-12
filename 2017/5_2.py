with open('2017/data/5.txt', 'r') as infile:
    data = [int(i) for i in infile.read().split('\n')]

pointer = 0 ; steps = 0

while True:
    if not 0<=pointer<=(len(data)-1):
        break
    else:
        found = data[pointer]
        if found >= 3:
            data[pointer] -= 1
        else:
            data[pointer] += 1
        steps += 1 ; pointer += found

print(steps)