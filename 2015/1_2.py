with open('2015/data/1.txt', 'r') as infile:
    data = [1 if i == '(' else -1 for i in list(infile.read())]
position = 0
for i in range(len(data)):
    position += data[i]
    if position == -1:
        print(i + 1)
        break