with open('2025/data/4.txt', 'r') as infile:
    data = infile.read().split('\n')
data = [list(i) for i in data]

def check_neighbors(row_count, col_count, data):
    check = True
    rolls = 0
    for row_delt, col_delt in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), ( 1, -1), (1, 0), ( 1, 1)):
        new_row, new_col = row_count + row_delt, col_count + col_delt
        if (not 0 <= new_row < len(data)) or (not 0 <= new_col < len(data[0])):
            continue
        else:
            if data[new_row][new_col] == '@':        
                rolls += 1 
    return rolls < 4

blocked_count = 0
for row_count, row in enumerate(data):
    for col_count, col in enumerate(row):
        if data[row_count][col_count] == '@':
            blocked = check_neighbors(row_count, col_count, data)
            blocked_count += blocked
print(blocked_count)