with open('2025/data/7.txt', 'r') as infile:
    data = [list(d) for d in infile.read().split('\n')]

start = (0, data[0].index('S'))
data[start[0]+1][start[1]] = '|'
split_count = 0

for row_count, row in enumerate(data):
    for col_count, col in enumerate(row):
        if data[row_count][col_count] == '^' and data[row_count-1][col_count] == '|':
            data[row_count][col_count-1] = '|' ;  data[row_count][col_count+1] = '|'
            split_count += 1
        elif data[row_count][col_count] == '.' and data[row_count-1][col_count] == '|':
            data[row_count][col_count] = '|'

print(split_count)