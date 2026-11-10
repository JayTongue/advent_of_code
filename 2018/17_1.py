from copy import deepcopy

def count_out(x):
    x = list(x)
    if len(x) == 1:
        return x
    return list(range(x[0], x[1]+1))

with open('2018/data/17.txt', 'r') as infile:
    data = [sorted(i.split(', ')) for i in infile.read().split('\n')]
    data = [(count_out(map(int, x[2:].split('..'))), count_out(map(int, y[2:].split('..')))) for x, y in data]
water_coord = (0, 500)

x_range = [xi for x, _ in data for xi in x] ; y_range = [yi for _, y in data for yi in y]
x_range = (min(x_range), max(x_range)) ; y_range = (min(y_range), max(y_range))

puz = []
for y_perm in range(0, y_range[1]+1):
    row = []
    for x_perm in range(x_range[0]-1, x_range[1]+2):
        found = False
        if water_coord == (y_perm, x_perm):
            row.append('+')
            found = True
        for dx, dy in data:
            if x_perm in dx and y_perm in dy and not found:
                row.append('#')
                found = True
                break
        if not found:
            row.append('.')
    puz.append(row)

def get_water_positions(puz):
    water = []
    for row_idx in range(len(puz)):
        for col_idx in range(len(row)):
            if puz[row_idx][col_idx] in ['|', '+']:
                water.append((row_idx, col_idx))
    return water

water = get_water_positions(puz)
prev_state = deepcopy(puz)
while True:
    for wx, wy in water:
        down_off = 1
        if wx+down_off > len(puz)-1:
            continue
        if puz[wx+down_off][wy] == '.':
            while puz[wx+down_off][wy] == '.':
                puz[wx+down_off][wy] = '|'
                down_off += 1
                if wx+down_off > len(puz)-1:
                    break
        elif puz[wx+1][wy] in ['#', '~']:
            row_coords = [(wx, wy)]
            left_off, right_off = -1, 1
            falling = False
            while True:
                if puz[wx][wy+left_off] != '#' and 0 <= wy+left_off <= len(puz[0]):
                    row_coords.append((wx, wy+left_off))
                    if puz[wx+1][wy+left_off] not in ['#', '~']:
                        falling = True
                        break
                    left_off -= 1
                else:
                    break
            while True:
                if puz[wx][wy+right_off] != '#' and 0 <= wy+right_off <= len(puz[0]):
                    row_coords.append((wx, wy+right_off))
                    if puz[wx+1][wy+right_off] not in ['#', '~']:
                        falling=True
                        break
                    right_off += 1
                else:
                    break
            for r, c in row_coords:
                if falling:
                    puz[r][c] = '|'
                else:            
                    puz[r][c] = '~'                 
    water = get_water_positions(puz)
    if puz == prev_state:
        break
    else:
        prev_state = deepcopy(puz)

sol = sum(1 
          for row in puz[y_range[0]:] 
          for col in row
          if col in ['~', '|']
        )
print(sol)
