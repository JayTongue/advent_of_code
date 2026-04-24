with open('2016/data/2.txt', 'r') as infile:
    data = [list(i) for i in infile.read().split('\n')]

keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
starting_pos = [1, 1] ; sol = []
for row in data:
    for move in row:
        if move == 'U':
            if 0 <= starting_pos[0]-1 < len(keypad):
                starting_pos = [starting_pos[0]-1, starting_pos[1]]
        elif move == 'D':
            if 0 <= starting_pos[0]+1 < len(keypad):
                starting_pos = [starting_pos[0]+1, starting_pos[1]]
        elif move == 'R':
            if 0 <= starting_pos[1]+1 < len(keypad[0]):
                starting_pos = [starting_pos[0], starting_pos[1]+1]
        elif move == 'L':
            if 0 <= starting_pos[1]-1 < len(keypad[0]):
                starting_pos = [starting_pos[0], starting_pos[1]-1]
    sol.append(keypad[starting_pos[0]][starting_pos[1]])
print(''.join(map(str, sol)))