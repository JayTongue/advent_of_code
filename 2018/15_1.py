from collections import Counter
'''
Every turn, each unit tries to 
    1. move into range in order to 
    2. attack if possible

NO DIAG
Ties: top to bottom, then left to right
'''

def get_neighbors(dims, walls):
    ...
    return neighbors

def get_strikeable(dims, players, walls):
    ...
    return strikeable


with open('2018/data/15.txt', 'r') as infile:
    data = [list(i) for i in infile.read().splitlines()]
dims = (len(data), len(data[0]))

walls = [(i, j) for i in range(dims[0]) for j in range(dims[1]) if data[i][j] == '#']
# print(walls)

def get_player_positions(dims=dims):
    players = []
    for row_idx in range(dims[0]):
        for col_idx in range(dims[1]):
            if data[row_idx][col_idx] in ['G', 'E']:
                players.append((data[row_idx][col_idx], (row_idx, col_idx)))
    return players

def find_best_move(player, players, walls):
    ...
    return best_move

while True:
    players = get_player_positions()
    goblin_count = [1 for i in players if i[0] == 'G']
    elf_count = [1 for i in players if i[0] == 'E']
    if goblin_count == 0 or elf_count == 0:
        break
    else:
        for p_type, p_coords in players:
            best_move = find_best_move(p_coords, players, walls)
            strikeable = get_strikeable(p_type)
            if best_move in strikeable:
                data[p_coords[0]][p_coords[1]] = '.'
                data[best_move[0]][best_move][1] = p_type
