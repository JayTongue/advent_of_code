import numpy as np


def main():
    infile = open('data/15.txt', 'r').read()
    infile = infile.split('\n\n')
    box_map, moves = infile

    box_map = process_box_map(box_map)
    moves = process_moves(moves)

    for move in moves:
        box_map = make_move(move, box_map)
        # print(box_map)
    total_score = calculate_score(box_map)

    print('Total_score:', total_score)


def calculate_score(box_map):
    boxes = np.where(box_map == 'O')
    x_score = sum([box_x * 100 for box_x in boxes[0]])
    y_score = sum([box_y for box_y in boxes[1]])
    return x_score + y_score



def make_move(move, box_map):
    x, y = np.argwhere(box_map == '@').flatten()
    # move = 'v'
    if move == '^':
        move_path = box_map[:x + 1, y]
        move_path = move_path[::-1]
    elif move == '<':
        move_path = box_map[x, :y + 1]
        move_path = move_path[::-1]
    elif move == '>':
        move_path = box_map[x, y:]
    elif move == 'v':
        move_path = box_map[x:, y]
    # print(move, move_path)

    if move_path[1] == '.':
        x1, y1 = coord_next(move, x, y)
        box_map[x1][y1] = '@'
        box_map[x][y] = '.'
        return box_map

    elif move_path[1] == 'O':
        boxes = np.where(move_path == 'O')
        walls = np.where(move_path == '#')
        spaces = np.where(move_path == '.')
        # print(boxes, walls, spaces)

        if spaces[0].size != 0: 
            # print(type(spaces), spaces)
            first_space = spaces[0][0]
        if boxes[0].size != 0:
            first_box = boxes[0][0]
        if walls[0].size != 0:
            first_wall = walls[0][0]
        # print (f'First Space: {first_space}, First Box: {first_box}, First Wall: {first_wall}')

        if spaces[0].size == 0:
            return box_map
        
        elif first_wall < first_space:
            return box_map
        
        else:
            x1, y1 = coord_next(move, x, y)
            box_map[x1][y1] = '@'
            box_map[x][y] = '.'

            if move == '^':
                box_map[x - first_space][y] = 'O'
            elif move == '<':
                box_map[x][y - first_space] = 'O'
            elif move == '>':
                box_map[x][y + first_space] = 'O'
            elif move == 'v':
                box_map[x + first_space][y] = 'O'

            return box_map

    elif move_path[1] == '#':
            return box_map

    
def coord_next(move, x, y):
    if move == '^':
        return x - 1, y
    elif move == '<':
        return x, y - 1
    elif move == '>':
        return x, y + 1
    elif move == 'v':
        return x + 1, y
    

def process_moves(moves):
    moves = list(moves)
    moves = [move for move in moves if move != '\n']
    # print(moves)
    return moves


def process_box_map(box_map):
    box_map = box_map.split('\n')
    box_map = [list(line.strip()) for line in box_map]
    box_map = np.array(box_map, dtype=str)
    # print(box_map)
    return box_map


if __name__ == '__main__':
    main()
