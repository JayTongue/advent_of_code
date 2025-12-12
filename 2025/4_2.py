from copy import deepcopy

with open('2025/data/4.txt', 'r') as infile:
    data = infile.read().split('\n')
data = [list(i) for i in data]

def check_neighbors(row_count, col_count, data):
    '''returns True if removable, False if blocked'''
    check, rolls = True, 0
    for row_delt, col_delt in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), ( 1, -1), (1, 0), ( 1, 1)):
        new_row, new_col = row_count + row_delt, col_count + col_delt
        if (not 0 <= new_row < len(data)) or (not 0 <= new_col < len(data[0])):
            continue
        else:
            if data[new_row][new_col] == '@':        
                rolls += 1 
    return rolls < 4

total_removed, removable, round_counter = 0, 1, 0
while removable > 0:
    changes = []
    removable = 0
    for row_count, row in enumerate(data):
        for col_count, col in enumerate(row):
            if data[row_count][col_count] == '@':
                blocked = check_neighbors(row_count, col_count, data)
                if blocked:
                    changes.append((row_count, col_count))
                removable += blocked
    total_removed += removable ; round_counter += 1

    for row_count, col_count in changes:
        data[row_count][col_count] = '.'

print(total_removed)