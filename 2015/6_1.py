with open('2015/data/6.txt', 'r') as infile:
    data = infile.read().split('\n')
    all_moves = []
    for line in data:
        line = line.split(' ')
        if len(line) == 4:
            line = (line[0], tuple(map(int, line[1].split(','))), tuple(map(int, line[3].split(','))))
        else:
            line = (line[1], tuple(map(int, line[2].split(','))), tuple(map(int, line[4].split(','))))
        all_moves.append(line)
bool_table = [[False for _ in range(1000)] for _ in range(1000)]
for command, corner_1, corner_2 in all_moves:
    for x in range(min(corner_1[0], corner_2[0]), max(corner_1[0], corner_2[0])+1):
        for y in range(min(corner_2[1], corner_1[1]), max(corner_2[1], corner_1[1])+1):
                if command == 'toggle':
                    bool_table[x][y] = not bool_table[x][y]
                elif command == 'on':
                     bool_table[x][y] = True
                else:
                     bool_table[x][y] = False
print(sum([sum(r) for r in bool_table]))